NetCat_Replacer.py

# Kirjastojen tuonti
import sys
import socket
import getopt
import threading
import subprocess

# Globaalien muuttujien alustus
# Nämä muuttujat määrittävät ohjelman toimintatilan
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# Funktio ohjelman käytön ohjeiden näyttämiseen
def usage():
    print("BHP Net Tool")
    # Tässä kohtaa tulostetaan ohjelman käyttöohjeet
    # Esimerkiksi miten ohjelmaa käytetään, mitä parametreja se ottaa vastaan
    sys.exit(0)

# Pääfunktio, joka käsittelee komentoriviparametreja
def main():
    global listen, port, execute, command, upload_destination, target

    # Jos komentoriviparametreja ei ole annettu, näytetään ohjeet
    if not len(sys.argv[1:]):
        usage()

    # Käsitellään komentoriviltä saadut parametrit
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # Käydään läpi kaikki parametrit ja asetetaan globaalit muuttujat niiden perusteella
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)

    # Tarkistetaan, toimitaanko asiakkaana vai palvelimena
    if not listen and len(target) and port > 0:
        # Luetaan puskuri standardisyötteestä ja lähetetään se
        buffer = sys.stdin.read()
        client_sender(buffer)

    # Jos ollaan palvelintilassa, käynnistetään palvelin
    if listen:
        server_loop()

# Asiakaspuolen lähetysfunktio
def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Yhdistetään määritettyyn kohteeseen
        client.connect((target, port))

        # Lähetetään data, jos sitä on
        if len(buffer):
            client.send(buffer)

        while True:
            # Odota vastausta ja prosessoi sitä
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print(response)

            # Odota lisää syötettä
            buffer = raw_input("")
            buffer += "\n"
            client.send(buffer)

    except:
        print("[*] Poikkeus! Poistutaan.")
        client.close()

# Palvelinpuolen kuuntelufunktio
def server_loop():
    global target

    # Jos kohdetta ei ole määritetty, kuunnellaan kaikkia liittymiä
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # Käynnistä säie asiakkaan käsittelyä varten
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

# Suoritettavan komennon käsittelyfunktio
def run_command(command):
    command = command.rstrip()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Komennon suoritus epäonnistui.\r\n"

    return output

# Palvelimen asiakkaan käsittelyfunktio
def client_handler(client_socket):
    global upload
    global execute
    global command

    # Tarkistetaan, onko tiedoston lähetys pyydetty
    if len(upload_destination):
        # Tallenna vastaanotettu data tiedostoon
        file_buffer = ""

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send("Tiedosto tallennettu kohteeseen %s\r\n" % upload_destination)
        except:
            client_socket.send("Tiedoston tallennus epäonnistui %s\r\n" % upload_destination)

    # Suoritetaan annettu komento
    if len(execute):
        output = run_command(execute)
        client_socket.send(output)

    # Jos komentotulkki on pyydetty, käynnistetään se
    if command:
        while True:
            # Näytä kehote
            client_socket.send("<BHP:#> ")

            # Odota syötettä kunnes rivinvaihto tapahtuu
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            # Suorita komento ja lähetä vastaus takaisin
            response = run_command(cmd_buffer)
            client_socket.send(response)

# Ohjelman käynnistys
if __name__ == "__main__":
    main()
