import streamlit as st

# Lista tablic rejestracyjnych (usunąłem duplikaty)
registration_numbers = sorted(set([
    "ZS 742LE (BUS MERCEDES) biały - miejsc 21",
    "ZS 604PS (MAN) biały 2015 - miejsc 59",
    "ZS 881MX (MAN) niebieski 2014 - miejsc 54",
    "ZS 395MR (MAN) złoty 2013 - miejsc 57",
    "ZS 078PN (MAN) biały 2015 - miejsc 57",
    "ZS 607PS (MAN) biały 2016 - miejsc 57",
    "ZS 079PN (MAN) biały 2015 - miejsc 57",
    "ZS 396MR (MAN) srebrny 2014 - miejsc 57",
    "ZS 102UC (MAN) biały 2024 - miejsc 61",
    "ZS 263LU (MAN) biały 2015 - miejsc 55",
    "ZS 724NY (MAN) biały 2014 - miejsc 59      ",
    "ZS 856PP (SETRA) żółty 2006 - miejsc 70",
    "ZS 869MW (MAN) czarny 2013 - miejsc 59",
    "ZS 808HE (VOLVO) biały 2017 - miejsc 63",
    "ZS 024MV (MAN) żółty 2014 - miejsc 57",
    "ZS 105MX (MAN) czarny 2013 - miejsc 59",
    "ZS 846MJ (MAN) czarny 2013 - miejsc 57",
    "ZS 913PM (MAN) biały 2014 - miejsc 54",
    "ZS 912PM (MAN) biały 2014 - miejsc 59",
    "ZS 974KN (MAN) biały 2018 - miejsc 51",
    "ZS 101UC (MAN) biały 2024 - miejsc 61",
    "ZS 103UC (MAN) biały 2024 - miejsc 61",
    "ZS 895PS (MAN) biały 2014 - miejsc 54",
    "ZS 745LE (Mercedes) 2019 - miejsc 21",
    "ZS 920NP (Neoplan) 2013 - miejsc 59",
    "ZST 77194 (Setra) 2009 - miejsc 52",
    "ZS 180PF (BOVA) 2007 - miejsc 59",
    "ZS 025MV (MAN) 2014 - miejsc 57",
    "ZS 871MW (MAN) 2013 - miejsc 59",
    "ZS 741LE (POLSTER) 2019 - miejsc 21",
    "ZS 749PM (MAN) 2015 - miejsc 57",
    "ZS 498LM (MAN) 2013 - miejsc 57",
    "DWR 9201H (MAN) 2020 - miejsc 57",
    "ZS 606PS (NEOPLAN) 2014 - miejsc 59",
    "ZST 9327A (IRISBUS) 2007 - miejsc 62",
    "ZS716NY (SETRA) 2010 - miejsc 80",
    "ZST47407 (MAN) 2006 - miejsc 59",
    "ZS 897PS (NEOPLAN) 2014 - miejsc 55",
    "ZS 972KN (MAN) 2018 - miejsc 52",
]))

# Lista relacji autobusów
bus_routes = ["Centrum Pomorzany", "Pogodno Gumieńce", "Niebuszewo", "Police", "Dąbie"]

# Sprawdzamy, czy istnieje lista w session_state, jeśli nie, to ją inicjujemy
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# Tytuł aplikacji
st.title("MASTER PREMIUM")

# Wybór tablicy rejestracyjnej
st.subheader("Wybierz numer rejestracyjny:")
registration_choice = st.selectbox("Tablica rejestracyjna", registration_numbers)

# Wybór relacji autobusów
st.subheader("Wybierz relację autobusu:")
bus_route_choice = st.selectbox("Relacja autobusu", bus_routes)

# Wybór liczby pasażerów
st.subheader("Wybierz liczbę pasażerów:")
passengers_count = st.slider("Liczba pasażerów", min_value=1, max_value=100, step=1)

# Wybór godziny przyjazdu/odjazdu
st.subheader("Wybierz godzinę przyjazdu/odjazdu:")
time_choice = st.time_input("Czas", value=None)

# Przycisk do dodania wyborów do listy
if st.button("Dodaj do listy"):
    new_entry = f"{len(st.session_state.selected_items) + 1}. {registration_choice} | Relacja: {bus_route_choice} | Pasażerowie: {passengers_count} | Godzina: {time_choice}"
    st.session_state.selected_items.append(new_entry)
    st.success("Dodano do listy!")

# Wyświetlanie listy wyborów
if st.session_state.selected_items:
    st.subheader("Twoja lista wyborów:")
    
    # Wyświetlanie listy w formie ponumerowanej
    for idx, item in enumerate(st.session_state.selected_items, start=1):
        st.write(f"{idx}. {item}")

    # Opcja usunięcia ostatniego wpisu
    if st.button("Usuń ostatni wpis"):
        st.session_state.selected_items.pop()
        st.experimental_rerun()

    # Opcja usunięcia wszystkich wpisów
    if st.button("Wyczyść listę"):
        st.session_state.selected_items = []
        st.experimental_rerun()

    # Opcja zapisu do pliku tekstowego
    file_content = "\n".join(st.session_state.selected_items)
    st.download_button(
        label="Pobierz listę jako plik tekstowy",
        data=file_content,
        file_name="lista_autobusów.txt",
        mime="text/plain"
    )
    
