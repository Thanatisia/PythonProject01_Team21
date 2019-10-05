import Tkinter as tk
import main
import settings
import ttk


class AnalysisPage(tk.Frame):
    def test(self):
        for x in settings.data_set[0]:
            print x

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        canvas = tk.Canvas(self, height=settings.HEIGHT, width=settings.WIDTH)
        canvas.pack()

        frame = tk.Frame(canvas, bd=5)
        frame.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.95, anchor='n')

        instruction_label = tk.Label(frame, text="What would you like to do?", font=50)
        instruction_label.pack()

        tree_list = []

        for data_set in settings.data_set:
            tree = ttk.Treeview(frame)

            for i in range(0, len(data_set)):
                heading_list = []
                value_list = []

                for x in data_set[i]:
                    heading_list.append(x)
                    value_list.append(data_set[i].get(x))

                tree["columns"] = heading_list
                tree['show'] = 'headings'

                for x in range(0, len(heading_list)):
                    tree.heading(heading_list[x], text=heading_list[x])

                tree.insert("", 0, values=value_list)

            tree.pack()
            tree_list.append(tree)

        function1_button = tk.Button(frame, text="To print test", command=lambda: self.test())
        function1_button.pack()

        function3_button = tk.Button(frame, text="Function 3")
        function3_button.pack()

        back_button = tk.Button(frame, text="Return to start page", command=lambda: master.switch_frame(main.StartPage))
        back_button.pack(side='bottom', )


