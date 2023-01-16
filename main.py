from functions import *
from urllib.request import urlopen
import webbrowser
import time
import psutil
import threading
from threading import Lock




url = "https://github.com/henryur/NeuralNetworking"
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

class globals:
    def __init__(self,lock):
        self.lock = lock
        with lock:

            self.vars = {}
    def newVar(self,ident,value=None):
        with self.lock:
            self.vars[ident] = value
    def getVar(self,ident):
        with self.lock:
            return self.vars[ident]
    def setvar(self,ident,value):
        with self.lock:
            self.vars[ident] = value




class gui:
    def reset(self):
        self.d.window.destroy()


        self.__init__()
        #TODO: add way of saving
    def __init__(self):
        checktheme()






        # theme = [back,mid,front,text,highlight]
        self.theme = getTheme()
        self.d = display(screenX=1600, screenY=800, bgc=self.theme[0], title="neural networking",icon="settings/Untitled (1).ico")
        self.performanceSidebar1 = self.performanceSidebar(self)
        self.topBar = self.topbar(self)

        self.updategui()
    def updategui(self):

        lasttime=0
        fpslasttime = 0
        currenttime=0
        while self.d.runing == True:
            currenttime = time.time()

            self.topBar.update_topbar()
            self.d.update()
            if((currenttime-lasttime) >= 0.1):

                lasttime = currenttime

                self.performanceSidebar1.caclateUsages(fpslasttime)
            self.performanceSidebar1.updatePerformanceSidbar()
            fpslasttime = currenttime


    class performanceSidebar:
        def __init__(self,down):
            self.gui = down
            self.width = 4.5
            self.gui.d.rect("performance sidbar BG",0,0,self.width,100,fill=self.gui.theme[1])
            #gen
            for i in range(9):

                self.gui.d.text(f"cpu/ram gen text N{i}",self.width/2,(i*2)+12,2,text=90-(i*10),fill=self.gui.theme[3])

            #FPS
            self.gui.d.rect("preformance sidbar FPS Highlight",self.width-.5,3.5,0.5,8,fill=self.gui.theme[2])
            self.gui.d.text("preformance sidebar FPS text",self.width/2,5,5,text="0",fill=self.gui.theme[3])
            self.gui.d.text("preformance sidebar FPS Label",self.width/2,7,3,text="FPS",fill=self.gui.theme[3])
            #CPU
            self.cpuUsage = psutil.cpu_percent(0.001)
            self.gui.d.rect("preformance sidbar cpu usage bg",(self.width/2)-0.5,10,0.5,30,fill=self.gui.theme[0])
            self.gui.d.rect("preformance sidebar cpu usage display",(self.width/2)-0.5,9.9,0.5,30,fill="#00ff66")
            self.gui.d.text("preformance sidbar cpu usage label",(((self.width/2))/2),31,2.5,text="CPU",fill=self.gui.theme[3])
            for i in range(19):
                self.gui.d.line(f"preformance sidebar line {i}",(self.width/2)-0.8,i+11,(self.width/2)-.5,i+11,color=self.gui.theme[2])
            #RAM
            self.ramUsage = 0
            self.gui.d.rect("preformance sidbar RAM usage bg", (self.width / 2) + 0.5, 10, 4, 30,
                            fill=self.gui.theme[0])
            self.gui.d.rect("preformance sidebar RAM usage display", (self.width / 2) + 0.5, 9.9, 4, 30,
                            fill="#00ff66")
            self.gui.d.text("preformance sidbar RAM usage label", (self.width / 2)+(((self.width/2))/2), 31, 2.5, text="RAM",fill=self.gui.theme[3])
            for i in range(19):
                self.gui.d.line(f"preformance sidebar line RAM {i}", (self.width / 2) + 0.8, i + 11, (self.width / 2) + .5,
                                i + 11, color=self.gui.theme[2])



            #fps vars
            self.curenttime = 0
            self.lasttime = 0
            self.fps = 0


        def updatePerformanceSidbar(self):
            pass
        def caclateUsages(self, lasttime):


            self.curenttime = time.time()
            self.fps = int(1/(self.curenttime-lasttime))
            lasttime = self.curenttime
            self.gui.d.settype("preformance sidebar FPS text",text=self.fps,fill=self.gui.theme[3])

            #CPU
            self.cpuUsage = psutil.cpu_percent(0.003)+20
            self.gui.d.settype("preformance sidebar cpu usage display",y=30-(self.cpuUsage/6))
            if self.cpuUsage >= 100:
                self.gui.d.settype("preformance sidebar cpu usage display",fill=self.gui.theme[7])
            else:
                self.gui.d.settype("preformance sidebar cpu usage display", fill=self.gui.theme[6])

            #RAM
            self.ramUsage = psutil.virtual_memory()[2]
            self.gui.d.settype("preformance sidebar RAM usage display", y=30 - (self.ramUsage / 5))
            if self.ramUsage >= 70:
                self.gui.d.settype("preformance sidebar RAM usage display", fill=self.gui.theme[7])
            else:
                self.gui.d.settype("preformance sidebar RAM usage display", fill=self.gui.theme[6])









    class topbar:
        def themeWizzerd(self):
            self.gui.d.mouseP = False
            self.gui.d.running = False
            t = checktheme(force=True)
            self.gui.d.running = True


            self.gui.theme = getTheme()
            del t
            self.gui.reset()

        def settings(self):
            self.gui.d.mouseP = False


            s = settings(self)

        def openNNwebGIT(self):
            giturl = "https://github.com/henryur/NeuralNetworking"
            webbrowser.open(giturl)






        def __init__(self,down):
            self.gui = down





            self.gui.d.rect("topbar box",0,0,100,3,fill=self.gui.theme[1])
            if cversion != iversion:
                vcolor = "#d94338"
            else:
                vcolor = self.gui.theme[3]
            self.gui.d.text("version text",2.3,1.5,2.4,text=iversion, fill=vcolor)



            self.file = topbar_item("file",1,self)
            self.edit = topbar_item("edit", 2, self)
            self.view = topbar_item("view",3,self)
            self.wizards = topbar_item("wizards",4,self)
            self.settings = topbar_item("settings",5,self)
            self.git = topbar_item("git",6,self)
            self.nnsite = topbar_item("NN website",7,self)




            #view options in order
            self.view.newDDoption("theme",self.themeWizzerd)



            #wizards options in order
            self.wizards.newDDoption("theme", self.themeWizzerd)


            #settings otions in order


            #nn site options in order
            self.nnsite.newDDoption("open github page",self.openNNwebGIT)




            self.file.bild()
            self.edit.bild()
            self.view.bild()
            self.wizards.bild()
            self.settings.bild()
            self.git.bild()
            self.nnsite.bild()



        def update_topbar(self):

            self.file.update_topbar_funct()
            self.edit.update_topbar_funct()
            self.view.update_topbar_funct()
            self.wizards.update_topbar_funct()
            self.settings.update_topbar_funct()
            self.nnsite.update_topbar_funct()
            self.git.update_topbar_funct()

        def closepopups(self):
            self.file.closepopup()
            self.edit.closepopup()
            self.view.closepopup()
            self.wizards.closepopup()
            self.settings.closepopup()
            self.git.closepopup()
            self.nnsite.closepopup()














g = gui()




