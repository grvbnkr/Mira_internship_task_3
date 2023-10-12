from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import re
global Entry4
Entry4=""



mw=Tk()
mw.geometry("700x700+350+30")
mw.title("Enquiry Management System by Gaurav")
mw.configure(bg="lightgreen")

def f1():
	mw.withdraw()
	us.deiconify()

def f3():

	us.withdraw()
	mw.deiconify()

def f5():

	mw.withdraw()
	ad.deiconify()

def f6():

	ad.withdraw()
	mw.deiconify()


def f4():
	global Entry4
	
	name=name_ent.get()
	phone=phone_ent.get()	
	add=add_ent.get(1.0, END)
	
	


	if name=="":
		showerror("Error","Name cannot be empty.")
		
	elif name.strip()=="":
		showerror("Error","Name cannot be spaces.")
		
	elif re.search(r'[^\w\s]', name):
		showerror("Error","Only use letters. ")
	elif re.search(r'[^\w\s]', phone):
		showerror("Error","Only use numbers. ")	
	elif not name.isalpha():
		showerror("Error","Only use letters in name.")

		
	elif len(name)<2:
		showerror("Error","Names require two letters minimum.")
		
	elif phone=="":
		showerror("Error","Phone No. cannot be empty.")
		
	elif phone.strip()=="":
		showerror("Error","Phone No. cannot be spaces.")
	elif  not phone.isnumeric():
		showerror("Error","Please use digits only  for phone numbers.")
	elif not phone.isnumeric():
		showerror("Error","Only use numbers in phone.")
		
	elif add=="":
		showerror("Error","Address cannot be empty.")
	elif add.strip()=="":
		showerror("Error","Address cannot be spaces.")
	elif len(add)<5:
		showerror("Error","Please provide a complete address.")

	else:
		con=None
		try:
			
			con=connect("enquiry.db")
			cursor=con.cursor()
			sql="insert into student values('%s','%s','%s', '%s')"

			cursor.execute(sql % (name,phone,add,Entry4))
			con.commit()
			showinfo("Success", "data inserted ")
		except Exception as e:
			con.rollback()
			showerror("Issue3333", e)
		finally:
			if con is not None:
				con.close()
	name_ent.delete(0, END)
	phone_ent.delete(0, END)
	add_ent.delete(1.0, END)
	radio1.select()
	name_ent.focus()
				
	
		
def f7():
	ad_name=ad_name_ent.get()
	ad_pass=ad_pass_ent.get()
	if ad_name=="":
		showerror("Error", "Name cannot be empty.")
	elif ad_name.strip()=="":
		showerror("Error","Name cannot be spaces.")
	elif len(ad_name)<2:
		showerror("Error", "Names require two letters minimum.")
	elif ad_pass=="":
		showerror("Error","Enter password")
	elif ad_pass.strip()=="":
		showerror("Error","Enter correct passwrod")
	elif not ad_pass.isalnum():
		showerror("Error","Special characters are not allowed.")
	elif re.search(r'[^\w\s]', ad_name):
		showerror("Error","Only use letters ")
	elif (ad_name=="gg") and (ad_pass=="gg"):
		ad.withdraw()
		sw.deiconify()
	else:
		showerror("Error","Please enter correct name and password.")
	ad_name_ent.delete(0,END)
	ad_pass_ent.delete(0, END)
	ad_name_ent.focus()

def f8():
	sw.withdraw()
	ad.deiconify()
	
