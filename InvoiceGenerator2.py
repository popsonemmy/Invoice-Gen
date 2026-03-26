import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
def clear_item():
    qty_entry.delete(0, tk.END)
    qty_entry.insert(0,"0")
    descripition_entry.delete(0, tk.END)
    unit_entry.delete(0, tk.END)
    unit_entry.insert(0,"0.0")
invoice_list=[]
def add_item():
     qty = int(qty_entry.get())
     desc = descripition_entry.get()
     price = float(unit_entry.get())
     line_total = qty*price
     invoice_item = [qty,desc,price,line_total]
     tree.insert('',0, values=invoice_item)
     clear_item()
     print(qty)

     invoice_list.append(invoice_item)
def new_invoice():
    firstname_entry.delete(0, tk.END)
    lastname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()

def save_invoice():
    doc=DocxTemplate('Invoice_template.docx')
    name=firstname_entry.get() + " " +lastname_entry.get()
    phone=phone_entry.get()
    subtotal= sum(item[3] for item in invoice_list)
    salestax=0.05
    total=subtotal*(1-salestax)
    docname="new_invoice"+name+datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")+".docx"
    messagebox.showinfo('invoice complete', 'print invoice')
    print(name)


    doc.render({'name':name, 'phone':phone,
               'invoice_list':invoice_list,
                'salestax':str(salestax*100)+"%",
                'subtotal':subtotal,
                'total':total})
    doc.save(docname)


root=tk.Tk()

root.title("invoice Generator")

Bigframe =tk.Frame(root)
Bigframe.pack()

firstname_label=tk.Label(Bigframe, text='first name')
firstname_label.grid(row=0,column=0)

lastname_label=tk.Label(Bigframe, text='last name')
lastname_label.grid(row=0,column=1)

firstname_entry=tk.Entry(Bigframe)
firstname_entry.grid(row=1,column=0, padx=10, pady=10)

lastname_entry=tk.Entry(Bigframe)
lastname_entry.grid(row=1,column=1, padx=10, pady=10)

phone_label=tk.Label(Bigframe, text='Phone Number')
phone_label.grid(row=0, column=2)

phone_entry=tk.Entry(Bigframe)
phone_entry.grid(row=1, column=2, padx=10, pady=10)

qty_label= tk.Label(Bigframe, text='Quantity Purchased')
qty_label.grid(row=2, column=0,)

qty_entry= ttk.Spinbox(Bigframe, from_=0, to=100)
qty_entry.grid(row=3, column=0, padx=10, pady=10)

decscription_label= tk.Label(Bigframe, text='Item Description')
decscription_label.grid(row=2, column=1)

descripition_entry= tk.Entry(Bigframe)
descripition_entry.grid(row=3, column=1, padx=10, pady=10)

unit_label=tk.Label(Bigframe, text='Unit Price')
unit_label.grid(row=2, column=2)

unit_entry= ttk.Spinbox(Bigframe, from_=0.0, to=1000, increment=0.5)
unit_entry.grid(row=3, column=2, padx=10, pady=10)

add_button=tk.Button(Bigframe, text='add item',command=add_item)
add_button.grid(row=4, column=2, pady=10, padx=10)

column=('qty', 'desc', 'price', 'line_total')
tree=ttk.Treeview(Bigframe,columns=column, show="headings")
tree.heading('qty',text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('line_total', text='Line Total')

tree.grid(row=5,column=0, columnspan=3,  padx=10, pady=10)

save_invoice = tk.Button(Bigframe, text='Generate Invoice', command=save_invoice)
save_invoice.grid(row=6, column=0, columnspan=3, sticky='news', padx=20, pady=5)
new_invoice=tk.Button(Bigframe, text='New Invoice', command=new_invoice)
new_invoice.grid(row=7, column=0, columnspan= 3,sticky='news',padx=20, pady=5)
root.mainloop()