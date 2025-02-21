import os
import re
import time
import platform
import logging
import subprocess
from watchdog.observers.polling import PollingObserver  # More reliable detection
from watchdog.events import FileSystemEventHandler
from pynput import keyboard

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def sanitize_filename(name):
    """Removes unsafe characters from a filename."""
    # Remove any character that is not alphanumeric, a space, dash or underscore.
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip()

def get_screenshot_folder():
    """Returns the actual screenshot folder based on macOS system settings."""
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
    elif system == "Darwin":  # macOS
        try:
            result = subprocess.run(
                ["defaults", "read", "com.apple.screencapture", "location"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            folder = result.stdout.strip()
            if folder and os.path.exists(folder):
                return folder
            else:
                return os.path.expanduser("~/Desktop")  # Fallback
        except Exception as e:
            logging.error(f"Error reading screenshot folder: {e}")
            return os.path.expanduser("~/Desktop")  # Default if command fails
    else:
        return None

def get_screen_recording_folder():
    """Returns the default screen recording folder on macOS."""
    return os.path.expanduser("~/Desktop")  # Default location for recordings

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or os.path.basename(event.src_path).startswith("."):
            return

        # Delay to allow macOS to finalize the file
        time.sleep(1)

        lower_path = event.src_path.lower()
        if lower_path.endswith(".png"):
            logging.info(f"📸 Screenshot detected: {event.src_path}")
            prompt_for_title(event.src_path)
        elif lower_path.endswith(".mov"):
            logging.info(f"🎥 Screen recording detected: {event.src_path}")
            prompt_for_title(event.src_path)

def prompt_for_title(filepath):
    """Shows a macOS pop-up to ask for a screenshot or screen recording title."""
    try:
        result = subprocess.run(
            ['osascript', '-e',
             'display dialog "Enter a title for your file:" default answer "" '
             'with title "File Detected" buttons {"OK"} default button "OK"'],
            stdout=subprocess.PIPE, text=True
        )
        new_title = result.stdout.strip()

        if "button returned:OK, text returned:" in new_title:
            new_title = new_title.split("text returned:")[-1].strip()
            new_title = sanitize_filename(new_title)
            if new_title:
                rename_file(filepath, new_title)
            else:
                logging.info("No valid title provided.")
    except Exception as e:
        logging.error(f"Error prompting for title: {e}")

def rename_file(filepath, title):
    """Renames the file with the user-provided title safely."""
    directory = os.path.dirname(filepath)
    ext = os.path.splitext(filepath)[1]
    new_filepath = os.path.join(directory, f"{title}{ext}")

    # Prevent overwriting existing files by appending a counter if needed
    counter = 1
    while os.path.exists(new_filepath):
        new_filepath = os.path.join(directory, f"{title}_{counter}{ext}")
        counter += 1

    try:
        os.rename(filepath, new_filepath)
        logging.info(f"✅ Renamed to: {new_filepath}")
    except Exception as e:
        logging.error(f"Failed to rename {filepath}: {e}")

def monitor_folders():
    """Watches both screenshot and screen recording folders for new files."""
    screenshot_folder = get_screenshot_folder()
    recording_folder = get_screen_recording_folder()

    if not screenshot_folder or not os.path.exists(screenshot_folder):
        logging.warning("⚠️ Screenshot folder not found! Check macOS settings.")
        return
    if not recording_folder or not os.path.exists(recording_folder):
        logging.warning("⚠️ Screen recording folder not found! Check macOS settings.")
        return

    logging.info(f"🔍 Monitoring screenshots in: {screenshot_folder}")
    logging.info(f"🔍 Monitoring screen recordings in: {recording_folder}")

    event_handler = ScreenshotHandler()
    observer = PollingObserver()
    observer.schedule(event_handler, screenshot_folder, recursive=False)
    observer.schedule(event_handler, recording_folder, recursive=False)
    observer.start()
    logging.info("✅ Monitoring started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping observer due to KeyboardInterrupt.")
        observer.stop()
    observer.join()

def detect_screenshot_keys():
    """Detects common screenshot key presses (macOS & Windows)."""
    def on_press(key):
        try:
            if key == keyboard.Key.print_screen:
                logging.info("🖼️ PrintScreen key detected!")
            elif key == keyboard.Key.cmd:
                logging.info("⌘ Cmd key pressed")
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

if __name__ == "__main__":
    # Uncomment the following line to enable key detection.
    # detect_screenshot_keys()
    monitor_folders()