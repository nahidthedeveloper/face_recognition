import cv2
import os


def generate_dataset():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        cropped_faces = []
        for (x, y, w, h) in faces:
            cropped_faces.append(img[y:y + h, x:x + w])

        return cropped_faces

    id = input('Enter your ID: ')

    # Create 'data' folder if it doesn't exist
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    cap = cv2.VideoCapture(0)  # Use 0 for default webcam
    img_id = 0

    while True:
        ret, frame = cap.read()
        faces = face_cropped(frame)

        if faces:
            for face in faces:
                img_id += 1
                face = cv2.resize(face, (200, 200))
                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = f"data/user.{id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face_gray)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped face", face)

                if img_id >= 200:
                    break

        if cv2.waitKey(1) == 13 or img_id >= 200:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Collecting samples is completed....")


generate_dataset()
