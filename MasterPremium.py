import streamlit as st

# Lista tablic rejestracyjnych
registration_numbers = [
    "ZS 024MV-2014", "ZS 025MV-2014", "ZS 078PN-2015", "ZS 079PN-2015", "ZS 101UC-2024",
    "ZS 102UC-2024", "ZS 103UC-2024", "ZS 105MX-2013", "ZS 180PF-2007", "ZS 263LU-2015",
    "ZS 395MR-2013", "ZS 396MR-2014", "ZS 498LM-2013", "ZS 604PS-2015", "ZS 607PS-2016",
    "ZS 608PS-2015", "ZS 724NY-2014", "ZS 736LE-2019", "ZS 741LE-2019", "ZS 742LE-2019",
    "ZS 745LE-2019", "ZS 749PM-2015", "ZS 808HE-2017", "ZS 845MJ-2013", "ZS 846MJ-2013",
    "ZS 856PP-2006", "ZS 869MW-2013", "ZS 871MW-2013", "ZS 881MX-2014", "ZS 895PS-2014",
    "ZS 912PM-2014", "ZS 913PM-2014", "ZS 920NP-2013", "ZS 974KN-2018", "ZST 77194-2009",
    "ZS716NY-2010"
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
