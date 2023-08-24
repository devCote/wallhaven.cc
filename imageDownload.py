import pyautogui
import keyboard
import pytesseract
from PIL import Image

mousePos=[[968, 649],[1014, 830],[1011, 692],[1059, 830]]
target_text = "Download"
isFound = True 

def find_and_move_to_download():
    global isFound
    
    try:
        data = pytesseract.image_to_data(pyautogui.screenshot())
        lines = data.strip().split("\n")

        x, y = None, None
        for line in lines:
            if target_text in line:
                fields = line.split()
                x = int(fields[6])
                y = int(fields[7])
                break

        if x is not None and y is not None:
            pyautogui.moveTo(x, y, .3)
        else:
            isFound = False
            print("possition not found")
            
    except pytesseract.TesseractNotFoundError:
        print("Tesseract not found. Please specify the correct path to Tesseract executable.")
        isFound = False
        return

def click():
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def wait(sec):
    pyautogui.sleep(sec)

def pos(pos):
    pyautogui.moveTo(pos[0], pos[1], .3)

def mouse_Interaction(mpos):
    pos(mpos)
    wait(1)
    click()
    
print("Press 'S' to start script")
keyboard.wait("s")

while isFound:
    wait(1)
    find_and_move_to_download()
    click()
    wait(.5)
    mouse_Interaction(mousePos[0])
    mouse_Interaction(mousePos[1])
    mouse_Interaction(mousePos[2])
    mouse_Interaction(mousePos[3])
    wait(1)
    pyautogui.keyDown('Ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('Ctrl')

