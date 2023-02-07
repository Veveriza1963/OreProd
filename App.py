# Creo lista tabelle per combo box
ListaTab = []
def CreaListaTab():
    for Index in range(1, 21):
        if Index in [15, 16, 17]:
            continue
        ListaTab.append(f"P{str(Index)}")

    return ListaTab

# Ritorna numero rispetto mese #
def NumeroMese(Mese):
    MeseNumero = {
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
    return MeseNumero[Mese]