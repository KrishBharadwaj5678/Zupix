import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.9,maxHands=2)
startDist = None
scale,cx,cy = 0,0,0

while True:
    success, img = cap.read()
    hands,img = detector.findHands(img)
    img1 = cv2.imread("book.jpeg")
    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1,1,0,0,0] and detector.fingersUp(hands[1]) == [1,1,0,0,0]:
            lmList1 = hands[0]['lmList']
            lmList2 = hands[1]['lmList']
            if startDist is None:
                length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img, scale=9)
                startDist = length

            length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img, scale=9)
            scale = int((length-startDist)//2)
            cx,cy = info[4:]
    else:
        startDist = None

    try:
        h1,w1,_ = img1.shape
        newW,newH = ((h1+scale)//2)*2, ((w1+scale)//2)*2
        img1 = cv2.resize(img1,(newW,newH))
        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1
    except:
        pass

    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)