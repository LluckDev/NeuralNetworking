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
                #how many items there are in the list starting at one
                self.NofL = 1
                self.actions = ["new"]


                self.sx = 0.5
                self.y = 20
                self.x = 10
                self.topbar = down


                self.topbar.gui.d.rect("file topbar rect",self.sx,0.5,self.sx+2.5,2.5, fill=self.topbar.gui.theme[0])
                self.topbar.gui.d.mouseover("file topbar mouse over",self.sx,0.5,self.sx+2.5,2.5,funct=self.openfilemenu)
                self.topbar.gui.d.rect("file dropdown background", self.sx, 3, self.sx+self.x, 3+self.y,visable=False,fill=self.topbar.gui.theme[1])
                self.topbar.gui.d.text("file toptbar text",1+self.sx, (2.5/2)+0.3, 3, text="file",stroke=self.topbar.gui.theme[3])

                self.newt()

            def update_topbar_file(self):
                #mouseX
                mx = self.topbar.gui.d.mx
                #mouseY
                my = self.topbar.gui.d.my
                #checking if mouse is in area
                if inZone(self.sx, 0, 0.5+self.x, 3+self.y,mx,my) == False :
                    #print("hi")
                    #if its not hiding the file dropdown background
                    self.topbar.gui.d.setpos("file dropdown background", 8, False)
                    #uslecting fiel button
                    self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[0])

                #set on and off here for the menu items
                #if dropdown is down
                if  self.topbar.gui.d.get("file dropdown background",8) == True:
                    #show dropdown items
                    self.topbar.gui.d.setpos("new file toolbar text", 9, True)
                    self.topbar.gui.d.setpos("new file topbar button",9,True)
                else:
                    #hide sropdown items
                    self.topbar.gui.d.setpos("new file toolbar text", 9, False)
                    self.topbar.gui.d.setpos("new file topbar button", 9, False)
                #if mouse is in area
                if inZone(self.sx+0.3,(0*2.5)+3.2,self.sx+self.x-0.3,(0*2)+5.2,mx,my):
                    #select
                    self.topbar.gui.d.changecolor("new file topbar button",self.topbar.gui.theme[5])
                else:
                    #deselct
                    self.topbar.gui.d.changecolor("new file topbar button", self.topbar.gui.theme[0])




            def openfilemenu(self):
                #called when your mouse is over file button
                #closes other dropdowns
                self.topbar.closepopups()
                #drops dropdown
                self.topbar.gui.d.setpos("file dropdown background",8,True)
                self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[5])
            def closepopup(self):
                #closes dropdown
                self.topbar.gui.d.setpos("file dropdown background", 8, False)
                self.topbar.gui.d.changecolor("file topbar rect", self.topbar.gui.theme[0])

            def newt(self):
                #new item on list
                listItem = 0
                self.topbar.gui.d.button("new file topbar button",self.sx+0.3,(listItem*2.5)+3.2,self.sx+self.x-0.3,(listItem*2)+5.2,self.newop,fill=[self.topbar.gui.theme[0]],visable=False)
                self.topbar.gui.d.text("new file toolbar text",((self.sx+0.3)+(self.sx+self.x-0.3))/2,(((listItem*2.5)+3.2)+((listItem*2)+5.2))/2,3,text="make new file",fill=self.topbar.gui.theme[3],visable=False)

            def newop(self):
                #gets called wen tou click on the new button
                print("click")







def start():


    g = gui()

if __name__ == '__main__':
    start()