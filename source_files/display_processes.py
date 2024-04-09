import tkinter as tk
from tkinter import W, Button, scrolledtext
import matplotlib.pyplot as plt
import os

class DISPLAY:
    def display_process_info(self, processes, total_time, average_turnaround_time, average_waiting_time, title):
        window = tk.Tk()
        window.geometry("840x370")
        window.title(f"{title} Simulation")

        text_area = scrolledtext.ScrolledText(window, width=150, height=20, wrap=tk.WORD, font=("Courier New", 10))
        text_area.pack(padx=10, pady=10)

        if title == "FCFS With Aging":
            text_area.insert(tk.END, "ID\tArrival Time\tExecution Time\tWaiting Time\tTurnaround Time\tPriority\tTime Until Finish\n")
            for process in processes:
                text_area.insert(tk.END, f"{process.id}\t{process.arrival_time}\t\t{process.execution_time}\t\t{process.waiting_time}\t\t {process.turnaround_time}\t   {process.priority}\t  {process.time_until_finish}\n")
        else:
            text_area.insert(tk.END, "ID\tArrival Time\tExecution Time\tWaiting Time\tTurnaround Time\tTime Until Finish\n")
            for process in processes:
                text_area.insert(tk.END, f"{process.id}\t{process.arrival_time}\t\t{process.execution_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}\t  {process.time_until_finish}\n")

        text_area.insert(tk.END, f"\nTotal time for all processes to finish: {total_time}\n")
        text_area.insert(tk.END, f"Average turnaround time: {average_turnaround_time}\n")
        text_area.insert(tk.END, f"Average waiting time: {average_waiting_time}\n")

        self.display_gantt_chart(processes, 13, 5)

        window.mainloop()

    def display_gantt_chart(self, processes, width, height):
        fig, ax = plt.subplots(figsize=(width, height))

        processes.sort(key=lambda x: x.time_until_finish)

        for index, process in enumerate(processes):
            ax.barh(y=index, width=process.execution_time, left=process.time_until_finish - process.execution_time, label=f"Process {process.id}")

        # Set y-ticks and labels to be the original process IDs
        ax.set_yticks(range(len(processes)))
        ax.set_yticklabels([process.id for process in processes])

        ax.set_xlabel("Time")
        ax.set_ylabel("Process ID")
        ax.set_title("Gantt Chart")

        ax.invert_yaxis()
        ax.legend(loc="upper right")
        plt.show()


    def save_to_file_for_processes(self, processes, execution_list, average_turnaround_time, average_waiting_time, total_time, output_file_path):
        with open(output_file_path, "w") as output_file:
            output_file.write("ID\tPriority\tArrival Time\tTime Until Finish\tTurnaround Time\tBurst Time\tWaiting Time\n")

            if output_file_path == 'fcfs_with_aging_raport.txt':
                for process in processes:
                    output_file.write(f"{process.id}\t{process.priority}\t{process.arrival_time}\t\t{process.time_until_finish}\t\t\t{process.turnaround_time}\t\t\t\t{execution_list[process.id]}\t\t{process.waiting_time}\n")
            else:
                for process in processes:
                    output_file.write(f"{process.id}\t{process.arrival_time}\t\t{process.time_until_finish}\t\t{process.turnaround_time}\t\t\t{execution_list[process.id]}\t\t\t\t{process.waiting_time}\n")
            # Write total time and averages to the file
            output_file.write(f"\nTotal time for all processes to finish: {total_time}\n")
            output_file.write(f"Average Turnaround Time: {average_turnaround_time}\n")
            output_file.write(f"Average Waiting Time: {average_waiting_time}\n")

    def save_to_file_for_processes(self, processes, execution_list, average_turnaround_time, average_waiting_time, total_time, output_file_path):
        os.makedirs("raports", exist_ok=True)   ## Create "raports" folder if it doesn't exist
        output_file_path = os.path.join("raports", output_file_path)

        with open(output_file_path, "w") as output_file:
            if "fcfs_with_aging" in output_file_path:
                    output_file.write("ID\tPriority\tArrival Time\tTime Until Finish\tTurnaround Time\tBurst Time\tWaiting Time\n")
            else:
                    output_file.write("ID\tArrival Time\tTime Until Finish\tTurnaround Time\tBurst Time\tWaiting Time\n")

            if "fcfs_with_aging" in output_file_path:
                for process in processes:
                    output_file.write(f"{process.id}\t{process.priority}\t\t{process.arrival_time}\t\t{process.time_until_finish}\t\t\t{process.turnaround_time}\t\t{execution_list[process.id]}\t\t{process.waiting_time}\n")
            else:
                for process in processes:
                    output_file.write(f"{process.id}\t{process.arrival_time}\t\t{process.time_until_finish}\t\t\t{process.turnaround_time}\t\t{execution_list[process.id]}\t\t{process.waiting_time}\n")
            output_file.write(f"\nTotal time for all processes to finish: {total_time}\n")
            output_file.write(f"Average Turnaround Time: {average_turnaround_time}\n")
            output_file.write(f"Average Waiting Time: {average_waiting_time}\n")
