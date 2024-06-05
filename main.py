import time
from tkinter import *
import math

REST = 1
WORK = 1
timer_fun = ""

window = Tk()
window.title("Pomodoro Project")
window.config(bg="#9bdeac")

img1 = PhotoImage(file="tomato.png")
canvas = Canvas(width=600,height=450, bg="#9bdeac")
canvas.create_image(300,225,image=img1)
timer = canvas.create_text(295,245,text=f"00:00", font=("Courier",24,"bold"), fill="white")
canvas.pack()

def count_down(tempo):
    global REST
    global WORK
    canvas.itemconfig(timer, text=(f"{math.floor(tempo/60)}:{tempo%60 if tempo%60 != 0 else "00"}"))
    if tempo>0:
        global timer_fun
        timer_fun = window.after(1000, count_down, tempo - 1)
        if my_label["text"] == "Timer":
            window.after(1000, count_down, 0)
            canvas.itemconfig(timer, text="00:00")
    else:
        REST += 1
        if REST == 1 or REST == 3 or REST == 5 or REST == 7:
            my_label["text"] = f"Work{WORK}/4"
            WORK += 1
            count_down(1500)
        elif REST == 2 or REST == 4 or REST == 6:
            my_label["text"] = "Rest"
            count_down(300)
        elif REST == 8:
            my_label["text"] = "Rest more"
            REST = 0
            count_down(1200)

def timer_start():
    if my_label["text"] == "Timer":
        my_label["text"] = "Work"
        count_down(1500)
    else:
        my_label_bottom.place(x=205, y=360)
def timer_reset():
    window.after_cancel(timer_fun)
    canvas.itemconfig(timer, text="00:00")
    my_label_bottom.place(x=2000, y=2000)
    my_label["text"] = "Timer"


my_label = Label(text="Timer", font=("Courier",30,"bold"), bg="#9bdeac")
my_label.place(x=240,y=50)
my_label_bottom = Label(text="please reset to continue", font=("Courier",10))

butao_st = Button(text="start", command=timer_start)
butao_st.place(x=180,y=400)

butao_st = Button(text="restart", command=timer_reset)
butao_st.place(x=360,y=400)
window.mainloop()