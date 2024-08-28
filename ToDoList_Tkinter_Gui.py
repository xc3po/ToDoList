import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc
import sv_ttk
import datetime
"""
Logik
"""
rowCounter = 1
frames = {}
aufgaben = {}
daten = {}
staten = {}
buttonsEdit = {}
buttonsDelete = {}


def eintrag_erstellen(aufgabe, datum, status, fenster):
    global mainFrame, buttonAdd, rowCounter
    rowCounter += 1
    aufgabeText = aufgabe.get()
    datumText = datum.get()
    statusText = status.get()
    fenster.destroy()

    print(aufgabeText, datumText, statusText, rowCounter )

    buttonAdd.grid(row=rowCounter+1)

    frames[rowCounter] = ttk.Frame(mainFrame)
    frames[rowCounter].grid(row=rowCounter, column=0, sticky="nsew")

    aufgaben[rowCounter] = ttk.Label(mainFrame, text=aufgabeText, font=("Helvetica", 12), anchor="center")
    aufgaben[rowCounter].grid(row=rowCounter, column=0, sticky="nsew", pady=5, padx=5)
    daten[rowCounter] = ttk.Label(mainFrame, text=datumText, font=("Helvetica", 12), anchor="center")
    daten[rowCounter].grid(row=rowCounter, column=1, sticky="nsew", pady=5, padx=5)
    staten[rowCounter] = ttk.Label(mainFrame, text=statusText, font=("Helvetica", 12), anchor="center")
    staten[rowCounter].grid(row=rowCounter, column=2, sticky="nsew", pady=5, padx=5)
    buttonsEdit[rowCounter] = ttk.Button(mainFrame, text="Ändern", command=lambda r=rowCounter: ändere_zeile(r))
    buttonsEdit[rowCounter].grid(row=rowCounter, column=3, sticky="", pady=5, padx=5)
    buttonsDelete[rowCounter] = ttk.Button(mainFrame, text="Löschen", command=lambda r=rowCounter: lösche_Zeile(r))
    buttonsDelete[rowCounter].grid(row=rowCounter, column=4, sticky="", pady=5, padx=5)

    
def erstelle_Zeile():
    toplevelEingabe = tk.Toplevel(root)
    toplevelEingabe.title("Aufgabe Eingeben")
    toplevelEingabe.geometry("400x300")
    toplevelEingabe.columnconfigure(0, weight=1)
    toplevelEingabe.rowconfigure(0, weight=1)

    toplevelEingabe.grab_set() 
    toplevelEingabe.transient(root)

    toplevelEingabeFrame = ttk.Frame(toplevelEingabe)
    toplevelEingabeFrame.grid(column=0, row=0, sticky="nsew")
    toplevelEingabeFrame.columnconfigure(0, weight=1)
    toplevelEingabeFrame.columnconfigure(1, weight=1)

    labelTitle = ttk.Label(toplevelEingabeFrame, text="Aufgabe eingeben", font=("Helvetica", 24, "bold"), anchor="center")
    labelTitle.grid(row=0, column=0, sticky="nsew", pady=(20,30), columnspan=2)

    labelAufgabe = ttk.Label(toplevelEingabeFrame, text="Aufgabenname: ", anchor="center")
    labelAufgabe.grid(row=1, column=0, pady=5, padx=5)

    textAufgabe = ttk.Entry(toplevelEingabeFrame, width=30)
    textAufgabe.grid(row=1, column=1, pady=5, padx=5)

    labelDate = ttk.Label(toplevelEingabeFrame, text="Erledigt bis: ", anchor="center")
    labelDate.grid(row=2, column=0, pady=5, padx=5)

    dateEingabe = tkc.DateEntry(toplevelEingabeFrame, width=26, date_pattern="DD/MM/YYYY", mindate=datetime.date.today())
    dateEingabe.grid(row=2, column=1, pady=5, padx=5)

    labelStat = ttk.Label(toplevelEingabeFrame, text="Welche Priorität: ", anchor="center")
    labelStat.grid(row=3, column=0, pady=5, padx=5)
    
    comboStatus = ttk.Combobox(toplevelEingabeFrame, state="readonly", values=["Hohe Prio", "Mittlere Prio", "Keine Prio"], width=26)
    comboStatus.grid(row=3, column=1, pady=5, padx=5)

    buttonDone = ttk.Button(toplevelEingabeFrame, text="Erstellen" ,command=lambda: eintrag_erstellen(textAufgabe, dateEingabe, comboStatus, toplevelEingabe))
    buttonDone.grid(row=4, column=0, pady=5, padx=5, sticky="nsew")

    buttonCancel = ttk.Button(toplevelEingabeFrame, text="Abbrechen", command=lambda: toplevelEingabe.destroy())
    buttonCancel.grid(row=4, column=1, pady=5, padx=5, sticky="nsew")

