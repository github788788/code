exec(open('util.py').read())

from pywinauto import Desktop
import time

def alt_tab():
    desktop = Desktop(backend="uia")
    desktop.send_keys("%{TAB}")  # Sends Alt+Tab

if __name__ == "__main__":
    # Sleep for a few seconds to give you time to switch to the desired window
    #time.sleep(5)
    # Perform Alt+Tab
    alt_tab()
