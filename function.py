#Functions ;)
def center_Screen(root,x,y):
	
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
    
	a = int((screen_width/2) - (x/2))    
	b = int((screen_height/2) - (y/2))
		
	root.geometry(f"{x}x{y}+{a}+{b}")

#Done 
def Done(Screen):
    
    import tkinter as tk
    import tkinter.font as font

    def close():
        DoneScreen.destroy()

    DoneScreen = tk.Toplevel(Screen)
    DoneScreen.title("Done")
    	
    center_Screen(DoneScreen,380,100)

    myFont = font.Font(size = 30,weight = 'bold')
    myFont2 = font.Font(size = 20,weight = 'bold')

    ok_label = tk.Label(DoneScreen,text = "Done")
    ok_label['font'] = myFont
    ok_label.place(x = 90 , y = 5 , height = 40 ,width = 200 )

    ok_button = tk.Button(DoneScreen,text = 'OK',fg = "black",bg = "grey",command = close)
    ok_button['font'] = myFont2
    ok_button.place(x = 160,y = 50,height = 40 , width = 50)

    DoneScreen.mainloop()


#Errors
def pass_error():
    
    import tkinter as tk
    import tkinter.font as font

    def close():
        errorScreen.destroy()

    errorScreen = tk.Tk()
    errorScreen.title("Error")
    
		
    center_Screen(errorScreen,380,100)

    myFont = font.Font(size = 20,weight = 'bold')

    retry_label = tk.Label(errorScreen,text = "Password incorrect")
    retry_label['font'] = myFont
    retry_label.place(x = 90 , y = 5 , height = 40 ,width = 200 )

    retry_button = tk.Button(errorScreen,text = 'Retry',fg = "black",bg = "grey",command = close)
    retry_button['font'] = myFont
    retry_button.place(x = 135,y = 50,height = 40 , width = 100)

    errorScreen.mainloop()

def con_error():
    import tkinter as tk
    import tkinter.font as font

    def close():
        error_screen.destroy()

    error_screen = tk.Tk()
    error_screen.title('Error')

    center_Screen(error_screen,380,100)

    myFont = font.Font(size = 20,weight = 'bold')

    retry_label = tk.Label(error_screen,text = "Connection error ...Is the server running??")
    retry_label['font'] = myFont
    retry_label.grid(row = 1,column = 1)

    retry_button = tk.Button(error_screen,text = 'Retry',fg = "black",bg = "grey",command = close)
    retry_button['font'] = myFont
    retry_button.grid(row = 2,column = 1)

    error_screen.mainloop()

def error():
    import tkinter as tk
    import tkinter.font as font
    def close():
        errorScreen.destroy()

    errorScreen = tk.Tk()
    errorScreen.title("Error")
		
    center_Screen(errorScreen,400,100)

    myFont = font.Font(size = 20,weight = 'bold')

    retry_label = tk.Label(errorScreen,text = "Some kind of error occured ")
    retry_label['font'] = myFont
    retry_label.place(x = 10 , y = 5 , height = 40 ,width = 400 )

    retry_button = tk.Button(errorScreen,text = 'Close',fg = "black",bg = "grey",command = close)
    retry_button['font'] = myFont
    retry_button.place(x = 135,y = 50,height = 40 , width = 100)

    errorScreen.mainloop()

def integrity_error():
    import tkinter as tk
    import tkinter.font as font
    def close():
        errorScreen.destroy()

    errorScreen = tk.Tk()
    errorScreen.title("Error")
		
    center_Screen(errorScreen,400,100)

    myFont = font.Font(size = 20,weight = 'bold')

    retry_label = tk.Label(errorScreen,text = "Customer ID Already Exists !!!")
    retry_label['font'] = myFont
    retry_label.place(x = 10 , y = 5 , height = 40 ,width = 400 )

    retry_button = tk.Button(errorScreen,text = 'Close',fg = "black",bg = "grey",command = close)
    retry_button['font'] = myFont
    retry_button.place(x = 135,y = 50,height = 40 , width = 100)

    errorScreen.mainloop()
    
