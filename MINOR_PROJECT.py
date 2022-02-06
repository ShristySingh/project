from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter.messagebox as tmsg
import os
import time

#################### 1ST PAGE ######################
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            main_screen.destroy()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 

 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
#################### END 1ST PAGE ##################### 

 
#################### SECOND PAGE #######################

root2=Tk
root2 =Tk() #where root is the name of main window object
root2.geometry("1400x750+0+0") #geometric configuration 
root2.title("RULES FOR BILLING")
root2.configure(background='sky blue')
ok_inp=StringVar()

def enter():
	if ok_inp.get() == "YES":
		root2.destroy()
		import question
	else:
		 root2.destroy()
        

def destroy():
	root2.destroy	

label = Label(root2, font = ('arial',50,'bold'), text =" RULES FOR BILLING ", bg = "dark blue" ,fg="sky blue",bd = 10,pady=15, anchor = 'w',relief=RIDGE)
label.grid(row = 0,column=2)
label1 = Label(root2, font = ('arial',20,'bold'), text ="1.Need to fill customer\ndetail", fg = "dark blue" ,bg="sky blue", anchor = 'w')
label1.grid(row = 3,column=0) 
label2 = Label(root2, font = ('arial',20,'bold'), text ="2.select type and show", fg = "dark blue" ,bg="sky blue", anchor = 'w')
label2.grid(row = 4,column=0)  
label3 = Label(root2, font = ('arial',20,'bold'), text ="3.select item and press \nadd item ", fg = "dark blue" ,bg="sky blue", anchor = 'w')
label3.grid(row = 5,column=0) 
label4 = Label(root2, font = ('arial',20,'bold'), text ="4.press bill button\nfor generating bill", fg = "dark blue" ,bg="sky blue", anchor = 'w')
label4.grid(row = 7,column=0) 
label5 = Label(root2, font=('slant',20,'bold'), text="####After read  type \nany alphabet for billing####",fg="dark blue",bg="sky blue")
entry5 = Entry(root2, textvariable = ok_inp,relief=RIDGE,fg="dark blue",bg="white")
label5.grid(row=9,column=0,sticky=E) 
entry5.grid(row=9,column=2)
ok_btn = Button(root2, text="OK", command= enter)
ok_btn.grid(row=10, column=1)
root2.mainloop()
####################### END 2ND PAGE #########################
 
####################### THIRD PAGE ###########################

menu_category = ["Tea & Coffee","Beverages","Fast Food","Starters","Main Course","Dessert"]

menu_category_dict = {"Tea & Coffee":"1 Tea & Coffee.txt","Beverages":"2 Beverages.txt",
                "Fast Food":"3 Fast Food.txt",
                "Starters":"4 Starters.txt","Main Course":"5 Main Course.txt",
                "Dessert":"6 Dessert.txt"}

order_dict = {}
for i in menu_category:
    order_dict[i] = {}

os.chdir(os.path.dirname(os.path.abspath('C:\TurboC++\Disk\TurboC3\BIN\Menu')))

def load_menu():
    menuCategory.set("")
    menu_tabel.delete(*menu_tabel.get_children())
    menu_file_list = os.listdir("Menu")
    for file in menu_file_list:
        f = open("Menu\\" + file , "r")
        category=""
        while True:
            line = f.readline()
            if(line==""):
                menu_tabel.insert('',END,values=["","",""])
                break
            elif (line=="\n"):
                continue
            elif(line[0]=='#'):
                category = line[1:-1]
                name = "\t\t"+line[:-1]
                price = ""
            elif(line[0]=='*'):
                name = line[:-1]
                price = ""
            else:
                name = line[:line.rfind(" ")]
                price = line[line.rfind(" ")+1:-3]
            
            menu_tabel.insert('',END,values=[name,price,category])
       

def load_order():
    order_tabel.delete(*order_tabel.get_children())
    for category in order_dict.keys():
        if order_dict[category]:
            for lis in order_dict[category].values():
                order_tabel.insert('',END,values=lis)
    update_total_price()

def add_button_operation():
    name = itemName.get()
    rate = itemRate.get()
    category = itemCategory.get()
    quantity = itemQuantity.get()

    if name in order_dict[category].keys():
        tmsg.showinfo("Error", "Item already exist in your order")
        return
    if not quantity.isdigit():
        tmsg.showinfo("Error", "Please Enter Valid Quantity")
        return
    lis = [name,rate,quantity,str(int(rate)*int(quantity)),category]
    order_dict[category][name] = lis
    load_order()
    
def load_item_from_menu(event):
    cursor_row = menu_tabel.focus()
    contents = menu_tabel.item(cursor_row)
    row = contents["values"]

    itemName.set(row[0])
    itemRate.set(row[1])
    itemCategory.set(row[2])
    itemQuantity.set("1")

