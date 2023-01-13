from functions import *
from urllib.request import urlopen
import  re
url = "https://github.com/henryur/nearlnetworking"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
stitle = []
stitle[:0] = title
cversion = ""
for i in range(len(stitle)):

    if stitle[i] == "\\":
        i+=1
        while stitle[i] != "\\":

            cversion += stitle[i]
            i+=1
        break
del url,page,html,start_index,end_index,title,stitle

iversion = "v1.0.0 Alpha"
class gui:
    def reset(self):
        self.d.window.destroy()
        del self.d
        self.__init__()
    def __init__(self):
        checktheme()

        # theme = [back,mid,front,text,highlight]
        self.theme = getTheme()
        self.d = display(screenX=800, screenY=600, bgc=self.theme[0], title="neural networking",icon="settings/Untitled (1).ico")
        self.topBar = self.topbar(self)
        self.updategui()
    def updategui(self):

        while self.d.runing == True:
            self.d.update()
            self.topBar.update_topbar()
    class topbar:
        def themeWizzerd(self):
            self.gui.d.mouseP = False
            self.gui.d.running = False
            t = checktheme(force=True)
            self.gui.d.running = True


            self.gui.theme = getTheme()
            del t
            self.gui.reset()


        def __init__(self,down):
            self.gui = down




            self.gui.d.rect("topbar box",0,0,100,3,fill=self.gui.theme[1])
            if cversion != iversion:
                vcolor = "#d94338"
            else:
                vcolor = self.gui.theme[3]
            self.gui.d.text("version text",2.3,1.5,2.4,text=iversion, fill=vcolor)



            self.file = self.topbar_item("file",1,self)
            self.edit = self.topbar_item("edit", 2, self)
            self.view = self.topbar_item("view",3,self)
            self.wizards = self.topbar_item("wizards",4,self)



            self.view.newDDoption("theme",self.themeWizzerd)




            self.wizards.newDDoption("theme", self.themeWizzerd)



            self.file.bild()
            self.edit.bild()
            self.view.bild()
            self.wizards.bild()


        def update_topbar(self):
            self.file.update_topbar_funct()
            self.edit.update_topbar_funct()
            self.view.update_topbar_funct()
            self.wizards.update_topbar_funct()

        def closepopups(self):
            self.file.closepopup()
            self.edit.closepopup()
            self.view.closepopup()
            self.wizards.closepopup()
        class topbar_item:
            def __init__(self, name, xNumber, down):
                self.name = name
                self.topbar = down
                self.dropdownItems = {}
                self.dropdownItemsNames = []

                self.NofL = 0

                self.sx = 0.5 + (xNumber * 4)
                self.y = (self.NofL * 2.5)
                self.x = 10


            def openfilemenu(self):
                #called when your mouse is over file button
                #closes other dropdowns
                self.topbar.closepopups()
                #drops dropdown
                self.topbar.gui.d.setpos(f"{self.name} dropdown background",8,True)
                self.topbar.gui.d.changecolor(f"{self.name} topbar rect", self.topbar.gui.theme[5])

            def newDDoption(self,name,function):
                # new item on list

                self.NofL+=1
                self.dropdownItems[f"{name}"] = function
                self.dropdownItemsNames.append(name)


            def update_topbar_funct(self):
                #mouseX
                mx = self.topbar.gui.d.mx
                #mouseY
                my = self.topbar.gui.d.my
                #checking if mouse is in area
                if inZone(self.sx, 0, self.sx+self.x, 3 + (self.NofL*2.5),mx,my) == False :
                    #print("hi")
                    #if its not hiding the file dropdown background
                    self.topbar.gui.d.setpos(f"{self.name} dropdown background", 8, False)
                    #uslecting fiel button
                    self.topbar.gui.d.changecolor(f"{self.name} topbar rect", self.topbar.gui.theme[0])

                #set on and off here for the menu items
                #if dropdown is down
                if  self.topbar.gui.d.get(f"{self.name} dropdown background",8) == True:
                    #show dropdown items
                    for i in range(self.NofL):
                        name = self.dropdownItemsNames[i]
                        self.topbar.gui.d.setpos(f"{name} {self.name} topbar button", 9, True)
                        self.topbar.gui.d.setpos(f"{name} {self.name} toolbar text", 9, True)

                else:
                    #hide sropdown items
                    for i in range(self.NofL):
                        name = self.dropdownItemsNames[i]
                        self.topbar.gui.d.setpos(f"{name} {self.name} topbar button", 9, False)
                        self.topbar.gui.d.setpos(f"{name} {self.name} toolbar text", 9, False)

                #if mouse is in area
                for i in range(self.NofL):
                    name = self.dropdownItemsNames[i]
                    if inZone(self.sx+0.3,(i*2.5)+3.2,self.sx+self.x-0.3,(i*2)+5.2,mx,my):
                        self.topbar.gui.d.changecolor(f"{name} {self.name} topbar button", self.topbar.gui.theme[5])
                    else:
                        self.topbar.gui.d.changecolor(f"{name} {self.name} topbar button", self.topbar.gui.theme[0])


            def checkslected(self,n):
                if self.topbar.gui.d.get(f"{self.name} dropdown background",8) == True:
                    name = self.dropdownItemsNames[n]
                    self.dropdownItems[name]()
            def closepopup(self):
                self.topbar.gui.d.setpos(f"{self.name} dropdown background", 8,False)
                self.topbar.gui.d.changecolor(f"{self.name} topbar rect", self.topbar.gui.theme[0])
            def bild(self):
                self.topbar.gui.d.rect(f"{self.name} topbar rect", self.sx, 0, self.sx + 3.9, 3,
                                       fill=self.topbar.gui.theme[0])
                self.topbar.gui.d.mouseover(f"{self.name} topbar mouse over", self.sx, 0.5, self.sx + 2.5, 2.5,
                                            funct=self.openfilemenu)
                self.topbar.gui.d.rect(f"{self.name} dropdown background", self.sx, 3, self.sx + self.x, 3 + (self.NofL*2.5),
                                       visable=False,
                                       fill=self.topbar.gui.theme[1])
                self.topbar.gui.d.text(f"{self.name} toptbar text", ((self.sx)+(self.sx + 3.9))/2, (2.5 / 2) + 0.3, 3, text=f"{self.name}",
                                       fill=self.topbar.gui.theme[3])
                for i in range(self.NofL):


                    name = self.dropdownItemsNames[i]
                    function = self.dropdownItems[f"{name}"]
                    listItem = i
                    self.topbar.gui.d.buttonM(i,f"{name} {self.name} topbar button", self.sx + 0.3, (listItem * 2.5) + 3.2,
                                             self.sx + self.x - 0.3, (listItem * 2.5) + 5.2, self.checkslected,
                                             fill=[self.topbar.gui.theme[0]], visable=False)
                    self.topbar.gui.d.text(f"{name} {self.name} toolbar text",
                                           ((self.sx + 0.3) + (self.sx + self.x - 0.3)) / 2,
                                           (((listItem * 2.5) + 3.2) + ((listItem * 2.5) + 5.2)) / 2, 3, text=f"{name}",
                                           fill=self.topbar.gui.theme[3], visable=False)














def start():


    g = gui()

if __name__ == '__main__':
    start()
