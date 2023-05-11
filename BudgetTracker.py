import tkinter as tk

class BudgetTracker:
    def __init__(self, master):
        self.master = master
        master.title("Budget Tracker")

        # Create labels and entries for input
        tk.Label(master, text="Date").grid(row=0)
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=0, column=1)

        tk.Label(master, text="Category").grid(row=1)
        self.category_entry = tk.Entry(master)
        self.category_entry.grid(row=1, column=1)

        tk.Label(master, text="Amount").grid(row=2)
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=2, column=1)

        tk.Label(master, text="Type").grid(row=3)
        self.type_entry = tk.Entry(master)
        self.type_entry.grid(row=3, column=1)

        # Create buttons for adding and viewing data
        self.add_button = tk.Button(master, text="Add Data", command=self.add_data)
        self.add_button.grid(row=4, column=0)

        self.view_button = tk.Button(master, text="View Data", command=self.view_data)
        self.view_button.grid(row=4, column=1)


    def add_data(self):
        pass

    def view_data(self):
        pass

root = tk.Tk()
app = BudgetTracker(root)
root.mainloop()

# To be Continued