def load_item_from_order(event):
    cursor_row = order_tabel.focus()
    contents = order_tabel.item(cursor_row)
    row = contents["values"]

    itemName.set(row[0])
    itemRate.set(row[1])
    itemQuantity.set(row[2])
    itemCategory.set(row[4])

def show_button_operation():
    category = menuCategory.get()
    if category not in menu_category:
        tmsg.showinfo("Error", "Please select valid Choice")
    else:
        menu_tabel.delete(*menu_tabel.get_children())
        f = open("Menu\\" + menu_category_dict[category] , "r")
        while True:
            line = f.readline()
            if(line==""):
                break
            if (line[0]=='#' or line=="\n"):
                continue
            if(line[0]=='*'):
                name = "\t"+line[:-1]
                menu_tabel.insert('',END,values=[name,"",""])
            else:
                name = line[:line.rfind(" ")]
                price = line[line.rfind(" ")+1:-3]
                menu_tabel.insert('',END,values=[name,price,category])

def clear_button_operation():
    itemName.set("")
    itemRate.set("")
    itemQuantity.set("")
    itemCategory.set("")

def cancel_button_operation():
    names = []
    for i in menu_category:
        names.extend(list(order_dict[i].keys()))
    if len(names)==0:
        tmsg.showinfo("Error", "Your order list is Empty")
        return
    ans = tmsg.askquestion("Cancel Order", "Are You Sure to Cancel Order?")
    if ans=="no":
        return
    order_tabel.delete(*order_tabel.get_children())
    for i in menu_category:
        order_dict[i] = {}
    clear_button_operation()
    update_total_price()

def update_button_operation():
    name = itemName.get()
    rate = itemRate.get()
    category = itemCategory.get()
    quantity = itemQuantity.get()

    if category=="":
        return
    if name not in order_dict[category].keys():
        tmsg.showinfo("Error", "Item is not in your order list")
        return
    if order_dict[category][name][2]==quantity:
        tmsg.showinfo("Error", "No changes in Quantity")
        return
    order_dict[category][name][2] = quantity
    order_dict[category][name][3] = str(int(rate)*int(quantity))
    load_order()

def remove_button_operation():
    name = itemName.get()
    category = itemCategory.get()

    if category=="":
        return
    if name not in order_dict[category].keys():
        tmsg.showinfo("Error", "Item is not in your order list")
        return
    del order_dict[category][name]
    load_order()

def update_total_price():
    price = 0
    for i in menu_category:
        for j in order_dict[i].keys():
            price += int(order_dict[i][j][3])
    if price == 0:
        totalPrice.set("")
    else:
        totalPrice.set("$ "+str(price)+"  /-")

def bill_button_operation():
    customer_name = customerName.get()
    customer_contact = customerContact.get()
    names = []
    for i in menu_category:
        names.extend(list(order_dict[i].keys()))
    if len(names)==0:
        tmsg.showinfo("Error", "Your order list is Empty")
        return
    if customer_name=="" or customer_contact=="":
        tmsg.showinfo("Error", "Customer Details Required")
        return
    if not customerContact.get().isdigit():
        tmsg.showinfo("Error", "Invalid Customer Contact")
        return   
    ans = tmsg.askquestion("Generate Bill", "Are You Sure to Generate Bill?")
    ans = "yes"
    if ans=="yes":
        bill = Toplevel()
        bill.title("Bill")
        bill.geometry("670x500+300+100")
        bill_text_area = Text(bill, font=("arial", 12))
        st = "\t\t\t\tHotel Billing System\n\t\t\tDLQ1231\n"
        st += "\t\t\tCODE.NO:- 34VASFD2215HKAAA\n"
        st += "-"*61 + "BILL" + "-"*61 + "\nDate:- "

        
        t = time.localtime(time.time())
        week_day_dict = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",
                            6:"Sunday"}
        st += f"{t.tm_mday} / {t.tm_mon} / {t.tm_year} ({week_day_dict[t.tm_wday]})"
        st += " "*10 + f"\t\t\t\t\t\tTime:- {t.tm_hour} : {t.tm_min} : {t.tm_sec}"

        
        st += f"\nCustomer Name:- {customer_name}\nCustomer Contact:- {customer_contact}\n"
        st += "-"*130 + "\n" + " "*4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
        st += "-"*130 + "\n"

        
        for i in menu_category:
            for j in order_dict[i].keys():
                lis = order_dict[i][j]
                name = lis[0]
                rate = lis[1]
                quantity = lis[2]
                price = lis[3]
                st += name + "\t\t\t\t\t" + rate + "\t      " + quantity + "\t\t  " + price + "\n\n"
        st += "-"*130

        
        st += f"\n\t\t\tTotal price : {totalPrice.get()}\n"
        st += "-"*130

        
        bill_text_area.insert(1.0, st)

        
        folder = f"{t.tm_mday},{t.tm_mon},{t.tm_year}"
        if not os.path.exists(f"Bill Records\\{folder}"):
            os.makedirs(f"Bill Records\\{folder}")
        file = open(f"Bill Records\\{folder}\\{customer_name+customer_contact}.txt", "w")
        file.write(st)
        file.close()

        
        order_tabel.delete(*order_tabel.get_children())
        for i in menu_category:
            order_dict[i] = {}
        clear_button_operation()
        update_total_price()
        customerName.set("")
        customerContact.set("")

        bill_text_area.pack(expand=True, fill=BOTH)
        bill.focus_set()
        bill.protocol("WM_DELETE_WINDOW", close_window)

