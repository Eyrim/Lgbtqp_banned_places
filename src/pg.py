import tkinter as tk
from tkinter import Frame, ttk, StringVar, Radiobutton, Entry

class Main:
    def __init__(self):
        pass

    def change_agab_post(self):
        self.agab_combobox["values"] = [
            "Male",
            "Female",
            "Intersex",
            "Prefer not to disclose".title()
        ]

    def change_sexu_post(self):
        self.sexu_combobox["values"] = [
            "Straight (Heterosexual)",
            "Lesbian",
            "Gay",
            "Bisexual",
            "Other",
            "prefer not to disclose".title()
        ]

    def change_romo_post(self):
        self.romo_combobox["values"] = [
            "Heteromantic",
            "Homoromantic (female)",
            "Homoromantic (male)",
            "Biromantic",
            "Other",
            "prefer not to disclose".title()
        ]

    def change_gender_post(self):
        self.gender_combobox["values"] = [
            "Male (Cisgender)",
            "Female (Cisgender)",
            "Male (Trans)",
            "Female (Trans)",
            "Non Binary",
            "Other",
            "Prefer not to disclose".title()
        ]

    def gender_expression_agab_activated(self):
        self.gender_expression_agab_button.configure(state = "normal", bg = "purple", fg = "white")
        self.gender_expression_true_button.configure(state = "normal", bg = "white", fg = "black")
        self.gender_expression_both_button.configure(state = "normal", bg = "white", fg = "black")

    def gender_expression_true_activated(self):
        self.gender_expression_agab_button.configure(state = "normal", bg = "white", fg = "black")
        self.gender_expression_true_button.configure(state = "normal", bg = "purple", fg = "white")
        self.gender_expression_both_button.configure(state = "normal", bg = "white", fg = "black")
        
    def gender_expression_both_activated(self):
        self.gender_expression_agab_button.configure(state = "normal", bg = "white", fg = "black")
        self.gender_expression_true_button.configure(state = "normal", bg = "white", fg = "black")
        self.gender_expression_both_button.configure(state = "normal", bg = "purple", fg = "white")

    def data_gather(self, event):
        self.agab = self.agab_combobox.get()

        if self.agab != "":
            print("AGAB:\n" + str(self.agab))

        ##

        self.sexu = self.sexu_combobox.get()

        if self.sexu != "":
            print("Sexuality:\n" + str(self.sexu))

        ##

        self.romo = self.romo_combobox.get()

        if self.romo != "":
            print("Romantic Orientation:\n" + str(self.romo))

        ##

        self.gender = self.gender_combobox.get()

        if self.gender != "":
            print("Gender:\n" + str(self.gender))

    def gui(self):
        self.root = tk.Tk()
        self.root.title("v0.0.2")
        self.root.geometry("500x750")
        self.root_frame = Frame(self.root, bg="pink")

        self.agab_top_label = tk.Label(self.root_frame, text = "What is your AGAB? (assigned gender at birth)".title(), bg = "tomato")
        self.agab_top_label.pack()

        '''
        startbutton = Button(root_frame, text="Start")
        startbutton.grid()
        '''

        # ---------------- AGAB COMBO ----------------

        self.agab_combobox = ttk.Combobox(self.root_frame,
        state = "readonly",
        values = [
            "",
            "Male",
            "Female",
            "Intersex",
            "Prefer not to disclose".title()
        ],
        postcommand = self.change_agab_post) # When the box is clicked on; self.change_agab_post() is called, changing the values to not include the empty one at the top

        self.agab_combobox.pack(anchor = "center")
        self.agab_combobox.current(0)

        self.agab_combobox.bind("<<ComboboxSelected>>", self.data_gather)

        # --------------------------------------------

        self.sexu_top_label = tk.Label(self.root_frame, text = "What is your sexuality?".title(), bg = "#fea026")
        self.sexu_top_label.pack()

        # ---------------- SEXU COMBO ----------------

        self.sexu_combobox = ttk.Combobox(self.root_frame,
        state = "readonly",
        values = [
            "",
            "Heterosexual",
            "Homosexual (female)",
            "Homosexual (male)",
            "Bisexual",
            "Other",
            "prefer not to disclose".title()
        ],
        postcommand = self.change_sexu_post)

        self.sexu_combobox.pack(anchor = "center")
        self.sexu_combobox.current(0)

        self.sexu_combobox.bind("<<ComboboxSelected>>", self.data_gather)

        # --------------------------------------------

        self.romo_top_label = tk.Label(self.root_frame, text = "What is your romantic orientation?".title(), bg = "#fee92e")
        self.romo_top_label.pack()

        # ---------------- ROMO COMBO ----------------

        self.romo_combobox = ttk.Combobox(self.root_frame,
        state = "readonly",
        values = [
            "",
            "Heteromantic",
            "Homoromantic (female)",
            "Homoromantic (male)",
            "Biromantic",
            "Other",
            "prefer not to disclose".title()
        ],
        postcommand = self.change_romo_post)

        self.romo_combobox.pack(anchor = "center")
        self.romo_combobox.current(0)

        self.romo_combobox.bind("<<ComboboxSelected>>", self.data_gather)

        # --------------------------------------------

        self.gender_top_label = tk.Label(self.root_frame, text = "What is your gender?".title(), bg = "#38fe4c")
        self.gender_top_label.pack()

        # ---------------- GENDER COMBO --------------

        self.gender_combobox = ttk.Combobox(self.root_frame,
        state = "readonly",
        values = [
            "",
            "Male (Cisgender)",
            "Female (Cisgender)",
            "Male (Trans)",
            "Female (Trans)",
            "Non Binary",
            "Other",
            "Prefer not to disclose".title()
        ],
        postcommand = self.change_gender_post)

        self.gender_combobox.pack(anchor = "center")
        self.gender_combobox.current(0)

        self.gender_combobox.bind("<<ComboboxSelected>>", self.data_gather)

        # --------------------------------------------

        # ---------------- GENDER BUTTONS ------------

        self.gender_expression_var = StringVar()
        self.gender_expression_var.set("")

        self.gender_expression_agab_top_label = tk.Label(self.root_frame, text = "Do you express, or want to express, as your AGAB?", bg = "#2e81fe")
        self.gender_expression_agab_top_label.pack()

        self.gender_expression_agab_button = tk.Button(self.root_frame, text = "Yes", command = self.gender_expression_agab_activated)
        self.gender_expression_agab_button.pack()

        self.gender_expression_true_top_label = tk.Label(self.root_frame, text = "Do you express, or want to express, as something other than your AGAB?", bg = "#4b0082", fg = "white")
        self.gender_expression_true_top_label.pack()

        self.gender_expression_true_button = tk.Button(self.root_frame, text = "Yes", command = self.gender_expression_true_activated)
        self.gender_expression_true_button.pack()

        '''
        self.gender_expression_radio_button_yes = Radiobutton(self.root_frame, text = "Yes".title(), variable = self.gender_expression_var, value = "expression_yes", state = "normal")
        self.gender_expression_radio_button_no = Radiobutton(self.root_frame, text = "No", variable = self.gender_expression_var, value = "expression_no", state = "active")
        '''

        self.gender_expression_both_label = tk.Label(self.root_frame, text = "Do you express, or want to express, as both your AGAB and something else?", bg = "#8F00FF", fg = "white")
        self.gender_expression_both_label.pack()

        self.gender_expression_both_button = tk.Button(self.root_frame, text = "Yes", command = self.gender_expression_both_activated)
        self.gender_expression_both_button.pack()

        # ------------------------------------------

# #8F00FF - violet

        #Configure the row/col of our frame and root window to be resizable and fill all available space
        self.root_frame.grid(row=0, column=0, sticky="NESW")
        self.root_frame.grid_rowconfigure(0, weight=1)
        self.root_frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.mainloop()


if __name__ == "__main__":
    instance = Main()
    instance.gui()