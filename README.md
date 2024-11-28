# Face Recognition Attendance System

## Overview
This project implements a **Face Recognition Attendance System** that automatically marks attendance by recognizing faces in real-time. It leverages computer vision and machine learning techniques to identify individuals and maintain an attendance record in a CSV file.

---

## Features
- **Face Detection and Recognition:** Recognizes faces from live video feeds or images.
- **Attendance Marking:** Automatically logs attendance into an `Attendance.csv` file with timestamps.
- **Image Dataset Capture:** Captures and stores images for training the recognition model.
- **Face Encoding:** Converts faces into numerical representations for accurate matching.
- **Custom Names Support:** Maps face encodings to individual names.

---

## Folder and File Structure
```
FR/
|
├── dataset/                # Folder for storing captured face images
├── Attendance.csv          # CSV file for recording attendance
├── capture_images.py       # Script to capture images for training
├── class_names.npy         # NumPy file for storing class (names) data
├── encoded_faces.npy       # NumPy file for storing encoded face data
├── encode_faces.py         # Script to encode face images into embeddings
├── mark_attendance.py      # Script to mark attendance based on recognition
├── recognize_faces.py      # Real-time face recognition script
├── README.md               # Project documentation
└── __pycache__/            # Compiled Python files
```

---

## Tech Stack
- **Programming Language:** Python
- **Libraries and Tools:**
  - OpenCV
  - NumPy
  - face_recognition
  - Pandas (for CSV operations)

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arishsaifi/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scripts:**
   - Capture images for training:
     ```bash
     python capture_images.py
     ```
   - Encode face images:
     ```bash
     python encode_faces.py
     ```
   - Start face recognition for attendance:
     ```bash
     python recognize_faces.py
     ```

---

## Usage

1. **Capture Images:**
   - Use the `capture_images.py` script to collect face data for individuals.
   - Images will be saved in the `dataset/` folder.

2. **Encode Faces:**
   - Run `encode_faces.py` to generate face encodings and save them in `encoded_faces.npy`.

3. **Mark Attendance:**
   - Execute `recognize_faces.py` to recognize faces and update `Attendance.csv` in real-time.

4. **CSV File:**
   - Attendance is logged in the `Attendance.csv` file with timestamps.

---

## Future Enhancements
- Add support for integrating with a database (e.g., MySQL or Firebase).
- Implement deep learning models for improved face recognition accuracy.
- Develop a graphical user interface (GUI) for ease of use.
- Expand to mobile and web platforms.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any queries or collaboration opportunities, reach out to:
- **Name:** Harish Saifi
- **Email:** harishsaifi2003@gmail.com
- **LinkedIn:** [http://www.linkedin.com/in/arishsaifi](http://www.linkedin.com/in/arishsaifi)
- **Website:** [https://www.harishsaifi.netlify.app/](https://www.harishsaifi.netlify.app/)

---

## Acknowledgments
Special thanks , if you work with this project.


