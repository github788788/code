exec(open('util.py').read())

#where = click_logo4(["paperclip4.png"])
import pyautogui
def find_image_on_screen(image_path):
    # Locate the center coordinates of the image on the screen
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path)
        print(f"Image found at coordinates: ({x}, {y})")
    except Exception as e:
        print("Image not found on the screen.")
    back = [x,y]
    return back
image_path = 'paperclip4.png'  # Path to the image you want to find
coordinates = find_image_on_screen(image_path)
print(coordinates)
x_coordinate = coordinates[0]
y_coordinate = coordinates[1]
pyautogui.click(x_coordinate,y_coordinate)


end()

if __name__ == "__main__":
    image_path = 'paperclip4.png'  # Path to the image you want to find
    find_image_on_screen(image_path)
    print(image_path[0])
    """
    x_coordinate = image_path[0][0]
    y_coordinate = image_path[0][1]
    pyautogui.click(x_coordinate,y_coordinate)
    """