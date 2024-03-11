from pyscript import document
def choice(out, one, two=None, three=None, four=None, five=None):
    document.querySelector("#out").innerText = out
    document.querySelector('#1').innerText = one
    document.querySelector('#1').style.display = 'inline-block'
    if two != None:
        document.querySelector('#2').innerText = two
        document.querySelector('#2').style.display = 'inline-block'
    if three != None:
        document.querySelector('#3').innerText = three
        document.querySelector('#3').style.display = 'inline-block'
    if four != None:
        document.querySelector('#4').innerText = four
        document.querySelector('#4').style.display = 'inline-block'
    if five != None:
        document.querySelector('#5').innerText = five
        document.querySelector('#5').style.display = 'inline-block'
