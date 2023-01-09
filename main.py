from gui import display
from functions import *

def start():
    checktheme()
    theme = getTheme()
    d = display(screenX=800,screenY=600,bgc=theme[0],title="neural networking")

    while d.runing == True:
        d.update()




if __name__ == '__main__':
    start()