# Book functions
def Book_menu(Password,Font,MainScreen):
    
    def Add_menu(Password,Font,BookMenu):
        
        def add_book(book_id,book_name,book_author,Qty,Price,password,add_menu): # using add_menu as attribute just to be on the safer side
            import mysql.connector
            try:
                connection = mysql.connector.connect(host = 'localhost',user = 'root',password = password,database = 'library')    
                cursor = connection.cursor()
                cursor.execute(f"Insert into Books values {book_id,book_name,book_author,Qty,Price}") # using f{a,b} returns (a,b) so no need to add () over the {}
                connection.commit()
                connection.close()
                add_menu.destroy()
                Done(add_menu)
            except:
                error()
                add_menu.destroy() 

        import tkinter as tk
    
        # Using grid on same line returns null which is then stored in the variable so no further calling can be done on the variable 
        # Using Toplevel creates a new window but it is a child of tk so when main tk is closed then toplevel also closes 

        add_menu = tk.Toplevel(BookMenu)

        center_Screen(add_menu,600,250)
        
        add_menu.title("Add Book")
        # If u don't add master, the widgets are added to root window
        book_id_label = tk.Label(add_menu,text = "Book ID:",font = Font).grid(column = 1,row=1)
        
        book_id_box = tk.Entry(add_menu,font = Font)
        
        book_id_box.grid(column = 2,row=1)
        
        book_name_label = tk.Label(add_menu,text = "Book Name:",font = Font).grid(column = 1,row=2)
        
        book_name_box = tk.Entry(add_menu,font = Font)
        book_name_box.grid(column = 2,row=2)

        book_author_label = tk.Label(add_menu,text = "Book Author Name:",font = Font).grid(column = 1,row=3)
        
        book_author_box = tk.Entry(add_menu,font = Font)
        book_author_box.grid(column = 2,row=3)
        
        Qty_label =tk.Label(add_menu,text = "Quantity:",font = Font).grid(column = 1,row=4)
        
        Qty_box =tk.Entry(add_menu,font = Font)
        Qty_box.grid(column = 2,row=4)
        
        Price_label=tk.Label(add_menu,text = "Price:",font = Font).grid(column = 1,row = 5)

        Price_box =tk.Entry(add_menu,font = Font)
        Price_box.grid(column = 2,row = 5)
    
        Confirm_Button = tk.Button(add_menu,text = "Confirm",font = Font,command = lambda : add_book(book_id_box.get(),book_name_box.get(),book_author_box.get(),int(Qty_box.get()),float(Price_box.get()),Password,add_menu)).grid(row = 6,column = 1,columnspan = 2)
        
        add_menu.mainloop()

    def delete_menu(Password,Font,BookMenu):
        
        def delete_book(book_id,password,delete_menu):
            import mysql.connector
            try:
                connection = mysql.connector.connect(host = 'localhost',user = 'root',password = password,database = 'library')    
                cursor = connection.cursor()
                
                cursor.execute(f"Delete from Books where book_id = '{book_id}'")
                connection.commit()
                connection.close()
                delete_menu.destroy()
                Done(delete_menu)
            except:
                error()
                delete_menu.destroy()
        
        import tkinter as tk

        delete_menu = tk.Toplevel(BookMenu)
        delete_menu.title("Delete Book")
        center_Screen(delete_menu,440,100)

        book_id_label = tk.Label(delete_menu,text = "Book ID:",font = Font).grid(row = 1,column = 1)
        
        book_id_Field = tk.Entry(delete_menu,font = Font)
        book_id_Field.grid(row = 1,column = 2)

        Confirm_Button = tk.Button(delete_menu,text = "Confirm",font = Font,command = lambda : delete_book(book_id_Field.get(),Password,delete_menu)).grid(row = 2,column = 1,columnspan = 2)
    
    def show_menu(Password,BookMenu):
        import tkinter as tk
        showing_menu = tk.Toplevel(BookMenu)
        showing_menu.title("Customer Details")
                
        center_Screen(showing_menu,700,300)
                
        s_text_box = tk.Text(showing_menu,bg = "white",fg = "black",insertbackground = "black")
        s_text_box.pack(fill = "both" ,expand = True)

        import mysql.connector 
        connection=mysql.connector.connect(host='localhost',password=Password,user='root',database='library')
        cursor=connection.cursor()
        cursor.execute(f"select * from books")
        out=cursor.fetchall()
        text = 'Book_ID \t\t Book_Name \t\t Author_Name \t\t Qty_in_stock \t\t Price\n'
        for i in out:
            for j in i :
                text = text + str(j) +' \t\t '
            text +='\n'
        s_text_box.delete(1.0,tk.END)
        s_text_box.insert(tk.END,text)

    import tkinter as tk
    book_menu = tk.Toplevel(MainScreen)#using small letter for screen and capital for function
    center_Screen(book_menu,450,300)

    Add_book_button = tk.Button(book_menu,text="Add Book",font = Font, command = lambda : Add_menu(Password,Font,book_menu))
    Add_book_button.place(x = 150,y = 20)

    Delete_book_button = tk.Button(book_menu,text = "Delete Book",font = Font,command = lambda : delete_menu(Password,Font,book_menu))
    Delete_book_button.place(x = 140,y = 100)

    Show_book_button = tk.Button(book_menu,text = "Show All Books",font = Font,command = lambda : show_menu(Password,book_menu))
    Show_book_button.place(x = 130,y = 180)

