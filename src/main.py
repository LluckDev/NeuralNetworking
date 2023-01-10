from src.functions import *



















class gui:
    def __init__(self):
        checktheme()
        # theme = [back,mid,front,text,highlight]
        self.theme = getTheme()
        self.d = display(screenX=800, screenY=600, bgc=self.theme[0], title="neural networking")
        self.topBar = self.topbar(self)
        while self.d.runing == True:
            self.d.update()
    class topbar:

        def __init__(self,down):
            self.gui = down




            self.gui.d.rect("topbar box",0,0,100,3,fill=self.gui.theme[1])

            f = self.file(self)
        class file:

            def __init__(self,down):
                self.actions = ["new"]



                self.topbar = down
                self.topbar.gui.d.rect("file topbar rect",0.5,0.5,3,2.5, fill=self.topbar.gui.theme[2])
                self.topbar.gui.d.mouseover("file topbar mouse over",0.5,0.5,3,2.5,funct=self.openfilemenu)
            def openfilemenu(self):
                self.topbar.gui.d.rect("file dropdown background",0.5,3,10,)




def start():


    g = gui()

if __name__ == '__main__':
    start()