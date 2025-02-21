# Auto Snap Title Capture

Auto Title Capture is a cross-platform application designed to capture and manage window titles efficiently. This project is built using Python 3 and is intended for users who need to monitor and log window titles for various applications.

## Features

- Detects active window titles in real-time.
- Cross-platform compatibility (Windows, macOS, Linux).
- Simple and intuitive user interface.

## Installation

To install the required dependencies, run:

`pip3 install -r requirements.txt`

## Usage

To run the application directly, execute:

`python3 src/auto_title_capture.py`

## Building the Application

This project supports creating standalone application bundles for both macOS and Windows.

### macOS

The project uses `py2app` to build a native macOS application bundle. To create the macOS app, run:

`python3 setup.py py2app`

The built application bundle will be located in the `dist` folder.

### Windows

On Windows, a console script entry point is defined. You can build a standalone executable using [PyInstaller](https://pyinstaller.org/). For example, run:

`pyinstaller --onefile --windowed src/auto_title_capture.py`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
