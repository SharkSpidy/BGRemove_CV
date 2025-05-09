# BGRemove_CV

### Project Description
Just a simple background changer! Just resize your images to 640x480 and you can simply drag and drop it into the BG folder and run the Code! You get a window with both your Original Camera feed and then a window with the replaced background attached to it!

## Technical Details
### Technologies/Components Used
##### For Software:
    Languages: Python
    Frameworks: OpenCV, MediaPipe
    Libraries: cvzone, numpy
    Tools: Visual Studio Code, Python virtual environments

##### For Hardware:
    Main Component: Webcam (internal/external)
    Specs: 720p or better for best results


### Implementation
##### Installation
```bash
# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

# Install dependencies
pip install cvzone mediapipe numpy
```
##### Run  
```bash
python main.py
```


### Project Documentation
For Software:
- `main.py` — Main program for hand tracking and volume control  
- `HandTrackingModule.py` — Custom wrapper around MediaPipe for easier hand landmark detection  
- `.venv/` — Python virtual environment (not required to be pushed to GitHub)  


# Screenshots
![Screenshot1](https://github.com/SharkSpidy/BGRemove_CV/blob/main/Media/Screenshot%202025-04-25%20191532.png)

![Screenshot2](https://github.com/SharkSpidy/BGRemove_CV/blob/main/Media/Screenshot%202025-04-25%20191542.png)

![Screenshot3](https://github.com/SharkSpidy/BGRemove_CV/blob/main/Media/Screenshot%202025-04-25%20191741.png)

### Project Demo
# Video
[Video](https://github.com/SharkSpidy/BGRemove_CV/blob/main/Media/Screen%20Recording%202025-04-25%20191637.mp4)

---
Made with ❤️ by [Joe](https://bento.me/SharkSpidy)