def f9():
	sw.withdraw()
	tw.deiconify()
	show_ent.delete(1.0, END)
	con=None
	try:
		con=connect("enquiry.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info + "Name ="+ str(d[0]) + ", \n"+"Phone No. = "+str(d[1]) + ", \n"+"Address = " + str(d[2]) +  "Choice = "  +str(d[3])+  " \n\n\n"
		show_ent.insert(INSERT, info)
	except Exception as e:
		showerror("Issue ",str(e))
	finally:
		if con is not None:
			con.close()

		
def f10():
	tw.withdraw()
	sw.deiconify()
	
def f11():
	sw.withdraw()
	fw.deiconify()
def f12():
	fw.withdraw()
	sw.deiconify()
def f13():
	name=fw_name_ent.get()
	if name=="":
		showerror("Error","Name cannot be empty.")
	elif name.strip()=="":
		showerror("Error","Name cannot be spaces.")
	elif not name.isalpha():
		showerror("Error","Only letters please.")
	elif re.search(r'[^\w\s]', name):
		showerror("Error","Only use letters ")
	else :
		con=None
		try:
			con=connect("enquiry.db")
			cursor=con.cursor()
			cursor.execute("SELECT COUNT(*) FROM student WHERE name=?", (name,))
			count = cursor.fetchone()[0]
			if count > 0:
				sql="Delete from student Where name = '%s'"
				cursor.execute(sql%(name))
				con.commit()
				showinfo("success","Data deleted")
			else:
   				showerror("Error","Not present in the database.")
			
		except Exception as e:
			con.rollback()
			showerror("Issue ",str(e))
		finally:
			if con is not None:
				con.close()
	fw_name_ent.delete(0, END)
		
	
	
	
	

f=("Times New Roman", 20, "bold")
f2=("Times New Roman", 18, "bold")
ad_btn=Button(mw, text="Admin", font=f, bg="lightyellow", width=10, command=f5)
ad_btn.place(x=260, y=230)

us_btn=Button(mw, text="User", font=f, bg="lightyellow", width=10, command=f1)
us_btn.place(x=260, y=330)


us=Tk()

us.geometry("700x700+350+30")
us.title("Enquiry Management System by Gaurav")
us.configure(bg="lightgreen")

name_lab=Label(us, text="Enter your Name : ", font=f2, bg="lightgreen")
name_lab.place(x=30, y=50)

name_ent=Entry(us, font=f2, bg="lightyellow")
name_ent.place(x=285, y=50)

phone_lab=Label(us, text="Enter your Phone No. : ", font=f2, bg="lightgreen")
phone_lab.place(x=30, y=150)

phone_ent=Entry(us, font=f2, bg="lightyellow")
phone_ent.place(x=285, y=150)

add_lab=Label(us, text="Enter your Address :", font=f2, bg="lightgreen")
add_lab.place(x=30, y=250)

add_ent=ScrolledText(us, font=f2, height=4, width=17, bg="lightyellow")
add_ent.place(x=285, y=250)

sel_lab=Label(us, text="Select any One : ", font=f2, bg="lightgreen")
sel_lab.place(x=30, y=400)



def python():
	global Entry4
	Entry4="Python"
	
def ml():
	global Entry4
	Entry4="ML"
	
def django():
	global Entry4
	Entry4="Django"
	
def js():
	global Entry4
	Entry4="JS"
	
def java():
	global Entry4
	Entry4="java"
	
ch=IntVar()


radio1 = Radiobutton(us,  text="Python",  font=f2, bg="lightgreen",variable=ch, value=1, command=python)
radio2 = Radiobutton(us, text="ML",  font=f2, bg="lightgreen",variable=ch, value=2, command=ml)
radio3 = Radiobutton(us, text="Django", font=f2, bg="lightgreen",variable=ch, value=3, command=django)
radio4 = Radiobutton(us, text="JS",  font=f2, bg="lightgreen",variable=ch, value=4, command=js)
radio5 = Radiobutton(us, text="Java", font=f2, bg="lightgreen",variable=ch, value=5,command=java)
radio1.select()


radio1.place(x=285, y=400)
radio2.place(x=285, y=440)
radio3.place(x=285, y=480)
radio4.place(x=285, y=520)
radio5.place(x=285, y=560)



sub_btn=Button(us, text="Submit", font=f2, bg="SpringGreen2", width=10, command=f4)
sub_btn.place(x=150, y=625)

back_btn=Button(us, text="Back", font=f2, bg="red2",width=10, command=f3)
back_btn.place(x=350, y=625)

us.withdraw()

ad=Tk()
ad.geometry("700x700+350+30")
ad.title("Enquiry Management System by Gaurav")
ad.configure(bg="lightgreen")

ad_name_lab=Label(ad, text="Enter your name : ", font=f2, bg="lightgreen")
ad_name_lab.place(x=230, y=200)

ad_name_ent=Entry(ad, font=f2, bg="lightyellow")
ad_name_ent.place(x=230, y=250)

ad_pass_lab=Label(ad, text="Enter Password : ", font=f2, bg="lightgreen")
ad_pass_lab.place(x=230, y=320)

ad_pass_ent=Entry(ad, font=f2,show="*", bg="lightyellow")
ad_pass_ent.place(x=230, y=370)

ad_sub_btn=Button(ad, text="Login", font=f2, bg="SpringGreen2", width=10, command=f7)
ad_sub_btn.place(x=180, y=450)

ad_back_btn=Button(ad, text="Back", font=f2, bg="red2",width=10, command=f6)
ad_back_btn.place(x=380, y=450)
ad.withdraw()

sw=Tk()
sw.geometry("700x700+350+30")
sw.title("Enquiry Management System by Gaurav")
sw.configure(bg="lightgreen")

sw_view=Button(sw, text="View", font=f2, bg="lightyellow",width=10, command=f9)
sw_view.place(x=280, y=150)

sw_delete=Button(sw, text="delete", font=f2, bg="lightyellow",width=10, command=f11)
sw_delete.place(x=280, y=210)

sw_back=Button(sw, text="back", font=f2, bg="lightyellow",width=10, command=f8)
sw_back.place(x=280, y=270)



sw.withdraw()

tw=Tk()
tw.geometry("700x700+350+30")
tw.title("Enquiry Management System by Gaurav")
tw.configure(bg="lightgreen")

show_ent=ScrolledText(tw, font=f2, height=20, width=40, bg="lightyellow")
show_ent.place(x=100, y=60)

tw_back=Button(tw, text="back", font=f2, bg="red2",width=10, command=f10)
tw_back.place(x=280, y=600)

tw.withdraw()

fw=Tk()
fw.geometry("700x700+350+30")
fw.title("Enquiry Management System by Gaurav")
fw.configure(bg="lightgreen")

fw_name_lab=Label(fw, text="Enter Name : ", font=f2, bg="lightgreen")
fw_name_lab.place(x=250, y=100)

fw_name_ent=Entry(fw, font=f2, bg="lightyellow")
fw_name_ent.place(x=250, y=150)


fw_delete_btn=Button(fw, text="Delete", font=f2, bg="red2", width=10, command=f13)
fw_delete_btn.place(x=180, y=250)

fw_back_btn=Button(fw, text="Back", font=f2, bg="red2",width=10, command=f12)
fw_back_btn.place(x=380, y=250)

fw.withdraw()

def on_closing():
	if askyesno("Exit", "Do you want to exit ? "):
		mw.destroy()
		us.destroy()
		ad.destroy()
		sw.destroy()
		tw.destroy()
		fw.destroy()




mw.protocol("WM_DELETE_WINDOW", on_closing)
us.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)
ad.protocol("WM_DELETE_WINDOW", on_closing)
tw.protocol("WM_DELETE_WINDOW", on_closing)
fw.protocol("WM_DELETE_WINDOW", on_closing)



mw.mainloop()