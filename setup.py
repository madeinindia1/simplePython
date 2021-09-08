from setuptools import _install_setup_requires, setup
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup(
    name="simplePython",
    version="1.0.0",
    author="Srikar(madeinindia1)",
    author_email="madeinindiasrikar@gmail.com",
    install_requires=['os',
                     'datetime',
                     'pyautogui'],
)