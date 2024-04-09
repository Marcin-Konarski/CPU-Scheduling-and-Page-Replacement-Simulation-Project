from visualize import VS
from tkinter import messagebox

class LFU:
    def __init__(self, frames_num):
        self.frames_num = frames_num
        self.page_frames = []
        self.faults = 0
        self.visualization_data = []
        self.page_frequency = {}
        self.fault_ratio = 0

    def lfu_simulation(self, pages_list):
        for page in pages_list:
            if page in self.page_frames:
                self.page_frequency[page] += 1   ## If page is already in frames increase it's frequency
                self.visualization_data.append(None)
            else:
                self.faults += 1    ## If page is not in frames - page fault occurs
                if len(self.page_frames) < self.frames_num:
                    self.page_frames.append(page)
                    self.page_frequency[page] = 1
                else:
                    min_page = min(self.page_frequency, key=self.page_frequency.get)    ## Find the page with the minimum frequency
                    self.page_frames[self.page_frames.index(min_page)] = page   ## Replace the page with minimum frequency with the new page
                    self.page_frequency.pop(min_page)  ## Remove the page from frequency dictionary
                    self.page_frequency[page] = 1  ## Set frequency of the new page to 1
            
                self.visualization_data.append((self.page_frames.copy(), self.faults))
        self.fault_ratio = self.faults / len(pages_list)
        visualize_lfu = VS()
        visualize_lfu.visualize(pages_list, self.visualization_data, self.fault_ratio, "LFU")
        visualize_lfu.save_to_file_for_pages(pages_list, self.visualization_data, self.fault_ratio, "lfu_raport.txt")

    def fifo_simulation(self, pages_list):
            pages_copy = pages_list.copy()
            index = 0
            while pages_copy:
                page = pages_copy[0]
                if len(self.page_frames) < self.frames_num:
                    if page not in self.page_frames:
                        self.page_frames.append(page)
                        self.faults += 1
                        self.visualization_data.append((self.page_frames.copy(), self.faults))
                    else:
                        self.visualization_data.append(None)
                else:
                    if page not in self.page_frames:
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
                    else:
                        self.visualization_data.append(None)
                pages_copy.pop(0)





    def start_simulation(self, pages_list):
        if self.frames_num > 0 and self.frames_num < 6:
            self.lfu_simulation(pages_list)
        elif self.frames_num < 6:
            messagebox.showerror("Error", "Invalid number of frames.")
        else:
            messagebox.showerror("Error", "Number of frames cannot be greater then 5.")