def close_window():
    tmsg.showinfo("Thanks", "Thanks for using our service")
    root.destroy()

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Hotel Billing System")


style_button = ttk.Style()
style_button.configure("TButton",font = ("arial",10,"bold"),
   background="lightgreen")

title_frame = Frame(root, bd=8, bg="sky blue", relief=GROOVE)
title_frame.pack(side=TOP, fill="x")

title_label = Label(title_frame, text="BILLING SYSTEM", 
                    font=("times new roman", 25, "bold"),bg = "dark blue", fg="white", pady=5)
title_label.pack()


customer_frame = LabelFrame(root,text="Customer Details",font=("times new roman", 15, "bold"),
                            bd=8, bg="lightblue", relief=GROOVE)
customer_frame.pack(side=TOP, fill="x")
customer_name_label = Label(customer_frame, text="Name", 
                    font=("arial", 15, "bold"),bg = "lightblue", fg="blue")
customer_name_label.grid(row = 0, column = 0)

customerName = StringVar()
customerName.set("")
customer_name_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,
                                textvariable=customerName)
customer_name_entry.grid(row = 0, column=1,padx=50)

customer_contact_label = Label(customer_frame, text="Contact", 
                    font=("arial", 15, "bold"),bg = "lightblue", fg="blue")
customer_contact_label.grid(row = 0, column = 2)

customerContact = StringVar()
customerContact.set("")
customer_contact_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,
                                textvariable=customerContact)
customer_contact_entry.grid(row = 0, column=3,padx=50)


menu_frame = Frame(root,bd=8, bg="lightblue", relief=GROOVE)
menu_frame.place(x=0,y=125,height=500,width=680)

menu_label = Label(menu_frame, text="Menu", 
                    font=("times new roman", 20, "bold"),bg = "lightblue", fg="red", pady=0)
menu_label.pack(side=TOP,fill="x")

menu_category_frame = Frame(menu_frame,bg="lightblue",pady=10)
menu_category_frame.pack(fill="x")

combo_lable = Label(menu_category_frame,text="Select Type", 
                    font=("arial", 12, "bold"),bg = "lightblue", fg="blue")
combo_lable.grid(row=0,column=0,padx=10)

menuCategory = StringVar()
combo_menu = ttk.Combobox(menu_category_frame,values=menu_category,
                            textvariable=menuCategory)
combo_menu.grid(row=0,column=1,padx=30)

show_button = ttk.Button(menu_category_frame, text="Show",width=10,
                        command=show_button_operation)
show_button.grid(row=0,column=2,padx=60)

show_all_button = ttk.Button(menu_category_frame, text="Show All",
                        width=10,command=load_menu)
show_all_button.grid(row=0,column=3)

############################# Menu Tabel ##########################################
menu_tabel_frame = Frame(menu_frame)
menu_tabel_frame.pack(fill=BOTH,expand=1)

scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)

style = ttk.Style()
style.configure("Treeview.Heading",font=("arial",13, "bold"))
style.configure("Treeview",font=("arial",12),rowheight=25)

menu_tabel = ttk.Treeview(menu_tabel_frame,style = "Treeview",
            columns =("name","price","category"),xscrollcommand=scrollbar_menu_x.set,
            yscrollcommand=scrollbar_menu_y.set)

menu_tabel.heading("name",text="Name")
menu_tabel.heading("price",text="Price")
menu_tabel["displaycolumns"]=("name", "price")
menu_tabel["show"] = "headings"
menu_tabel.column("price",width=50,anchor='center')

scrollbar_menu_x.pack(side=BOTTOM,fill=X)
scrollbar_menu_y.pack(side=RIGHT,fill=Y)

scrollbar_menu_x.configure(command=menu_tabel.xview)
scrollbar_menu_y.configure(command=menu_tabel.yview)

menu_tabel.pack(fill=BOTH,expand=1)



load_menu()
menu_tabel.bind("<ButtonRelease-1>",load_item_from_menu)


item_frame = Frame(root,bd=8, bg="lightblue", relief=GROOVE)
item_frame.place(x=680,y=125,height=230,width=680)

