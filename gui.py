from tkinter import *


class display:

    def empty(self,key=""):
        pass
    def __init__(self, grid=100, screenX=100, screenY=100, bgc="#ffffff", fullscreen=True,title="gui",icon = None):

        self.storage = {}
        self.extra = {}
        self.data = []
        self.location = {}
        self.window = Tk()
        self.window.iconbitmap(icon)
        self.window.title(title)
        self.window.configure(bg=bgc)
        self.window.geometry(str(screenX) + "x" + str(screenY))
        self.window.columnconfigure(100, weight=100)
        self.window.rowconfigure(100, weight=100)
        self.canvis = Canvas(self.window, width=self.window.winfo_width() / 1.25,
                             height=self.window.winfo_height() / 1.25, bg=bgc)
        self.funkts = []
        if fullscreen == True:
            self.window.state('zoomed')
        self.canvis.grid(row=1)
        self.numb = 0
        self.incrment = grid
        self.canvis.bind("<Button-1>", self.callback)

        self.window.bind_all('<Key>', self.key)
        self.mouseP = False
        self.rep = 100
        self.runing = True
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.lastkey = None
        self.odk = None
        self.keypressed = False
        self.mx = 0
        self.my = 0
        self.sendkeyF = {}
        self.cp = {}

    def key(self, tag):

        self.lastkey = tag.char
        self.keypressed = True


    def setkey(self,keypressed=None,key=None):
        self.funkts.append(keypressed)
        self.funkts.append(key)



    def callback(self, event):
        self.rep = 0
        self.mouseP = True
        self.update()
        self.mouseP = False
        self.update()

    def close(self):
        self.runing = False

    def update(self):
        self.winy = self.window.winfo_height()

        self.winx = self.window.winfo_width()
        self.canvis.config(width=self.winx, height=self.winy)
        # set mouse pos
        self.mx = self.mouseX()
        self.mx -= self.window.winfo_x()
        self.mx = (self.incrment / self.winx) * self.mx

        self.my = self.mousey()
        self.my -= self.window.winfo_y()
        self.my -= 30
        self.my = (self.incrment / self.winy) * self.my

        if self.keypressed:
            self.sendkeyF["keys"](self.lastkey)
            self.keypressed = False



        for i in range(self.numb):

            if self.data[i][0] == 4:
                self.canvis.coords(self.storage["{0}".format(str(self.data[i][1]))],
                                   self.data[i][2] * self.winx / self.incrment,
                                   self.data[i][3] * self.winy / self.incrment,
                                   self.data[i][4] * self.winx / self.incrment,
                                   self.data[i][5] * self.winy / self.incrment)
                if self.data[i][8]==True:
                    self.canvis.itemconfig(self.storage["{0}".format(str(self.data[i][1]))],state='normal')
                else:
                    self.canvis.itemconfig(self.storage["{0}".format(str(self.data[i][1]))],state='hidden')
            elif self.data[i][0] == 6:
                self.canvis.coords(self.storage["{0}".format(str(self.data[i][1]))],
                                   self.data[i][2] * self.winx / self.incrment,
                                   self.data[i][3] * self.winy / self.incrment,
                                   self.data[i][4] * self.winx / self.incrment,
                                   self.data[i][5] * self.winy / self.incrment,
                                   self.data[i][6] * self.winx / self.incrment,
                                   self.data[i][7] * self.winy / self.incrment)
                if self.data[i][10]==True:
                    self.canvis.itemconfig(self.storage["{0}".format(str(self.data[i][1]))],state='normal')
                else:
                    self.canvis.itemconfig(self.storage["{0}".format(str(self.data[i][1]))],state='hidden')

            elif self.data[i][0] == 2:
                self.canvis.itemconfig(self.storage["{0}".format(str(self.data[i][1]))],
                                       font=("Purisa", int(self.data[i][4] * (self.winx + self.winy) / 600)))
                self.canvis.coords(self.storage["{0}".format(str(self.data[i][1]))],
                                   self.data[i][2] * self.winx / self.incrment,
                                   self.data[i][3] * self.winy / self.incrment)
            elif self.data[i][0] == "4a":
                if self.mx >= self.data[i][2] and self.mx <= self.data[i][4]:
                    if self.my >= self.data[i][3] and self.my <= self.data[i][5]:
                        if self.mouseP == True:
                            self.data[i][6]()
            elif self.data[i][0] == "4b":
                self.canvis.coords(self.storage["{0}".format(str(self.data[i][1]))],
                                   self.data[i][2] * self.winx / self.incrment,
                                   self.data[i][3] * self.winy / self.incrment,
                                   self.data[i][4] * self.winx / self.incrment,
                                   self.data[i][5] * self.winy / self.incrment)
                if self.mx >= self.data[i][2] and self.mx <= self.data[i][4]:
                    if self.my >= self.data[i][3] and self.my <= self.data[i][5]:
                        if self.mouseP == True:
                            self.data[i][8]()
            elif self.data[i][0] == "4c":
                self.canvis.coords(self.storage["{0}".format(str(self.data[i][1]))],
                                   self.data[i][2] * self.winx / self.incrment,
                                   self.data[i][3] * self.winy / self.incrment,
                                   self.data[i][4] * self.winx / self.incrment,
                                   self.data[i][5] * self.winy / self.incrment)
                if self.mouseP == True:
                    self.data[i][10] = False
                if self.mx >= self.data[i][2] and self.mx <= self.data[i][4]:
                    if self.my >= self.data[i][3] and self.my <= self.data[i][5]:
                        if self.mouseP == True:
                            self.data[i][10] = True
                if self.keypressed and self.data[i][10]:

                    self.keypressed = False
                    if self.data[i][8] == self.data[i][9]:
                        self.data[i][8] = ""

                    self.data[i][8] += self.lastkey
                    self.canvis.itemconfig(self.extra['{0}'.format(str(self.data[i][1]))], text=self.data[i][8])
                    if self.lastkey == "\b":
                        self.data[i][8] = self.data[i][8][:-2]

                self.canvis.itemconfig(self.extra["{0}".format(str(self.data[i][1]))],
                                       font=("Purisa", int((((self.data[i][2] - self.data[i][4]) + (
                                                   self.data[i][3] - self.data[i][5])) / 2) * (
                                                                       self.winx + self.winy) / 1000)))
                self.canvis.coords(self.extra["{0}".format(str(self.data[i][1]))],
                                   (((self.data[i][4] - self.data[i][2]) / 2) + self.data[i][
                                       2]) * self.winx / self.incrment,
                                   (((self.data[i][5] - self.data[i][3]) / 2) + self.data[i][
                                       3]) * self.winy / self.incrment)

        self.window.update_idletasks()
        self.window.update()

    def line(self, tag, x, y, xp, yp, color="#000000", visable=True):
        self.storage["{0}".format(str(tag))] = self.canvis.create_line(100, 100, 100, 100)
        self.location["{0}".format(str(tag))] = self.numb
        self.data.append([4, tag, x, y, xp, yp, color, "#000000", visable])
        self.numb += 1

    def rect(self, tag, x, y, xp, yp, fill="#ffffff", stroke="#000000",visable=True):
        self.storage['{0}'.format(str(tag))] = self.canvis.create_rectangle(100, 100, 100, 100, fill=fill,
                                                                            outline=stroke)
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append([4, tag, x, y, xp, yp, fill, stroke, visable])
        self.numb += 1

    def ellipse(self, tag, x, y, xp, yp, fill="#ffffff", stroke="#000000",visable=True):
        self.storage['{0}'.format(str(tag))] = self.canvis.create_oval(x, y, xp, yp, fill=fill, outline=stroke)
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append([4, tag, x, y, xp, yp, fill, stroke, visable])
        self.numb += 1

    def text(self, tag, x, y, size, text=10, fill="#ffffff", stroke="#000000", font="Lato",visable=True):

        self.storage['{0}'.format(str(tag))] = self.canvis.create_text(x, y, text=str(text))
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append([2, tag, x, y, size, fill, stroke, text, font,visable])
        self.numb += 1

    def triangle(self, tag, x1, y1, x2, y2, x3, y3, fill="#000000",visable=True):
        self.storage['{0}'.format(str(tag))] = self.canvis.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill)
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append([6, tag, x1, y1, x2, y2, x3, y3, fill,visable])
        self.numb += 1

    def hitbox(self, tag, x1, y1, x2, y2, funct):
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append(["4a", tag, x1, y1, x2, y2, funct])

        self.numb += 1

    def button(self, tag, x1, y1, x2, y2, funct, fill="#ffffff", stroke="#000000", Text=None,visable=True):
        self.storage['{0}'.format(str(tag))] = self.canvis.create_rectangle(100, 100, 100, 100, fill=fill,
                                                                            outline=stroke)
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append(["4b", tag, x1, y1, x2, y2, fill, stroke, funct,visable])
        self.numb += 1

    def textbox(self, tag, x1, y1, x2, y2, starttext="text", fill="#ffffff", stroke="#000000"):
        self.storage['{0}'.format(str(tag))] = self.canvis.create_rectangle(100, 100, 100, 100, fill=fill,
                                                                            outline=stroke)
        self.location['{0}'.format(str(tag))] = self.numb
        self.data.append(["4c", tag, x1, y1, x2, y2, fill, stroke, "", starttext, False])
        self.numb += 1
        self.extra['{0}'.format(str(tag))] = self.canvis.create_text(100, 100, text=starttext)

    def mouseX(self):
        return self.window.winfo_pointerx()

    def mousey(self):
        return self.window.winfo_pointery()

    def mouseXY(self):
        return self.window.winfo_pointerxy()

    def setpos(self, tag, loc, value):
        tagloc = self.location["{0}".format(str(tag))]
        self.data[tagloc][loc] = value

    def settype(self, tag, x=None, y=None, xp=None, yp=None, fill=None, text=None):
        tagloc = self.location["{0}".format(str(tag))]

        if x != None:
            self.data[tagloc][2] = x
        if y != None:
            self.data[tagloc][3] = y
        if xp != None:
            self.data[tagloc][4] = xp
        if yp != None:
            self.data[tagloc][5] = yp
        if fill != None:
            self.data[tagloc][6] = fill
            self.canvis.itemconfig(self.storage['{0}'.format(str(tag))], fill=fill)
        if text != None:
            self.canvis.itemconfig(self.storage['{0}'.format(str(tag))], text=text)

    def mathset(self, tag, mathop, firstloc, second):
        tagloc = self.location["{0}".format(str(tag))]

        if mathop == "+":
            self.data[tagloc][firstloc] += second

        elif mathop == "-":
            self.data[tagloc][firstloc] -= second
        elif mathop == "*":
            self.data[tagloc][firstloc] *= second
        elif mathop == "/":
            self.data[tagloc][firstloc] /= second

    def get(self, tag, loc):
        tagloc = self.location["{0}".format(str(tag))]
        return self.data[tagloc][loc]

    def sendkeys(self,function):
        self.sendkeyF["keys"] = function

    def addcolorpalette(self,tag,color):
        self.cp[tag] = color
