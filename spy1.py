from guizero import App, Text, PushButton
from random import choice

def choose_name():
    #print("Button was pressed")
    #bapp = App("BOTTOM SECRET")
    #bapp.display()
    first_names = ["Barbara", "Woody", "Tiberius", "Smokey", "Jennifer", "Ruby"]
    last_names  = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingbreath"]
    spy_name = choice(first_names) + " " + choice(last_names)
    #print(spy_name)
    name.value = spy_name

app = App("TOP SECRET")

title = Text(app, "Push the red button to find out your spy name")

button = PushButton(app, choose_name, text="Tell me!")
button.bg = "red"
button.text_size = 30

name = Text(app, "")


app.display()