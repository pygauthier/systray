from pystray import MenuItem as item
import pystray, time, socket, webbrowser
from PIL import Image

# Magic Here
def callback(icon):
    #Image Correct
    image = Image.open("go.png")
    percent = 100
    while True:
        img = image.copy()

        # Recupération de l'IP
        ip = getip()
        ipsplit = ip.split(".")
        time.sleep(1)
        percent -= 5

        # si l'ip est 10.0
        if (ipsplit[0] == "10"):
            icon.icon = Image.open("go.png")

        # sinon Flash rouge et vert
        else:
            if percent%2 == 0:
                icon.icon = Image.open("alarm-red.png")
            else:
                icon.icon = Image.open("alarm-yellow.png")
        
        if percent < 0:
            percent = 100

# Recupere l'IP local
def getip():
    return socket.gethostbyname(socket.gethostname())

# Exit ! 
def exit_action(icon):
    icon.visible = False
    icon.stop()

# Open browser at localhost
def action():
    return webbrowser.open_new_tab("http://localhost") 

image = Image.open("go.png")
menu = (item('IP: ' + getip(), action), item('Exit', lambda : exit_action(icon)))
#menu = (item('Exit', lambda : exit_action(icon)))
icon = pystray.Icon("IP CHECKER", image, menu = menu)
icon.visible = True
icon.run(setup=callback)
