from setuptools import setup

APP = ["src/auto_title_capture.py"]
DATA_FILES = []
OPTIONS = {
    "packages": ["watchdog", "pynput"],
    "plist": {
        "CFBundleName": "Screen Detector",
        "CFBundleShortVersionString": "1.0.0",
        "CFBundleVersion": "1.0.0",
        "CFBundleIdentifier": "com.yourname.screendetector",
        "LSUIElement": True,
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
