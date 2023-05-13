"""'
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18

"""

import cv2
import numpy as np
from Speaker import speak

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
cascadePath = "FacialRecognitionhaarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
# names = ['None', 'Ashiq', 'None', 'Dharshenee',
#         'Keerthana', 'KD Prince', 'Antony', 'Dharshanaa']
# names = {'items': 1}
# names = ['None', 'Sasikumar', 'Gopalakrishnan', 'Brindha', 'Sharath Chandhar']
# names = ['None', 'Sharath Chandhar', 'Sharath Chandhar', 'Sharath Chandhar']
names = [
    "None",
    "None",
    "hi doctor p s s srinivasan",
    "None",
    "hi doctor rajhendran",
    "hello doctor thanghavhel",
]
# names = ['None', 'Ashiq', 'Gowtham']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip horizontlly

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

        id, confidence = recognizer.predict(gray[y : y + h, x : x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        """if (confidence < 100):
            if (id == 1):
                id = 'Ashiq'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))

            elif (id == 3):
                id = 'Dharshini'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))

            elif (id == 4):
                id = 'Keerthana'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))

            elif (id == 5):
                id = 'KD Prince'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))

            elif (id == 6):
                id = 'Antony Daniel'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))

            elif (id == 7):
                id = 'Dharshana'
                if ((str(id)) not in names):
                    names[str(id)] = str(id)
                    confidence = "  {0}%".format(round(100 - confidence))"""

        if confidence < 70:
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            speak(str(id))
            speak(
                "sir, I cordially welcome you to our department association inauguration, VIBES , Thank you for your wonderful presence!!"
            )
            # speak("This is chimera, if you are willing, we can interact some time about our college and department for a while.")
            break

        else:
            id = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            speak("Welcome to our dapartment association inauguration")

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow("camera", img)

    k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
    if k == 27:
        break


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
