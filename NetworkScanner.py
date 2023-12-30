""" Simple ICMP (Internet Control Message Protocol) scanner to identify potential targets on the network. 
ICMP packets can be monitored or blocked as the target organization would not expect a regular user to “ping a server”. 
On the other hand, systems can be configured to not respond to ICMP requests. 
These are the main reasons why using the ARP (Address Resolution Protocol) to identify targets on the local network is more effective. """

# Scapy on Python-ohjelmointikielen kirjasto, jota käytetään verkkopakettien luomiseen, manipulointiin ja niiden vastaanottoon. Se mahdollistaa monipuolisen verkkoliikenteen käsittelyn ja analysoinnin, tarjoten toimintoja pakettien luomiseen, lähetys- ja vastaanottoprosesseihin sekä niiden sisällön tutkimiseen.
# apt install python3-scapy
from scapy.all import *

# Asetetaan verkon liittymä (network interface), jota käytetään pakettien lähettämiseen.
interface = "eth0"

# Määritellään IP-osoitealue, jolle ARP-pyyntöjä lähetetään. Tämä voi olla esim. paikallisen verkon alue.
ip_range = "10.10.X.X/24"

# Määritellään broadcast-MAC-osoite, joka tarkoittaa, että paketti lähetetään kaikille verkon laitteille.
broadcastMac = "ff:ff:ff:ff:ff:ff"

# Luodaan paketti, joka sisältää Ethernet-kehyksen (Ether) ja ARP-pyynnön (ARP).
# Ethernet-kehys määritellään käyttämällä broadcast-MAC-osoitetta kohteena (dst),
# ja ARP-pyyntö määritellään kysymään IP-osoitteita määritellyltä IP-alueelta (pdst).
packet = Ether(dst=broadcastMac)/ARP(pdst=ip_range)

# Lähetetään luotu paketti ja odotetaan vastauksia.
# 'srp' on funktio, joka lähettää ja vastaanottaa paketteja linkkikerroksella (Layer 2, esim. Ethernet).
# 'timeout=2' asettaa odotusajan 2 sekuntiin vastauksia varten.
# 'iface=interface' määrittelee, mitä verkkoliitäntää käytetään.
# 'inter=0.1' asettaa aikaviiveen pakettien lähettämisen välillä sekunneissa.
ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

# Avataan (tai luodaan) tiedosto 'NetworkScanner.txt' kirjoitustilassa.
with open("NetworkScanner.txt", "w") as file:
    # Käydään läpi kaikki vastaukset, jotka saatiin.
    for send, receive in ans:
        # Luodaan merkkijono, joka sisältää lähetetyn paketin lähettäjän MAC- ja IP-osoitteen.
        result = receive.sprintf(r"%Ether.src% - %ARP.psrc%")

        # Tulostetaan tulos terminaaliin.
        print(result)

        # Tallennetaan sama tieto tiedostoon.
        file.write(result + "\n")

