
from tkinter import *


sonu=Tk()

sonu.title("Calulator")
sonu.geometry("400x420+80+80")
sonu.resizable(False,False)

sonu.config(bg="#17161b")



equation = ""
def show(value):
    global equation
    equation+=value
    label_res.config(text=equation)


def clear():
    global equation
    equation = ""
    label_res.config(text=equation )
    
def calculate():
    global equation
    result=""
    if equation !=" ":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation = ""
    label_res.config(text=result)
    
    

    

#label
label_res=Label(sonu,width=30,height=2,text="",font=("arial,30"))
label_res.pack()




#button
btn=Button(sonu,text="C",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=50,y=100)
btn=Button(sonu,text="/",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=130,y=100)
btn=Button(sonu,text="%",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=210,y=100)
btn=Button(sonu,text="*",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=290,y=100)



btn=Button(sonu,text="7",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=50,y=160)
btn=Button(sonu,text="8",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=130,y=160)
btn=Button(sonu,text="9",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=210,y=160)
btn=Button(sonu,text="-",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=290,y=160)



btn=Button(sonu,text="4",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=50,y=220)
btn=Button(sonu,text="5",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=130,y=220)
btn=Button(sonu,text="6",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=210,y=220)
btn=Button(sonu,text="+",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=290,y=220)



btn=Button(sonu,text="1",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=50,y=280)
btn=Button(sonu,text="2",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=130,y=280)
btn=Button(sonu,text="3",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=210,y=280)
btn=Button(sonu,text="0",width=12,height=1,font=("arial,40"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=50,y=340)


btn=Button(sonu,text=".",width=5,height=1,font=("arial,30"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=210,y=340)
btn=Button(sonu,text="=",width=5,height=4,font=("arial,30"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=290,y=270)


sonu.mainloop()

