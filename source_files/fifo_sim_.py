from visualize import VS
from tkinter import messagebox

class FIFO:
    def __init__(self, frames_num):
        self.frames_num = frames_num
        self.page_frames = []
        self.faults = 0
        self.faults_ratio = 0
        self.visualization_data = []

    def fifo_simulation(self, pages_list):
            index = 0
            for page in pages_list:
                if page in self.page_frames:
                    self.visualization_data.append(None)
                else:
                    if len(self.page_frames) < self.frames_num:
                        self.page_frames.append(page)
                        self.faults += 1
                        self.visualization_data.append((self.page_frames.copy(), self.faults))
                    else:
                        if len(self.page_frames) < self.frames_num:
                            self.page_frames.append(page)
                        else:
                            self.page_frames[index] = page
                        if index < self.frames_num - 1:
                            index += 1
                        else:
                            index = 0
                        self.faults += 1
                        self.visualization_data.append((self.page_frames.copy(), self.faults))
            self.faults_ratio = self.faults / len(pages_list)
            visualize_fifo = VS()
            visualize_fifo.visualize(pages_list, self.visualization_data, self.faults_ratio, "FIFO")
            visualize_fifo.save_to_file_for_pages(pages_list, self.visualization_data, self.faults_ratio, "fifo_raport.txt")

    def start_simulation(self, pages_list):
        if self.frames_num > 0 and self.frames_num < 6:
            self.fifo_simulation(pages_list)
        elif self.frames_num < 6:
            messagebox.showerror("Error", "Invalid number of frames.")
        else:
            messagebox.showerror("Error", "Number of frames cannot be greater then 5.")

