import sys
from setuptools import setup, find_packages

name = "auto-title-capture"
version = "1.0.0"

# Common setup options
common_options = dict(
    name=name,
    version=version,
    description="A cross-platform application for capturing titles from screens.",
    author="Az Muth",
    author_email="aziyatalik4@gmail.com",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "watchdog",
        "pynput",
    ],
    python_requires='>=3.6',
)

if sys.platform == "darwin":
    # macOS: use py2app to build a native application bundle
    setup(
        app=["src/auto_title_capture.py"],
        setup_requires=["py2app"],
        options={
            "py2app": {
                "argv_emulation": True,
                "plist": {
                    "CFBundleName": name,
                    "CFBundleShortVersionString": version,
                    "CFBundleVersion": version,
                    "CFBundleIdentifier": "com.yourname.autotitlecapture",
                },
            }
        },
        **common_options
    )
elif sys.platform == "win32":
    # Windows: use a console script entry point
    setup(
        entry_points={
            'console_scripts': [
                'auto-title-capture=auto_title_capture:main',
            ],
        },
        **common_options
    )
else:
    # Fallback for other platforms
    setup(**common_options)