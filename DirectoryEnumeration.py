""" Once subdomains have been discovered, the next step would be to find directories.

The following code will build a simple directory enumeration tool. """




# Tuo 'requests'-kirjaston käyttöön verkkopyyntöjen tekemiseen.
import requests 

# Tuo 'sys'-moduulin käyttöön, jota käytetään komentoriviparametrien lukemiseen.
import sys 


# Avaa tiedoston 'wordlist.txt', lukee sen sisällön ja sulkee tiedoston.
sub_list = open("wordlist.txt").read() 
# Jakaa tiedoston sisällön riveihin ja tallentaa ne 'directories'-listaan.
directories = sub_list.splitlines()


# Avaa (tai luo) tiedoston 'DirectoryEnumeration.txt' kirjoitustilassa.
with open("DirectoryEnumeration.txt", "w") as file:
    # Käy läpi jokainen 'directories'-listan alkio.
    for dir in directories:
        # Muodostaa URL-osoitteen käyttäen komentoriviltä saatua ensimmäistä argumenttia ja listan alkiota.
        dir_enum = f"http://{sys.argv[1]}/{dir}.html" 

        # Suorittaa HTTP GET -pyynnön muodostettuun URL-osoitteeseen.
        r = requests.get(dir_enum)

        # Tarkistaa, palauttaako pyyntö 404-vastauskoodin (sivua ei löydy).
        if r.status_code != 404: 
            # Jos vastauskoodi ei ole 404, tallentaa URL:n tiedostoon ja tulostaa sen terminaaliin.
            file.write(dir_enum + "\n")
            print("Valid directory:", dir_enum)

