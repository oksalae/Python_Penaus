import sys
import socket
#import pyfiglet

# Luodaan ja tulostetaan ASCII-banneri käyttäen pyfiglet-kirjastoa.
#ascii_banner = pyfiglet.figlet_format("Skannaa \n menemään")
#print(ascii_banner)

# Määritellään tutkittavan laitteen IP-osoite. Esimerkki alla
ip = '10.10.24.30' 
open_ports = [] 

# Määritellään porttien alue, joka skannataan. # 
ports = range(1, 65535)

#However, if you are looking for a specific service or want to save time by scanning a few common ports, the code could be changed as follows;
#ports = { 21, 22, 23, 53, 80, 135, 443, 445}

# Funktio, joka tutkii yksittäisen portin.
def probe_port(ip, port, result = 1): 
  try: 
    # Luodaan socket-objekti verkkoyhteyden muodostamiseen.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5)  # Asetetaan aikakatkaisu 0.5 sekuntiin.

    # Yritetään muodostaa yhteys annettuun IP-osoitteeseen ja porttiin.
    r = sock.connect_ex((ip, port))   
    if r == 0:  # arkastetaan, palauttaako connect_ex nollan, mikä tarkoittaa, että yhteys porttiin onnistui ja portti on auki. Jos funktio palauttaa jonkin muun kuin nollan, se indikoi, että portti on kiinni tai yhteyttä ei voitu muodostaa muusta syystä.
      result = r 
    sock.close()  # Suljetaan socket-objekti.
  except Exception as e: 
    pass 
  return result


# Avataan tiedosto tulosten tallentamiseen.
with open("PortScanner.txt", "w") as file:
  # Skannataan jokainen portti määritellyllä alueella.
  for port in ports: 
      sys.stdout.flush() #  kutsu tyhjentää tulostuspuskurin, joka varmistaa, että kaikki tulostus tulee näkyviin heti, kun se suoritetaan, erityisesti kun ohjelma suoritetaan pitkiä aikoja.
      response = probe_port(ip, port)  # Kutsutaan probe_port-funktiota jokaiselle portille. Tämä funktio palauttaa tuloksen siitä, onko portti auki vai kiinni.
      if response == 0:  # os portti on auki (eli probe_port palauttaa 0), portin numero lisätään open_ports-listaan ja kirjoitetaan tiedostoon merkkijonona "Port {port} is open\n".
          open_ports.append(port) 
          file.write(f"Port {port} is open\n")  # Kirjoitetaan auki oleva portti tiedostoon.

  # Tulostetaan lopputulokset.
  if open_ports: 
    print("Open Ports are: ") 
    print(sorted(open_ports)) 
    # Lisätään avoimet portit myös tiedostoon.
    file.write("Open Ports are:\n")
    file.write(str(sorted(open_ports)) + "\n")
  else: 
    print("Looks like no ports are open :(")
    file.write("Looks like no ports are open :(\n")