def ändere_zeile(row):
    global frames, aufgaben, daten, staten, buttonsEdit, buttonsDelete
    
    toplevelEingabe = tk.Toplevel(root)
    toplevelEingabe.title("Aufgabe Bearbeiten")
    toplevelEingabe.geometry("400x300")
    toplevelEingabe.columnconfigure(0, weight=1)
    toplevelEingabe.rowconfigure(0, weight=1)

    toplevelEingabe.grab_set() 
    toplevelEingabe.transient(root)

    toplevelEingabeFrame = ttk.Frame(toplevelEingabe)
    toplevelEingabeFrame.grid(column=0, row=0, sticky="nsew")
    toplevelEingabeFrame.columnconfigure(0, weight=1)
    toplevelEingabeFrame.columnconfigure(1, weight=1)

    labelTitle = ttk.Label(toplevelEingabeFrame, text="Aufgabe bearbeiten", font=("Helvetica", 24, "bold"), anchor="center")
    labelTitle.grid(row=0, column=0, sticky="nsew", pady=(20,30), columnspan=2)

    labelAufgabe = ttk.Label(toplevelEingabeFrame, text="Aufgabenname: ", anchor="center")
    labelAufgabe.grid(row=1, column=0, pady=5, padx=5)

    # Lade den aktuellen Wert der Aufgabe
    textAufgabe = ttk.Entry(toplevelEingabeFrame, width=30)
    textAufgabe.grid(row=1, column=1, pady=5, padx=5)
    textAufgabe.insert(0, aufgaben[row].cget("text"))

    labelDate = ttk.Label(toplevelEingabeFrame, text="Erledigt bis: ", anchor="center")
    labelDate.grid(row=2, column=0, pady=5, padx=5)

    # Lade das aktuelle Datum
    current_date = daten[row].cget("text")
    dateEingabe = tkc.DateEntry(toplevelEingabeFrame, width=26, date_pattern="DD/MM/YYYY", mindate=datetime.date.today())
    dateEingabe.grid(row=2, column=1, pady=5, padx=5)
    dateEingabe.set_date(current_date)

    labelStat = ttk.Label(toplevelEingabeFrame, text="Welche Priorität: ", anchor="center")
    labelStat.grid(row=3, column=0, pady=5, padx=5)
    
    # Lade den aktuellen Status
    current_status = staten[row].cget("text")
    comboStatus = ttk.Combobox(toplevelEingabeFrame, state="readonly", values=["Hohe Prio", "Mittlere Prio", "Keine Prio"], width=26)
    comboStatus.grid(row=3, column=1, pady=5, padx=5)
    comboStatus.set(current_status)

    buttonDone = ttk.Button(toplevelEingabeFrame, text="Speichern", command=lambda: speichere_änderungen(row, textAufgabe, dateEingabe, comboStatus, toplevelEingabe))
    buttonDone.grid(row=4, column=0, pady=5, padx=5, sticky="nsew")

    buttonCancel = ttk.Button(toplevelEingabeFrame, text="Abbrechen", command=lambda: toplevelEingabe.destroy())
    buttonCancel.grid(row=4, column=1, pady=5, padx=5, sticky="nsew")

def speichere_änderungen(row, textAufgabe, dateEingabe, comboStatus, fenster):
    global aufgaben, daten, staten

    aufgabeText = textAufgabe.get()
    datumText = dateEingabe.get_date().strftime("%d/%m/%Y")
    statusText = comboStatus.get()

    aufgaben[row].config(text=aufgabeText)
    daten[row].config(text=datumText)
    staten[row].config(text=statusText)

    fenster.destroy()


