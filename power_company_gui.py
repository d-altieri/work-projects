import tkinter as tk
import webbrowser

def submit():
    power_selection = listbox.get(listbox.curselection())
    for number in power_companies_sorted:
        if power_selection in power_companies_sorted[number]["name"]:
            webbrowser.open(power_companies_sorted[number]["url"])

window = tk.Tk()
window.geometry("400x450")
window.title("Power Check")


#Window layout
label = tk.Label(window, text="Power Company", font=("consolas", 16))
label.pack(padx=20, pady=5)

listbox = tk.Listbox(window)
listbox.pack(padx=20, pady=5)
listbox.config(width=50, height=20)

button = tk.Button(window, text="Submit", font=("consolas", 16) , command=submit)
button.pack()


#Power company information
power_companies = {
    1: {"name": "[FL] Florida Power and Light" , "url": "https://www.fplmaps.com/"},
    2: {"name": "[HN] Centerpoint" , "url": "https://tracker.centerpointenergy.com/map/texas/"},
    3: {"name": "[DA] Oncor" , "url": "https://stormcenter.oncor.com/"},
    4: {"name": "[TX] AEP" , "url": "https://www.aeptexas.com/outagemap/"},
    5: {"name": "[GA] GPC" , "url": "https://outagemap.georgiapower.com/external/default.html?hp=tm_po_view_outage_map?mnuOpco=GPC"},
    6: {"name": "[OH] AEP Ohio" , "url": "https://outagemap.aepohio.com/"},
    7: {"name": "[AL] APC", "url": "https://outagemap.alabamapower.com/"},
    8: {"name": "[AU] Austin Energy", "url": "https://outagemap.austinenergy.com/"},
    9: {"name": "[CH] ComEd", "url": "https://www.comed.com/outages/experiencing-an-outage/outage-map"},
    10: {"name": "[DE] DTE Energy", "url": "https://outage.dteenergy.com/map"},
    11: {"name": "[DN] Xcel Energy", "url": "https://www.outagemap-xcelenergy.com/outagemap/?state=CO"},
    12: {"name": "[FL] Duke Energy", "url": "https://outagemaps.duke-energy.com/#/current-outages/fl"},
    13: {"name": "[IA] MEC Outage Watch", "url": "https://www.midamericanenergy.com/OutageWatch/dsk.html"},
    14: {"name": "[IE] SCE", "url": "https://www.sce.com/outages-safety/outage-center/check-outage-status"},
    15: {"name": "[JK] JEA", "url": "https://www.jea.com/outage_center/outage_map/"},
    16: {"name": "[KC] Evergy", "url": "https://outagemap.evergy.com/?_ga=2.213755092.1320559232.1775947460-605485997.1775947459"},
    17: {"name": "[LA] LADWP", "url": "https://www.ladwp.com/outages/power-outage-map"},
    18: {"name": "[LA] PGE", "url": "https://pgealerts.alerts.pge.com/outage-tools/outage-map/"},
    19: {"name": "[LI] PSEG", "url": "https://mypowermap.psegliny.com/external/default.html"},
    20: {"name": "[MD] BGE", "url": "https://www.bge.com/outages/experiencing-an-outage/outage-map"},
    21: {"name": "[ML] We Energies", "url": "https://www.we-energies.com/OutageSummary/view/outagegrid"},
    22: {"name": "[MN] Xcel Energy", "url": "https://www.outagemap-xcelenergy.com/outagemap/?state=MN"},
    23: {"name": "[MO] Entergy", "url": "https://www.etrviewoutage.com/map?state=LA&_gl=1*1bb4n1u*_ga*OTk2MjMxMjEuMTY5NzQ4MDMyNw..*_ga_HK6YSZ6LT0*MTY5NzczMTY3Ni4yLjAuMTY5NzczMTY3Ni42MC4wLjA."},
    24: {"name": "[NE] Eversource", "url": "https://outagemap.eversource.com/external/default.html"},
    25: {"name": "[NJ] Con Edison", "url": "https://outagemap.coned.com/external/default.html"},
    26: {"name": "[NJ] Jersey Central", "url": "https://www.firstenergycorp.com/outages_help.html"},
    27: {"name": "[NJ] PSE&G Outage Map", "url": "https://outagecenter.pseg.com/external/default.html"},
    28: {"name": "[OK] PSO Outage Map", "url": "https://outagemap.psoklahoma.com/?_gl=1*xllkrf*_ga*MTc1MTQ2OTY3My4xNzc0ODIzNjEw*_ga_8TY18DQCWB*czE3NzQ4MjM2MDkkbzEkZzAkdDE3NzQ4MjM2MDkkajYwJGwwJGgw*_ga_NFK8JY5JH3*czE3NzQ4MjM2MDkkbzEkZzAkdDE3NzQ4MjM2MDkkajYwJGwwJGgw"},
    29: {"name": "[PO] PGE", "url": "https://portlandgeneral.com/outages/"},
    30: {"name": "[PX] SRP Power", "url": "https://myaccount.srpnet.com/power/MyAccount/Outages"},
    31: {"name": "[RI] RI Energy", "url": "https://outagemap.rienergy.com/"},
    32: {"name": "[SA] CPS Energy", "url": "https://outagemap.cpsenergy.com/"},
    33: {"name": "[SD] San Diego Gas & Electric", "url": "https://www.sdge.com/residential/customer-service/outage-center/outage-map"},
    34: {"name": "[SF] PG&E Outage Center", "url": "https://pgealerts.alerts.pge.com/outage-tools/outage-map/"},
    35: {"name": "[SL] Rocky Mountain Power", "url": "https://www.rockymountainpower.net/outages-safety.html"},
    36: {"name": "[NY] National Grid", "url": "https://outagemap.ny.nationalgridus.com/?_gl=1*abkr8d*_ga*MjYwNDcxMTYyLjE2OTg5NDk0Njk.*_ga_FH50R0D4B4*MTY5ODk0OTQ2OS4xLjAuMTY5ODk0OTQ2OS42MC4wLjA."},
    37: {"name": "[VA] Dominion Energy", "url": "https://istheservicedown.com/problems/dominion-energy/map"},
    38: {"name": "[VG] NV energy", "url": "https://www.nvenergy.com/outages-and-emergencies/view-current-outages"},
    39: {"name": "[PA] First Energy", "url": "https://outages-pa.firstenergycorp.com/"},
    40: {"name": "[PA] Penn Power", "url": "https://www.firstenergycorp.com/penn_power.html"},
    41: {"name": "[WA] PSE", "url": "https://www.pse.com/en/outage/outage-map"},
    #42: {"name": "", "url": ""},
    #43: {"name": "", "url": ""},
    #44: {"name": "", "url": ""},
    #45: {"name": "", "url": ""},
    #46: {"name": "", "url": ""},
    #47: {"name": "", "url": ""},
    #48: {"name": "", "url": ""},
    #49: {"name": "", "url": ""},
    #50: {"name": "", "url": ""}
}


power_companies_sorted = dict(sorted(power_companies.items(), key=lambda x: x[1]["name"], reverse=True))

for number, name in power_companies_sorted.items():
    listbox.insert(0, name["name"])

window.mainloop()

