# Usage example
# python img_xml_filter.py --imgdir "Path to images, default ./" --imgSize "int" --xmlSize"int" --output "Path to output directory"

from glob import glob
import os
import shutil
import argparse

# Filter by size
def sizeFilter(imgList,args):
    print('Now Filtering..')
    tgImageSize = args.imgSize
    tgXmlSize = args.xmlSize
    newImgList = list()
    for imgName in imgList:
        xmlName = imgName[:-4]+'.xml'
        imgSize = os.path.getsize(os.path.join(args.imgdir, imgName))//1000
        xmlSize = os.path.getsize(os.pat.join(args.imgdir, xmlName))
        if imgSize > tgImageSize:
            continue
        elif xmlSize > tgXmlSize:
            continue
        else:
            newImgList.append(imgName)
    print ('Filtering done..')
    return newImgList

# Copy filtered file
def copyFile(imgList,args):
    print('Now Copying..')
    for imgName in imgList:
        xmlName = imgName[:-4]+'.xml'
        shutil.copy(os.path.join(args.imgdir, imgName), args.output)
        shutil.copy(os.path.join(args.imgdir, xmlName), args.output)
    print ('Copy done..')
    

def main():
    # Read img name list
    imgList = glob('*.jpg')

    # Parsing argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgdir', type=str, default='./', help='Path to image directory')
    parser.add_argument('--imgSize', type=int, required = True, help='Size of image that you want to filter(KB)')
    parser.add_argument('--xmlSize', type=int, required = True, help='Size of xml that you want to filter(Bytes)')
    parser.add_argument('--output', type=str, required = True, help='Path to output directory')
    args = parser.parse_args()

    imgList = sizeFilter(imgList,args)
    copyFile(imgList, args)

    print('All tasks successfully done..')

if __name__=="__main__":
    main()
