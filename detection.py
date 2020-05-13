import cv2
import time



cascade_src = 'cars.xml'

video_src = 'video1.avi'
video_src1 = 'video.avi'


cap = cv2.VideoCapture(video_src)
cap1 = cv2.VideoCapture(video_src1)


car_cascade = cv2.CascadeClassifier(cascade_src)
car_cascade1 = cv2.CascadeClassifier(cascade_src)


# to connect with camera
# cam = cv2.VideoCapture(0)

# width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))




number = 0
density = 0
lone = 0
ltwo = 0

one = time.perf_counter()
print(one)

while True:

    #ret, cam = cam.read()



    ret, img = cap.read()
    ret2, img1 = cap1.read()


   
    if ((type(img) == type(None)) and (type(img1) == type(None))):
        break

    #here the image/video is converted to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    
    
    mithun = car_cascade.detectMultiScale(gray, 1.1, 2)
    mithun1 = car_cascade1.detectMultiScale(gray1, 1.1, 2)


    density = len(mithun)
    density1 = len(mithun1)

    lone = lone + density1
    ltwo = ltwo + density

    #print(density)
    tic = time.perf_counter()
    
    # at 5th sec
    if (tic >= 5.0 and tic <= 5.1 ):
        #print(tic)
        if(ltwo > lone):            
            print("\n\ngreen =" + str(density) + "\ntotal is =" + str(ltwo))
        elif(ltwo < lone):
            print("\n\nblue =" +str(density1) + "\ntotal is =" + str(lone))

    


    for (x,y,w,h) in mithun:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    for(a,b,c,d) in mithun1:
        cv2.rectangle(img1,(a,b),(a+c,b+d),(155,0,25),4)      


    #concatinate

    final = cv2.hconcat([img,img1])

    cv2.imshow('video', final)

    
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()