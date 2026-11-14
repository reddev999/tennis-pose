# Tennis Pose Analysis

Analysing tennis strokes from video with pose estimation: tracking the
player's arm, measuring elbow angle and wrist speed, and filtering the
noisy signals.

**Status:** work in progress

## Progress
- [x] Step 1: pose detection on a single frame (MediaPipe)
- [ ] Step 2: pose tracking on video, saved to CSV
- [ ] Step 3: elbow angle and wrist speed
- [ ] Step 4: signal filtering

## Setup
1. Python 3.11+ and a virtual environment
2. `pip install opencv-python mediapipe numpy pandas scipy matplotlib`
3. Download the Pose Landmarker (Full) model from Google's MediaPipe
   guide into `models/`
4. Put your own image or video in `data/` (not included in the repo)

## Run
python src/step1_image.py

## Credits
Pose estimation: Google MediaPipe Pose Landmarker.
Video footage is not included for copyright reasons.