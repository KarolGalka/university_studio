import PySimpleGUI as sg


def get_username_gui():
    layout = [[sg.Text('My one-shot window.')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Window Title', layout)
    event, values = window.Read()
    window.Close()
    twitter_username = values[0]
    return twitter_username
x = get_username_gui()
