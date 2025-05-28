# Hand Gesture Recognition Tool 🤖✋

A lightweight and efficient real-time hand gesture recognition tool using Python, OpenCV, and Mediapipe. This project allows gesture tracking through a webcam and lays the foundation for gesture-based user interfaces and interactive systems.

## 📸 Demo

![Demo](https://user-images.githubusercontent.com/your-demo-gif-or-image.gif)  
*Example: Real-time finger counting using webcam*

## 🚀 Features

- 🔍 Real-time hand tracking
- 🖐️ Finger counting and basic gesture recognition
- ⚙️ Built with OpenCV and Google Mediapipe
- 🧩 Easily extendable to custom gestures or commands
- 🖥️ Simple UI for gesture testing and debugging

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**: OpenCV, Mediapipe
- **Runtime**: Works with most webcams and standard Python environments

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/janithsuraweera/hand-gesture-recognition-tool.git
   cd hand-gesture-recognition-tool
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   python main.py
   ```

> **Note:** Make sure your webcam is connected and accessible by your system.

## 🧠 How It Works

* Mediapipe’s Hand Tracking module detects hand landmarks.
* Finger tips and joints are analyzed to determine which fingers are raised.
* Logic is applied to count fingers and detect basic gestures.

## 💡 Potential Use Cases

* Touchless UI control
* Virtual presentations
* Gaming/AR/VR gesture interfaces
* Assistive technologies (e.g., sign language input)

## 🖼️ Screenshots

| Gesture Detection                        | Finger Counting                              |
| ---------------------------------------- | -------------------------------------------- |
| ![screenshot1](screenshots/gesture1.png) | ![screenshot2](screenshots/finger_count.png) |

## 📂 Project Structure

```
hand-gesture-recognition-tool/
│
├── main.py                 # Entry point
├── gestures.py             # Gesture logic
├── utils/                  # Helper functions (e.g., drawing, detection)
├── screenshots/            # Sample output images
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open-source under the [MIT License](LICENSE).

## 👤 Author

Developed by [Janith Suraweera](https://github.com/janithsuraweera)

---

Feel free to customize the content, add demo videos or screenshots to the `screenshots/` folder, and update links as needed.

```

---

Let me know if you'd like help creating demo GIFs, screenshots, or setting up GitHub Pages for this project!
```
