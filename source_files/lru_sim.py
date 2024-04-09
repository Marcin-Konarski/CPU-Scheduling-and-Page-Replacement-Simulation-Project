from visualize import VS
from tkinter import messagebox

class LRU:
    def __init__(self, frames_num):
        self.frames_num = frames_num
        self.page_frames = []
        self.faults = 0
        self.visualization_data = []
        self.access_order = []  ## a list to maintain the order of page accesses
        self.fault_ratio = 0

    def lru_simulation(self, pages_list):
        for page in pages_list:
            if page in self.page_frames:
                # Page is already in frames, move it to the front to indicate most recent usage
                self.access_order.remove(page)
                self.access_order.insert(0, page)
                self.visualization_data.append(None)
            else:
                self.faults += 1
                if len(self.page_frames) < self.frames_num:
                    self.page_frames.append(page)
                    self.access_order.insert(0, page)
                    self.visualization_data.append((self.page_frames.copy(), self.faults))
                else:
                    # If there are no empty frames, remove the least recently used page and append the new one
                    lru_page = self.access_order.pop()
                    index = self.page_frames.index(lru_page)
                    self.page_frames[index] = page
                    self.access_order.insert(0, page)
                    self.visualization_data.append((self.page_frames.copy(), self.faults))

        self.fault_ratio = self.faults / len(pages_list)
        visualize_lru = VS()
        visualize_lru.visualize(pages_list, self.visualization_data, self.fault_ratio, "LRU")
        visualize_lru.save_to_file_for_pages(pages_list, self.visualization_data, self.fault_ratio, "lru_report.txt")


    def start_simulation(self, pages_list):
        if self.frames_num > 0 and self.frames_num < 6:
            self.lru_simulation(pages_list)
        elif self.frames_num < 6:
            messagebox.showerror("Error", "Invalid number of frames.")
        else:
            messagebox.showerror("Error", "Number of frames cannot be greater then 5.")
