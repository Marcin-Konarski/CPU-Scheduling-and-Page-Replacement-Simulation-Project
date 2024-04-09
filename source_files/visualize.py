import tkinter as tk
import os

class VS:
    def visualize(self, pages_list, visualization_data, fault_ratio, title):
        window = tk.Tk()
        window.title(f"{title} Simulation")

        frame_texts_list = []

        for i, data in enumerate(visualization_data):  ## for every tuple in a list display 
            if data is not None:
                frames, faults = data
                frame_text = f'Current: {pages_list[i]} Frame Status: {frames} Page Faults: {faults}'
            else:
                frame_text = f'Current: {pages_list[i]} Frame Status: {frames} Page Hit'

            frame_texts_list.append(frame_text)

        final_text = '\n'.join(frame_texts_list)
        text_label = tk.Label(window, text=final_text, font=("Calibri", 16), justify="left")    ## create a label with a text to display
        text_label.pack(padx=10, pady=10)
        hit_ratio_label = tk.Label(window, text=f"Fault Ratio: {fault_ratio}", font=("Calibri", 16), justify="left")
        hit_ratio_label.pack(padx=10, pady=10)
        window.mainloop()

    def save_to_file_for_pages(self, pages_list, visualization_data, hit_ratio, output_file_path):
        os.makedirs("raports", exist_ok=True)
        output_file_path = os.path.join("raports", output_file_path)
        with open(output_file_path, "w") as file:
            for i, data in enumerate(visualization_data):
                if data is not None:
                    frames, faults = data
                    file.write(f'Current: {pages_list[i]} Frame Status: {frames} Page Faults: {faults}\n')
                else:
                    file.write(f'Current: {pages_list[i]} Frame Status: {frames}\n')
            file.write(f"Fault Ratio: {hit_ratio}")
