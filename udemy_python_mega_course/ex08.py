# import os
# import cv2

# img=[]
# filenames=[]

# for filename in os.listdir(".\\imgs"):
   # if filename.endswith(".jpg"):
      # name, ext = os.path.splitext(filename)
      # img.append(cv2.imread(".\\imgs\\" + filename, 1))
      # filenames.append(name)

# for i in range(0, len(img)):
   # img[i] = cv2.resize(img[i], (100, 100))
   # cv2.imwrite(".\\imgs\\" + filenames[i] + "_resized.jpg", img[i])
   
import glob
import cv2

images = glob.glob(r".\imgs\*.jpg")

for image in images:         
      img = cv2.imread(image, 0)
      re  = cv2.resize(img, (100, 100))
      cv2.imshow("img", re)
      cv2.waitKey(500)
      cv2.destroyAllWindows()
      cv2.imwrite(r".\imgs\resized_" + image, re) #only works when script is in same folder (remove \imgs\)