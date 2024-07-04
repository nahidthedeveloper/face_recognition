import cv2


def draw_boundary(image, classifier, scale_factor, min_neighbors, color, text, cl_fier):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scale_factor, min_neighbors)

    for (x, y, w, h) in features:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

        # Perform prediction and compute confidence
        user_id, pred = cl_fier.predict(gray_img[y:y + h, x:x + w])
        confidence = int(100 * (1 - pred / 300))  # Calculate confidence level

        # Display ID or 'UNKNOWN' based on confidence
        if confidence > 70:
            cv2.putText(image, f"ID: {user_id} - {confidence}%", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1,
                        cv2.LINE_AA)
        else:
            cv2.putText(image, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    return image


# loading classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

video_capture = cv2.VideoCapture(0)  # Use index 0 for the first camera

while True:
    ret, img = video_capture.read()
    img = draw_boundary(img, faceCascade, 1.3, 6, (255, 255, 255), "Face", clf)
    cv2.imshow("Face Detection", img)

    if cv2.waitKey(1) == 13:  # Enter key to exit
        break

video_capture.release()
cv2.destroyAllWindows()
