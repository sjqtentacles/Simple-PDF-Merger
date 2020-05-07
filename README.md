# PDF Merger

## Description
Built using PyPDF2 for pdf manipulation, and PySimpleGUI for the GUI.

Sadly it's TKinter so it looks like shit, but it's pretty speedy, and super simple.

![](screen.png)

## How it works
It takes in a directory, sorts all the files ending in `.pdf`, and merges them in that order. It writes to the output of the python program as `merged-files.pdf`.


## How to Install
1. Download zip, unzip, cd into project directory
2. `python3 -m venv myenv & source myenv/bin/activate & pip3 install -r requirements.txt`
3. `sudo pyinstaller --onefile --noconsole --paths=myenv/lib/python3.7/site-packages/  main.py`
