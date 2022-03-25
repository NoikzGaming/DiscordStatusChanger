from asyncio.windows_events import NULL
import os
import time
from pypresence import Presence as status
import PySimpleGUI as sg

debugMode = False

sg.theme('DarkAmber')

filePath = os.path.dirname(__file__) + "/savedStatus.txt"
if debugMode == True:
    print(filePath)

try:
    f = open(filePath, "r")
    line_numbers = [0]
    lines = ""
    Text1 = ""
    for i, line in enumerate(f):
        if i in line_numbers:
            lines = (line.strip())
            if debugMode == True:
                if debugMode == True:
                    print(lines)
            Text1 = lines

    f = open(filePath, "r")
    line_numbers2 = [1]
    lines2 = ""
    Text2 = ""
    for i, line in enumerate(f):
        if i in line_numbers2:
            lines2 = (line.strip())
            if debugMode == True:
                if debugMode == True:
                    print(lines2)
            Text2 = lines2
    f = open(filePath, "r")
    line_numbers3 = [2]
    lines3 = ""
    Text3 = ""
    for i, line in enumerate(f):
        if i in line_numbers3:
            lines3 = (line.strip())
            if debugMode == True:
                print(lines3)
            Text3 = lines3
    f = open(filePath, "r")
    line_numbers4 = [3]
    lines4 = ""
    Text4 = ""
    for i, line in enumerate(f):
        if i in line_numbers4:
            lines4 = (line.strip())
            if debugMode == True:
                print(lines4)
            Text4 = lines4
    f = open(filePath, "r")
    line_numbers5 = [4]
    lines5 = ""
    Text5 = ""
    for i, line in enumerate(f):
        if i in line_numbers5:
            lines5 = (line.strip())
            if debugMode == True:
                print(lines5)
            Text5 = lines5
    f = open(filePath, "r")
    line_numbers6 = [5]
    lines6 = ""
    Text6 = ""
    for i, line in enumerate(f):
        if i in line_numbers6:
            lines6 = (line.strip())
            if debugMode == True:
                print(lines6)
            Text6 = lines6
except: 
    f = open(filePath, "w")
    f.write("\n\n\n\n\n")
    try:
        f = open(filePath, "r")
        line_numbers = [0]
        lines = ""
        Text1 = ""
        for i, line in enumerate(f):
            if i in line_numbers:
                lines = (line.strip())
                if debugMode == True:
                    print(lines)
                Text1 = lines

        f = open(filePath, "r")
        line_numbers2 = [1]
        lines2 = ""
        Text2 = ""
        for i, line in enumerate(f):
            if i in line_numbers2:
                lines2 = (line.strip())
                if debugMode == True:
                    print(lines2)
                Text2 = lines2
        f = open(filePath, "r")
        line_numbers3 = [2]
        lines3 = ""
        Text3 = ""
        for i, line in enumerate(f):
            if i in line_numbers3:
                lines3 = (line.strip())
                if debugMode == True:
                    print(lines3)
                Text3 = lines3
        f = open(filePath, "r")
        line_numbers4 = [3]
        lines4 = ""
        Text4 = ""
        for i, line in enumerate(f):
            if i in line_numbers4:
                lines4 = (line.strip())
                if debugMode == True:
                    print(lines4)
                Text4 = lines4
        f = open(filePath, "r")
        line_numbers5 = [4]
        lines5 = ""
        Text5 = ""
        for i, line in enumerate(f):
            if i in line_numbers5:
                lines5 = (line.strip())
                if debugMode == True:
                    print(lines5)
                Text5 = lines5
        f = open(filePath, "r")
        line_numbers6 = [5]
        lines6 = ""
        Text6 = ""
        for i, line in enumerate(f):
            if i in line_numbers6:
                lines6 = (line.strip())
                if debugMode == True:
                    print(lines6)
                Text6 = lines6
    except: sg.popup("Failed to open")

def main():
    column_to_be_centered = [
                [sg.Text('Text 1 ex: "Join the discord server!"')],
                [sg.InputText(Text1)],
                [sg.Text('Text 2 ex: "Click on the button!"')],
                [sg.InputText(Text2)],
                [sg.Text('Button 1 Text')],
                [sg.InputText(Text3)],
                [sg.Text('Button 1 Link')],
                [sg.InputText(Text4)],
                [sg.Text('Button 2 Text')],
                [sg.InputText(Text5)],
                [sg.Text('Button 2 Link')],
                [sg.InputText(Text6)],
                [sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Change Status'),
                sg.Button('Save')],
                ]

    layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
              [sg.Text('', pad=(0,0),key='-EXPAND2-'),              # the thing that expands from left
               sg.Column(column_to_be_centered, vertical_alignment='center', justification='center',  k='-C-')]]

    window = sg.Window('Custom Status Changer', layout, resizable=True,finalize=True)
    window['-C-'].expand(True, True, True)
    window['-EXPAND-'].expand(True, True, True)
    window['-EXPAND2-'].expand(True, False, True)

    start = int(time.time())
    try:
        sg.popup('Connecting to Discord\n\nPlease wait a few seconds while its connecting!')
        rpc = status(928615823352942634)
        rpc.connect()
    except: 
        sg.popup("Discord is not running!\n\nClosing program!")
        window.close()


    while True:             # Event Loop
        event, values = window.read()
        if debugMode == True:
            print(event, values)
        if event == sg.WIN_CLOSED:
            rpc.close()
            break
        if event == 'Change Status':
            try:
                rpc.update(
                    state=values[0],
                    details=values[1],
                    large_image="main",
                    buttons = [{"label": values[2], "url": values[3]}, {"label": values[4], "url": values[5]}],
                    start = start
                    )
            except: sg.popup("Invalid Status")
        if event == 'Save':
            if values[0] != "":
                if values[1] != "":
                    if values[2] != "": 
                        if values[3] != "":
                            if values[4] != "":
                                if values[5] != "":
                                    with open(filePath, 'w') as f:
                                        f.write(values[0] + '\n' +
                                        values[1] + '\n' +
                                        values[2] + '\n' +
                                        values[3] + '\n' +
                                        values[4] + '\n' +
                                        values[5])
if __name__ == '__main__':
    main()