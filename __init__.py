def write(write):
    print(write)


def talk(talk):
    import pyttsx3
    pyttsx3.speak(talk)


def take(take):
    input(take)


def time():
    import datetime
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strtime)


def keyboard(write_something):
    import pyautogui
    import time

    time.sleep(3)
    pyautogui.typewrite(write_something)


def web(website_link):
    import webbrowser
    webbrowser.open(website_link)


def open_app(file_path):
    import os
    os.startfile(file_path)
def pip(module_name):
    import os
    import pyautogui as py
    import time

    os.startfile(r"C:\WINDOWS\system32\cmd.exe")
    time.sleep(3)
    py.typewrite(f"pip install {module_name}")
    py.press("enter")