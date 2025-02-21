# Auto Snap Title Capture

**Auto Snap Title Capture** is a cross-platform, system-level application that detects when a screenshot or screen recording is taken and prompts the user to enter a title before saving it. Unlike browser-based solutions, this application works across the entire operating system, ensuring better control and organization of screen captures.

---

## 🚀 Features

- 📸 Detects screenshots and screen recordings in real-time.
- 📝 Prompts users to enter a title before saving captures.
- 💻 Works system-wide, not just within browsers.
- 🌍 Cross-platform compatibility (Windows, macOS, Linux).
- 🎨 Simple and intuitive user interface.

---

## 📥 Installation

To install the required dependencies, run:
`pip3 install -r requirements.txt`

---

## ▶️ Usage

To run the application directly, execute:
`python3 src/auto_snap_title_capture.py`


---

## 📦 Building the Application

This project supports creating a standalone application bundle for both macOS and Windows using **PyInstaller**.

1. Install the build dependency (if not already installed):
`pip3 install -r requirements.txt`

2. Build the application by running:
`pyinstaller --onefile --windowed src/auto_snap_title_capture.py`

The built application bundle will appear in the `dist` folder.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or improvements.

---

## 📸 Screenshots

<div style="display: flex; justify-content: center; gap: 40px;">
<div style="display: flex; flex-direction: column; align-items: center;">
 <p style="margin: 0; font-weight: bold;">As Is</p>
 <img src="images/as_is.png" alt="As Is Image" style="height: 250px; margin-top: 10px;" />
</div>
<div style="display: flex; flex-direction: column; align-items: center;">
 <p style="margin: 0; font-weight: bold;">To Be</p>
 <img src="images/to_be.png" alt="To Be Image" style="height: 250px; margin-top: 10px;" />
</div>
</div>

---

## 🙏 Acknowledgments

This project was inspired by a post on LinkedIn:
[Is there a program that will automatically capture window titles?](https://www.linkedin.com/posts/dangericke_is-there-a-program-that-will-automatically-activity-7297400112937414659-2pwo?utm_source=share&utm_medium=member_desktop&rcm=ACoAACSsjHQBIzh_KO1xQP5DJ08ul0x7C_cYedQ)

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
