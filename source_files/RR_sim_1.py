from display_processes import DISPLAY

import tkinter as tk
from tkinter import W, scrolledtext

class ROUND_ROBIN:
    def __init__(self, id, arrival_time, execution_time, turnaround_time, waiting_time, time_until_finish, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.turnaround_time = turnaround_time
        self.waiting_time = waiting_time
        self.time_until_finish = time_until_finish
        self.priority = priority
        self.started_execution = False  # Flag to track if the process has started executing
        self.average_turnaround_time = 0
        self.average_waiting_time = 0

    def round_robin_simulation(self, processes, quantum_variable, current_time):
        execution_list = [process.execution_time for process in processes]
        processes.sort(key=lambda x: (x.arrival_time, x.priority))
        while any(process.execution_time > 0 for process in processes):
            for process in processes:
                if process.execution_time == 0:
                    continue

                if process.execution_time <= quantum_variable:
                    if not process.started_execution:
                        process.waiting_time = current_time - process.arrival_time
                        process.started_execution = True
                    current_time += process.execution_time
                    process.turnaround_time = current_time - process.arrival_time
                    process.time_until_finish = current_time
                    process.execution_time = 0
                    print(f"id: {process.id}\tarrival: {process.arrival_time},\tburst time: {process.execution_time},\t\tpriority: {process.priority}\tcurrent time: {current_time}")
                else:
                    if not process.started_execution:
                        process.waiting_time = current_time - process.arrival_time
                        process.started_execution = True
                    current_time += quantum_variable
                    process.execution_time -= quantum_variable
                    print(f"id: {process.id}\tarrival: {process.arrival_time},\tburst time: {quantum_variable},\t\tpriority: {process.priority}\tcurrent time: {current_time}")
            self.print_processes_info(processes, execution_list)
        print("\n\n")
        self.print_processes_info(processes, execution_list)

    def print_processes_info(self, processes, execution_list):
        processes.sort(key=lambda x: (x.time_until_finish))
        average_turnaround_time = sum([process.turnaround_time for process in processes]) / len(processes)
        average_waiting_time = sum([process.waiting_time for process in processes]) / len(processes)
        print("ID\tPriority\tArrival Time\tTime Until Finish\tTurnaround Time\tBurst Time\tWaiting Time")
        for process in processes:
            print(f"{process.id}\t{process.priority}\t{process.arrival_time}\t\t{process.time_until_finish}\t\t{process.turnaround_time}\t\t{execution_list[process.id]}\t\t{process.waiting_time}")
        print(f"\nAverage Turnaround Time: {average_turnaround_time}\nAverage Waiting Time: {average_waiting_time}")
