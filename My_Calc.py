from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading


font=("Verdana",22,)
ob=PlayAudio()






#  *******************   Functions of scientific calculator  *****************
def calculate_sc(event):
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textfield.get()
    ans=''
    if text == "ToDeg":
        print("cal degree")
        ans=str(m.degrees(float(ex)))

    elif text=='ToRad':
        print("radian")
        ans=str(m.radians(float(ex)))

    elif text=='x!':
        print("cal factorial")
        ans=str(m.factorial(int(ex)))

    elif text == 'Sinϴ':
        print("cal sin")
        ans=str(m.sin(m.radians(float(ex))))

    elif text == 'Sinhϴ':
        print("cal sinh")
        ans=str(m.sinh(m.radians(float(ex))))

    elif text == 'Coshϴ':
        print("cal cosh")
        ans=str(m.cosh(m.radians(float(ex))))

    elif text == 'Tanhϴ':
        print("Cal tanh")
        ans=str(m.tanh(m.radians(float(ex))))

    elif text == 'Cosϴ':
        print("cal cos")
        ans=str(m.cos(m.radians(float(ex))))

    elif text =="Tanϴ":
        print("cal tan")
        ans=str(m.tan(m.radians(float(ex))))

    elif text=="log(x)":
        print("cal log base 10")
        ans=str(m.log10(float(ex)))

    elif text =="lg(x)":
        print("cal log base e")
        ans=str(m.log(float(ex)))

    elif text == "√":
        print("cal sqrt")
        ans=str(m.sqrt(float(ex)))

    elif text=="x^2":
        print("sq calculated")
        ans=str(float(ex)*float(ex))

    textfield.delete(0,END)
    textfield.insert(0,ans)






# ******************To get Scientific Calculator LAYOUT *********************
normalcalc=True
def sc_clicked():
    global normalcalc
    if normalcalc:
        print("show sc")
        normalcalc=False

        # Forgetting button frame
        buttonFrame.pack_forget()

        #adding TOP frame, SC frame, Button frame AGAIN
        topFrame.pack(side=TOP,fill="x",pady=6,padx=3)
        scFrame.pack(side=RIGHT,padx=2,expand="true",fill="both")
        buttonFrame.pack(side=TOP,padx=5)


        # ROOT Window Positioning
        win_w,win_h=650,610

        screen_w=root.winfo_screenwidth()
        screen_h=root.winfo_screenheight()

        pos_top=int(screen_h/2 - win_h/2)
        pos_right=int(screen_w/2 - win_w/2)

        root.geometry(f'{win_w}x{win_h}+{pos_right}+{pos_top-50}')

    else:
        print("show normal")
        normalcalc=True

        # **  Showing only Normal Layout  ***
        scFrame.pack_forget()
        topFrame.pack_forget()
        # **  Again Positioning of Root Window ***

        window_width, window_height = 450, 530

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top - 50}')





#  **********************  Functions to Change Voice  **************************

vReq=True
m_or_f=0
def noVoice():
    global vReq
    print("No voice")
    vReq = False

def maleVoice():
    global vReq
    global m_or_f
    print("Male voice")
    vReq = True
    m_or_f = 0

def femaleVoice():
    global vReq
    global m_or_f
    print("Female voice")
    vReq = True
    m_or_f = 1







# ********************Functions for Normal Calculator LAYOUT ********************
def clear():
    ex=textfield.get()
    ex = ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

def all_clear():
    textfield.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    t=threading.Thread(target=ob.speak,args=(text,vReq,m_or_f))
    t.start()


    if text =='x':
        textfield.insert(END,'*')
        return
    

    if text == "x^y":
        print("cal power")
        textfield.insert(END,'**')
        return

    if text == '=':
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print("Error",e)
            showerror("Error","Wrong Syntax")
            textfield.delete(0,END)
        return

    textfield.insert(END,text)





# *********************** Creating a ROOT window **************************
root=Tk()
root.title("My Calculator")
root.resizable(0,0)

# *********************** Window Positioning ***************************
window_width,window_height=450,530

screen_width= root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right=int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top-50}')



root.config(bg="royalblue2")








# *********************** MENU Bar *****************************

menubar=Menu(root)
root.config(menu=menubar)

sc_layout=Menu(menubar,font=("Verdana",11),tearoff=0)
sc_layout.add_checkbutton(label="Scientific Calculator",command=sc_clicked)
menubar.add_cascade(label="SC Layout",menu=sc_layout)

voice=Menu(menubar, font=("Verdana",11), tearoff=0)
voice.add_radiobutton(label="No Voice", command=noVoice)
voice.add_radiobutton(label="Male Voice", command=maleVoice)
voice.add_radiobutton(label="Female Voice", command=femaleVoice)
menubar.add_cascade(label="Voice", menu=voice)





# ************************  Using Label for picture  ******************
pic=PhotoImage(file="image/Green_Cal.png")
imgLabel=Label(root, image=pic)
imgLabel.pack(side=TOP,pady=10)


# ************************ Using label for heading  ******************
heading=Label(root,text="Scientific Calculator",font=("Verdana",23,"bold"),bg="royalblue2",fg="olivedrab2")
heading.pack(side=TOP)


# ************************ Using Entry for textfield  ****************
textfield=Entry(root,font=font,justify=CENTER)
textfield.pack(side=TOP,pady=10,fill=X,padx=10)




