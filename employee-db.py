import Tkinter
import tkFont
import MySQLdb

class Employees():

    def __init__(self):
        root = Tkinter.Tk()
        root.title('Welcome to the Employee Data Base')

        times = tkFont.Font(family = 'Times New Roman', weight = 'bold', size = 15)

        top_label = Tkinter.Label(root, text = 'Choose one of the options below')
        top_label.grid(column = 2, pady = 20)

        look_up = Tkinter.Button(root, text = 'Look Up Employee', command = self.lookup,
                                 font = times)
        look_up.grid(row = 2, column = 1, pady = 20)

        add = Tkinter.Button(root, text = 'Add New Employee', command = self.addnew,
                             font = times)
        add.grid(row = 3, column = 1, padx = 10, pady = 10)

        change = Tkinter.Button(root, text = 'Change Employee', command = self.change,
                                font = times)
        change.grid(row = 2, column = 3, padx = 10)

        delete = Tkinter.Button(root, text = 'Delete Employee', command = self.delete,
                                font = times)
        delete.grid(row = 3, column = 3, padx = 10)

        quit_button = Tkinter.Button(root, text = 'Quit', command = root.destroy, width = 10
                                     , fg = 'red', height = 2, font = times)
        quit_button.grid(row = 4, column = 2, pady = 10)

        Tkinter.mainloop()

    def lookup(self):

        root = Tkinter.Tk()
        root.title('Look Up Employee')

        label = Tkinter.Label(root, text = "Look Up Employee's Information")
        label.grid(column = 2, pady = 20)

        label_id = Tkinter.Label(root, text = "Enter Employee's ID_Number")
        label_id.grid(row = 2, column = 1, pady = 10, padx = 10)

        id_entry = Tkinter.Entry(root)
        id_entry.grid(row = 2, column = 3, padx = 10)

        lookup_button = Tkinter.Button(root, text = "Look Up Employee in DB")
        lookup_button.grid(row = 3, column = 2, pady = 10)

        Tkinter.mainloop()

    def addnew(self):

        root = Tkinter.Tk()
        root.title('Add a New Employee')

        label = Tkinter.Label(root, text = "Add a new Employee's Information")
        label.grid(column = 2, pady = 20)

        label_employee = Tkinter.Label(root, text = "Enter Employee's Name:")
        label_employee.grid(row = 2, column = 1, pady = 10, padx = 10)

        entry_employee = Tkinter.Entry(root)
        entry_employee.grid(row = 2, column = 3, padx = 10)

        label_ID_Number = Tkinter.Label(root, text = "Enter Employee's ID_Number:")
        label_ID_Number.grid(row = 3, column = 1, pady = 10)

        entry_ID_Number = Tkinter.Entry(root)
        entry_ID_Number.grid(row = 3, column = 3)

        label_department = Tkinter.Label(root, text = "Enter Employee's Department:")
        label_department.grid(row = 4, column = 1, pady = 10)

        entry_department = Tkinter.Entry(root)
        entry_department.grid(row = 4, column = 3)

        label_job_title = Tkinter.Label(root, text = "Enter Employee's Job Title:")
        label_job_title.grid(row = 5, column = 1, pady = 10)

        entry_job_title = Tkinter.Entry(root)
        entry_job_title.grid(row = 5, column = 3)

        add_employee = Tkinter.Button(root, text = 'Add Employee to DB')
        add_employee.grid(row = 6, column = 2, pady = 10)

        Tkinter.mainloop()

    def change(self):

        root = Tkinter.Tk()

        root.title("Change Employee's information")

        label = Tkinter.Label(root, text = "Change Employee's Information")
        label.grid(column = 2, pady = 20)

        label_id = Tkinter.Label(root, text = "Enter Employee's ID_Number")
        label_id.grid(row = 2, column = 1, pady = 10, padx = 10)

        id_entry = Tkinter.Entry(root)
        id_entry.grid(row = 2, column = 3, padx = 10)

        change_button = Tkinter.Button(root, text = "Change Employee in DB")
        change_button.grid(row = 3, column = 2, pady = 10)

        Tkinter.mainloop()

    def delete(self):

        root = Tkinter.Tk()
        root.title("Delete Employee")

        label = Tkinter.Label(root, text = "Delete Employee's Information")
        label.grid(column = 2, pady = 20)

        label_id = Tkinter.Label(root, text = "Enter Employee's ID_Number")
        label_id.grid(row = 2, column = 1, pady = 10, padx = 10)

        id_entry = Tkinter.Entry(root)
        id_entry.grid(row = 2, column = 3, padx = 10)

        delete_button = Tkinter.Button(root, text = "Delete Employee from DB")
        delete_button.grid(row = 3, column = 2, pady = 10)

        Tkinter.mainloop()


gui = Employees()