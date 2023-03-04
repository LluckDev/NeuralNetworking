import files as file
from gui import display

f = file.fileIntrations()




def getTheme():
    fi = open("settings/theme")
    x = f.loadFile(fi)

    return [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7]]


class checktheme:
    def __init__(self,force=False):
        fi = open("settings/theme")
        x = f.loadFile(fi)
        fi.close()

        if x[0][0] == "ask" or force:
            self.w = display(screenX=400, screenY=250, fullscreen=False, title="chose theme",icon="settings/wizerdNN.ico")

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

SOL = [[0,4.5]]

class topbar_item:
    def __init__(self, name, xNumber, down):

        self.name = name

        self.topbar = down
        self.dropdownItems = {}
        self.dropdownItemsNames = []

        self.NofL = 0
        startn = SOL[xNumber-1][0]
        endn = SOL[xNumber-1][1]
        self.sx = startn + endn
        self.y = (self.NofL * 2.5)
        self.x = 10



        self.ex = (4/7)*len(name)
        SOL.append([self.sx,self.ex])


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
            self.topbar.gui.d.changecolor(f"{self.name} topbar rect", self.topbar.gui.theme[1])

        #set on and off here for the menu items
        #if dropdown is down
        if  self.topbar.gui.d.get(f"{self.name} dropdown background",8) == True:
            #show dropdown items
            i = 0
            while i < self.NofL:

                name = self.dropdownItemsNames[i]
                self.topbar.gui.d.setpos(f"{name} {self.name} topbar button", 9, True)
                self.topbar.gui.d.setpos(f"{name} {self.name} toolbar text", 9, True)
                i += 1
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
        self.topbar.gui.d.changecolor(f"{self.name} topbar rect", self.topbar.gui.theme[1])
    def clear(self):
        del self.dropdownItems
        del self.dropdownItemsNames
    def bild(self):
        self.topbar.gui.d.rect(f"{self.name} topbar rect", self.sx, 0, self.sx + self.ex-0.01, 3,
                               fill=self.topbar.gui.theme[1],stroke=self.topbar.gui.theme[0])
        self.topbar.gui.d.mouseover(f"{self.name} topbar mouse over", self.sx, 0.5, self.sx + 2.5, 2.5,
                                    funct=self.openfilemenu)
        self.topbar.gui.d.rect(f"{self.name} dropdown background", self.sx, 3, self.sx + self.x, 3 + (self.NofL*2.5),
                               visable=False,
                               fill=self.topbar.gui.theme[1],stroke=self.topbar.gui.theme[0])
        self.topbar.gui.d.text(f"{self.name} toptbar text", ((self.sx)+(self.sx +self.ex-0.1))/2, (2.5 / 2) + 0.3, 3, text=f"{self.name}",
                               fill=self.topbar.gui.theme[3])
        for i in range(self.NofL):


            name = self.dropdownItemsNames[i]
            function = self.dropdownItems[f"{name}"]
            listItem = i
            self.topbar.gui.d.buttonM(i,f"{name} {self.name} topbar button", self.sx + 0.3, (listItem * 2.5) + 3.2,
                                     self.sx + self.x - 0.3, (listItem * 2.5) + 5.2, self.checkslected,
                                     fill=[self.topbar.gui.theme[0]], visable=False,stroke=self.topbar.gui.theme[0])
            self.topbar.gui.d.text(f"{name} {self.name} toolbar text",
                                   ((self.sx + 0.3) + (self.sx + self.x - 0.3)) / 2,
                                   (((listItem * 2.5) + 3.2) + ((listItem * 2.5) + 5.2)) / 2, 3, text=f"{name}",
                                   fill=self.topbar.gui.theme[3], visable=False,stroke=self.topbar.gui.theme[0])
class settings:
    def __init__(self,down):
        self.topbar = down
        self.w = display(screenX=400, screenY=250, fullscreen=False, title="chose theme", icon="settings/wizerdNN.ico")






