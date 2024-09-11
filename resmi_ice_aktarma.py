import cv2

# içe aktarma
img = cv2.imread("dog-7514202_640.jpg", 0)

# görselleştirme
cv2.imshow("First image", img)

k = cv2.waitKey(0) & 0xFF

if k == 27: # esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("dog-7514202_6400.png", img)
    cv2.destroyAllWindows();
































