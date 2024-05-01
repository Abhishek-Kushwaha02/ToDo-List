import customtkinter
from tkinter import *
from tkinter import messagebox

proj= customtkinter.CTk()
proj.title('To-Do List')
proj.geometry('450x450')
proj.maxsize(450, 450)
proj.minsize(200, 100)
proj.config(bg='#09112e')

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 10, 'bold')

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0,task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Enter a task.')

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error','Choose a task to delete.')


def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            tasks  = f.readlines()
            for tasks in tasks:
                tasks_list.insert(0, tasks.strip())
    except  FileNotFoundError:
        # messagebox.showerror('Error','Cannot load tasks.')
        pass

    
    

title_label = customtkinter.CTkLabel(proj,font=font1,text='To-Do List',text_color='#fff',bg_color='#09112e')
title_label.place(x=120,y=20)

add_button = customtkinter.CTkButton(proj,command=add_task,font=font2,text_color='#fff',text='Add Task',fg_color='#06911f',hover_color='#06911f',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120)
add_button.place(x=40,y=80)

remove_button = customtkinter.CTkButton(proj,command=remove_task,font=font2,text_color='#fff',text='Remove Task',fg_color='#96061c',hover_color='#96061c',bg_color='#09112e',cursor='hand2',corner_radius=5)
remove_button.place(x=180,y=80)

task_entry = customtkinter.CTkEntry(proj,font=font2,text_color='#000', fg_color='#fff', border_color='#fff',width=280)
task_entry.place(x=40,y=120)

tasks_list = Listbox(proj,width=40,height=15,font=font3)
tasks_list.place(x=80,y=200)

load_tasks() 

proj.mainloop()



proj.mainloop()