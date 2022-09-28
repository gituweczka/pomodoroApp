from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 35
SHORT_BREAK_MIN = 6
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_counting():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Timer", fg= GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_counting():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 2 == 1:
        main_label.config(text="Study", fg=PINK)
        count_down(work_sec)
    elif reps % 8 == 0:
        main_label.config(text="Break", fg=GREEN)
        count_down(long_break_sec)
    else:
        main_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_counting()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += " ✔"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


main_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
main_label.grid(column=1, row=0)

check_marks = Label(bg=YELLOW, fg=RED)
check_marks.grid(column=1, row=3)


start_button = Button(text="Start", command=start_counting, fg=RED, bg=YELLOW)
start_button.grid(column=0, row=2)

reset_button= Button(text="Reset", command=reset_counting, fg=RED, bg=YELLOW)
reset_button.grid(column=2, row=2)





window.mainloop()