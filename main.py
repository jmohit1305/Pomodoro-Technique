from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    window.after_cancel(my_timer)
    REPS = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = 0
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        work_sec = WORK_MIN * 60
        title_label.config(text="Work", fg=RED)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        work_sec = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)
    elif REPS == 8:
        work_sec = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg=GREEN)

    count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS
    global my_timer
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        my_timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    elif count < 0 and REPS < 8:
        start_timer()
        tick = ""
        for i in range(math.floor(REPS / 2)):
            tick += "✔"
        checkmark_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.minsize(250, 250)
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

# tomato image and timer
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg="white", highlightthickness=0, bd=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg="white", highlightthickness=0, bd=0,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmark label

checkmark_label = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW, )
checkmark_label.grid(column=1, row=3)

window.mainloop()