#Customer Functions

def Cust_menu(password,Font,MainScreen):
    
    def Add_cust_menu(Password,Font,Cust_Menu):
        
        def add_cust(cust_id,cust_name,books_brought,pno,email,Password,add_menu):

            import mysql.connector
            try:
                connection = mysql.connector.connect(host = 'localhost',user = 'root',password = password,database = 'library')    
                cursor = connection.cursor()
                cursor.execute(f"Insert into cust values {cust_id,cust_name,books_brought,pno,email}") # using f{a,b} returns (a,b) so no need to add () over the {}
                connection.commit()
                connection.close()
                Done()
                add_menu.destroy()
            
            except mysql.connector.errors.IntegrityError:
                integrity_error()
                add_menu.destroy() 
            
            except:
                error()
                add_menu.destroy() 
        import tkinter as tk
    
        add_menu = tk.Toplevel(Cust_Menu)

        center_Screen(add_menu,600,250)
        
        add_menu.title("Add Customer")
        # If u don't add master, the widgets are added to root window
        cust_id_label = tk.Label(add_menu,text = "Customer ID:",font = Font).grid(column = 1,row=1)
        
        cust_id_box = tk.Entry(add_menu,font = Font)
        
        cust_id_box.grid(column = 2,row=1)
        
        cust_name_label = tk.Label(add_menu,text = "Customer Name:",font = Font).grid(column = 1,row=2)
        
        cust_name_box = tk.Entry(add_menu,font = Font)
        cust_name_box.grid(column = 2,row=2)

        books_brought_label = tk.Label(add_menu,text = "Books Brought:",font = Font).grid(column = 1,row=3)
        
        books_brought_box = tk.Entry(add_menu,font = Font)
        books_brought_box.grid(column = 2,row=3)
        
        pno_label =tk.Label(add_menu,text = "Phone Number:",font = Font).grid(column = 1,row=4)
        
        pno_box =tk.Entry(add_menu,font = Font)
        pno_box.grid(column = 2,row=4)
        
        email_label=tk.Label(add_menu,text = "Email:",font = Font).grid(column = 1,row = 5)

        email_box =tk.Entry(add_menu,font = Font)
        email_box.grid(column = 2,row = 5)
    
        Confirm_Button = tk.Button(add_menu,text = "Confirm",font = Font,command = lambda : add_cust(cust_id_box.get(),cust_name_box.get(),int(books_brought_box.get()),pno_box.get(),email_box.get(),Password,add_menu)).grid(row = 6,column = 1,columnspan = 2)
        
        add_menu.mainloop()

    def Cust_search_menu(password,cust_menu,Font):
        
        def cust_search(cust_id,password,Font,cust_search_menu):
            
            def does_not_exist(font,cust_search_menu):
                import tkinter as tk

                not_exist_menu = tk.Toplevel(cust_search_menu)

                center_Screen(not_exist_menu,380,100)

                not_exist_label = tk.Label(not_exist_menu,font = font,text = "ID Does Not Exist").pack()
                close = tk.Button(not_exist_menu,font = font,text = "Close",command = not_exist_menu.destroy).pack()
            
            if not cust_id: # if no customer id is given it will not run
                return

            import mysql.connector 
            connection=mysql.connector.connect(host='localhost',password=password,user='root',database='library')
            cursor=connection.cursor()
            cursor.execute(f"select * from cust where cust_id = '{str(cust_id).upper()}'")
            out=cursor.fetchall()
            
            if not out:
                does_not_exist(Font,cust_search_menu)

            else:
                import tkinter as tk
                Customer_details = tk.Toplevel(cust_search_menu)
                Customer_details.title("Customer Details")
                
                center_Screen(Customer_details,700,300)
                
                text_box = tk.Text(Customer_details,bg = "white",fg = "black",insertbackground = "black")
                text_box.pack(fill = "both" ,expand = True)
                
                text = "CUST_ID" + ' \t\t ' + "C_NAME " + ' \t\t ' "BOOKS_BROUGHT \t PHNO  \t\t\t EMAIL \n"# manually tried these indents
                
                for i in out:
                    for j in i :
                        text = text + str(j) +' \t\t '
                    text +='\n'
               
                text_box.delete(1.0,tk.END)
                text_box.insert(tk.END,text)
                    
                Customer_details.mainloop()

        import tkinter as tk
        
        
        cust_search_menu = tk.Toplevel(cust_menu)
        cust_search_menu.title("Search Menu")
        
        center_Screen(cust_search_menu,500,100)
        
        cust_name_label = tk.Label(cust_search_menu,font = Font,text = "Customer Id :").grid(column = 1,row = 1)
        
        cust_id_field = tk.Entry(cust_search_menu,font = Font)
        cust_id_field.grid(row = 1,column = 2)

        confirm_button = tk.Button(cust_search_menu,font = Font,text = "Search",command = lambda :cust_search(cust_id_field.get(),password,Font,cust_search_menu))
        confirm_button.grid(column = 1,row = 2,columnspan = 2)


    import tkinter as tk

    cust_menu = tk.Toplevel(MainScreen)
    cust_menu.title("Customer Menu")
    center_Screen(cust_menu,440,300)
    
    add_button = tk.Button(cust_menu,font = Font,text = "Add Customer",command = lambda :Add_cust_menu(password,Font,cust_menu)).place(x = 120,y = 30)
    search_button = tk.Button(cust_menu,font = Font,text = "Search Customer",command = lambda :Cust_search_menu(password,cust_menu,Font)).place(x = 100,y = 100)
    
    cust_menu.mainloop()

"""
#jff not in use ;)
def net_worth(password):
    import mysql.connector

    connection = mysql.connector.connect(host = 'localhost',user = 'root',password = password,database = 'library')    
    cursor = connection.cursor()
    cursor.execute("Select sum(Qty_in_stock),Price from Books group by book_id")
    out = cursor.fetchall()
    total = 0
    for i in out:
        qty = str(i[0]).lstrip("(Decimal'").rstrip("')")
        price = i[1]
        total+=(int(qty)*price)
    print(total)
"""