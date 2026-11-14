import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent   # the tennis-pose folder

base = python.BaseOptions(model_asset_path="models/pose_landmarker_full.task")
options = vision.PoseLandmarkerOptions(base_options=base, num_poses=4)
detector = vision.PoseLandmarker.create_from_options(options)

image = mp.Image.create_from_file("data/frame.jpg")      # <- real file name
result = detector.detect(image)
print("people found:", len(result.pose_landmarks))

img = cv2.imread("data/frame.jpg")                        # <- same name
h, w = img.shape[:2]


def pick_near_player(result):
    """Return the landmarks of the person lowest in the image (the near player)."""
    if len(result.pose_landmarks) == 0:
        return None                     # nobody detected

    best_person = None
    best_avg_y = -1
    for person in result.pose_landmarks:
        avg_y = sum(lm.y for lm in person) / len(person)   # average height in the image
        if avg_y > best_avg_y:                              # lower in image = nearer
            best_avg_y = avg_y
            best_person = person
    return best_person
person=pick_near_player(result)
for person in result.pose_landmarks:
    for i, lm in enumerate(person):
        x = int(lm.x * w)
        y = int(lm.y * h)
        if i in (12, 14, 16):
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        cv2.circle(img, (x, y), 4, color, -1)

cv2.imwrite("outputs/step1_pose.png", img)