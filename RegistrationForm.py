from tkinter import *

#create an App root
root = Tk()

# change window title
root.title("Registration Form")

#window geometry - width x height
root.geometry("500x500")

#background for window
root["bg"] = "#e3e3e3"

#create any widget
#1. write Class of Widget
#2. Pass root variable as parameter
#3. Save it in another variable
#4. Pack, place, grid

def click_submit_button():
	gender = var.get()
	if(gender==1):
		gender_selected = "Male"
	else:
		gender_selected = "Female"

	country_selected = temp.get()

	if java.get() and python.get():
		lang= "Java, Python"
	elif java.get():
		lang= "Java"
	elif python.get():
		lang="Python"
	else:
		lang= "No language selected"

	#user_values = "\t"+fullname_entrytext.get() + "\t"+ email_entrytext.get()
	user_values = "\n"+fullname_entrytext.get() + "\n"+ email_entrytext.get()+ "\n" + gender_selected+ "\n" + country_selected+ "\n" + lang
	print(user_values)
	file=open("Registration.txt",'a')
	file.write(user_values)
	file.close()

#Registration Form Label
registration_form_label = Label(root)
registration_form_label.place(x=180,y=60)

#dictionary attributes for label
registration_form_label["text"] = "Registration Form"
registration_form_label["font"] = ("Calibri", 30)
registration_form_label["bg"] = "#e3e3e3"

#Fullname Label
fullname_label = Label(root, text="FullName", bg="#e3e3e3")
fullname_label.place(x=70,y=130)

#textbox - Entry text
fullname_entrytext = Entry(root)
fullname_entrytext.place(x=240,y=130)

#Email Label
email_label = Label(root, text="Email", bg="#e3e3e3")
email_label.place(x=70,y=180)

#textbox - Entry text
email_entrytext = Entry(root)
email_entrytext.place(x=240,y=180)

#Gender Label
gender_label = Label(root, text="Gender", bg="#e3e3e3")
gender_label.place(x=70,y=230)

#Radiobutton
#male_radiobutton

var = IntVar() #1 or 2 
male_radiobutton = Radiobutton(root, text="Male", value=1, variable = var ,bg="#e3e3e3")
male_radiobutton.place(x=235,y=230)

#female_radiobutton
female_radiobutton = Radiobutton(root, text="Female", value=2,  variable = var ,bg="#e3e3e3")
female_radiobutton.place(x=290,y=230)

#Country Label
country_label = Label(root, text="Country", bg="#e3e3e3")
country_label.place(x=70,y=280)

list_of_countries = ["India","Sri Lanka","Germany","Australia","Poland"]
temp = StringVar()
#Dropdown / Option menu - select country

country_optionmenu = OptionMenu(root, temp, *list_of_countries)
country_optionmenu.place(x=240,y=280)
temp.set("Select your country")

#Programming Label
programming_label = Label(root, text="Programming", bg="#e3e3e3")
programming_label.place(x=70,y=330)

#checkbutton - Programming
java= IntVar()
checkbutton_java = Checkbutton(root, text="Java", bg="#e3e3e3", onvalue=1, offvalue=0, variable=java)
checkbutton_java.place(x=230,y=330)

python= IntVar()
checkbutton_python = Checkbutton(root, text="Python", bg="#e3e3e3", onvalue=1, offvalue=0, variable= python)
checkbutton_python.place(x=290,y=330)

#Submit Button
button_submit = Button(root, text="Submit", command=click_submit_button)
button_submit.place(x=180,y=380)

#Dictionary method for changing attributes of button
button_submit["width"] = 20
button_submit["fg"] = "white"
#windows users
button_submit["bg"] = "#761515"

#start the app / run
root.mainloop()

