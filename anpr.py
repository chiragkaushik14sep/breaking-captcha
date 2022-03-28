import cv2
import imutils

def show_image(image):
    cv2.imshow('image',image)
    c = cv2.waitKey()
    if c >= 0 : return -1
    return 0
img = r"C:\Users\Ckaushik\Downloads\tmp\tmp\50-20190601-100700_DL12CN8151.jpg"
img = cv2.imread(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(img.getType())
cv2.imshow("img.jpg",img)
#print(img)

thres = cv2.threshold(img,100,100,cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = cnts[0]
print(len(cnt))
#cnts = cnt if imutils.is_cv2() else cnts[1]
#cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(cnt[0])

    roi = img[y - 5:y + h + 5, x - 5:x + w + 5]

    # display the character, making it large enough for us
    # to see, then wait for a keypress
    cv2.imshow("ROI", imutils.resize(roi, width=28))
    key = cv2.waitKey(0)

# cv2.imshow("img1.jpg",img)
# #cv2.imshow("img.jpg",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

