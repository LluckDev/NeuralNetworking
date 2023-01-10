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

            self.file = self.file(self)

        def update_topbar(self):
            self.file.update_topbar_file()
        def closepopups(self):
            self.file.closepopup()
        class file:

            def __init__(self,down):

                self.actions = ["new"]


                self.sx = 0.5
                self.y = 20
                self.x = 10
                self.topbar = down

                self.topbar.gui.d.rect("file topbar rect",self.sx,0.5,3,2.5, fill=self.topbar.gui.theme[2])
                self.topbar.gui.d.mouseover("file topbar mouse over",self.sx,0.5,3,2.5,funct=self.openfilemenu)
                self.topbar.gui.d.rect("file dropdown background", self.sx, 3, self.sx+self.x, 3+self.y,visable=False,fill=self.topbar.gui.theme[2])
                self.topbar.gui.d.text("file toptbar text",1+self.sx, (2.5/2)+0.3, 3, text="file")


            def update_topbar_file(self):
                mx = self.topbar.gui.d.mx
                my = self.topbar.gui.d.my
                if inZone(self.sx, 0, 0.5+self.x, 3+self.y,mx,my) == False :
                    #print("hi")
                    self.topbar.gui.d.setpos("file dropdown background", 8, False)
                    self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[2])
            def openfilemenu(self):
                self.topbar.closepopups()
                self.topbar.gui.d.setpos("file dropdown background",8,True)
                self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[5])
            def closepopup(self):
                self.topbar.gui.d.setpos("file dropdown background", 8, False)
                self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[2])






def start():


    g = gui()

if __name__ == '__main__':
    start()