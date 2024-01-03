
"""Yksinkertainen TCP-ohjelma, jota voidaan käyttää verkkopalveluiden testaamiseen, satunnaisdatan lähettämiseen, järjestelmän testaukseen (fuzzing) ja muihin tehtäviin erityisesti silloin, kun käytettävissä ei ole laajempia verkkotyökaluja tai ohjelmistokehitystyökaluja. """

import socket

# Kohde-isäntä ja portti määritellään.
# Tässä esimerkissä yhteys muodostetaan www.google.com-sivustolle, käyttäen HTTP:n oletusporttia 80.
target_host = "www.google.com"
target_port = 80

# Luodaan socket-objekti.
# AF_INET käytetään IPv4-osoitteiden kanssa, ja SOCK_STREAM määrittää, että käytetään TCP:tä.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ➊

# Muodostetaan yhteys määritettyyn isäntään ja porttiin.
# Tässä tapauksessa 'connect' ottaa tuplen, joka sisältää isäntänimen ja portin.
client.connect((target_host, target_port))  # ➋

# Lähetetään dataa palvelimelle.
# Tässä lähetetään yksinkertainen HTTP GET -pyyntö.
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())  # ➌

# Vastaanotetaan dataa palvelimelta.
# 'recv'-metodilla otetaan vastaan 4096 tavua dataa.
response = client.recv(4096)  # ➍

# Tulostetaan vastaanotettu vastaus.
# Vastaus on tavumuodossa, joten se voidaan tulostaa suoraan.
print(response.decode())
