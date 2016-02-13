#Title: Level comparison tool
#Author: Tham Mbung

import os
import csv

from tkinter import*


cwd='O:/Staff/Curriculum/01 CURRICULUM AREA RESOURCES/02 Maths/02 Resources/Python'

os.chdir(cwd)

class Application(Frame):
    """This program compares students' attainment using KS3 level on a termly basis,
and it displays the names of those whose prior attainment is higher than current term.
This helps identify who has not made progress or address mistakes in data input.
    """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    
    def create_widgets(self):
        
        self.label1=Label(self, text="Enter the name of your 'csv' file:")
        self.label1.grid(row=1, column=0, sticky=W)
        self.label2=Label(self, text='Current Working Directory:')
        self.label2.grid(row=2, column=0, sticky=W)
        self.label3=Label(self, text="by Tham Mbung")
        self.label3.grid(row=3, column=3, sticky=E)
        
        
        self.entry1=Entry(self)
        self.entry1.grid(row=1, column=1, columnspan=4)
        self.entry2=Entry(self, width=70)
        self.entry2.grid(row=2, column=1, columnspan=4)
        
        
        
        self.button1= Button(self, text='Start',bg="green", fg="red",command=self.term_comparison)
        self.button1.grid(row=3, column=0, sticky=W)
        self.button2= Button(self, text='Clear', bg="blue",command = self.clear)
        self.button2.grid(row=3, column=1, sticky=W)
        
        self.text1 = Text(self, width=100, height=80, wrap =CHAR)
        self.text1.grid(row=4, column=0, columnspan = 4)
        self.text1.focus_set()

        
    def term_comparison(self):
        conv={"X":0,"2c":1,"2b":2,"2a":3,
      "3c":4,"3b":5,"3a":6,
      "4c":7,"4b":8,"4a":9,
      "5c":10,"5b":11,"5a":12,
      "6c":13,"6b":14,"6a":15,
      "7c":16,"7b":17,"7a":18}
        myname=[]
        try:
            file = self.entry1.get()
            cwd = self.entry2.get()
            os.chdir(cwd)
        except FileNotFoundError as error:
            warn=self.text1.insert(END, error)
        except OSError as error:
            warn=self.text1.insert(END, error)
        
        try:
            
            with open(file) as th:
                rdr = csv.reader(th, delimiter=',')
                for item in rdr:
                    if (conv[item[1]] > conv[item[2]]):
                        myname.append(item)
                    
                        
        except OSError as error:
            warn=self.text1.insert(END, error)
            
        yourname=myname
        if(yourname == []):
            empty="Your search has not returned anything!" + "\n" + "The list must be empty."
            self.text1.insert(END, empty)
            self.text1.tag_add("start", "0.1", "4.11")
            self.text1.tag_config("start", background="white", foreground="red")
        else:
            for item in yourname:
                
                item.insert(len(item)+1, "\n")
                x=" ".join(item)    
                self.text1.insert(END, x)
                self.text1.tag_add("start", "0.1", "4.11")
                self.text1.tag_config("start", background="white", foreground="blue")
        
        self.entry1.delete(0, END)
        self.text1.focus_set()
    def clear(self):
        
        self.entry1.delete(0, END)
        self.text1.delete(0.0, END)
        self.entry1.focus_set()
        
        
root=Tk()
root.title('KS3 Level Comparison')
root.geometry('625x300')
app=Application(root)
app.mainloop()