def lösche_Zeile(row):
    global frames, aufgaben, daten, staten, buttonsEdit, buttonsDelete

    if row in frames:
        frames[row].destroy()  # Löscht den Frame und alle darin enthaltenen Widgets
        
        # Entferne die zugehörigen Einträge aus den Dictionaries
        if row in aufgaben:
            aufgaben[row].destroy()  # Optional: Löscht nur das Label-Widget, falls notwendig
            del aufgaben[row]
        if row in daten:
            daten[row].destroy()  # Optional: Löscht nur das Label-Widget, falls notwendig
            del daten[row]
        if row in staten:
            staten[row].destroy()  # Optional: Löscht nur das Label-Widget, falls notwendig
            del staten[row]
        if row in buttonsEdit:
            buttonsEdit[row].destroy()  # Optional: Löscht nur den Button, falls notwendig
            del buttonsEdit[row]
        if row in buttonsDelete:
            buttonsDelete[row].destroy()  # Optional: Löscht nur den Button, falls notwendig
            del buttonsDelete[row]

        # Optional: Button neu positionieren, wenn keine Zeilen mehr vorhanden sind

"""
GUI
"""

# Wurzelfenster (1 Column, 2 Rows)
root = tk.Tk()
root.title("To-Do List")
root.geometry("1280x720")
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)

# Textframe (1 Column, 2 Rows)
frameText = ttk.Frame(root)
frameText.grid(column=0, row=0, sticky="nsew")
# Gewichte
frameText.columnconfigure(0, weight=1)
frameText.rowconfigure(0, weight=0)
frameText.rowconfigure(1, weight=0)

# TaskFrame (2 Cols, 5 Rows + Dynamisch)
mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=1, sticky="nsew")
# Gewichte
mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.columnconfigure(0, weight=5)
mainFrame.columnconfigure(1, weight=2)
mainFrame.columnconfigure(2, weight=1)
mainFrame.columnconfigure(3, weight=1)
mainFrame.columnconfigure(4, weight=1)

# Headline und Subtitle für den Text Frame
labelHead = ttk.Label(frameText, text="Meine To-Do's", font=("Helvetica", 24, "bold"), anchor="center")
labelHead.grid(row=0, column=0, sticky="nsew", pady=(70,10))

labelSub = ttk.Label(frameText, text="Zieh es durch", font=("Helvetica", 16, "italic"), anchor="center")
labelSub.grid(row=1, column=0, sticky="nsew", pady=(0, 40))

# Überschriften für die Tasks (Aufgabe, Datum, Status, Editieren, Entfernen)
labelTask = ttk.Label(mainFrame, text="Aufgabe", font=("Helvetica", 12, "bold"), anchor="center")
labelTask.grid(row=0, column=0, sticky="nsew", pady=5)

labelDatum = ttk.Label(mainFrame, text="Erledigen bis", font=("Helvetica", 12, "bold"), anchor="center")
labelDatum.grid(row=0, column=1, sticky="nsew", pady=5)

labelStatus = ttk.Label(mainFrame, text="Status", font=("Helvetica", 12, "bold"), anchor="center")
labelStatus.grid(row=0, column=2, sticky="nsew", pady=5)

labelEdit = ttk.Label(mainFrame, text="Bearbeiten", font=("Helvetica", 12, "bold"), anchor="center")
labelEdit.grid(row=0, column=3, sticky="nsew", pady=5)

labelEntfernen = ttk.Label(mainFrame, text="Löschen", font=("Helvetica", 12, "bold"), anchor="center")
labelEntfernen.grid(row=0, column=4, sticky="nsew", pady=5)

# Button +, wenn keine To-Dos, oder weitere hinzufügen
buttonAdd = ttk.Button(mainFrame, text="Aufgabe hinzufügen", command=erstelle_Zeile)
buttonAdd.grid(row=1, column=0, sticky="nsew", columnspan=5, pady=(5, 0))


sv_ttk.set_theme("dark")
root.mainloop()

