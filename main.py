from functions import *



















class gui:
    def __init__(self):
        checktheme()
        # theme = [back,mid,front,text,highlight]
        self.theme = getTheme()
        self.d = display(screenX=800, screenY=600, bgc=self.theme[0], title="neural networking")
        self.topBar = self.topbar(self)
        while self.d.runing == True:
            self.d.update()
            self.topBar.update_topbar()
    class topbar:

        def __init__(self,down):
            self.gui = down




            self.gui.d.rect("topbar box",0,0,100,3,fill=self.gui.theme[1])

            self.f1 = self.file(self)

        def update_topbar(self):
            self.f1.update_topbar_file()
        class file:

            def __init__(self,down):
                self.actions = ["new"]


                self.y = 20
                self.x = 10
                self.topbar = down
                self.topbar.gui.d.rect("file topbar rect",0.5,0.5,3,2.5, fill=self.topbar.gui.theme[2])
                self.topbar.gui.d.mouseover("file topbar mouse over",0.5,0.5,3,2.5,funct=self.openfilemenu)
                self.topbar.gui.d.rect("file dropdown background", 0.5, 3, 0.5+self.x, 3+self.y,visable=False,fill=self.topbar.gui.theme[2])


            def update_topbar_file(self):
                mx = self.topbar.gui.d.mx
                my = self.topbar.gui.d.my
                if inZone(0.5, 0, 0.5+self.x, 3+self.y,mx,my) == False:
                    #print("hi")
                    self.topbar.gui.d.setpos("file dropdown background", 8, False)
            def openfilemenu(self):
                self.topbar.gui.d.setpos("file dropdown background",8,True)






def start():


    g = gui()

if __name__ == '__main__':
    start()