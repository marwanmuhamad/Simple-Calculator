import tkinter as tk  


root = tk.Tk()
width = 250
height = 300
x = int(0.5*(root.winfo_screenwidth() - width))
y = int(0.5*(root.winfo_screenheight() - height))
# root.minsize(width = width, height= height)
root.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
root.title("Calculator")
root.iconbitmap('question.ico')
root.resizable(0,0)
root.configure(background = "#303030")

frame1 = tk.Frame(root, width = width)
frame1.pack(side = "top", fill = "x")

inVar = tk.StringVar()
inVar.set("")
label1 = tk.Label(frame1, bg = "#fafafa", textvariable = inVar, fg = "#252525",relief = "flat")
label1.pack(side = "top", fill = "x", anchor = "e", expand = 1)
label1.configure(font = ("Roboto", 20))

resVar = tk.StringVar()
# x = inVar
resVar.set("0")
label2 = tk.Label(frame1, bg = "#fafafa", text="", textvariable = resVar, fg = "#252525",relief = "flat")
label2.pack(side = "top", fill = "x", anchor = "e", expand = 1)
label2.configure(font = ("Roboto", 20))

frame2 = tk.Frame(root, width = width, background = "#404040")
frame2.pack(side = "top", fill = "both", expand = 1)

# Functions:
def clean(e):
    global inVar
    global resVar
    inVar.set("")
    resVar.set("0")

def del_one(e):
    global inVar
    
    x = list(inVar.get())
    del x[len(x) - 1]
    y = ''
    for i in x:
        y += i
    inVar.set(y) 

def psn_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'%'

    inVar.set(x)

def div_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'/'

    inVar.set(x)   

def bnt7_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'7'

    inVar.set(x)  

def bnt8_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'8'

    inVar.set(x)

def bnt9_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'9'

    inVar.set(x)

def bntx_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'*'

    inVar.set(x)
def bnt4_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'4'

    inVar.set(x)
def bnt5_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'5'

    inVar.set(x)
def bnt6_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'6'

    inVar.set(x)
def bntsub_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'-'

    inVar.set(x)
def bnt1_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'1'

    inVar.set(x)
def bnt2_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'2'

    inVar.set(x)
def bnt3_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'3'

    inVar.set(x)
def bntpls_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'+'

    inVar.set(x)
def bnt00_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'00'

    inVar.set(x)
def bnt0_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'0'

    inVar.set(x)
def bntdot_fnc(e):
    global inVar
    x = inVar.get()
    x = x+'.'

    inVar.set(x)

def bnteq_fnc(e):
    global inVar
    global resVar
    x = inVar.get()
    x = x.lstrip('0')
    x = eval(x)

    resVar.set(x)
    

#baris 0:
c_btn = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  C  ", relief = "flat", bd =0)
c_btn.grid(row=0, column=0, ipadx = 5, ipady=5, padx = 5)
c_btn.bind("<Button-1>", clean)
del_btn = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "DEL", relief = "flat", bd =0)
del_btn.grid(row=0, column=1, ipadx = 5, ipady=5, padx = 5)
del_btn.bind("<Button-1>", del_one)
psn_btn = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  %  ", relief = "flat", bd =0)
psn_btn.grid(row=0, column=2, ipadx = 5, ipady=5, padx = 5)
psn_btn.bind("<Button-1>", psn_fnc)
div_btn = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  /  ", relief = "flat", bd =0)
div_btn.grid(row=0, column=3, ipadx = 5, ipady=5, padx = 5)
div_btn.bind("<Button-1>", div_fnc)

#baris 1:
btn_7 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  7  ", relief = "flat", bd =0)
btn_7.grid(row=1, column=0, ipadx = 5, ipady=5, padx = 5)
btn_7.bind("<Button-1>", bnt7_fnc)
btn_8 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  8  ", relief = "flat", bd =0)
btn_8.grid(row=1, column=1, ipadx = 5, ipady=5, padx = 5)
btn_8.bind("<Button-1>", bnt8_fnc)
btn_9 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  9  ", relief = "flat", bd =0)
btn_9.grid(row=1, column=2, ipadx = 5, ipady=5, padx = 5)
btn_9.bind("<Button-1>", bnt9_fnc)
btn_x = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  \u00D7  ", relief = "flat", bd =0)
btn_x.grid(row=1, column=3, ipadx = 5, ipady=5, padx = 5)
btn_x.bind("<Button-1>", bntx_fnc)

#baris 2:
btn_4 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  4  ", relief = "flat", bd =0)
btn_4.grid(row=2, column=0, ipadx = 5, ipady=5, padx = 5)
btn_4.bind("<Button-1>", bnt4_fnc)
btn_5 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  5  ", relief = "flat", bd =0)
btn_5.grid(row=2, column=1, ipadx = 5, ipady=5, padx = 5)
btn_5.bind("<Button-1>", bnt5_fnc)
btn_6 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  6  ", relief = "flat", bd =0)
btn_6.grid(row=2, column=2, ipadx = 5, ipady=5, padx = 5)
btn_6.bind("<Button-1>", bnt6_fnc)
btn_sub = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  -  ", relief = "flat", bd =0)
btn_sub.grid(row=2, column=3, ipadx = 5, ipady=5, padx = 5)
btn_sub.bind("<Button-1>", bntsub_fnc)

#baris 3:
btn_1 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  1  ", relief = "flat", bd =0)
btn_1.grid(row=3, column=0, ipadx = 5, ipady=5, padx = 5)
btn_1.bind("<Button-1>", bnt1_fnc)
btn_2 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  2  ", relief = "flat", bd =0)
btn_2.grid(row=3, column=1, ipadx = 5, ipady=5, padx = 5)
btn_2.bind("<Button-1>", bnt2_fnc)
btn_3 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  3  ", relief = "flat", bd =0)
btn_3.grid(row=3, column=2, ipadx = 5, ipady=5, padx = 5)
btn_3.bind("<Button-1>", bnt3_fnc)
btn_pls = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  +  ", relief = "flat", bd =0)
btn_pls.grid(row=3, column=3, ipadx = 5, ipady=5, padx = 5)
btn_pls.bind("<Button-1>", bntpls_fnc)

#baris 4btn_7:
btn_00 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = " 00 ", relief = "flat", bd =0)
btn_00.grid(row=4, column=0, ipadx = 5, ipady=5, padx = 5)
btn_00.bind("<Button-1>", bnt00_fnc)
btn_0 = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  0  ", relief = "flat", bd =0)
btn_0.grid(row=4, column=1, ipadx = 5, ipady=5, padx = 5)
btn_0.bind("<Button-1>", bnt0_fnc)
btn_dot = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  .  ", relief = "flat", bd =0)
btn_dot.grid(row=4, column=2, ipadx = 5, ipady=5, padx = 5)
btn_dot.bind("<Button-1>", bntdot_fnc)
btn_eq = tk.Button(frame2,  bg = "#404040", fg = "#fabc12", font=("Roboto, 13"), text = "  =  ", relief = "flat", bd =0)
btn_eq.grid(row=4, column=3, ipadx = 5, ipady=5, padx = 5)
btn_eq.bind("<Button-1>", bnteq_fnc)

root.mainloop()
