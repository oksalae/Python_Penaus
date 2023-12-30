"""Wget on Linux systems or Certutil on Windows are useful tools to download files.

Python can also be used for the same purpose. """

import requests

# Määritellään ladattavan tiedoston URL-osoite.
# Tässä esimerkissä ladataan PSTools-paketti, joka sisältää PSexec-työkalun.
url = 'https://download.sysinternals.com/files/PSTools.zip'

# Tehdään HTTP GET -pyyntö annettuun URL-osoitteeseen.
# 'allow_redirects=True' sallii HTTP-uudelleenohjaukset, jos sellaisia esiintyy.
# Tämä on tärkeää, koska jotkut palvelimet ohjaavat pyynnöt uudelle URL-osoitteelle.
r = requests.get(url, allow_redirects=True)

# Avataan (tai luodaan) tiedosto 'PSTools.zip' kirjoitustilassa ('wb') ja kirjoitetaan siihen vastauksen sisältö.
# 'wb' eli 'write binary' -tila on tärkeä, koska ladattava tiedosto on pakattu ja sisältää binääridataa.
open('PSTools.zip', 'wb').write(r.content)

# Ladattu tiedosto 'PSTools.zip', joka sisältää PSexec-työkalun, lisätään 'FilesDownloaded.txt'-tiedostoon.
# Käytetään 'a' (append) tilaa, joka takaa, että tiedosto ei ylikirjoita olemassa olevaa sisältöä,
# vaan lisää uuden rivin tiedoston loppuun.
with open("FilesDownloaded.txt", "a") as file:
    file.write(url + "\n")
