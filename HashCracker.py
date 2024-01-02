import hashlib

# Pyydetään käyttäjää antamaan sanalistan sijainti ja murrettava hash-arvo.
# Sanalista sisältää mahdolliset salasanat ja hash-arvo on salasanan tiivistearvo.
wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))

# Avataan annettu sanalistatiedosto lukemista varten.
# Käytetään 'with open' -rakennetta, mikä huolehtii tiedoston asianmukaisesta sulkemisesta.
with open(wordlist_location, 'r') as file:
    # Käydään läpi jokainen rivi tiedostossa.
    for line in file.readlines():
        # Poistetaan rivinvaihdot ja ylimääräiset välit, muunnetaan rivi bittijonoksi ja luodaan MD5-hash.
        hash_ob = hashlib.md5(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()

        # Tarkistetaan, vastaako hashattu arvo annettua hash-arvoa.
        if hashed_pass == hash_input:
            # Jos vastaavuus löytyy, tulostetaan löydetty salasana ja tallennetaan se tiedostoon.
            found_password = 'Found cleartext password! ' + line.strip()
            print(found_password)

            # Tallennetaan löydetty salasana tiedostoon "HashCracker.txt".
            with open("HashCracker.txt", "w") as output_file:
                output_file.write(found_password + "\n")
            
            # Lopetetaan skriptin suoritus.
            exit(0)

# Jos vastaavaa salasanaa ei löydy sanalistasta, tulostetaan viesti.
print("Password not found in wordlist.")
with open("HashCracker.txt", "a") as output_file:
    output_file.write("Password not found for hash: " + hash_input + "\n")
