import PySimpleGUI as sg


def get_username():
    layout = [[sg.Text('What is your Twitter nickname?')],
              [sg.InputText()],
              [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Window Title', layout)
    event, values = window.Read()
    window.Close()
    twitter_username = values[0]
    return twitter_username


def show_proposals(username, places, categories):
    user_preferences = "Hello @" + username + "! I can see that You like:"
    for i, category in enumerate(categories):
        user_preferences += " " + category + " and" if i != len(categories) else " " + category + "."
    user_preferences += "\nI recommend You to visit:"
    layout = [[sg.Text(place)] for place in places]
    # layout.append(sg.Submit(), sg.Cancel())
    layout.insert(0, [sg.Text(user_preferences)])
    window = sg.Window('Window Title', layout) #layout)
    event, values = window.Read()
    window.Close()
    twitter_username = values[0]
    return twitter_username
