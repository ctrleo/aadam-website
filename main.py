import time
from pyscript import document
button_bind = 0
def write(text):
    document.querySelector("#out").innerText = text
def activate_button(button_number):
    button_bind = button_number
def choice(out, one, two=None, three=None, four=None, five=None):
    document.querySelector("#out").innerText = out
    document.querySelector('#one').innerText = one
    document.querySelector('#one').style.display = 'inline-block'
    if two != None:
        document.querySelector('#two').innerText = two
        document.querySelector('#two').style.display = 'inline-block'
    if three != None:
        document.querySelector('#three').innerText = three
        document.querySelector('#three').style.display = 'inline-block'
    if four != None:
        document.querySelector('#four').innerText = four
        document.querySelector('#four').style.display = 'inline-block'
    if five != None:
        document.querySelector('#five').innerText = five
        document.querySelector('#five').style.display = 'inline-block'
    while button_bind == 0:
        waiting_for_input = True
    return button_bind

first = choice("New test choice", "A", "B", "C")
match first:
    case 1:
        write("You chose A")
    case 2:
        write("You chose B")
    case 3:
        write("You chose C")
