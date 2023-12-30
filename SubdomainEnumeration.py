""" Finding subdomains used by the target organization is an effective way to increase the attack surface and discover more vulnerabilities.

The script will use a list of potential subdomains and prepends them to the domain name provided via a command-line argument.

The script then tries to connect to the subdomains and assumes the ones that accept the connection exist. """


# Käyttö: python3 SubdomainEnumeration.py 192.168.1.1


# Tuo requests-kirjaston käyttöön verkkopyyntöjen tekemiseen, kuten HTTP GET -pyyntöjen lähettämiseen.
import requests 
# Tuo sys-moduulin käyttöön, jota käytetään komentoriviparametrien lukemiseen, esimerkiksi skriptille annettujen syötteiden käsittelyyn.
import sys 


# Avataan tiedosto 'subdomains.txt' ja luetaan sen sisältö.
sub_list = open("wordlist.txt").read()

# Jaetaan tiedoston sisältö riveiksi ja tallennetaan ne 'subdoms'-listaan.
subdoms = sub_list.splitlines()

# Avataan (tai luodaan) tiedosto 'Subdomainit.txt' kirjoitustilassa.
with open("Subdomainit.txt", "w") as file:
    # Käydään läpi 'directories'-listan alkiot.
    for dir in directories:
        dir_enum = f"http://{sys.argv[1]}/{dir}.html"
        r = requests.get(dir_enum)

        if r.status_code != 404:
            # Kirjoitetaan voimassa olevan kansion URL tiedostoon.
            file.write(dir_enum + "\n")
            # Voit myös tulostaa sen näytölle, jos haluat.
            print("Valid directory:", dir_enum)


