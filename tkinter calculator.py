from tkinter import *

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
     global val
     val=" "
     data.set(" ")

def btnEqual():
    global val
    result=eval(str(val))
    data.set(result)
root=Tk()
root.title("my calculator")
root.geometry("361x381+500+200")
val=""
data=StringVar()
display=Entry(root,bd=29,textvariable=data,justify='right',bg='powder blue',font=("arial",20))
display.grid(row=0,columnspan=4)
#button of first row
btn7=Button(root,text='7',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text='8',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text='9',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text='+',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick('+'))
btn_add.grid(row=1,column=3)
#button of second row
btn4=Button(root,text='4',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text='5',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text='6',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text='-',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick('-'))
btn_sub.grid(row=2,column=3)
#buttions of third row
btn1=Button(root,text='1',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text='2',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text='3',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btn_into=Button(root,text='*',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick('*'))
btn_into.grid(row=3,column=3)
#buttons of 4th row
btn0=Button(root,text='0',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick(0))
btn0.grid(row=4,column=0)
btn_clear=Button(root,text='C',font=("arial",12,'bold'),bd=12,height=2,width=6,command=btnClear)
btn_clear.grid(row=4,column=1)
btn_equal=Button(root,text='=',font=("arial",12,'bold'),bd=12,height=2,width=6,command=btnEqual)
btn_equal.grid(row=4,column=2)
btn_div=Button(root,text='/',font=("arial",12,'bold'),bd=12,height=2,width=6,command=lambda:btnclick('/'))
btn_div.grid(row=4,column=3)

root.mainloop()

