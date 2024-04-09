from display_processes import DISPLAY

class FCFS_with_aging:
    def __init__(self, id, arrival_time, execution_time, turnaround_time, waiting_time, time_until_finish, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.turnaround_time = turnaround_time
        self.waiting_time = waiting_time
        self.time_until_finish = time_until_finish
        self.priority = priority 
        self.average_turnaround_time = 0
        self.average_waiting_time = 0

    def aging_implementaton(self, queue, current_time, quantum_variable):
        ready_processes_list = [process for process in queue if process.arrival_time <= current_time]
        for process in ready_processes_list:
            process.waiting_time = current_time - process.arrival_time
            if process.waiting_time >= quantum_variable:
                process.priority -= (process.waiting_time // quantum_variable)
                process.priority = max(0, process.priority)
        return ready_processes_list

    def fcfs_with_aging_simulation(self, processes, quantum_variable):
        execution_list = [process.execution_time for process in processes]
        processes_done = []
        current_time = 0
        queue = processes.copy()
        while queue:
            ready_processes = self.aging_implementaton(queue, current_time, quantum_variable)
            if ready_processes:
                current_process = min(ready_processes, key=lambda x: (x.priority, x.arrival_time))
                queue.remove(current_process)
                current_process.waiting_time = current_time - current_process.arrival_time
                current_time += current_process.execution_time
                current_process.time_until_finish = current_time
                current_process.turnaround_time = current_time - current_process.arrival_time
                processes_done.append(current_process)
            else:
                current_time += 1
        self.average_waiting_time = sum([process.waiting_time for process in processes]) / len(processes)
        self.average_turnaround_time = sum([process.turnaround_time for process in processes]) / len(processes)
        processes.sort(key=lambda x: x.time_until_finish)   ## just for displaying purposes
        display_fcfs_aging = DISPLAY()
        display_fcfs_aging.display_process_info(processes, current_time, self.average_turnaround_time, self.average_waiting_time, "FCFS With Aging")
        display_fcfs_aging.save_to_file_for_processes(processes, execution_list, self.average_turnaround_time, self.average_waiting_time, current_time, 'fcfs_with_aging_raport.txt')
