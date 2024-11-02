import tkinter as tk
from tkinter.font import Font
import mysql.connector 
from function import center_Screen

#Grand Total
total = 0
grandlist = []

def bill(password,MainScreen):

    screen=tk.Toplevel(MainScreen)
    screen.title('bookstore billing')
    center_Screen(screen,750,600)
    screen.configure(bg='grey')
    
    #Fonts
    fon=welcomefont=Font(family='Courier New',size=20,weight='bold',slant='italic',underline=1)
    myfont=Font(family='courier new',size=15,slant='italic',weight='bold')
    billfont=Font(family='helvetica',size=10,weight='bold')
    billfont1=Font(family='helvetica',size=10,slant='italic')
    
    def additems(custid,phone,bookid,quantity):
        global total
        global grandlist
        
        connection = mysql.connector.connect(host='localhost',password=password,user='root',database='library')
        cursor = connection.cursor()
        
        inp = str(bookid).lstrip("(").rstrip(",)")
        
        cursor.execute(f'select Price from books where book_id = {inp}')
        bookprice = cursor.fetchone()
        cursor.execute(f"select book_name from books where book_id = {inp}")
        bookname_tup = cursor.fetchone()
        connection.close()

        bookname = str(bookname_tup).lstrip("(").rstrip(",)")
        bookprice = float(str(bookprice).lstrip("(").rstrip(",)"))
        final=(int(bookprice))*(int(quantity))
        total=total+final
        grandlist.append([custid,phone,bookname,quantity,bookprice,final,bookid])# added bookid at end cause didn't want to rewrite:(
        
        

    def Clear():
        global grandlist
        grandlist = []
        
    def Generate_bill(billfont,screen,password):
        global total
        global grandlist
        
        if not grandlist:
            return

        bill=tk.Toplevel(screen)
        bill.geometry('500x500')
        center_Screen(bill,500,500)

        billhead=tk.Label(bill,text='BILL').place(x=200,y=0)
        
        cust_name=tk.Label(bill,text='Customer ID:',font=billfont).place(x=0,y=15)
        cust_number=tk.Label(bill,text='Phone.no:',font=billfont).place(x=0,y=35)
        
        line=tk.Label(bill,text='*'*250).place(x=0,y=60)
        
        b_book_name=tk.Label(bill,text='BOOK',font=billfont1).place(x=2,y=75)
        b_book_qty=tk.Label(bill,text='Qty',font=billfont1).place(x=132,y=75)
        b_book_pr=tk.Label(bill,text='PRICE',font=billfont1).place(x=182,y=75)
        
        final_price=tk.Label(bill,text='finalprice',font=billfont1).place(x=350,y=75)
        total_price=tk.Label(bill,text='GRAND TOTAL:',font=billfont).place(x=300,y=450)

    
        i = 95 # y value for labels
        bcn=tk.Label(bill,text=grandlist[0][0],font=billfont1).place(x=100,y=15)
        bph=tk.Label(bill,text=grandlist[0][1],font=billfont1).place(x=100,y=35)
        
        for item_list in grandlist:
            connection = mysql.connector.connect(host='localhost',password=password,user='root',database='library')
            cursor = connection.cursor()
            cursor.execute(f"insert into sales values ({str(item_list[6]).lstrip('(').rstrip(',)')},{item_list[2]},{item_list[3]},{item_list[4]},{item_list[5]},{str(item_list[0]).lstrip('(').rstrip(',)')})")
            
            book=tk.Label(bill,text=item_list[2],font=billfont1).place(x=0,y=i)
            quan=tk.Label(bill,text=item_list[3],font=billfont1).place(x=130,y=i)
            bprice=tk.Label(bill,text=item_list[4],font=billfont1).place(x=180,y=i)
            totprice=tk.Label(bill,text=item_list[5],font=billfont1).place(x=350,y=i)
            totl=tk.Label(bill,text=total,font=billfont1).place(x=400,y=450)
            i=i+20  
        
        connection.commit()
        connection.close()
        grandlist = [] #deleting all items of current bill

        bill.mainloop()
        

    Title=tk.Label(screen,text='BILLING SYSTEM',bg='grey',fg='white',padx=40,font=fon)
    Title.place(x=225,y=10)

    #labels/entryfields
    id=tk.Label(screen,text='CUSTOMER ID',font=myfont,bg='grey',fg='white')
    id.place(x=10,y=70)

    connection=mysql.connector.connect(host='localhost',password=password,user='root',database='library')
    cursor=connection.cursor()
    cursor.execute("select cust_id from cust")
    drop_down_data = cursor.fetchall()
    connection.close()
    val_id = tk.StringVar(screen,value = "Select ID")
    book_id_drop_down = tk.OptionMenu(screen,val_id,*drop_down_data)
    book_id_drop_down.place(x = 170,y = 70)

    ph=tk.Label(screen,text='PHONE.NO',font=myfont,bg='grey',fg='white')
    ph.place(x=400,y=70)

    ph_entry=tk.Entry(screen,text='',width=30)
    ph_entry.place(x=520,y=70)

    product=tk.Label(screen,text='*'*15+'BOOK DETAILS'+'*'*15,font=fon,bg='grey',fg='orange')
    product.place(x=1,y=100)

    book_id=tk.Label(screen,text='Book Id',font=myfont,bg='grey',fg='black')
    book_id.place(x=1,y=140)

    connection=mysql.connector.connect(host='localhost',password=password,user='root',database='library')
    cursor=connection.cursor()
    cursor.execute("select book_id from books")
    drop_down_data = cursor.fetchall()
    connection.close()
    val = tk.StringVar(screen,value = "Select Book Id")
    book_id_drop_down = tk.OptionMenu(screen,val,drop_down_data[0],*drop_down_data)
    book_id_drop_down.place(x =150,y = 140)

    quantity=tk.Label(screen,text='Quantity',font=myfont,bg='grey',fg='black')
    quantity.place(x=1,y=200)

    quantity_entry=tk.Entry(screen,text='',width=25)
    quantity_entry.place(x=150,y=200)


    #buttons
    add_items_button= tk.Button(screen,text='Add Items',font=myfont,bg='green',fg='white',command=lambda :additems(val_id.get(),ph_entry.get(),val.get(),quantity_entry.get()))
    add_items_button.place(x=1,y=250)

    generate_bill_button = tk.Button(screen,text='Generate bill',font=myfont,bg='blue',fg='white',command=lambda: Generate_bill(billfont,screen,password))
    generate_bill_button.place(x=200,y=250)

    clear_bill= tk.Button(screen,text='Clear bill',font=myfont,bg='goldenrod',fg='white',command=Clear)
    clear_bill.place(x=1,y=300)

    exit_button= tk.Button(screen,text='Exit',font=myfont,bg='maroon',fg='white',command=screen.destroy)
    exit_button.place(x=200,y=300)
    
    screen.mainloop()








