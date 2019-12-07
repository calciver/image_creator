import cv2
import numpy as np
import os
import glob
import tqdm
import argparse

#Folder locations
input_folder = 'input'
output_folder = 'output'
width = 512
height = 512
dim = (width, height)


#Flipping Functions
def flip_horizontal(img):
    horizontal_img = cv2.flip( img, 0 )
    return horizontal_img

def flip_vertical(img):
    vertical_img = cv2.flip( img, 1 )
    return vertical_img

#Rotation Functions
def rotate_left(img):
    h,w,c = img.shape
    empty_img = np.zeros([h,w,c], dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            empty_img[i,j] = img[j-1,i-1]
            empty_img = empty_img[0:h,0:w]
    return empty_img

def rotate_right(img):
    h,w,c = img.shape
    empty_img = np.zeros([h,w,c], dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            empty_img[i,j] = img[h-j-1,w-i-1]
            empty_img = empty_img[0:h,0:w]
    return empty_img

def rotate_180(img):
    h,w,c = img.shape
    empty_img = np.zeros([h,w,c], dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            empty_img[i,j] = img[h-i-1,w-j-1]
            empty_img = empty_img[0:h,0:w]
    return empty_img


#Write to file
def write_files(resized,output_path,base_name):
    output_path = os.path.join(output_path,base_name)
    #Save the resized image
    cv2.imwrite(output_path+"_resized.jpg",resized)
    #Save the flipped images
    cv2.imwrite(output_path+"_horizontal.jpg",flip_horizontal(resized))
    cv2.imwrite(output_path+"_vertical.jpg",flip_vertical(resized))
    #Save the rotated images
    cv2.imwrite(output_path+"_left.jpg",rotate_left(resized))
    cv2.imwrite(output_path+"_right.jpg",rotate_right(resized))
    cv2.imwrite(output_path+"_180.jpg",rotate_180(resized))

def dir_creator(file_path):
    if os.path.isdir(file_path):
        pass
    else:
        os.mkdir(file_path)
        print(f'The directory {file_path} does not exist. Creating directory.')

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Specify your input files and where you want to save output')
    parser.add_argument('--data', metavar='DIR', help='Path to the train dataset',default='Normal')
    parser.add_argument('--output', metavar='OUT', type=str,
                        help='Path to the train dataset',default= 'Normal_Augmented')
    args = parser.parse_args()
    image_files = glob.glob(os.path.join(args.data, '*.jpg'))
    dir_creator(args.output)


    file_count = len(image_files)

    for i in tqdm.tqdm(range(file_count)):
    #for file in image_files:
        file = image_files[i]
        base_name_no_ext = os.path.basename(file)[0:-4]
        img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #output_path = os.path.join(args.output,file_name)
        write_files(resized,output_path = args.output,base_name = base_name_no_ext)
