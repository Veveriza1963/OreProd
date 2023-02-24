from datetime import date as Dt

# Creo lista tabelle per combo box
ListaTab = [f"P{str(I)}" for I in range(1, 21) if I not in [15, 16, 17]]

# Data di oggi #
Oggi = Dt.today()

# Ritorna numero rispetto mese #
MeseToNumero = {
    "Gennaio": "01",
    "Febbraio": "02",
    "Marzo": "03",
    "Aprile": "04",
    "Maggio": "05",
    "Giugno": "06",
    "Luglio": "07",
    "Agosto": "08",
    "Settembre": "09",
    "Ottobre": "10",
    "Novembre": "11",
    "Dicembre": "12",
}

# Ritorna mese rispetto numero #
NumeroToMese = {
        "01": "Gennaio",
        "02": "Febbraio",
        "03": "Marzo",
        "04": "Aprile",
        "05": "Maggio",
        "06": "Giugno",
        "07": "Luglio",
        "08": "Agosto",
        "09": "Settembre",
        "10": "Ottobre",
        "11": "Novembre",
        "12": "Dicembre",
}

# Ritorna colonna database #
Colonna = {
        "Gennaio": "Gen",
        "Febbraio": "Feb",
        "Marzo": "Mar",
        "Aprile": "Apr",
        "Maggio": "Mag",
        "Giugno": "Giu",
        "Luglio": "Lug",
        "Agosto": "Ago",
        "Settembre": "Sett",
        "Ottobre": "Ott",
        "Novembre": "Nov",
        "Dicembre": "Dic",
    }