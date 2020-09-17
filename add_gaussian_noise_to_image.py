# Usage
# python add_gaussian_noise_to_image.py --imgDir path_to_img
# Please change sigma if you want
# Notice that this code will overwrite the image

# Package import
import numpy as np
import os
import cv2
import argparse as ap
from glob import glob

# Define gaussian noise function
def gaussian_noise(image):
    row,col,ch=image.shape
    # Image to ndarray
    temp_image=np.float64(np.copy(image))
    mean=0
    # The high value will provide more noise
    sigma=20

    # Noise function
    noise=np.random.randn(row,col)*sigma
    noisy_image=np.zeros(temp_image.shape,np.float64)
    if len(temp_image.shape)==2:
        noisy_image=temp_image+noise
    else:
        noisy_image[:,:,0]=temp_image[:,:,0]+noise
        noisy_image[:,:,1]=temp_image[:,:,1]+noise
        noisy_image[:,:,2]=temp_image[:,:,2]+noise
    return noisy_image

def main():
    parser=ap.ArgumentParser()
    parser.add_argument('--imgDir',type=str,default='./',help='Path to the image directory(default=./)')
    args=parser.parse_args()

    imgList=glob(os.path.join(args.imgDir,'*.jpg'))

    # Add noise for each 3rd image.
    cnt=0
    for imgName in imgList:
        if cnt%3==0:
            imgPath=os.path.join(args.imgDir,imgName)
            img=cv2.imread(imgPath)
            img=gaussian_noise(img)
            cv2.imwrite(imgPath,img)
        cnt=cnt+1

    # Done
    print('Successfully add Gaussian noise to selected images')

if __name__=='__main__':
    main()
