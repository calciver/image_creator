import cv2
import numpy as np

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
def write_files(resized,output_path):
  #Save the resized image
  cv2.imwrite(output_path+"_resized.jpg",resized)
  #Save the flipped images
  cv2.imwrite(output_path+"_horizontal.jpg",flip_horizontal(resized))
  cv2.imwrite(output_path+"_vertical.jpg",flip_vertical(resized))
  #Save the rotated images
  cv2.imwrite(output_path+"_left.jpg",rotate_left(resized))
  cv2.imwrite(output_path+"_right.jpg",rotate_right(resized))
  cv2.imwrite(output_path+"_180.jpg",rotate_180(resized))


for file in os.listdir(input_folder):
  file_name = file[0:-4]
  img = cv2.imread(input_folder+'/'+file, cv2.IMREAD_UNCHANGED)
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

  #Write images
  output_path=output_folder+"/"+file_name
  write_files(resized,output_path)
