from tkinter import *
from tkinter import messagebox
from class_databace import Database
root = Tk()
root.title('')
root.geometry('575x450')
root.resizable(0,0)
# باید جلوی ورورد کاربر تکراری رو بگیرم
bd=Database('d:\Python6.db')


s= Scrollbar(root, bg= 'red',)
s.place(x =5, y = 125, height=200)

def select(event):
    try:
        global selected
        global index
        index = lb.curselection()
        selected = lb.get(index)
        selected=selected.split()
        e1.delete(0,END)
        e1.insert(END,selected[1])
        e2.delete(0,END)
        e2.insert(END,selected[2])
        e3.delete(0,END)
        e3.insert(END,selected[3])
        e4.delete(0,END)
        e4.insert(END,selected[4])
    except Exception as error:
        messagebox.showerror("ERROR",f'you have got {error} error')
# IndexError
lb= Listbox(root,yscrollcommand=s.set,borderwidth=10)
lb.place(x= 25, y=125,width=525,height=200)
s.config(command=lb.yview)
lb.bind('<<ListboxSelect>>',select)
# for i in range(1,21):
#     lb.insert(END, i)

def bring_back():
    bg=bd.fetch()
    return bg
r2=bring_back()
 
for i in r2:
    lb.insert(END, f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}')
def delete(): 
    try:
        bd.remove(selected[0])
        clear()
        lb.delete(index)
    except Exception as error:
        messagebox.showerror("ERROR",f'you have got {error} error')
def add():
    try:
        if e1.get()==''or e2.get()==''or e3.get()==''or e4.get()=='':
            messagebox.showerror('ERROR','please enter everything completely')
            return
        try:
            int(e4.get())
        except:
            messagebox.showerror('ERROR','invalid phone number')
            return
        bd.insert(e1.get(), e2.get(), e3.get(), e4.get() )
        lb.delete(0,END)
        records = bd.fetch()
        for i in records:
            lb.insert(END,f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    except Exception as error:
        messagebox.showerror("ERROR",f'you have got {error} error')
  
    # es =f'{e1.get()} {e2.get()} {e3.get()} {e4.get()}'
    # lb.insert(0,es)
def updatee():
    global selected
    global index
    try:
        index=index
    except:
        messagebox.showerror('EMPTY','you have not chose any thing to update')
        messagebox.showwarning("LIMITATION","you cannot change fname and lname")
        return

    messagebox.showwarning("LIMITATION","you cannot change fname and lname")
    try:
        bd.update(selected[0],e1.get(),e2.get(),e3.get(),e4.get())
        lb.delete(0,END)
        records = bd.fetch()
        for i in records:
            lb.insert(END,f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}')
    except Exception as error:
        messagebox.showerror("ERROR",f'you have got {error} error')
def searchh(search_value=0):
    global lb1
    global s1
        # records = bd.search(e5.get())
    try:
        if len(e5.get())==0:
            messagebox.showwarning("EMPTY",'please entery something')
            return
            
        try:
            lb1.destroy()
            s1.destroy()
        except:
            pass
        records =[]
        record = list(lb.get(0,END))
        for i in record:
            result=(''.join(str(x) for x in i)).find(str(e5.get()))
            # messagebox.showinfo('sfgvgh',result)
            # messagebox.showinfo('sfgvgh',' '.join(list(i)))
            if result == -1:
    
                pass
            else:
                index2 =i[0]
                y = bd.search(index2)
                records.append(y)
                # records=(records)
        if records == []:
            messagebox.showerror('NO RESULT','there is no such a thing ')   
            return
        height = len(records)*20
        s1= Scrollbar(root, bg= 'red',)
        s1.place(x =142.5, y = 390-height, height=height)
        lb1= Listbox(root,yscrollcommand=s1.set,borderwidth=0)
        lb1.place(x = 162.5, y = 390-height ,height=height,width=250)
        s1.config(command=lb.yview)
        # if len(records)==0:
        #     messagebox.showerror('ERROR',"nothing was found")
            # pass
        # lb.delete(0,END)
        for i in records:
            messagebox.showinfo('jg',i[0])
            # messagebox.showinfo('jg',i[1])
            # messagebox.showinfo('jg',i[2])
            # messagebox.showinfo('jg',i[3])
            # messagebox.showinfo('jg',i[4])
            lb1.insert(END,f'{i[0]}')
            # def destroy():
            #     lb1.destroy()
            #     s1.destroy()
            # lb1.after(10000,destroy)
    
        def select(event):
            try:
                global selected
                global index
                index = lb1.curselection()
               
                selected = list(lb1.get(index))
                lb.select_set(len(((selected)))-index)
                # selected=list(selected.split())
                e1.delete(0,END)
                e1.insert(END,selected[1])
                e2.delete(0,END)
                e2.insert(END,selected[2])
                e3.delete(0,END)
                e3.insert(END,selected[3])
                e4.delete(0,END)
                e4.insert(END,selected[4])
                lb1.destroy()
                s1.destroy()
            except Exception as error:
                messagebox.showerror("ERROR",f'you have got {error} error')
        lb1.bind('<<ListboxSelect>>',select)
    except Exception as error:
        messagebox.showerror("ERROR",f'you have got {error} error')
def change(*args):
    current_value=e_var.get()
    searchh(current_value)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
def exit1 ():
    root.destroy()
def close(event):
    t1=Tk()
    t1.title('')
    t1.geometry('575x450')
    t1.resizable(0,0)
    t1.mainloop()

l1= Label(root,text = 'Fname:')
l1.place(x=25,y=25,width=50)
l2= Label(root,text = 'Lname:')
l2.place(x=300,y=25,width=50)
l3= Label(root,text = 'Address:')
l3.place(x=25,y=75, width=50)
l4= Label(root,text = 'Phone:')
l4.place(x=300,y=75,width=50)
e1 = Entry(root,bg = 'white', fg = "black",border = 2)
e1.place(x = 75, y = 25,height=25,width=200)
e2 = Entry(root,bg = 'white', fg = "black",border = 2)
e2.place(x = 350, y = 25,height=25,width=200)
e3 = Entry(root,bg = 'white', fg = "black",border = 2)
e3.place(x = 75, y = 75,height=25,width=200)
e4 = Entry(root,bg = 'white', fg = "black",border = 2)
e4.place(x = 350, y = 75,height=25,width=200)
e_var=StringVar()
e_var.trace("w", change)
e5 = Entry(root,bg = 'white', fg = "black",border = 2,font='Ariel 10 bold',textvariable=e_var)
e5.place(x = 162.5, y = 390,height=25,width=250)
b1 = Button(root,text='insert',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold ',border=3,cursor='spider',command=add)
b1.place(x = 25, y= 335,width=112.5)
b2 = Button(root,text='clear',bg = '#C0C0C0', fg = 'black' ,font='Ariel 10 bold',border=3,cursor='spider',command=clear)
b2.place(x =162.5, y= 335,width=112.5)
b3 = Button(root,text='delete',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=delete)
b3.place(x = 300, y= 335,width=112.5)
b4 = Button(root,text='update',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=updatee)
b4.place(x = 432.5, y= 335,width=112.5)
b5 = Button(root,text='search:',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=searchh)
b5.place(x = 25, y= 385,width=112.5)
b6 = Button(root,text='exit',bg = '#C0C0C0', fg = 'black',font='Ariel 10 bold' ,border=3,cursor='spider',command=exit1)
b6.place(x = 432.5, y= 385,width=112.5)
e5.bind('<<Back Space>>',close)









root.mainloop()

