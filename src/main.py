import tkinter as tk
from tkinter import Frame, ttk, StringVar, Radiobutton, Entry
from json import loads
import json as json

class Main:
    def __init__(self):
        with open('hate.json') as hate:
            hate = hate.read()
            self.hate = json.loads(hate)

    def search(self):
        self.search_results = tk.Label(self.root_frame, text = self.hate[self.search_term.get()])
        self.search_results.pack()

    def submit(self):
        print("-" * 100)
        print("\nAGAB: " + str(self.agab) + "\nSexuality: " + str(self.sexu) + "\nRomantic Orientation: " + str(self.romo) + "\nGender: " + str(self.gender) + "\nGender Expression: " + str(self.gender_expression))
        print("-" * 100)

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
            "Asexual",
            "Other",
            "prefer not to disclose".title()
        ]

    def change_romo_post(self):
        self.romo_combobox["values"] = [
            "Heteromantic",
            "Homoromantic (female)",
            "Homoromantic (male)",
            "Biromantic",
            "Asexual",
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

    def change_gender_expression_post(self):
        self.gender_expression_combobox["values"] = [
            "My AGAB",
            "My true gender".title(),
            "Both"
        ]


    def data_gather(self, event):
        self.agab = str(self.agab_combobox.get())

        if self.agab != "":
            print("AGAB:\n" + str(self.agab))

        ##

        self.sexu = str(self.sexu_combobox.get())

        if self.sexu != "":
            print("Sexuality:\n" + str(self.sexu))

        ##

        self.romo = str(self.romo_combobox.get())

        if self.romo != "":
            print("Romantic Orientation:\n" + str(self.romo))

        ##

        self.gender = str(self.gender_combobox.get())

        if self.gender != "":
            print("Gender:\n" + str(self.gender))

        ##

        self.gender_expression = str(self.gender_expression_combobox.get())

        if self.gender_expression != "":
            print("Gender Expression:\n" + str(self.gender_expression))

        if self.agab != "" and self.sexu != "" and self.romo != "" and self.gender != "" and self.gender_expression != "":
            self.start_button.pack()

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
            "Asexual",
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
            "Aromantic",
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

        self.gender_expression_top_label = tk.Label(self.root_frame, text = "Which gender do you express as?".title(), bg = "#8F00FF")
        self.gender_expression_top_label.pack()

        # ---------------- GENDER COMBO --------------

        self.gender_expression_combobox = ttk.Combobox(self.root_frame,
        state = "readonly",
        values = [
            "",
            "My AGAB",
            "My true gender".title(),
            "Both"
        ],
        postcommand = self.change_gender_expression_post)

        self.gender_expression_combobox.pack(anchor = "center")
        self.gender_expression_combobox.current(0)

        self.gender_expression_combobox.bind("<<ComboboxSelected>>", self.data_gather)

        # --------------------------------------------

        # ---------------- SEARCH BAR ----------------

        self.search_button_top_label = tk.Label(self.root_frame, text = "Search for a country, crime or sentence")
        self.search_button_top_label.pack()
        self.search_term = StringVar()
        self.search_entry = Entry(self.root_frame, textvariable = self.search_term)
        self.search_entry.pack()

            # ---------------- SEARCH BUTTON --------------

        self.search_button = tk.Button(self.root_frame, text = "Search", command = self.search)
        self.search_button.pack()
            
            # ---------------------------------------------

        # --------------------------------------------

        # ---------------- START BUTTON ------------

        self.start_button = tk.Button(self.root_frame, text = "Find out where hates me :)", command = self.submit)

        # ------------------------------------------

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