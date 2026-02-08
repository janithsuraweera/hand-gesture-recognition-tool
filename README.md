# Hand Gesture Recognition Tool 

A lightweight and efficient real-time hand gesture recognition tool using Python, OpenCV, and Mediapipe. This project allows gesture tracking through a webcam and lays the foundation for gesture-based user interfaces and interactive systems.

## Features

- 🔍 Real-time hand tracking
- 🖐️ Finger counting and basic gesture recognition
- ⚙️ Built with OpenCV and Google Mediapipe
- 🧩 Easily extendable to custom gestures or commands
- 🖥️ Simple UI for gesture testing and debugging

##  Tech Stack

- **Language**: Python
- **Libraries**: OpenCV, Mediapipe
- **Runtime**: Works with most webcams and standard Python environments
  

##  Features

* **Real-time Tracking:** High-speed hand landmark detection.
* **Finger Counting:** Accurately counts how many fingers are raised.
* **Gesture Recognition:** Detects specific patterns for touchless interaction.
* **Visual Feedback:** On-screen overlays showing detection results.

##  Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/janithsuraweera/hand-gesture-recognition-tool.git]
cd hand-gesture-recognition-tool

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Run the Application

```bash
python main.py
```

> **Note:** Make sure your webcam is connected and accessible by your system.

---

## How It Works

* **MediaPipe Hand Tracking:** Utilizes a pre-trained ML model to locate 21 hand landmarks (joints).
* **Geometric Analysis:** Calculates the relative positions of finger tips vs. joints to determine if a finger is "open" or "closed."
* **Gesture Logic:** Custom algorithms in `gestures.py` map these finger states to specific actions.

## Potential Use Cases

* **Touchless UI:** Control software without physical contact.
* **Presentations:** Switch slides using hand movements.
* **Gaming:** Simple gesture-based controls for AR/VR.
* **Accessibility:** Assistive tools for individuals with mobility challenges.

---

## Project Structure

```text
hand-gesture-recognition-tool/
│
├── main.py               # Main entry point for the application
├── gestures.py           # Core logic for gesture identification
├── utils/                # Helper functions for drawing and processing
├── screenshots/          # Documentation images
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation

```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source under the [MIT License](https://www.google.com/search?q=LICENSE).

## Author

Developed by **Janith Suraweera** GitHub: [@janithsuraweera](https://github.com/janithsuraweera)



