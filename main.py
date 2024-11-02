import mysql.connector
import tkinter as tk
import function as f
import bill_s as bill
import tkinter.font as font

Password = ''

# I didn't want to rename database so it is still library :)
def main():
    global Password
    MainScreen = tk.Tk()
    MainScreen.title("Bookstore Management System")
    font1 = font.Font(size=20, weight='bold')
    font2 = font.Font(size = 30, weight = 'bold')
    f.center_Screen(MainScreen, 720, 480)

    Books_Button = tk.Button(text = "Books",font = font2,command = lambda : f.Book_menu(Password,font1,MainScreen))
    Books_Button.place(x = 280,y = 30)

    Customer_button = tk.Button(text = "Customer",font = font2, command = lambda : f.Cust_menu(Password,font1,MainScreen))
    Customer_button.place(x = 260,y = 130)

    Billing_button = tk.Button(text = "Billing",font = font2, command = lambda : bill.bill(Password,MainScreen))
    Billing_button.place(x = 280,y = 230)
    MainScreen.mainloop()


# Login Screen
def login():

    def confirm(password):

        try:
            connection = mysql.connector.connect(host='localhost', user='root', password=password)
            global Password
            Password = password
            connection.close()
            loginScreen.destroy()
            main()

        except mysql.connector.errors.ProgrammingError:  # Found these errors using sys :)
            password_field.delete(0, tk.END)
            f.pass_error()

        except mysql.connector.errors.InterfaceError:
            password_field.delete(0, tk.END)
            f.con_error()

    loginScreen = tk.Tk()
    loginScreen.title("Login")

    f.center_Screen(loginScreen, 550, 200)

    myFont = font.Font(size=20, weight='bold')

    password_label = tk.Label(loginScreen, text="Enter Password :")
    password_label['font'] = myFont
    password_label.place(x=10, y=20, height=50, width=250)

    password_field = tk.Entry(loginScreen, bg="black",fg="white", show='*', width=20)
    password_field['font'] = myFont
    password_field.config(insertbackground="white")  # change cursor colour
    password_field.place(x=255, y=30, height=30, width=260)

    confirm_button = tk.Button(text='Ok', fg="black", bg="grey", command=lambda: confirm(password_field.get()))
    confirm_button['font'] = myFont
    confirm_button.place(x=230, y=100, height=50, width=50)

    loginScreen.mainloop()


login()
