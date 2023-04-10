"""
    Demo Command Line Application or GUI Application

    If your program is run with arguments, then a command line version is used.
    If no arguments are given, then a GUI is shown that asks for a filename.

    http://www.PySimpleGUI.org
    Copyright 2022 PySimpleGUI
"""

import PySimpleGUI as sg
import sys

def main_cli(filename):
    print(f'Your filename = {filename}')

def callback_function1():
    filename = sg.popup_get_file('Please enter a filename:')
    main_cli(filename)

def callback_function2():
    sg.popup('In Callback Function 2')
    print('In the callback function 2')
def main_gui():
    layout = [[sg.Text('Demo of Button Callbacks')],
            [sg.Button('Button 1'), sg.Button('Button 2')]]

    window = sg.Window('Button Callback Simulation', layout)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Button 1':
            callback_function1()        # call the "Callback" function
        elif event == 'Button 2':
            callback_function2()        # call the "Callback" function

    window.close()    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main_gui()
    else:
        main_cli(sys.argv[1])