#!/usr/bin/env python
import PySimpleGUI as sg
from m_sailing_as_GUI_module import M_Sailing


sg.theme('Topanga')


layout = [[sg.Text('By Michael Mulkern V1.1', size=(20,1), font=("Bookman", 8))],
		  [sg.Text('Start Position:')],
          [sg.Text('Lat-1', size=(5, 1)),sg.Input(key='-DEG1-', size=(5,1)),
          sg.Text('-', size=(0, 1)),sg.Input(key='-SEC1-', size=(5,1)),sg.Drop(key='c1', values=('n', 's'), size=(2,1))],
          

          [sg.Text('Lon-1', size=(5, 1)),sg.Input(key='-DEG2-', size=(5,1)),
          sg.Text('-', size=(0, 1)),sg.Input(key='-SEC2-', size=(5,1)),sg.Drop(key='c2',values=('e', 'w'), size=(2,1))],
  
  		  [sg.Text('\nEnd Position:')],
          [sg.Text('Lat-2', size=(5, 1)),sg.Input(key='-EDEG1-', size=(5,1)),
          sg.Text('-', size=(0, 1)),sg.Input(key='-ESEC1-', size=(5,1)),sg.Drop(key='c3',values=('n', 's'), size=(2,1))],
          
          
          [sg.Text('Lon-2', size=(5, 1)),sg.Input(key='-EDEG2-', size=(5,1)),
          sg.Text('-', size=(0, 1)),sg.Input(key='-ESEC2-', size=(5,1)),sg.Drop(key='c4',values=('e', 'w'), size=(2,1))],

		  [sg.Text(key='-OUTPUT-', size=(30, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
         # [sg.Text(f"Distance is {ms.departure()} NM.")],
          [sg.Button('Calculate'), sg.Button('Exit')]]

window = sg.Window('Mercator Sailing', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    try:
        if event == 'Calculate':
            # Update the "output" text element to be the value of "input" element
            degs1 = int(values['-DEG1-'])
            secs1 = float(values['-SEC1-'])
            decidegs1 = (secs1 / 60) + degs1

            degs2 = int(values['-DEG2-'])
            secs2 = float(values['-SEC2-'])
            decidegs2 = (secs2 / 60) + degs2

            edegs1 = int(values['-EDEG1-'])
            esecs1 = float(values['-ESEC1-'])
            edecidegs1 = (esecs1 / 60) + edegs1

            edegs2 = int(values['-EDEG2-'])
            esecs2 = float(values['-ESEC2-'])
            edecidegs2 = (esecs2 / 60) + edegs2

            c1 = values['c1'].lower()
            c2 = values['c2'].lower()
            c3 = values['c3'].lower()
            c4 = values['c4'].lower()

            directionTest = [c1,c2,c3,c4]
            directionsList = ['n','s','e','w']
            for direction in directionTest:
                if(direction not in directionsList):
                    window['-OUTPUT-'].update("Please enter N, S, E, or W")
                else:
                    answer = M_Sailing(decidegs1, c1, decidegs2, c2, edecidegs1, c3, edecidegs2, c4)

                    window['-OUTPUT-'].update(answer.m_run())
    except:
        window['-OUTPUT-'].update("Please enter valid positions")

window.close()



