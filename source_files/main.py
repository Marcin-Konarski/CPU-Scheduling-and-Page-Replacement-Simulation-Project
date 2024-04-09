from process_manager import MANAGER, ProcessEntryWindow
from fcfs_sim import FCFS
from sjf_sim import SJF
from RR_sim_1 import ROUND_ROBIN
from fcfs_with_aging import FCFS_with_aging
from fifo_sim_ import FIFO
from opt_sim import OPT
from lru_sim import LRU
from lfu_sim import LFU


import customtkinter as ctk
from customtkinter import *

def open_question_pool():
    add_new = ProcessEntryWindow(master=ctk.CTkToplevel())
    add_new.open_process_entry_window()

def create_buttons_for_processes(window):
    fcfs_button = CTkButton(window, text="FCFS", command=fcfs_action, height = 100)
    sjf_button = CTkButton(window, text="SJF", command=sjf_action, height = 100)
    fcfs_aging_button = CTkButton(window, text="FCFS with Aging", command=fcfs_aging_action, height = 100)

    fcfs_button.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    sjf_button.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    fcfs_aging_button.grid(row=2, column=0, padx=20, pady=20, sticky="w")

def create_buttons_for_pages(window):
    fifo_button = CTkButton(window, text="FIFO", command=fifo_action, height = 100)
    opt_button = CTkButton(window, text="OPT", command=opt_action, height = 100)
    lru_button = CTkButton(window, text="LRU", command=lru_action, height = 100)
    lfu_button = CTkButton(window, text="LFU", command=lfu_action, height = 100)

    fifo_button.grid(row=0, column=1, padx=20, pady=20)
    opt_button.grid(row=0, column=2, padx=20, pady=20)
    lru_button.grid(row=1, column=1, padx=20, pady=20)
    lfu_button.grid(row=1, column=2, padx=20, pady=20)

def fcfs_action():
    process_manager = MANAGER()
    process_manager.init_processes()
    processes_fcfs = [FCFS(i, process_manager.arrival_list[i], process_manager.execution_list[i], 0, 0, 0) for i in range(process_manager.number_of_processes)]
    fcfs_instance = FCFS(0, 0, 0, 0, 0, 0)
    fcfs_instance.fcfs_simulation(processes_fcfs)

def sjf_action():
    process_manager = MANAGER()
    process_manager.init_processes()
    processes_sjf = [SJF(i, process_manager.arrival_list[i], process_manager.execution_list[i], 0, 0, 0) for i in range(process_manager.number_of_processes)]
    sjf_instance = SJF(0, 0, 0, 0, 0, 0)
    sjf_instance.sjf_simulation(processes_sjf)

def fcfs_aging_action():
    process_manager = MANAGER()
    process_manager.init_processes()
    processes_fcfs_aging = [FCFS_with_aging(i, process_manager.arrival_list[i], process_manager.execution_list[i], 0, 0, 0, process_manager.priority_list[i])
                    for i in range(process_manager.number_of_processes)]
    fcfs_aging_instance = FCFS_with_aging(0, 0, 0, 0, 0, 0, 0)
    fcfs_aging_instance.fcfs_with_aging_simulation(processes_fcfs_aging, process_manager.quantum_fcfs)

def fifo_action():
    page_manager = MANAGER()
    pages_list, frames_num = page_manager.init_pages()
    fifo_simulator = FIFO(frames_num)
    fifo_simulator.start_simulation(pages_list)

def opt_action():
    page_manager = MANAGER()
    pages_list, frames_num = page_manager.init_pages()
    opt_simulator = OPT(frames_num)
    opt_simulator.start_simulation(pages_list)

def lru_action():
    page_manager = MANAGER()
    pages_list, frames_num = page_manager.init_pages()
    lru_simulation = LRU(frames_num)
    lru_simulation.start_simulation(pages_list)

def lfu_action():
    page_manager = MANAGER()
    pages_list, frames_num = page_manager.init_pages()
    lfu_simulation = LFU(frames_num)
    lfu_simulation.start_simulation(pages_list)

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("Simulations Marcin Konarski")
    window.geometry("500x300")

    create_buttons_for_processes(window)
    create_buttons_for_pages(window)

    add_processes_button = CTkButton(window, text="Add New Processes", command = open_question_pool, width = 50, height = 10)
    add_processes_button.grid(row=2, column=1, padx=20, pady=20, sticky="nsew", columnspan=2)

    for i in range(3):
        window.grid_rowconfigure(i, weight=1)

    for i in range(3):
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()
