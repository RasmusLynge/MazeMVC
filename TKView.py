import tkinter as tk
import controller
import plotGenerator as plot_generator

WIDTH = 1500
HEIGHT = 700

# https://refactoring.guru/design-patterns/observer

maze_array = []
isLog = False


def start_plot():

    def generate_simple_mazes():
        # write_to_log(
        #    "\n\nCreating 6 mazes \nof size 5, 10, 15, \n20, 25 and 30...")
        pub.dispatch(
            "\n\nCreating 6 mazes \nof size 5, 10, 15, \n20, 25 and 30...")
        controller.generate_mazes(6, [5, 10, 15, 20, 25, 30])
        pub.dispatch("\nDone.")
        load_maze_list()

    def generate_single_maze(number, size):
        if number:
            pub.dispatch("\n\nCreating %s mazes \nwith a size of %s..." %
                         (size, number))
            number_list = number.split(" ")
            size_list = [int(i) for i in number_list]
            controller.generate_mazes(int(size), size_list)
            pub.dispatch("\nDone.")
            load_maze_list()
        else:
            pub.dispatch("\n\nType preferred \nmaze size and number.")

    def plot_mazes():
        pub.dispatch("\n\nPlotting data from \nthe list of mazes...")
        plot_data = controller.show_plot()
        plot_generator.generate_plot(plot_data)

    def select_maze():
        global maze_array
        maze_number = 0
        maze_array = controller.mazes_from_file()
        selected = Listbox_maze_list.curselection()
        if selected:
            for value in selected:
                maze_number = value
            pub.dispatch(
                "\n\nYou selected maze nr %s \nGenerating maze" % (maze_number + 1))
            show_maze(maze_array[maze_number])
        else:
            load_maze_list()
            pub.dispatch("\n\nSelect a maze")

    def solve_single_maze():
        global maze_array
        maze_number = 0
        selected = Listbox_maze_list.curselection()
        if selected:
            for value in selected:
                maze_number = value
            pub.dispatch("\n\nSolving the maze nr %s..." % (maze_number + 1))
            maze = controller.solve_one_maze(maze_array[maze_number])
            show_maze(maze)
        else:
            pub.dispatch("\n\nPlease select a maze")

    def show_maze(maze):
        row_count = 0
        for row in maze:
            value_count = 0
            for value in row:
                color = "white"
                if(value == 1):
                    color = "black"
                if(value == 2):
                    color = "green"
                if(value == 3):
                    color = "pink"
                tk.Label(display_maze, bg=color, borderwidth=1).place(
                    relwidth=(1 / len(maze)), relheight=(1 / len(maze)),
                    relx=(value_count/len(maze)), rely=(row_count/len(maze)))
                value_count += 1
            row_count += 1

    def show_maze_list():
        global maze_array
        maze_array = controller.mazes_from_file()

    def load_maze_list():
        global maze_array
        maze_array = controller.mazes_from_file()
        Listbox_maze_list.delete(0, tk.END)

        maze_count = 1
        for maze in maze_array:
            Listbox_maze_list.insert(
                tk.END, "Maze number " + str(maze_count) + " with size " + str(int((len(maze)-1)/2)))
            maze_count += 1
        Listbox_maze_list.place(relwidth=1, relheight=1)
        scrollbar.config(command=Listbox_maze_list.yview)

    def log_action():
        global isLog

        if isLog:
            hide_log.place(relx=0.1, rely=1)
            pub.register(test)
            isLog = False
        else:
            hide_log.place(relx=0.1, rely=0.5)
            pub.unregister(test)
            isLog = True

    ###### Observer Pattern ######

    class Subscriber:
        def __init__(self, name):
            self.name = name

        def update(self, message):
            self.name(message)

    class Publisher:
        def __init__(self):
            self.subscribers = set()

        def register(self, who):
            self.subscribers.add(who)

        def unregister(self, who):
            self.subscribers.discard(who)

        def dispatch(self, message):
            for subscriber in self.subscribers:
                subscriber.update(message)

    def write_to_log(message):
        text_log['text'] += message

    pub = Publisher()
    test = Subscriber(write_to_log)
    pub.register(test)

    if(maze_array == []):
        try:
            show_maze_list()
        except:
            print("No file in archive")

    root = tk.Tk()
    root.title('Maze Solver 9000')

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, relief='raised')
    canvas.pack()

    ############### Top Frame ###############
    top_frame = tk.Frame(root, bg="grey")
    top_frame.place(relwidth=1, relheight=0.1)

    header = tk.Label(top_frame, text='Maze Solver', bg="grey")
    header.config(font=('lucida console', 19))
    header.place(relx=0.45, rely=0.45)

    ############### Center Frame ###############
    frame_center = tk.Frame(root, bg="grey")
    frame_center.place(relwidth=0.45, relheight=0.7, relx=0.3, rely=0.1)

    frame_center_window = tk.Frame(frame_center, bd=1, bg="black")
    frame_center_window.place(relwidth=0.9, relheight=0.9, relx=0, rely=0.1)

    label_center = tk.Label(frame_center_window)
    label_center.place(relwidth=1, relheight=1)

    display_maze = tk.Label(label_center, bg="white")
    display_maze.place(relwidth=1, relheight=1)

    ############### Left side Frame ###############
    frame_left_side = tk.Frame(root, bg='grey')
    frame_left_side.place(relwidth=0.3, relheight=0.9, rely=0.1)

    label_maze_list = tk.Label(frame_left_side, text='Generate mazes:',
                               bg="gray", font=('helvetica', 12, 'bold'))
    label_maze_list.place(relx=0.1, rely=0.075)

    label_maze_size = tk.Label(frame_left_side, text='Choose a maze size:',
                               bg="gray", font=('helvetica', 8, 'bold'))
    label_maze_size.place(relx=0.1, rely=0.2)

    input_maze_size = tk.Entry(frame_left_side)
    input_maze_size.place(relx=0.1, rely=0.24, relwidth=0.6, relheight=0.05)

    label_maze_number = tk.Label(frame_left_side, text='Choose a number of mazes:',
                                 bg="gray", font=('helvetica', 8, 'bold'))
    label_maze_number.place(relx=0.1, rely=0.3)

    input_maze_number = tk.Entry(frame_left_side)
    input_maze_number.place(relx=0.1, rely=0.34, relwidth=0.6, relheight=0.05)

    button_generate_maze = tk.Button(frame_left_side, text='Generate', bg='brown', fg='white', font=('helvetica', 9, 'bold'),
                                     command=lambda: generate_single_maze(input_maze_size.get(), input_maze_number.get()))
    button_generate_maze.place(
        relx=0.1, rely=0.425, relwidth=0.6, relheight=0.05)

    label_log = tk.Label(frame_left_side, text='Helping log:',
                         bg="gray", font=('helvetica', 8, 'bold'))
    label_log.place(relx=0.1, rely=0.5)

    frame_log = tk.Frame(frame_left_side, bd=1, bg="black")
    frame_log.place(relx=0.1, rely=0.55, relwidth=0.65, relheight=0.35)

    fill_log = tk.Frame(frame_log)
    fill_log.place(relwidth=1, relheight=1)

    text_log = tk.Label(frame_log, text='Welcome', borderwidth=1)
    text_log.config(font=('lucida console', 9))
    text_log.place(relx=0, rely=1, anchor="sw")

    hide_log = tk.Frame(frame_left_side, bg="grey")
    hide_log.place(relx=0.1, rely=1, relwidth=0.65, relheight=0.4)

    button_generate_maze = tk.Button(frame_left_side, text='Show/Hide log', bg='brown', fg='white', font=('helvetica', 9, 'bold'),
                                     command=log_action)
    button_generate_maze.place(
        relx=0.1, rely=0.9, relwidth=0.2, relheight=0.03)

    ############### Right side frame ###############
    frame_right_side = tk.Frame(root, bg='grey')
    frame_right_side.place(relwidth=0.3, relheight=0.9, rely=0.1, relx=0.75)

    label_maze_list = tk.Label(frame_right_side, text='List of mazes:',
                               bg="gray", font=('helvetica', 12, 'bold'))
    label_maze_list.place(relx=0.1, rely=0.075)

    frame_maze_list_outer = tk.Frame(frame_right_side, bd=1, bg="black")
    frame_maze_list_outer.place(
        relx=0.1, rely=0.14, relwidth=0.65, relheight=0.635)

    frame_maze_list = tk.Frame(frame_maze_list_outer, bd=1, bg="white")
    frame_maze_list.place(relwidth=1, relheight=1)

    scrollbar = tk.Scrollbar(frame_maze_list)

    Listbox_maze_list = tk.Listbox(
        frame_maze_list, yscrollcommand=scrollbar.set, selectbackground="brown")

    button_select_maze = tk.Button(frame_right_side, text='Select maze',
                                   command=select_maze, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    button_select_maze.place(relx=0.1, rely=0.838,
                             relwidth=0.3, relheight=0.072)

    ############### Bottom Frame ###############
    frame_bottom = tk.Frame(root, bg='grey')
    frame_bottom.place(relwidth=0.45, relheight=0.2, relx=0.3, rely=0.8)

    button_generate_simple = tk.Button(frame_bottom, text='Simple Generate',
                                       command=generate_simple_mazes, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    button_generate_simple.place(
        relx=0.0, rely=0.3, relwidth=0.2, relheight=0.3)

    button_solve = tk.Button(frame_bottom, text='Solve Maze', command=solve_single_maze,
                             bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    button_solve.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.3)

    button_plot = tk.Button(frame_bottom, text='Show plot', command=plot_mazes,
                            bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    button_plot.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.3)

    root.mainloop()
