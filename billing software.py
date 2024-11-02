from tkinter import *
from tkinter.font import Font
screen=Tk()
screen.title('bookstore billing')
screen.geometry('750x600')
screen.configure(bg='grey')
fon=welcomefont=Font(family='Courier New',size=20,weight='bold',slant='italic',underline=1)
myfont=Font(family='courier new',size=15,slant='italic',weight='bold')
billfont=Font(family='helvetica',size=10,weight='bold')
billfont1=Font(family='helvetica',size=10,slant='italic')
TITLE=Label(screen,text='BILLING SOFTWARE',bg='grey',fg='white',padx=40,font=fon)
TITLE.place(x=225,y=10)

#functions
i=95
total=0
def Open():
    global billfont
    global bill
    global lst
    global i
    global j
    global total
    bcn=Label(bill,text=lst[0],font=billfont1).place(x=100,y=15)
    bph=Label(bill,text=lst[1],font=billfont1).place(x=100,y=35)
    book=Label(bill,text=lst[2],font=billfont1).place(x=0,y=i)
    quan=Label(bill,text=lst[3],font=billfont1).place(x=130,y=i)
    bprice=Label(bill,text=lst[4],font=billfont1).place(x=180,y=i)
    totprice=Label(bill,text=lst[5],font=billfont1).place(x=350,y=i)
    totl=Label(bill,text=total,font=billfont1).place(x=400,y=450)
    i=i+20    
def additems():
    global lst
    global total
    custname=str(ne.get())
    phone=str(pe.get())
    bookname=str(bne.get())
    bookprice=str(bpe.get())
    quantity=str(qe.get())
    final=(int(bookprice))*(int(quantity))
    total=total+final
    lst=[custname,phone,bookname,quantity,bookprice,final]
def clear():
    bne.delete(0,END)
    bpe.delete(0,END)
    qe.delete(0,END)
#customer details
name=Label(screen,text='CUSTOMER NAME',font=myfont,bg='grey',fg='white')
name.place(x=10,y=70)
ne=Entry(screen,text='',width=30)
ne.place(x=180,y=70)
ph=Label(screen,text='PHONE.NO',font=myfont,bg='grey',fg='white')
ph.place(x=400,y=70)
pe=Entry(screen,text='',width=30)
pe.place(x=520,y=70)
#product details
product=Label(screen,text='*'*15+'BOOK DETAILS'+'*'*15,font=fon,bg='grey',fg='orange')
product.place(x=1,y=100)
     #fields
bn=Label(screen,text='book name',font=myfont,bg='grey',fg='black')
bn.place(x=1,y=140)
bp=Label(screen,text='book price',font=myfont,bg='grey',fg='black')
bp.place(x=1,y=170)
q=Label(screen,text='quantity',font=myfont,bg='grey',fg='black')
q.place(x=1,y=200)
    #entrybox
bne=Entry(screen,text='',width=25)
bne.place(x=150,y=140)
bpe=Entry(screen,text='',width=25)
bpe.place(x=150,y=170)
qe=Entry(screen,text='',width=25)
qe.place(x=150,y=200)
#buttons
add=Button(screen,text='add items',font=myfont,bg='green',fg='white',command=additems)
add.place(x=1,y=250)
gen=Button(screen,text='generate bill',font=myfont,bg='lightblue',fg='white',command=Open)
gen.place(x=200,y=250)
clear=Button(screen,text='clear fields',font=myfont,bg='goldenrod',fg='white',command=clear)
clear.place(x=1,y=300)
ex=Button(screen,text='exit',font=myfont,bg='maroon',fg='white',command=screen.destroy)
ex.place(x=200,y=300)
#bill
bill=Toplevel(screen)
bill.geometry('500x500')
bhead=Label(bill,text='BILL').place(x=200,y=0)
cn=Label(bill,text='customer name:',font=billfont).place(x=0,y=15)
cp=Label(bill,text='phone.no:',font=billfont).place(x=0,y=35)
line=Label(bill,text='*'*250).place(x=0,y=60)
bn=Label(bill,text='BOOK',font=billfont1).place(x=2,y=75)
qty=Label(bill,text='Qty',font=billfont1).place(x=132,y=75)
pr=Label(bill,text='PRICE',font=billfont1).place(x=182,y=75)
finalpr=Label(bill,text='finalprice',font=billfont1).place(x=350,y=75)
totpr=Label(bill,text='GRAND TOTAL:',font=billfont).place(x=300,y=450)








screen.mainloop()








