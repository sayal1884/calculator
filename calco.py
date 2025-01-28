from tkinter import *
import math, os

class calco(LabelFrame):
    def __init__(self, width = 200, height = 400, color = 'dark blue'):
        LabelFrame.__init__(self, bg= color, width = width, height = height, relief = FLAT, bd = 5)
        self.width, self.height, self.color = width, height, color
        self.lab = Label(self, text = 'python Lite Calco',relief='ridge',font=("verdana",10,"bold",'italic'), bg = '#ffffaa',fg = 'dark blue')
        self.configure(labelwidget = self.lab, labelanchor = 'nw')

        #creation des etiquettes des buttons
        self.label = [1,2,3,'CE',4,5,6,'+',7,8,9,'-',0,'.','/','*','(',')','del','=']
        self.buttons , self.r, self.c = [], 2, 0
        self.valeur = []
        self.entryVar, self.outVar = StringVar(), StringVar()

        #creation des ecrans
        self.screen1 = Label(self, textvariable = self.entryVar, font=("verdana",10,"bold"), anchor = 'w', bd = 0, width = 20)
        self.screen2 = Label(self, textvariable = self.outVar, font=("verdana",10,"bold"), anchor = 'e', bd = 0, width = 20)
        self.screen1.grid(column = 0, row = 0, columnspan = 4, sticky = 'wens')
        self.screen2.grid(column = 0, row = 1, columnspan = 4, sticky = 'wens')

        #creation des buttons
        for i in range(len(self.label)):
            self.buttons.append(Button(self, text = str(self.label[i]), relief = RIDGE,font=("verdana",10,"bold"),fg = 'dark blue',
                                       command = lambda a = i : self.add(a), overrelief = 'sunken', bg = '#ffffaa'))
            self.buttons[i].grid(column = self.c, row = self.r, sticky = 'wens', padx = 1, pady = 1)
            if self.label[i]=='=':
                self.buttons[i].config(command = self.egal)
            elif self.label[i] =='del':
                self.buttons[i].config(command = self.delete)
            elif self.label[i] =='CE':
                self.buttons[i].config(command = self.reset)
            self.c+=1
            if self.c==4:
                self.c=0
                self.r+=1
        self.pack()

    #creation des fonctions 
    def add(self, arg):
        self.valeur.append(str(self.label[arg]))
        self.entryVar.set(''.join(self.valeur))
        
    def delete(self):
        del self.valeur[-1]
        self.entryVar.set(''.join(self.valeur))
        
    def egal(self):
        self.outVar.set(eval(self.entryVar.get()))
        
    def reset(self):
        self.outVar.set('')
        self.entryVar.set('')
        self.valeur = []
        
if __name__=="__main__":
    calco().mainloop()
        
