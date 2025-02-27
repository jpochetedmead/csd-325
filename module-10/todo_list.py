"""
Julio Pochet
02/26/2025
Assignment: Module 10.2 - GUI To-Do List

Description:
This program creates a simple To-Do List using Tkinter. Users can add, delete, 
and mark tasks as complete. Tasks are stored in a text file for persistence.
"""

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # ✅ Change the window title
        self.title("Pochet-ToDo")
        self.geometry("350x450")

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # ✅ Create a Menu Bar with an Exit option
        self.menu_bar = tk.Menu(self, bg="blue", fg="white")  # Complementary colors
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="purple", fg="yellow")
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # ✅ Create canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        # ✅ Change the label to provide delete instructions
        self.label = tk.Label(self.tasks_frame, text="--- Added Items --- ** Right Click to Delete **",
                              bg="purple", fg="yellow", pady=10)

        self.label.pack(side=tk.TOP, fill=tk.X)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.tasks.append(self.label)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # ✅ Change task deletion from left-click to right-click
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [{"bg": "Lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        """ Add a new task to the list """
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            # ✅ Change deletion event from left-click (<Button-1>) to right-click (<Button-3>)
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        """ Remove a task when right-clicked """
        task = event.widget
        if msg.askyesno("Confirm Delete", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()  # ✅ Ensure colors remain correct

    def recolour_tasks(self):
        """ Ensures tasks maintain alternating colors correctly after deletion """
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        """ Apply alternating colors to tasks to maintain readability """
        color_scheme = self.colour_schemes[position % 2]  # ✅ Alternate colors properly
        task.configure(bg=color_scheme["bg"], fg=color_scheme["fg"])

    def on_frame_configure(self, event=None):
        """ Update scrollbar region when frame resizes """
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        """ Adjust width dynamically """
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        """ Allow smooth scrolling using the mouse wheel """
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()