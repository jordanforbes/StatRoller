import PySimpleGUI as sg
import statroller as cc

open = False
sg.theme('DarkAmber')
layout = [  
                [sg.Text('Name: '+cc.player1.name)], 
                [sg.Text('Race: '+cc.player1.race)], 
                [sg.Text('Strength: '+str(cc.player1.stre))],
                [sg.Text('Dexterity: '+str(cc.player1.dext))],
                [sg.Text('Constitution: '+str(cc.player1.cons))],
                [sg.Text('Intelligence: '+str(cc.player1.inte))],
                [sg.Text('Wisdom: '+str(cc.player1.wisd))],
                [sg.Text('Charisma: '+str(cc.player1.char))],
                [sg.Button('Re-Roll Stats',cc.player1.rerollStats())],
                [sg.Button('Close')]
            ]
  
window = sg.Window(
    title="Stats",  
    layout=layout
    )

while open == True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    
window.close()