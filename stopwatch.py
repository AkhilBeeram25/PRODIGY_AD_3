import tkinter as tk
from datetime import timedelta
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.start_time = None

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:000")

        self.label = tk.Label(root, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_pause)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update()

    def start_pause(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(text="Start")
        else:
            self.is_running = True
            self.start_button.config(text="Pause")
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time += time.time() - self.pause_time

    def reset(self):
        self.is_running = False
        self.start_time = None
        self.time_var.set("00:00:000")
        self.start_button.config(text="Start")

    def update(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            formatted_time = str(timedelta(seconds=elapsed_time))[:-3]
            self.time_var.set(formatted_time)
        else:
            if self.start_time is not None:
                self.pause_time = time.time()
        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