item_title_label = Label(item_frame, text="Item", 
                    font=("times new roman", 20, "bold"),bg = "lightblue", fg="red")
item_title_label.pack(side=TOP,fill="x")

item_frame2 = Frame(item_frame, bg="lightblue")
item_frame2.pack(fill=X)

item_name_label = Label(item_frame2, text="Name", 
                    font=("arial", 12, "bold"),bg = "lightblue", fg="blue")
item_name_label.grid(row=0,column=0)

itemCategory = StringVar()
itemCategory.set("")

itemName = StringVar()
itemName.set("")
item_name = Entry(item_frame2, font="arial 12",textvariable=itemName,state=DISABLED, width=25)
item_name.grid(row=0,column=1,padx=10)

item_rate_label = Label(item_frame2, text="Price", 
                    font=("arial", 12, "bold"),bg = "lightblue", fg="blue")
item_rate_label.grid(row=0,column=2,padx=40)

itemRate = StringVar()
itemRate.set("")
item_rate = Entry(item_frame2, font="arial 12",textvariable=itemRate,state=DISABLED, width=10)
item_rate.grid(row=0,column=3,padx=10)

item_quantity_label = Label(item_frame2, text="Quantity", 
                    font=("arial", 12, "bold"),bg = "lightblue", fg="blue")
item_quantity_label.grid(row=1,column=0,padx=30,pady=15)

itemQuantity = StringVar()
itemQuantity.set("")
item_quantity = Entry(item_frame2, font="arial 12",textvariable=itemQuantity, width=10)
item_quantity.grid(row=1,column=1)

item_frame3 = Frame(item_frame, bg="lightblue")
item_frame3.pack(fill=X)

add_button = ttk.Button(item_frame3, text="Add Item"
                        ,command=add_button_operation)
add_button.grid(row=0,column=0,padx=40,pady=30)

remove_button = ttk.Button(item_frame3, text="Remove Item"
                        ,command=remove_button_operation)
remove_button.grid(row=0,column=1,padx=40,pady=30)

update_button = ttk.Button(item_frame3, text="Update Quantity"
                        ,command=update_button_operation)
update_button.grid(row=0,column=2,padx=40,pady=30)

clear_button = ttk.Button(item_frame3, text="Clear",
                        width=8,command=clear_button_operation)
clear_button.grid(row=0,column=3,padx=40,pady=30)


order_frame = Frame(root,bd=8, bg="lightblue", relief=GROOVE)
order_frame.place(x=680,y=335,height=370,width=680)

order_title_label = Label(order_frame, text="Your Order", 
                    font=("times new roman", 20, "bold"),bg = "lightblue", fg="red")
order_title_label.pack(side=TOP,fill="x")

order_tabel_frame = Frame(order_frame)
order_tabel_frame.place(x=0,y=40,height=260,width=680)

scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

order_tabel = ttk.Treeview(order_tabel_frame,
            columns =("name","rate","quantity","price","category"),xscrollcommand=scrollbar_order_x.set,
            yscrollcommand=scrollbar_order_y.set)

order_tabel.heading("name",text="Name")
order_tabel.heading("rate",text="Rate")
order_tabel.heading("quantity",text="Quantity")
order_tabel.heading("price",text="Price")
order_tabel["displaycolumns"]=("name", "rate","quantity","price")
order_tabel["show"] = "headings"
order_tabel.column("rate",width=100,anchor='center', stretch=NO)
order_tabel.column("quantity",width=100,anchor='center', stretch=NO)
order_tabel.column("price",width=100,anchor='center', stretch=NO)

order_tabel.bind("<ButtonRelease-1>",load_item_from_order)

scrollbar_order_x.pack(side=BOTTOM,fill=X)
scrollbar_order_y.pack(side=RIGHT,fill=Y)

scrollbar_order_x.configure(command=order_tabel.xview)
scrollbar_order_y.configure(command=order_tabel.yview)

order_tabel.pack(fill=BOTH,expand=1)


total_price_label = Label(order_frame, text="Total Price", 
                    font=("arial", 12, "bold"),bg = "lightblue", fg="blue")
total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=10)

totalPrice = StringVar()
totalPrice.set("")
total_price_entry = Entry(order_frame, font="arial 12",textvariable=totalPrice,state=DISABLED, 
                            width=10)
total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=10)

bill_button = ttk.Button(order_frame, text="Bill",width=8,
                        command=bill_button_operation)
bill_button.pack(side=LEFT,anchor=SW,padx=80,pady=10)

cancel_button = ttk.Button(order_frame, text="Cancel Order",command=cancel_button_operation)
cancel_button.pack(side=LEFT,anchor=SW,padx=20,pady=10)

root.mainloop()
###################  END 3RD PAGE ##################