import PySimpleGUI as sg
import characterclass as ch 

# name = input("enter name:")
# race = input("enter race:")
name = "Steve"
race = "Human"
player1 = ch.CharacterClass(name,race)
player1.showStats()



sg.theme('DarkAmber')
layout = [  
                [sg.Text('Name: '+player1.name)], 
                [sg.Text('Race: '+player1.race)], 
                [sg.Text('Strength: '+str(player1.stre))],
                [sg.Text('Dexterity: '+str(player1.dext))],
                [sg.Text('Constitution: '+str(player1.cons))],
                [sg.Text('Intelligence: '+str(player1.inte))],
                [sg.Text('Wisdom: '+str(player1.wisd))],
                [sg.Text('Charisma: '+str(player1.char))],
                [sg.Button('Re-Roll Stats',player1.rerollStats())],
                [sg.Button('Close')]
            ]
  
window = sg.Window(
    title="Stats",  
    layout=layout
    )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    
window.close()