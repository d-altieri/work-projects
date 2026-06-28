#Ideal ticket structure
# Site ID - Sector # - Technologies(priority) - Alarm


#Prompt for sector

sector = input("Provide sector ID: \n")

if sector == "1":
    sector = "Sector 1"
if sector == "2":
    sector = "Sector 2"
if sector == "3":
    sector = "Sector 3"
if sector == "4":
    sector = "Sector 4"
if sector == "5":
    sector = "Sector 5"
if sector == "6":
    sector = "Sector 6"
if sector == "7":
    sector = "Sector 7"
if sector == "8":
    sector = "Sector 8"
if sector == "9":
    sector = "Sector 9"
if sector == "all":
    sector = "All Sectors"
if sector == "p":
    sector = "PICO"

#Prompt for brand of equipment

brand = input("\nBrand: \n1) Ericsson\n2) Nokia\n")

if brand == "1":
    brand = "Ericsson"
if brand == "2":
    brand = "Nokia"


#Prompt for node name
node_name = input("\nEnter affected node name:\n")


#Prompt for affected technologies

tech_answer = input("\nAffected technologies: \n")

if tech_answer == "all":
    tech_answer = "All Technologies"


#Prompt for priority

priority = input("\nSelect outage priority: \n2) Service Impacting\n3) Service Degraded\n4) Non-service Impacting\n")

if priority == "2":
    priority = "Down"
    severity = "SI"
if priority == "3":
    priority = "Degraded"
    severity = "SI"
if priority == "4":
    priority = "Non-service impacting"
    severity = "NSI"


#Prompt for presenting alarm

alarm = input("\nAlarm: Press enter for manual entry\n\n1) Heartbeat Failure\n2) Input Power Failure\n3) NE3SWS AGENT NOT RESPONDING TO REQUESTS\n4) Link Failure\n5) No connection to unit\n")

if alarm == "1":
    alarm = "Heartbeat Failure"
if alarm == "2":
    alarm = "Input Power Failure"
if alarm == "3":
    alarm = "NE3SWS AGENT NOT RESPONDING TO REQUESTS"
if alarm == "4":
    alarm = "Link Failure"
if alarm == "5":
    alarm = "No connection to unit"
if alarm == "":
    alarm = input("Enter alarm title: \n")


#Creation of ticket title

print(f" - {severity} - {brand} - {node_name}", end=" - ")
print(f"{sector} - {tech_answer} {priority}", end=" - ")
print(f"{alarm}")

