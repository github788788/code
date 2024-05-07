exec(open('util.py').read())

import pygetwindow as gw
import pyautogui

def get_window_names():
    return [window.title for window in gw.getAllWindows()]

def activate_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].activate()
        else:
            print(f"Window '{window_title}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
window_names = get_window_names()
pri(window_names)
end()
print("Available Windows:", window_names)

# Activate a specific window by its title
activate_window("Calculator")
