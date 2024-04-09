from display_processes import DISPLAY

class SJF:
    def __init__(self, id, arrival_time, execution_time, turnaround_time, waiting_time, time_until_finish):
        self.id = id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.turnaround_time = turnaround_time
        self.waiting_time = waiting_time
        self.time_until_finish = time_until_finish
        self.average_turnaround_time = 0
        self.average_waiting_time = 0

    def sjf_simulation(self, processes):
        execution_list = [i.execution_time for i in processes]
        processes_done = []
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        queue = processes.copy()

        while queue:
            ready_processes = [process for process in queue if process.arrival_time <= current_time]
            if ready_processes:
                shortest_job = min(ready_processes, key=lambda x: x.execution_time)
                queue.remove(shortest_job)

                shortest_job.waiting_time = current_time - shortest_job.arrival_time
                self.waiting_time += shortest_job.waiting_time
                current_time += shortest_job.execution_time
                shortest_job.time_until_finish = current_time
                shortest_job.turnaround_time = current_time - shortest_job.arrival_time
                processes_done.append(shortest_job)
            else:
                current_time += 1
        self.average_waiting_time = sum([process.waiting_time for process in processes]) / len(processes)
        self.average_turnaround_time = sum([process.turnaround_time for process in processes]) / len(processes)

        display_sjf = DISPLAY()
        display_sjf.display_process_info(processes_done, current_time, self.average_turnaround_time, self.average_waiting_time, "SJF")
        display_sjf.save_to_file_for_processes(processes, execution_list, self.average_turnaround_time, self.average_waiting_time, current_time, 'sjf_raport.txt')
