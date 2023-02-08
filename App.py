# Creo lista tabelle per combo box
ListaTab = []
def CreaListaTab():
    for Index in range(1, 21):
        if Index in [15, 16, 17]:
            continue
        ListaTab.append(f"P{str(Index)}")

    return ListaTab

# Ritorna numero rispetto mese #
def MeseToNumero(Mese):
    X = {
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
    return X[Mese]

# Ritorna mese rispetto numero #
def NumeroToMese(Mese):
    X = {
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
    return X[Mese]

# Ritorna colonna database #
def GetColonna(Mese):
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
    return Colonna[Mese]