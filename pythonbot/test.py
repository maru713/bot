import cv2,random
iname=["","","","","","","",""]
a=81
for w in range(8):
            r=random.randint(0,a-1)
            iname[w]=str(r)+".png"
img0=cv2.imread(iname[0])
img1=cv2.imread(iname[1])
img2=cv2.imread(iname[2])
img3=cv2.imread(iname[3])
img4=cv2.imread(iname[4])
img5=cv2.imread(iname[5])
img6=cv2.imread(iname[6])
img7=cv2.imread(iname[7])
print(iname)
img5 = cv2.hconcat([img0, img1])
img6 = cv2.hconcat([img2, img3])
img7 = cv2.hconcat([img4, img5])

cv2.imwrite('output.jpg', img7)
