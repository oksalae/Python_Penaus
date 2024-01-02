README.txt

Ohjeet Python-skriptien kompiloimiseksi suoritettaviksi tiedostoiksi PyInstallerin avulla

Tässä ohjeessa käytetään esimerkkinä keylogger.py tiedostoa. Voit soveltaa näitä ohjeita mihin tahansa Python-skriptiin samassa kansiosta.

Vaihe 1: PyInstallerin asennus

Ennen kuin aloitat, varmista, että sinulla on PyInstaller asennettuna. Jos se ei ole vielä asennettu, voit asentaa sen käyttämällä Pythonin paketinhallintaa (pip). Avaa komentorivi tai terminaali ja suorita seuraava komento:

bash

pip install pyinstaller

Vaihe 2: Skriptin kompiloiminen

    Avaa komentorivi tai terminaali.

    Siirry hakemistoon, jossa keylogger.py (tai muu kompiloitava skripti) sijaitsee.

    Suorita seuraava komento:

    bash

    pyinstaller --onefile --noconsole keylogger.py

    Tämä komento luo yhden suoritettavan tiedoston, joka sisältää kaikki tarvittavat riippuvuudet, ja estää konsoli-ikkunan avautumisen sovellusta suoritettaessa. Vaihtoehtoisesti voit jättää pois --onefile-parametrin, jolloin PyInstaller luo hakemiston, jossa suoritettava tiedosto ja kaikki riippuvuudet sijaitsevat.

Vaihe 3: Suoritettavan tiedoston käyttö

PyInstaller luo dist-nimisen hakemiston, joka sisältää kompiloidun suoritettavan tiedoston. Voit jakaa tämän tiedoston tai koko dist-hakemiston muille järjestelmille.

    Jos käytit --onefile-parametria, löydät yhden suoritettavan tiedoston dist-hakemistosta.
    Jos et käyttänyt --onefile-parametria, dist-hakemisto sisältää suoritettavan tiedoston lisäksi muita tarvittavia tiedostoja.

Lisähuomiot

    Kompiloitu suoritettava tiedosto toimii vain samantyyppisessä käyttöjärjestelmässä, jossa se on luotu (esim. Windowsissa luotu suoritettava toimii vain Windowsissa).
    Ole tietoinen mahdollisista turvallisuusriskeistä, kun jaat suoritettavia tiedostoja, erityisesti herkkien toimintojen, kuten näppäimistön seurannan, osalta.