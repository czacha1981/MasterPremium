import streamlit as st

# Lista tablic rejestracyjnych
registration_numbers = [
[
    "ZS 742LE (BUS MERCEDES) biały  21          ",
    "ZS 604PS (MAN) biały 2015   59          ",
    "ZS 881MX (MAN) niebieski 2014  54        ",
    "ZS 395MR (MAN) złoty 2013  57               ",
    "ZS 078PN (MAN) biały 2015   57         ",
    "ZS 724NY (MAN) biały 2014    59         ",
    "ZS 607PS (MAN) biały 2016    57        ",
    "ZS 079PN (MAN) biały 2015    57        ",
    "ZS 396MR (MAN) srebrny 2014 57        ",
    "ZS 102UC (MAN) biały 2024     61      ",
    "ZS 263LU (MAN) biały 2015      55        ",
    "ZS 724NY (MAN) biały 2014      59      ",
    "ZS 856PP (SETRA) żółty 2006   70     ",
    "ZS 869MW (MAN) czarny 2013 59     ",
    "ZS 808HE (VOLVO) biały 2017   63     ",
    "ZS 024MV (MAN) żółty 2014     57      ",
    "ZS 105MX (MAN) czarny 2013   59       ",
    "ZS 846MJ (MAN) czarny 2013   57       ",
    "ZS 913PM (MAN) biały 2014      54         ",
    "ZS 912PM (MAN) biały 2014      59        ",
    "ZS 974KN (MAN) biały 2018       51        ",
    "ZS 101UC (MAN) biały 2024      61         ",
    "ZS 103UC (MAN) biały 2024      61         ",
    "ZS 895PS (MAN) biały 2014      54            ",
    "ZS 745LE (Mercedes) 2019   21             ",
    "ZS 920NP (Neoplan) ",
    "ZST 77194 (Setra)",
    "ZS 180PF",
    "ZS 025MV",
    "ZS 871MW",
    "ZS 846MJ",
    "ZS 741LE",
    "ZS 856PP",
    "ZS 749PM",
    "ZS 498LM",
    "ZS 736LE",
    "ZS 102UC (MAN) biały 2024     61      ",
    "ZS 263LU (MAN) biały 2015      55        ",
    "ZS 724NY (MAN) biały 2014      59      ",
    "ZS 856PP (SETRA) żółty 2006   70     ",
    "ZS 869MW (MAN) czarny 2013 59     ",
    "ZS 808HE (VOLVO) biały 2017   63     ",
    "ZS 024MV (MAN) żółty 2014     57      ",
    "ZS 105MX (MAN) czarny 2013   59       ",
    "ZS 846MJ (MAN) czarny 2013   57       ",
    "ZS 913PM (MAN) biały 2014      54         ",
    "ZS 912PM (MAN) biały 2014      59        ",
    "ZS 974KN (MAN) biały 2018       51        ",
    "ZS 101UC (MAN) biały 2024      61         ",
    "ZS 103UC (MAN) biały 2024      61         ",
    "ZS 895PS (MAN) biały 2014      54            ",
    "ZS 745LE (Mercedes) 2019   21             ",
    "ZS 920NP (Neoplan) ",
    "ZST 77194 (Setra)",
    "ZS 845MJ",
    "DWR9201H",
    "ZS606PS",
    "ZS608PS",
    "ZS741LE",
    "ZS 749PM",
    "ZS498LM",
    "ZST9327A",
]

# Lista relacji autobusów
bus_routes = [
    "Centrum Pomorzany", "Pogodno Gumieńce", "Niebuszewo", "Police", "Dąbie"
]

# Funkcja aplikacji Streamlit
def app():
    # Tytuł aplikacji
    st.title("MASTER PREMIUM")

    # Sprawdzamy, czy istnieje lista w session_state, jeśli nie, to ją inicjujemy
    if 'selected_items' not in st.session_state:
        st.session_state.selected_items = []

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
    if st.button('Dodaj do listy'):
        # Dodanie do session_state
        new_entry = f"Tablica rejestracyjna: {registration_choice}, Relacja autobusu: {bus_route_choice}, Liczba pasażerów: {passengers_count}, Godzina: {time_choice}"
        st.session_state.selected_items.append(new_entry)
        st.success("Dodano do listy!")

    # Wyświetlanie listy wyborów
    if st.session_state.selected_items:
        st.subheader("Twoja lista wyborów:")
        for idx, item in enumerate(st.session_state.selected_items, start=1):
            st.write(f"{idx}. {item}")

    # Opcja zapisu do pliku tekstowego
    if st.session_state.selected_items:
        st.download_button(
            label="Pobierz listę jako plik tekstowy",
            data="\n".join(st.session_state.selected_items),
            file_name="wybory.txt",
            mime="text/plain"
        )

# Uruchomienie aplikacji
if __name__ == "__main__":
    app()
