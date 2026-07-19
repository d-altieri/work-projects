import tkinter as tk

def generate_ticket_title():
    # Get the values from the input fields
    node_name = node_name_entry.get()
    alarm_label = alarm_entry.get()

    # Generate the ticket title
    ticket_title = f"{(combined_tech_final)} {node_name}: {alarm_label}"
    ticket_title_label.config(text=ticket_title)

# Create the main window
root = tk.Tk()
root.title("Ticket Titler")
root.geometry("300x600")

### Create the input fields

#Dropdown for ticket severity
ticket_type_var = tk.StringVar(value="Severity")
ticket_type_menu = tk.OptionMenu(root, ticket_type_var, "Service Impacting", "Service Degraded", "Non-Service Impacting")
ticket_type_menu.pack(padx=10, pady=10)



#Checkboxes for technology selection
tech_var1 = tk.BooleanVar()
tech_var2 = tk.BooleanVar()
tech_var3 = tk.BooleanVar()
tech_var4 = tk.BooleanVar()
tech_var5 = tk.BooleanVar()
tech_checkbox1 = tk.Checkbutton(root, text="5G", variable=tech_var1)
tech_checkbox2 = tk.Checkbutton(root, text="2100", variable=tech_var2)
tech_checkbox3 = tk.Checkbutton(root, text="1900", variable=tech_var3)
tech_checkbox4 = tk.Checkbutton(root, text="700", variable=tech_var4)
tech_checkbox5 = tk.Checkbutton(root, text="600", variable=tech_var5)
tech_checkbox1.pack()
tech_checkbox2.pack()
tech_checkbox3.pack()
tech_checkbox4.pack()
tech_checkbox5.pack()


combined_tech = []
combined_tech_final = print(combined_tech)

if tech_var1.get() == True:
    combined_tech.append("5G")
if tech_var2.get() == True:
    combined_tech.append("2100")
if tech_var3.get() == True:
    combined_tech.append("1900")
if tech_var4.get() == True:
    combined_tech.append("700")
if tech_var5.get() == True:
    combined_tech.append("600")

#Checkboxes for technology selection
node_name_label = tk.Label(root, text="Node Name:")
node_name_label.pack()
node_name_entry = tk.Entry(root)
node_name_entry.pack()

alarm_label = tk.Label(root, text="Alarm:")
alarm_label.pack()
alarm_entry = tk.Entry(root)
alarm_entry.pack()

# Create the Generate button
generate_button = tk.Button(root, text="Generate Ticket Title", command=generate_ticket_title)
generate_button.pack()

# Create the label to display the generated ticket title
ticket_title_label = tk.Label(root, text="")
ticket_title_label.pack()

# Start the main event loop
root.mainloop()