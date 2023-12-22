# RealTime FaceSwap

RealTime FaceSwap is a Python project that leverages computer vision and image processing techniques to perform real-time face swapping through your webcam. The application uses facial landmarks detection to identify key points on your face, aligns the source and destination faces, warps the source face to match the shape of the destination face, and blends the two faces seamlessly, creating a live face-swapping experience.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- Python (recommended version 3.10)
- pip (package installer for Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/heyitspratik/RealTime-FaceSwap.git

2. Create virtual env and install required packages using below command:

   ```bash
   pip install -r requirements.txt

3. Download the shape predictor file:
   - in our main faceswap_realtime.py file, there is one file called shape_predictor_68_face_landmarks.dat which you can download from (download might take some time):

     http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

4. Run the script with:

   ```bash
   python faceswap_realtime.py
   
