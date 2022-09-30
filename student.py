from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import filedialog
import os
from tkinter import messagebox


class Student():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1320x720+0+0")
        self.root.title("Student management System")

        # Variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_add = StringVar()
        self.var_teach = StringVar()

        # 1st
        img = Image.open("college_images/6th.jpg")
        img = img.resize((440, 100), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        self.bt_1 = Button(self.root, image=self.photo, command=self.open_img, cursor="hand1")
        self.bt_1.place(x=0, y=0, width=440, height=100)

        img1 = Image.open("college_images/7th.jpg")
        img1 = img1.resize((440, 100), Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.bt_2 = Button(self.root, image=self.photo1, command=self.open_img2, cursor="hand2")
        self.bt_2.place(x=440, y=0, width=440, height=100)

        img2 = Image.open("college_images/9th.jpg")
        img2 = img2.resize((440, 100), Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.bt_3 = Button(self.root, image=self.photo2, command=self.open_img3, cursor="hand1")
        self.bt_3.place(x=880, y=0, width=440, height=100)

        img3 = Image.open("college_images/11th.jpg")
        img3 = img3.resize((1350, 560), Image.Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        bg_lbl = Label(self.root, image=self.photo3, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=100, width=1350, height=560)

        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, 'bold'), fg="blue",
                          bg="red")
        lbl_title.place(x=0, y=0, width=1350, height=35)

        manage_frame = Frame(bg_lbl, bd=1, relief=RIDGE, bg="white")
        manage_frame.place(x=10, y=40, width=1250, height=500)

        data_left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                     font=("times new roman", 15, 'bold'), fg="green", bg="white")
        data_left_frame.place(x=3, y=3, width=580, height=490)

        img5 = Image.open("college_images/clg.jpg")
        img5 = img5.resize((570, 100), Image.Resampling.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(img5)

        bg_lbl1 = Label(data_left_frame, image=self.photo5, bd=2, relief=RIDGE)
        bg_lbl1.place(x=0, y=0, width=570, height=100)

        # current course label information

        stud_frame = LabelFrame(data_left_frame, bd=2, relief=RIDGE, padx=2, text="Current Course Information",
                                font=("times new roman", 15, 'bold'), fg="maroon", bg="white")
        stud_frame.place(x=0, y=100, width=570, height=100)

        # label
        dep_lbl = Label(stud_frame, text="Department", bd=2, font=("aerial", 10, 'bold'), bg="white", fg="blue")
        dep_lbl.grid(row=0, column=0, padx=2, sticky=W)

        # combobox
        comb_dep = ttk.Combobox(stud_frame, font=("aerial", 10, 'bold'), textvariable=self.var_dep, width=15,
                                state="readonly")
        comb_dep["value"] = ("Select Department", "computer", "It", "Civil", "Mechanical")
        comb_dep.current(0)
        comb_dep.grid(row=0, column=1, padx=12, pady=10, sticky=W)

        # course combo box

        course_lbl = Label(stud_frame, text="Courses", bd=2, font=("aerial", 10, 'bold'), bg="white", fg="blue")
        course_lbl.grid(row=0, column=2, padx=2, sticky=W)

        comb_course = ttk.Combobox(stud_frame, font=("aerial", 10, 'bold'), textvariable=self.var_course, width=15,
                                   state="readonly")
        comb_course["value"] = ("Select Course", "B.tech", "M.tech", "P.hd", "staff")
        comb_course.current(0)
        comb_course.grid(row=0, column=3, padx=12, pady=10, sticky=W)

        # ComboBox for year

        year_lbl = Label(stud_frame, text=" Year ", bd=3, font=("aerial", 10, 'bold'), bg="white", fg="blue")
        year_lbl.grid(row=1, column=0, padx=2, sticky=W)

        comb_year = ttk.Combobox(stud_frame, font=("aerial", 10, "bold"), textvariable=self.var_year, width=15,
                                 state="readonly")
        comb_year["value"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        comb_year.current(0)
        comb_year.grid(row=1, column=1, padx=12, pady=4, sticky=W)

        # semester

        semster_lbl = Label(stud_frame, text="Semester", bd=2, font=("aerial", 10, "bold"), bg="white", fg="blue")
        semster_lbl.grid(row=1, column=2, padx=2, sticky=W)

        comb_sem = ttk.Combobox(stud_frame, font=("aerial", 10, "bold"), textvariable=self.var_semester, width=15,
                                state="readonly")
        comb_sem["value"] = ("Select Sem", "1st Sem", "2nd Sem")
        comb_sem.current(0)
        comb_sem.grid(row=1, column=3, padx=12, pady=4, sticky=W)

        # student label information
        stud_frame1 = LabelFrame(data_left_frame, bd=2, relief=RIDGE, padx=2, text="Student Information",
                                 font=("times new roman", 15, 'bold'), fg="maroon", bg="white")
        stud_frame1.place(x=0, y=200, width=570, height=180)

        # information of student

        st_id_lbl = Label(stud_frame1, text="Student_Id_No:", font=("aerial", 10, "bold"), bg="white", fg="red")
        st_id_lbl.grid(row=0, column=0, padx=2, sticky=W)

        id_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_std_id, width=15)
        id_fill.grid(row=0, column=1, padx=4, pady=4, sticky=W)

        # student name

        st_name_lbl = Label(stud_frame1, text="Student_Name:", font=("aerial", 10, "bold"), bg="white", fg="red")
        st_name_lbl.grid(row=0, column=3, padx=30, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_std_name, width=15)
        std_fill.grid(row=0, column=4, padx=4, pady=4, sticky=W)

        # class divison

        class_lbl = Label(stud_frame1, text="Class Division:", font=("aerial", 10, "bold"), bg="white", fg="red")
        class_lbl.grid(row=1, column=0, padx=2, sticky=W)

        std_fill = ttk.Combobox(stud_frame1, font=("aerial", 11, "bold"), textvariable=self.var_div, width=11)
        std_fill["values"] = ("select", "a", "b", "c")
        std_fill.current(0)
        std_fill.grid(row=1, column=1, padx=4, pady=4, sticky=W)

        # roll no

        roll_no_lbl = Label(stud_frame1, text="Roll No:", font=("aerial", 10, "bold"), bg="white", fg="red")
        roll_no_lbl.grid(row=1, column=3, padx=30, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_roll, width=15)
        std_fill.grid(row=1, column=4, padx=4, pady=4, sticky=W)

        # gender
        gender_lbl = Label(stud_frame1, text="Gender:", font=("aerial", 10, "bold"), bg="white", fg="red")
        gender_lbl.grid(row=2, column=0, padx=2, sticky=W)

        std_fill = ttk.Combobox(stud_frame1, font=("aerial", 11, "bold"), textvariable=self.var_gender, width=11)
        std_fill["value"] = ("select", "male", "female")
        std_fill.current(0)
        std_fill.grid(row=2, column=1, padx=4, pady=4, sticky=W)

        # dob

        dob_lbl = Label(stud_frame1, text="D.O.B:", font=("aerial", 10, "bold"), bg="white", fg="red")
        dob_lbl.grid(row=2, column=3, padx=30, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_dob, width=15)
        std_fill.grid(row=2, column=4, padx=4, pady=4, sticky=W)

        # E.mail

        email_lbl = Label(stud_frame1, text="E.mail:", font=("aerial", 10, "bold"), bg="white", fg="red")
        email_lbl.grid(row=3, column=0, padx=2, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_email, width=15)
        std_fill.grid(row=3, column=1, padx=4, pady=4, sticky=W)

        # Phone.No

        phone_no_lbl = Label(stud_frame1, text="Phone.No:", font=("aerial", 10, "bold"), bg="white", fg="red")
        phone_no_lbl.grid(row=3, column=3, padx=30, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_phone, width=15)
        std_fill.grid(row=3, column=4, padx=4, pady=4, sticky=W)

        # Address

        address_lbl = Label(stud_frame1, text="Address:", font=("aerial", 10, "bold"), bg="white", fg="red")
        address_lbl.grid(row=4, column=0, padx=2, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_add, width=15)
        std_fill.grid(row=4, column=1, padx=4, pady=4, sticky=W)

        # Teacher Name

        teacher_name_lbl = Label(stud_frame1, text="Teacher Name:", font=("aerial", 10, "bold"), bg="white", fg="red")
        teacher_name_lbl.grid(row=4, column=3, padx=30, sticky=W)

        std_fill = ttk.Entry(stud_frame1, font=("aerial", 10, "bold"), textvariable=self.var_teach, width=15)
        std_fill.grid(row=4, column=4, padx=4, pady=4, sticky=W)

        # Background Image as label

        img7 = Image.open("college_images/11th.jpg")
        img7 = img7.resize((570, 80), Image.Resampling.LANCZOS)
        self.photo7 = ImageTk.PhotoImage(img7)

        bg_lbl7 = Label(data_left_frame, image=self.photo7, bd=2, relief=RIDGE)
        bg_lbl7.place(x=0, y=380, width=570, height=80)

        # frame for buttons

        st_lbl = Frame(data_left_frame, bd=2, relief=RIDGE, bg="white")
        st_lbl.place(x=0, y=420, width=570, height=40)

        btn_std = Button(st_lbl, text="Save", command=self.add_data, font=("aerial", 11, "bold"), width=14, fg="white",
                         bg="blue")
        btn_std.grid(row=0, column=0, padx=2.5, pady=2)

        btn_std1 = Button(st_lbl, text="Update", command=self.update_data, font=("aerial", 11, "bold"), width=14,
                          fg="white", bg="blue")
        btn_std1.grid(row=0, column=1, padx=2.5, pady=2)

        btn_std2 = Button(st_lbl, text="Delete", command=self.del_data, font=("aerial", 11, "bold"), width=14,
                          fg="white", bg="blue")
        btn_std2.grid(row=0, column=2, padx=2.5, pady=2)

        btn_std3 = Button(st_lbl, text="Reset", command=self.reset_data, font=("aerial", 11, "bold"), width=14,
                          fg="white", bg="blue")
        btn_std3.grid(row=0, column=3, padx=2.5, pady=2)

        #right frame

        data_right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Information",
                                      font=("times new roman", 15, 'bold'), fg="green", bg="white")
        data_right_frame.place(x=600, y=3, width=640, height=490)

        # image as label on right side

        img9 = Image.open("college_images/university.jpg")
        img9 = img9.resize((620, 140), Image.Resampling.LANCZOS)
        self.photo9 = ImageTk.PhotoImage(img9)

        bg_lbl2 = Label(data_right_frame, image=self.photo9, bd=2, relief=RIDGE)
        bg_lbl2.place(x=0, y=0, width=630, height=140)

        # view student detail and search system

        std_det = LabelFrame(data_right_frame, text="view student details and search system",
                             font=("times new roman", 10, "bold"), bg="white")
        std_det.place(x=0, y=145, width=630, height=50)

        # search button

        searh_btn = Button(std_det, text="Search By", font=("times new roman", 10, "bold"), bd=2, width=15, fg="white",
                           bg="red", cursor="hand2")
        searh_btn.grid(row=0, column=0, padx=2, pady=2)

        self.var_com_search = StringVar()

        # comboBox

        search_combo = ttk.Combobox(std_det, font=("aerial", 12, "bold"), textvariable=self.var_com_search, width=13,
                                    state="readonly")
        search_combo["values"] = ("select", "roll.no", "Phone", "student_Id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        self.var_search = StringVar()

        # entering data
        search_fill = ttk.Entry(std_det, textvariable=self.var_search, font=("aerial", 12, "bold"), width=13)
        search_fill.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        searh_btn = Button(std_det, text="SEARCH", command=self.search_data, font=("times new roman", 10, "bold"), bd=2,
                           width=15, fg="white", bg="red")
        searh_btn.grid(row=0, column=3, padx=1, pady=2)

        searh_btn = Button(std_det, text="SHOW ALL", command=self.fetch_data, font=("times new roman", 10, "bold"),
                           bd=2, width=15, fg="white", bg="red")
        searh_btn.grid(row=0, column=4, padx=1, pady=2)

        # ===============================Student table and scorll bar===========================
        table_frame = Frame(data_right_frame, bd=4, relief=SUNKEN)
        table_frame.place(x=0, y=195, width=630, height=260)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
        "Department", "course", "year", "sem", "std_id", "std_name", "cl_div", "roll.no", "gender", "dob", "email",
        "ph.no", "add", "tech_name"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("std_id", text="Student_Id.")
        self.student_table.heading("std_name", text="Student_Name")
        self.student_table.heading("cl_div", text="Class_Division")
        self.student_table.heading("roll.no", text="Roll.No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="E.mail")
        self.student_table.heading("ph.no", text="Phone.No")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("tech_name", text="Teacher_name")

        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("std_id", width=100)
        self.student_table.column("std_name", width=100)
        self.student_table.column("cl_div", width=100)
        self.student_table.column("roll.no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("ph.no", width=100)
        self.student_table.column("add", width=100)
        self.student_table.column("tech_name", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>", self.get_Cursor)

        self.fetch_data()

    def add_data(self):
        if ((self.var_dep).get() == "" or (self.var_email).get() == "" or (self.var_std_id).get() == ""):

            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rahulsingh78@",
                                               database="new_schema")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_add.get(),
                    self.var_teach.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess", "student has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:{str(es)}", parent=self.root)

    # fetch_data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Rahulsingh78@",
                                       database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_dataset")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Cursur Function
    def get_Cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_add.set(data[12])
        self.var_teach.set(data[13])

    # update data

    def update_data(self):
        if ((self.var_dep).get() == "" or (self.var_email).get() == "" or (self.var_std_id).get() == ""):
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                update = messagebox.askyesno("update", "are you sure to update the student data", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Rahulsingh78@",
                                                   database="new_schema")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student_dataset set dep=%s,course=%s,year=%s,semester=%s,Name=%s,division=%s,roll.no=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher_name=%s where student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_add.get(),
                            self.var_teach.get(),
                            self.var_std_id.get()

                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("success", "student successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:{str(es)}", parent=self.root)

    # delete data
    def del_data(self):
        if self.var_std_id == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Delete", "are you sure to delete this student", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Rahulsingh78@",
                                                   database="new_schema")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from student_dataset where student_id=%s", (
                        self.var_std_id.get(),
                    ))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Your data has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:{str(es)}", parent=self.root)

    # reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Sem")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select ")
        self.var_roll.set("")
        self.var_gender.set("select ")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_teach.set("")

    # search Data

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "please select option", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rahulsingh78@",
                                               database="new_schema")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select * from student_dataset where " + str(self.var_com_search.get()) + " LIKE '%" + str(
                        self.var_search.get()) + "%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("error", f"due to:{str(es)}", parent=self.root)

                # openning image

    def open_img(self):
        fil1 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Image",
                                          filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.pnj"), ("ALL File", "*.*")))
        img10 = Image.open(fil1)
        img_resize = img10.resize((440, 100), Image.ANTIALIAS)
        self.photoimage10 = ImageTk.PhotoImage(img_resize)
        self.bt_1.config(image=self.photoimage10)

    def open_img2(self):
        fil2 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Image",
                                          filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.pnj"), ("ALL File", "*.*")))
        img11 = Image.open(fil2)
        img_resize1 = img11.resize((440, 100), Image.ANTIALIAS)
        self.photoimage11 = ImageTk.PhotoImage(img_resize1)
        self.bt_2.config(image=self.photoimage11)

    def open_img3(self):
        fil = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Image",
                                         filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.pnj"), ("ALL File", "*.*")))
        img12 = Image.open(fil)
        img_resize2 = img12.resize((440, 100), Image.ANTIALIAS)
        self.photoimage12 = ImageTk.PhotoImage(img_resize2)
        self.bt_3.config(image=self.photoimage12)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

