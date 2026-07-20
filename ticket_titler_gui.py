import tkinter as tk

def generate_ticket_title():
    node_name = node_name_entry.get()
    alarm_label = alarm_entry.get()
    sector = sector_var.get()
    brand = brand_var.get()

    while True:
        technologies = []
        if tech_var1.get() == True:
            technologies.append(tech_checkbox1.cget("text"))
        if tech_var2.get() == True:
            technologies.append(tech_checkbox2.cget("text"))
        if tech_var3.get() == True:
            technologies.append(tech_checkbox3.cget("text"))
        if tech_var4.get() == True:
            technologies.append(tech_checkbox4.cget("text"))
        if tech_var5.get() == True:
            technologies.append(tech_checkbox5.cget("text"))
        break

    while True:
        if severity_var.get() == "Service Impacting":
            severity = "SI"
            condition = "Down"
        if severity_var.get() == "Service Degraded":
            severity = "SI"
            condition = "Degraded"
        if severity_var.get() == "Non-Service Impacting":
            severity = "NSI"
            condition = "Non-Service Impacting"
        break

    while True:
        if sector == "1" or sector == "2" or sector == "3" or sector == "4" or sector == "5" or sector == "6" or sector == "7" or sector == "8" or sector == "9":
            sector = f"Sector {sector_var.get()}"
        if sector == "All":
            sector = "All Sectors"
        break

    # Ticket title generation
    ticket_title = f"- {severity} - {brand} - {node_name} - {sector} - {' '.join(technologies)} {condition} - {alarm_label}"
    ticket_title_label.config(text=ticket_title)
    print(ticket_title)


# Main Window
root = tk.Tk()
root.title("Ticket Titler")
root.geometry("300x600")


### Input fields

# Dropdown for ticket severity
severity_label = tk.Label(root, text="Severity")
severity_var = tk.StringVar(value="Service Impacting")
severity_menu = tk.OptionMenu(root, severity_var, "Service Impacting", "Service Degraded", "Non-Service Impacting")
severity_menu.pack(padx=10, pady=10)

# Checkboxes for technology selection
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
tech_checkbox1.pack(anchor='w',padx=80)
tech_checkbox2.pack(anchor='w',padx=80)
tech_checkbox3.pack(anchor='w',padx=80)
tech_checkbox4.pack(anchor='e',padx=80)
tech_checkbox5.pack(anchor='e',padx=80)

# Brand of equipment selection
brand_var = tk.StringVar(root, value="Ericsson")
brand_menu = tk.OptionMenu(root, brand_var, "Ericsson", "Nokia")
brand_menu.pack(padx=10, pady=10)

# Checkboxes for technology selection
node_name_label = tk.Label(root, text="Node Name:")
node_name_label.pack()
node_name_entry = tk.Entry(root)
node_name_entry.pack()

# Dropdown for sector selection
sector_menu_label = tk.Label(root, text="Sector")
sector_menu_label.pack(padx=0, pady=5)
sector_var = tk.StringVar(root, value="1")
sector_menu = tk.OptionMenu(root, sector_var, "1", "2", "3", "4", "5", "6", "7", "8", "9", "All", "PICO")
sector_menu.pack()

# Prompt for alarm signature
alarm_label = tk.Label(root, text="Alarm:")
alarm_label.pack(padx=0, pady=5)
alarm_entry = tk.Entry(root, width=30)
alarm_entry.pack()


### Button and display for ticket title generation

# Generate button
generate_button = tk.Button(root, text="Generate Ticket Title", command=generate_ticket_title, width=30, height=2)
generate_button.pack(padx=60, pady=60)

# Ticket title display
ticket_title_label = tk.Label(root, text="")
ticket_title_label.pack()


root.mainloop()

