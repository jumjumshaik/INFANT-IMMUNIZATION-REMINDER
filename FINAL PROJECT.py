#Importing modules
import smtplib
import tkinter as tk
from tkinter import messagebox
import re
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#Collecting the Baby info - name
Baby_name = input(str("Please enter baby name: "))

#Function for sending e-mail reminders
def send_an_email():

    #Collecting the Baby info - age
    Baby_age = Baby_age_entry.get()
    print(f"{Baby_name}'s age: ", Baby_age)

    #Figuring if given age is valid or not
    try:
        Baby_age = float(Baby_age)
    except ValueError:
        messagebox.showerror("INVALID AGE!", "Kindly enter a valid age (in months).")
        return

    #Collecting the Baby info - Parent email address
    Parent_email = Parent_email_entry.get()
    print("Sent email to: ", Parent_email)

    #Figuring if given email address is valid or not
    if not re.match(r"[^@]+@[^@]+\.[^@]+", Parent_email):
        messagebox.showerror("INVALID EMAIL!", "Kindly enter a valid email address.")
        return

    #Vaccination reminder message based on the baby age
    if Baby_age == 0:
        message = f"""Dear parents, it's time for your newborn baby {Baby_name}'s HepB vaccination .

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 1:
        message = f"""Dear parents, it's time for your 1 month old baby {Baby_name}'s HepB vaccination .

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 2:
        message = f"""Dear parents, it's time for your 2 months old baby {Baby_name}'s RV, DTap, Hib, PCV13, PCV15, IPV vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 3:
        message = f"""Dear parents, it's time for your 3 months old baby {Baby_name}'s RV, DTap, Hib, PCV13, PCV15, IPV vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 4:
        message = f"""Dear parents, it's time for your 4 months old baby {Baby_name}'s RV, DTap, Hib, PCV13, PCV15, IPV vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 6:
        message = f"""Dear parents, it's time for your 6 months old baby {Baby_name}'s RV, DTap, Hib, PCV13, PCV15, IPV, COVID-19, Flu vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 12:
        message = f"""Dear parents, it's time for your 12 months old baby {Baby_name}'s HepB, Hib, PCV13, PCV15, IPV, COVID-19, Flu, MMR, Varicella, HepA vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 15:
        message = f"""Dear parents, it's time for your 15 months old baby {Baby_name}'s HepB, DTap, Hib, PCV, IPV, COVID-19, Flu, MMR, Varicella vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    elif Baby_age == 18:
        message = f"""Dear parents, it's time for your 18 months old baby {Baby_name}'s HepB, DTaP, IPV, HepA vaccinations.

Note -
1. If your Child misses a shot recommended of their age, talk to your child's doctor as soon as possible to see when the missed shot can be given.
2.If your child has any medical conditions that put them at risk for infection (e.g., sickle cell, HIV infection, Cochlear implants) or travelling outside states, talk to your child's doctor about additional vaccines that they may need.
"""

    else:
        messagebox.showerror("OOPS!", "Please indicate the appropriate baby age in months for immunization.")
        return

    #Deciding on an email subject line
    email_subject = f"Gentle reminder : Baby {Baby_name}'s Vaccination Time"

    #Creating a multipart message to send both text and image
    msg = MIMEMultipart()
    msg['From'] = "shaikjumjum63@gmail.com"
    msg['To'] = Parent_email
    msg['Subject'] = email_subject

    #Attaching the text message to the email
    msg.attach(MIMEText(message))

    #Attaching the image to the email
    with open("mail_image.png", 'rb') as Jumjum:
        img_data = Jumjum.read()
    image = MIMEImage(img_data, name='baby.jpg')
    msg.attach(image)

    #Using SMTP server to send an email
    #Using default SMTP port - port 587
    server = smtplib.SMTP("smtp.gmail.com", 587)
    
    #Initiating secure connection using TLS protocol to prevent unauthorized access
    server.starttls()

    #Providing login credentials
    server.login("shaikjumjum63@gmail.com", "rzzkjqgnajivctha")

    #Sending the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    #Exiting the server
    server.quit()

    #Analyzing if an email sent or not
    messagebox.showinfo("HURRAY!", "The email reminder was successfully sent.")
    print("Email sent successfully")

#GUI

#Creating a new instance of tkinter
root = tk.Tk()

#Setting window's title with the baby name
root.title(f"Baby {Baby_name}'s Vaccination Reminder")

#Setting window's size
root.geometry("400x150")

#Creating label for baby's age
Baby_age_label = tk.Label(root, text= "Baby's Age (in months): ")

#Packing age widget into root window
Baby_age_label.pack()

#Creating a entry widget that allows user to enter the baby age in months
Baby_age_entry = tk.Entry(root)

#Packing widget into root window
Baby_age_entry.pack()

#Creating label for parent's email address
Parent_email_label = tk.Label(root, text = "Parent's Email address: ")

#Packing email address widget into root window
Parent_email_label.pack()

#Creating a entry widget that allows user to enter the parent's email address
Parent_email_entry = tk.Entry(root)

#Packing widget into root window
Parent_email_entry.pack()

#Creating button to send the vaccination reminder email
send_button = tk.Button(root, text = "Send Reminder", command = send_an_email)

#Packing button widget into root window
send_button.pack()

#Method that runs the main event loop of the tkinter window, until it's closed
root.mainloop()

