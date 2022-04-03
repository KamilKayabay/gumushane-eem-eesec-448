import cv2
cap = cv2.VideoCapture(0)
k = 1
i = 1
while True:
    ret, frame = cap.read()
    text = 'Frame #%i' %k
    k = k+1
    frame = cv2.putText(frame, text, (30,50), 1, 2, (255, 0, 0), 1, 1)
    cv2.imshow('web kamerasi video', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'): # eğer bir an bile c'ye basarsa
        text = 'web kamerasi resim %i.jpg' %i
        cv2.imwrite(text, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('web kamerası resmi %s ismiyle dosyaya kaydedildi.' %text)
        i = i+1
    elif cv2.waitKey(1) & 0xFF == ord('q'): # eğer bir an bile q'ye basarsa:
        break
cap.release()
cv2.destroyAllWindows()