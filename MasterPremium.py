import streamlit as st

# Lista tablic rejestracyjnych
registration_numbers = [
    "ZS 024MV", "ZS 025MV", "ZS 078PN", "ZS 079PN", "ZS 101UC", "ZS 102UC",
    "ZS 103UC", "ZS 105MX", "ZS 180PF", "ZS 263LU", "ZS 395MR", "ZS 396MR",
    "ZS 498LM", "ZS 604PS", "ZS 607PS", "ZS 607PS", "ZS 608PS", "ZS 724NY",
    "ZS 724NY", "ZS 736LE", "ZS 741LE", "ZS 742LE", "ZS 745LE", "ZS 749PM",
    "ZS 808HE", "ZS 846MJ", "ZS 846MJ", "ZS 856PP", "ZS 856PP", "ZS 869MW",
    "ZS 871MW", "ZS 881MX", "ZS 895PS", "ZS 912PM", "ZS 913PM", "ZS 920NP",
    "ZS 974KN", "ZST 77194"
]

# Lista relacji autobusów
bus_routes = [
    "Centrum Pomorzany",
    "Pogodno Gumieńce",
    "Niebuszewo",
    "Police",
    "Dąbie"
]

# Funkcja aplikacji Streamlit
def app():
    # Tytuł aplikacji
    st.title("Wybór autobusu i pasażerów")

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

    # Przycisk do dodania wyborów do listy
    if st.button('Dodaj do listy'):
        # Dodanie do session_state
        new_entry = f"Tablica rejestracyjna: {registration_choice}, Relacja autobusu: {bus_route_choice}, Liczba pasażerów: {passengers_count}"
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
       
