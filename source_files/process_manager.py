class MANAGER:
    def __init__(self):
        self.arrival_list = []  ## for processes algorithms
        self.execution_list = []
        self.priority_list = []
        self.quantum_fcfs = 0
        self.quantum_rr = 0
        self.number_of_processes = 0
        self.pages_list = []    ## <-- for page replacement algorithms

    def init_processes(self, file_path='processes_generated.txt'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                values = list(map(int, line.split()))   ## prepare values to processes
                if index == 0:
                    self.arrival_list.extend(values)
                elif index == 1:
                    self.execution_list.extend(values)
                elif index == 2:
                    self.priority_list.extend(values)
                elif index == 3:
                    self.quantum_fcfs = values[0]
                elif index == 4:
                    self.quantum_rr = values[0]

        self.number_of_processes = min(len(self.arrival_list), len(self.execution_list), len(self.priority_list))

    def init_pages(self, file_path = 'pages_generated.txt'):
        with open(file_path, 'r') as file:
            for line in file.readlines():
                self.pages_list.extend(line.split())
        frames = int(self.pages_list[len(self.pages_list) - 1])
        self.pages_list = self.pages_list[:-1]
        return self.pages_list, frames
    

import tkinter as tk
from tkinter import messagebox

class ProcessEntryWindow:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Add New Process")

        self.label_arrival_time = tk.Label(master, text="Arrival Time:")
        self.label_execution_time = tk.Label(master, text="Execution Time:")
        self.label_priority = tk.Label(master, text="Priority:")

        self.entry_arrival_time = tk.Entry(master)
        self.entry_execution_time = tk.Entry(master)
        self.entry_priority = tk.Entry(master)

        self.button_submit = tk.Button(master, text="Add Process", command=lambda: self.add_process())

        ## make it into nice layout
        self.label_arrival_time.grid(row=0, column=0, padx=10, pady=10)
        self.entry_arrival_time.grid(row=0, column=1, padx=10, pady=10)
        self.label_execution_time.grid(row=1, column=0, padx=10, pady=10)
        self.entry_execution_time.grid(row=1, column=1, padx=10, pady=10)
        self.label_priority.grid(row=2, column=0, padx=10, pady=10)
        self.entry_priority.grid(row=2, column=1, padx=10, pady=10)
        self.button_submit.grid(row=3, column=0, columnspan=2, pady=10)

    def add_process(self, file_path='processes_generated.txt'):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
     
            arrival_time = int(self.entry_arrival_time.get())
            execution_time = int(self.entry_execution_time.get())
            priority = int(self.entry_priority.get())

            lines[0] = lines[0].rstrip() + f" {arrival_time}\n"
            lines[1] = lines[1].rstrip() + f" {execution_time}\n"
            lines[2] = lines[2].rstrip() + f" {priority}\n"
            
            with open(file_path, "w") as file:
                file.writelines(lines)

            self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for arrival time, execution time, and priority.")

    def open_process_entry_window(self):
        self.master.mainloop()
