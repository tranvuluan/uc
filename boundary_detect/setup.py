from setuptools import setup, find_packages

setup(
    name="boundary_detect",
    version="0.1.0",
    description="A module for detecting screen boundaries and seamlessly transitioning the cursor between devices.",
    author="Your Name",
    author_email="tranvuluan069@gmail.com",
    install_requires=[
        "pyautogui",
        "pygetwindow",
        "screeninfo",
        "pynput"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
