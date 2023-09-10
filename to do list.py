from tkinter import *
from tkinter import messagebox
root=Tk()
########## main headinhg  ###########3
def mainheading():
    head = Label(root,text="            THE TO - DO LIST                    ",font=("algerian",40,'bold'),
                 bg="aliceblue",fg="#cc3300",padx=20,bd=10)
    head.grid(row=0,column=0,columnspan=4)
mainheading()
######### list box #########
l=Listbox(root,height=20,width=33,selectmode=EXTENDED,font=("algerian",15,'bold'))
l.place(x=350,y=120)
l.insert(0)

adminentry=StringVar()
################ buttton task #############
def addtask():
    s1=adminentry.get()
    if s1=='':
        messagebox.showerror("ADD SOMTHING"," PLASE ADD SOME TASK ")
    else:
     l.insert(END,s1)
     adminentry.set('')
def deltask():
     click_item=l.curselection()
     for item in click_item:
        print(l.delete(item))

def alldeltask():
        l.delete(0, END)
def exittask():
    root.destroy()
####### admin work ##########
def adminwork():

    adminlbl=Label(root,text=" ENTER THE TASK :",font=("algerian",20,'bold'),bg="aliceblue",fg="#cc3300")
    adminlbl.place(x=30,y=120)

    admintentry=Entry(root,font=("calibri",22,'bold'),bd=3,fg='black',textvariable=adminentry)
    admintentry.place(x=30,y=170)

    btnadditem = Button(root, text="ADD TASK", bd=7,bg="aliceblue",fg="#cc3300", font=("cambria", 15, 'bold'),command=addtask)
    btnadditem.place(x=30,y=240,width=310)

    btndelitem = Button(root, text=" DELETE TASK", bd=7,bg="aliceblue",fg="#cc3300", font=("cambria", 15, 'bold'),command=deltask)
    btndelitem.place(x=30,y=300,width=310)

    btnalldelitem = Button(root, text="DELETE ALL TASK", bd=7,bg="aliceblue",fg="#cc3300", font=("cambria", 15, 'bold'),command=alldeltask)
    btnalldelitem.place(x=30,y=360,width=310)

    btnexit = Button(root, text="EXIT", bd=7,bg="aliceblue",fg="#cc3300", font=("cambria", 15, 'bold'),command=exittask)
    btnexit.place(x=30,y=420,width=310)

adminwork()
root.configure(bg="aliceblue")
root.title("A TO DO LIST")
root.geometry("800x700+250+70")
root.resizable(0,0)
root.mainloop()