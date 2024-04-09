from visualize import VS
from tkinter import messagebox

class OPT:
    def __init__(self, frames_num):
        self.frames_num = frames_num
        self.page_frames = []
        self.faults = 0
        self.visualization_data = []
        self.fault_ratio = 0

    def opt_simulation(self, pages_list):
        for i, page in enumerate(pages_list):
            found = any(frame == page for frame in self.page_frames)    ## if found in page in current frame
            if found:
                self.visualization_data.append(None)    ## then there is no page fault
                continue

            if len(self.page_frames) < self.frames_num: ## otherwise if there are any empty frames then just add a page to empty frame
                self.page_frames.append(page)
                self.faults += 1
            else:
                remaining_pages = pages_list[i + 1:]    ## create a list of remaining pages from the current page up until the end
                frame_distances = {}    ## create dictionary in order to...
                for frame in self.page_frames:  ## ... associate every page's value from a frame with it's distance 
                    if frame in remaining_pages:
                        frame_distances[frame] = remaining_pages.index(frame)
                    else:
                        frame_distances[frame] = float('inf')   ## if there is no more such page in reference string then assign inf value
                page_to_replace = max(frame_distances, key=frame_distances.get) ## get the dictionary with highest key's value - highest distance
                replaceIndex = self.page_frames.index(page_to_replace) ## find out which frame in the current frames has the maximum distance to the current page
                self.page_frames[replaceIndex] = page ## replaces the page at found index
                self.faults += 1    ## indicate page fault
                
            self.visualization_data.append((self.page_frames.copy(), self.faults))  ## append data for displaying
        self.fault_ratio = self.faults / len(pages_list)
        visualize_opt = VS()
        visualize_opt.visualize(pages_list, self.visualization_data, self.fault_ratio, "OPT")
        visualize_opt.save_to_file_for_pages(pages_list, self.visualization_data, self.fault_ratio, "opt_raport.txt")

    def start_simulation(self, pages_list):
        if self.frames_num > 0 and self.frames_num < 6:
            self.opt_simulation(pages_list)
        elif self.frames_num < 6:
            messagebox.showerror("Error", "Invalid number of frames.")
        else:
            messagebox.showerror("Error", "Number of frames cannot be greater then 5.")
