#!/usr/bin/env python

import tkinter as tk
from tkinter.font import Font
import time


class TaskEntry(object):
    def __init__(self):
        self.window_taskenter = tk.Tk()
        self.window_taskenter.title("Enter your tasks")
        self.tasks = None
        #label = tk.Label(text="Enter your tasks")
        #label.pack()
        self.entries = []
        for _ in range(10):
            entry = tk.Entry(width=60)
            entry.pack()
            self.entries.append(entry)

        btn_entered = tk.Button(text="Done", command=self.handle_entrybutton)
        btn_entered.pack()

        self.window_taskenter.mainloop()

    def handle_entrybutton(self):
        print("Woohoo!")
        self.tasks = ([entry.get().strip() for entry in self.entries
                      if len(entry.get()) > 0])
        self.window_taskenter.destroy()


class TaskButtons(object):

    def __init__(self, tasks):
        self.window = tk.Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        windowwidth = int(screen_width * 2 / 3)
        windowheight = int(screen_height * 5 / 6)
        self.window.geometry(f"{windowwidth}x{windowheight}")
        print(f"screen: {screen_width} x {screen_height}")
        self.window.title("Click 'em when they're done!")
        self.dones = [False] * len(tasks)
        btnheight = min(10, int((100 / len(tasks))))
        print(f"btnheight: {btnheight}")
        fontsize = max(btnheight-2, 20)
        fontsize = 20
        myfont = ("Times", str(fontsize), "bold")
        btnwidth = screen_width
        self.buttons = []
        for i in range(len(tasks)):
            button = tk.Button(text=tasks[i], command=lambda idx=i: self.handle_donebutton(idx),
                              # width=btnwidth, height=btnheight, highlightthickness=int(btnheight/2)
                               )
            button['font'] = myfont
            button.pack()
            self.buttons.append(button)
        self.window.mainloop()

    def handle_donebutton(self, task_idx):
        self.dones[task_idx] = True
        self.buttons[task_idx].configure(bg="purple", highlightbackground="red", fg="green")
        print(self.dones)
        if sum(self.dones) == len(self.dones):
            #self.window.destroy()

            #newwindow = tk.Tk()
            #newwindow.title("All done!")
            label = tk.Label(text="You're Done! That's amazing!", font=("Times", 20, "bold")).pack()
            #newwindow.after(3000, newwindow.destroy)
            #newwindow.mainloop()



def main():
    taskentry = TaskEntry()
    print(taskentry.tasks)

    taskbuttons = TaskButtons(taskentry.tasks)



main()

