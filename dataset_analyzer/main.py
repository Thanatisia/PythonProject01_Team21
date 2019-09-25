import Tkinter as tk
import analysis_page

# Set the window size here
HEIGHT = 600
WIDTH = 600


class Application (tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    # Destroys current frame and replaces it with a new one.
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    # Reads a csv file and stores it in a dictionary list
    def read_csv(self, _file_path):
        # TODO: Implement read_csv() function
        self.data_set1 = ["Placeholder"]
        self.data_set2 = ["Placeholder"]

    def __init__(self, master):
        self.data_set1 = []
        self.data_set2 = []

        tk.Frame.__init__(self, master)

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        frame = tk.Frame(canvas, bd=5)
        frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.95, anchor='n')

        instruction_label = tk.Label(frame, text="Enter the file path of data sets", font=50)
        instruction_label.place(relx=0, rely=0)

        path1_label = tk.Label(frame, text="Data set 1:", font=40)
        path1_label.place(relx=0, rely=0.05)

        path1_entry = tk.Entry(frame)
        path1_entry.place(relx=0.2, rely=0.06, relwidth=0.5)

        path2_label = tk.Label(frame, text="Data set 2:", font=40)
        path2_label.place(relx=0, rely=0.1)

        path2_entry = tk.Entry(frame)
        path2_entry.place(relx=0.2, rely=0.11, relwidth=0.5)

        path_array = [path1_entry.get(), path2_entry.get()]

        confirm_button = tk.Button(frame, text="Confirm",
                                   command=lambda: [self.read_csv(path_array),
                                                    master.switch_frame(analysis_page.AnalysisPage)])

        confirm_button.place(relx=0, rely=0.175, relwidth=0.2)


if __name__ == "__main__":
    app = Application()
    app.minsize(HEIGHT, WIDTH)
    app.mainloop()