# ************************  Making FRAME for buttons  *****************
buttonFrame=Frame(root,bg="royalblue2")
buttonFrame.pack(side="top",padx=5)



# ************************  Adding Buttons in Frames  ******************
allClearBtn=Button(buttonFrame,text="AC",font=font,width=11,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white",
                   command=all_clear)
allClearBtn.grid(row=0,column=0,columnspan=2,padx=3,pady=3)

clearBtn=Button(buttonFrame,text="Del",font=font,width=11,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white",
                command=clear)
clearBtn.grid(row=0,column=2,columnspan=2,padx=3,pady=3)

temp=9
for i in range(1,4):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
        btn.grid(row=i,column=j,padx=3,pady=3)
        btn.bind("<Button-1>",click_btn_function)
        temp-=1

zeroBtn=Button(buttonFrame,text="0",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
zeroBtn.grid(row=4,column=0,padx=3,pady=3)


dotBtn=Button(buttonFrame,text=".",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
dotBtn.grid(row=4,column=1,padx=3,pady=3)

equalBtn=Button(buttonFrame,text="=",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
equalBtn.grid(row=4,column=2,padx=3,pady=3)

plusBtn=Button(buttonFrame,text="+",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
plusBtn.grid(row=1,column=3,padx=3,pady=3)

minusBtn=Button(buttonFrame,text="-",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
minusBtn.grid(row=2,column=3,padx=3,pady=3)

multBtn=Button(buttonFrame,text="x",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
multBtn.grid(row=3,column=3,padx=3,pady=3)

divBtn=Button(buttonFrame,text="/",font=font,width=5,relief="flat",bg="gray88",activebackground="gray70",activeforeground="white")
divBtn.grid(row=4,column=3,padx=3,pady=3)





#  *************************  Binding all Normal buttons  ********************
plusBtn.bind("<Button-1>",click_btn_function)
multBtn.bind("<Button-1>",click_btn_function)
divBtn.bind("<Button-1>",click_btn_function)
minusBtn.bind("<Button-1>",click_btn_function)
zeroBtn.bind("<Button-1>",click_btn_function)
dotBtn.bind("<Button-1>",click_btn_function)
equalBtn.bind("<Button-1>",click_btn_function)

def enterClick(event):
    print("= clicked")
    e=Event()
    e.widget=equalBtn
    click_btn_function(e)

textfield.bind("<Return>",enterClick)





# ****************************  Scientific Calculator  *********************

scfont=("verdana",22)

# *************************** Frames for SCIENTIFIC Layout ****************
topFrame=Frame(root,bg="royalblue2")
scFrame=Frame(root,bg="royalblue2")


# *********************** Adding SC Buttons in TOP FRAME  *******************
lbracBtn=Button(topFrame,text="(",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
lbracBtn.grid(row=0,column=0,padx=3,pady=3)

rbracBtn=Button(topFrame,text=")",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
rbracBtn.grid(row=0,column=1,padx=3,pady=3)

sqBtn=Button(topFrame,text="x^2",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
sqBtn.grid(row=0,column=5,padx=3,pady=3)

sqrtBtn=Button(topFrame,text="√",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
sqrtBtn.grid(row=0,column=6,padx=3,pady=3)


# *************************  Adding SC buttons in SC FRAME  *********************
powBtn=Button(scFrame,text="x^y",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
powBtn.grid(row=1,column=0,padx=3,pady=3)

factBtn=Button(scFrame,text="x!",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
factBtn.grid(row=1,column=1,padx=3,pady=3)

radBtn=Button(topFrame,text="ToRad",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
radBtn.grid(row=0,column=2,padx=3,pady=3)

degBtn=Button(topFrame,text="ToDeg",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
degBtn.grid(row=0,column=3,padx=3,pady=3)

sinBtn=Button(scFrame,text="Sinϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
sinBtn.grid(row=3,column=0,padx=3,pady=3)

sinhBtn=Button(scFrame,text="Sinhϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
sinhBtn.grid(row=3,column=1,padx=3,pady=3)

cosBtn=Button(scFrame,text="Cosϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
cosBtn.grid(row=4,column=0,padx=3,pady=3)

coshBtn=Button(scFrame,text="Coshϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
coshBtn.grid(row=4,column=1,padx=3,pady=3)

tanBtn=Button(scFrame,text="Tanϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
tanBtn.grid(row=5,column=0,padx=3,pady=3)

tanhBtn=Button(scFrame,text="Tanhϴ",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
tanhBtn.grid(row=5,column=1,padx=3,pady=3)

logBtn=Button(scFrame,text="log(x)",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
logBtn.grid(row=6,column=0,padx=3,pady=3)

lgBtn=Button(scFrame,text="lg(x)",font=scfont,width=5,relief="flat",bg="olivedrab2",activebackground="gray70",activeforeground="white")
lgBtn.grid(row=6,column=1,padx=3,pady=3)










# **************************  Binding SC buttons  **************************

lbracBtn.bind("<Button-1>",click_btn_function)
rbracBtn.bind("<Button-1>",click_btn_function)
sqBtn.bind("<Button-1>",calculate_sc)
sqrtBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",click_btn_function)
factBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
sinhBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
coshBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)
tanhBtn.bind("<Button-1>",calculate_sc)
logBtn.bind("<Button-1>",calculate_sc)
lgBtn.bind("<Button-1>",calculate_sc)






root.mainloop()