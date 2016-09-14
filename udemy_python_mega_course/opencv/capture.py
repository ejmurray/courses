import cv2, time

video=cv2.VideoCapture(0)
a=1
start=time.time()
while True:
   a=a+1
   check, frame = video.read()

   print(check)
   print(frame)

   gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #time.sleep(3)
   cv2.imshow("Capturing", frame)
   
   key=cv2.waitKey(1)
   
   if key==ord('q'):
      break
elapsed=time.time() - start
print(elapsed)
print(a)
fps=a/elapsed
print("Average FPS: " + str(fps))
video.release()
cv2.destroyAllWindows()
