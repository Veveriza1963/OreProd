import PySimpleGUI as Sg
import DbContext as Db
import App

# Scelta Tema Grafico
Sg.theme("Dark")

# Elementi della Finestra
Layout = [
    # Riga 1 #
    [
        Sg.T("Tabella Selezionata:", pad=(0, 10), font="size 10"),
        Sg.Combo(App.CreaListaTab(), s=(10, 20), enable_events=True, readonly=True, k="CbxTabella", pad=10),
        Sg.T("Calcola Ore:", font="size 10", pad=(10, 10)),
        Sg.Combo(["2021", "2022", "2023", "2024", "2025", "2026"], k="CbxAnno", s=(20, 5),
                 pad=10, default_value="2023"),
        Sg.Combo(["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre",
                  "Ottobre", "Novembre", "Dicembre"], pad=10, s=(20, 12), default_value="Gennaio", k="CbxMese"),
        Sg.B("Visualizza", k="BtnVisualizza", pad=10),
        Sg.B("Registra", k="BtnRegistra", pad=10)
    ],
    # Riga 2 #
    [
        Sg.Table([], ["  Anno  ", "  Gen  ", "  Feb  ", "  Mar  ", "  Apr  ", "  Mag  ", "  Giu  ",
                      "  Lug  ", "  Ago  ", "  Sett  ", "  Ott  ", "  Nov  ", "  Dic  "],
                 k="Table", expand_x=True, font="size 12", background_color="white", text_color="black")
    ],
    # Riga 3 #
    [
        Sg.B("Exit (Ctrl + x)", k="Exit", s=20, pad=(0, 10))
    ],
    # Riga 4 Finestra
    [
        Sg.StatusBar("", k="Sbar", expand_x=True, justification="center", s=50)
    ],
]

# Creazione Finestra
Window = Sg.Window("Ore Produzione", Layout, return_keyboard_events=True, finalize=True)

# Connette al Database
if Db.Connect():
    Window["Sbar"].update("Connessione Database Ok")
else:
    Sg.popup_ok("Errore Connessione Database")

# Main Loop
while True:
    Event, Values = Window.read(timeout=100)
    if Event in (Sg.WINDOW_CLOSED, "Exit"):
        break

    if Event == "CbxTabella":
        Values["Table"] = Db.GetAllData(Values["CbxTabella"])
        Window["Table"].update(Values["Table"])

    if Event == "BtnVisualizza":
        MeseAnno = "%/" + App.NumeroMese(Values["CbxMese"]) +"/" + Values["CbxAnno"]
        Sg.popup_ok("Tempo Produzione Mese {}-{}: {} Ore".format(Values["CbxMese"], Values["CbxAnno"],
                                                             Db.CalcolaTempo(Values["CbxTabella"], MeseAnno)))

Window.close()
