from display_processes import DISPLAY

class FCFS:
    def __init__(self, id, arrival_time, execution_time, turnaround_time, waiting_time, time_until_finish):
        self.id = id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.turnaround_time = turnaround_time
        self.waiting_time = waiting_time
        self.time_until_finish = time_until_finish
        self.average_turnaround_time = 0
        self.average_waiting_time = 0

    def fcfs_simulation(self, processes):
        execution_list = [i.execution_time for i in processes]
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        for process in processes:
            process.waiting_time = max(0, current_time - process.arrival_time)
            process.turnaround_time = current_time + process.execution_time - process.arrival_time
            process.time_until_finish = current_time + process.execution_time
            current_time = process.time_until_finish
        self.average_turnaround_time = sum(process.turnaround_time for process in processes) / len(processes)
        self.average_waiting_time = sum(process.waiting_time for process in processes) / len(processes)

        display_fcfs = DISPLAY()
        display_fcfs.display_process_info(processes, current_time, self.average_turnaround_time, self.average_waiting_time, "FCFS")
        display_fcfs.save_to_file_for_processes(processes, execution_list, self.average_turnaround_time, self.average_waiting_time, current_time, 'fcfs_raport.txt')
