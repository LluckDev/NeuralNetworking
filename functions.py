import files as file
from gui import display

f = file.fileIntrations()




def getTheme():
    fi = open("settings/theme")
    x = f.loadFile(fi)

    return [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5]]


class checktheme:
    def __init__(self,force=False):
        fi = open("settings/theme")
        x = f.loadFile(fi)
        fi.close()

        if x[0][0] == "ask" or force:
            self.w = display(screenX=400, screenY=250, fullscreen=False, title="chose theme")

            self.w.button("dark", 10, 30, 45, 90, self.darktheme, fill="#373737",stroke="#000000")
            self.w.text("dark text",25,60,30,text="dark",fill="#000000")
            self.w.button("light", 55, 30, 90, 90, self.lighttheme, fill="#d6d6d6", stroke="#000000")
            self.w.text("light text", 75, 60, 30, text="light", fill="#000000")
            self.w.text("theme title",50,10,40,text="chose theme")

            while self.w.runing:

                self.w.update()
            self.w.window.destroy()



    def darktheme(self):

        self.w.runing = False
        f1 = open("settings/theme", "w")
        f2 = open("settings/themes")
        themes = f.loadFile(f2)

        f.closefile1d(f1,themes[0])

    def lighttheme(self):
        self.w.runing = False
        f1 = open("settings/theme", "w")
        f2 = open("settings/themes")
        themes = f.loadFile(f2)

        f.closefile1d(f1,themes[1])




def inZone(x,y,xp,yp,mx,my):
    if mx >= x and mx<=xp and my >= y and my <= yp:

        return True
    else:
        return False



