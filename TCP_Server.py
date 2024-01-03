
import socket
import threading
import http.server
import socketserver

PORT = 8000

# Luodaan HTTPRequestHandler-luokka, joka laajentaa SimpleHTTPRequestHandleria.
# Tämä handler palvelee tiedostoja ja kansioita nykyisestä hakemistosta.
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Tässä voitaisiin lisätä lisää logiikkaa pyyntöjen käsittelyyn.
        # Oletuksena tämä näyttää nykyisen hakemiston tiedostot ja kansiot.
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Asetetaan HTTP-palvelin kuuntelemaan määriteltyä porttia.
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# Määritellään IP-osoite ja portti, joihin palvelin sitoutuu.
# "0.0.0.0" tarkoittaa, että palvelin hyväksyy yhteyksiä kaikista verkkoliitännöistään.
#bind_ip = "0.0.0.0"
#bind_port = 9999

# Luodaan uusi socket-olio, joka käyttää IPv4-osoitteita (AF_INET) ja TCP-yhteyksiä (SOCK_STREAM).
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sidotaan socket määriteltyyn IP-osoitteeseen ja porttiin.
#server.bind((bind_ip, bind_port))

# Asetetaan palvelin kuuntelemaan tulevia yhteyksiä.
# Parametri 5 määrittää maksimimäärän yhteyksiä, jotka voivat odottaa, jos palvelin on kiireinen.
#server.listen(5)

#print(f"[*] Listening on {bind_ip}:{bind_port}")

# Tämä funktio käsittelee yhteyden asiakkaaseen.
#def handle_client(client_socket):
    # Tulostetaan, mitä asiakas lähettää.
 #   request = client_socket.recv(1024)
  #  print(f"[*] Received: {request.decode()}")
#
    # Lähetetään vastaus takaisin asiakkaalle.
 #   client_socket.send(b"ACK!")
  #  client_socket.close()

# Pääsilmukka, joka odottaa asiakkaiden yhteyksiä.
#while True:
    # Hyväksytään tuleva yhteys.
  #  client, addr = server.accept()
 #   print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    # Luodaan ja käynnistetään säie (thread) asiakkaan datan käsittelyä varten.
#    client_handler = threading.Thread(target=handle_client, args=(client,))
 #   client_handler.start()
