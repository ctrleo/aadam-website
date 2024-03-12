from pyscript import document, when
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

# pls add some code :3