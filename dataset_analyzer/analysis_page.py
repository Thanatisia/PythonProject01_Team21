import Tkinter as tk
import main
import settings


class AnalysisPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        canvas = tk.Canvas(self, height=settings.HEIGHT, width=settings.WIDTH)
        canvas.pack()

        frame = tk.Frame(canvas, bd=5)
        frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.95, anchor='n')

        instruction_label = tk.Label(frame, text="What would you like do do?", font=50)
        instruction_label.place(relx=0, rely=0)

        function1_button = tk.Button(frame, text="Function 1")
        function1_button.place(relx=0, rely=0.1, relwidth=0.2)

        function2_button = tk.Button(frame, text="Function 2")
        function2_button.place(relx=0, rely=0.175, relwidth=0.2)

        function3_button = tk.Button(frame, text="Function 3")
        function3_button.place(relx=0, rely=0.25, relwidth=0.2)

        back_button = tk.Button(frame, text="Return to start page", command=lambda: master.switch_frame(main.StartPage))
        back_button.pack(side='bottom', )
