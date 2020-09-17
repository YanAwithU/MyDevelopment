# Usage
# python image_selector.py --imgdir path_to_img --output path_to_output

# import packages
from glob import glob
import cv2
import os
import argparse
import shutil

# Select image
def image_select_func(imgList,args):
    nimgList=list()
    for imgName in imgList:
        img=cv2.imread(imgName)
        cv2.imshow(imgName[-16:],img)
        key=cv2.waitKey(0)&0xFF
        if key == 32:
            cv2.destroyAllWindows()
            print('passed..')
            continue
        elif key == 115:
            nimgList.append(imgName[-16:])
            print('saved..')
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
            img_copy(nimgList,args)
            return nimgList
        
    img_copy(nimgList,args)
    print('Selecting images done..')
    return nimgList

# Copy image
def img_copy(imgList,args):
    for imgName in imgList:
        imgPath=os.path.join(args.imgdir,imgName)
        shutil.copy(imgPath,os.path.join(args.output,imgName))
    print('Copying images done..')
    


# Copy xml
def xml_copy(imgList,args):
    for imgName in imgList:
        xmlName=imgName[:-4]+'.xml'
        xmlPath=os.path.join(args.imgdir,xmlName)
        shutil.copy(xmlPath,os.path.join(args.output,xmlName))
    print('Copying .xml files done..')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--imgdir',required=True,help='Path to image')
    parser.add_argument('--output',required=True,help='Path to output')
    args=parser.parse_args()

    # List image
    imgList=glob(os.path.join(args.imgdir,'*.jpg'))
    selectedList=image_select_func(imgList,args)

    # Attach xml to image
    xml_copy(selectedList,args)

    print('All tasks are successfully done..')

if __name__=='__main__':
    main()
