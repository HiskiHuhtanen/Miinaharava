import random
import datetime
import haravasto

tila = {
    "kentta": [],
    "vapaat": [],
    "miinoitus": False,
    "räjähdys": False,
    "vuorot" : 0,
    "aika" : 0
    }
tallennus = {"kentta": []
}
aloitus_tila = {"kentta" : []
}
lopetus_tila = {"kentta" : []
}

def piirra_aloituskentta():
    "Piirtää aloitusruudukon, jossa satunnainen kuva kolmesta mahdollisuudesta."
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.piirra_tekstia("MIINANTALLAAJA", 210, 500, vari=(255, 0, 0, 255))
    haravasto.piirra_tekstia("Paina mihin tahansa aloittaaksesi", 90, 400, vari=(255, 0, 0, 255))
    graafiikka_muuntuja = random.randint(1, 3)
    if graafiikka_muuntuja == 3:  #voisi tehdä loopilla, teen myöhemmin jos muistan
        haravasto.piirra_tekstia("8", 395, 250, vari=(255, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 345, 250, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 445, 250, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 345, 200, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 395, 200, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 395, 300, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 445, 200, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 445, 300, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 345, 300, vari=(0, 0, 0, 255), fontti="serif", koko=32)
    elif graafiikka_muuntuja == 2:
        haravasto.piirra_tekstia("3", 395, 250, vari=(0, 128, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 345, 250, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 445, 250, vari=(0, 0, 0, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 345, 200, vari=(0, 0, 0, 255), fontti="serif", koko=32)
    else:
        haravasto.piirra_tekstia("1", 395, 250, vari=(0, 0, 255, 255), fontti="serif", koko=32)
        haravasto.piirra_tekstia("X", 395, 200, vari=(0, 0, 0, 255), fontti="serif", koko=32)
    haravasto.aloita_ruutujen_piirto()
    for yrivi, rivi in enumerate(aloitus_tila["kentta"]):
        for xsarake, sarake in enumerate(rivi):
            haravasto.lisaa_piirrettava_ruutu(sarake, xsarake * 40, yrivi * 40)
            #40 on ruudun leveys ja piteys
    haravasto.piirra_ruudut()

def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for yrivi, rivi in enumerate(tila["kentta"]):
        for xsarake, sarake in enumerate(rivi):
            if sarake != "x":
                haravasto.lisaa_piirrettava_ruutu(sarake, xsarake * 40, yrivi * 40)
            else:
                haravasto.lisaa_piirrettava_ruutu(" ", xsarake * 40, yrivi * 40)
    haravasto.piirra_ruudut()
#jos sarake saa arvoksi "x", tehdään funktio parametrilla " ", muuten miinat paljastuu

def piirra_lopetus():
    "hävio ikkunan piirron määritelmä"
    haravasto.piirra_tekstia("ASTUIT MIINAAN :(", 100, 100, vari=(255, 0, 0, 255))
    haravasto.aloita_ruutujen_piirto()
    haravasto.piirra_ruudut()

def piirra_voitto():
    "voitto ikkunan piirron määritelmä"
    haravasto.piirra_tekstia("VOITIT PELIN :)", 100, 100, vari=(0, 255, 0, 255))
    haravasto.aloita_ruutujen_piirto()
    haravasto.piirra_ruudut()

def ruutu_kysely():
    """
    Kysyy pelaajalta leveyden, korkeuden ja miinat ja muodostaa niiden
    mukaisen pelikentän.
    """
    try:
        annettu_l = int(input("Valitse kentän leveys: "))
        if annettu_l < 1:
            print("Anna positiivinen kokonaisluku")
            return ruutu_kysely()
        annettu_k = int(input("Valitse kentän korkeus: "))
        if annettu_k < 1:
            print("Anna positiivinen kokonaisluku")
            return ruutu_kysely()
        annettu_m = int(input("Anna miinojen määrä: "))
        if annettu_m > annettu_l * annettu_k or annettu_m == annettu_l * annettu_k or annettu_m < 0:
            print("Virheellinen miinamäärä")
            return ruutu_kysely()
    except ValueError:
        print("Anna kokonaisnumero")
        return ruutu_kysely()
    return annettu_k, annettu_l, annettu_m

def kasittele_hiiri(xkor, ykor, painike, muokkausnpm):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä. 
    Ensimmäisellä inputilla sijoittaa miinat.
    """

    if tila["miinoitus"] is False:
        miinoita(tila["kentta"], tila["vapaat"], tila["miinat"], xkor//40, ykor//40)
        tila["miinoitus"] = True
        tila["aika"] = datetime.datetime.now() #aloitetaan ajan lasku ensimmäiseltä inputilla
    miinat = laske_miinat(xkor//40, ykor//40, tila["kentta"])
    if tila["räjähdys"] is False:
        if miinat == 0:
            tulvataytto(tila["kentta"], xkor // 40, ykor // 40)
        elif miinat == 1:
            tila["kentta"][ykor//40][xkor//40] = "1"
        elif miinat == 2:
            tila["kentta"][ykor//40][xkor//40] = "2"
        elif miinat == 3:
            tila["kentta"][ykor//40][xkor//40] = "3"
        elif miinat == 4:
            tila["kentta"][ykor//40][xkor//40] = "4"
        elif miinat == 5:
            tila["kentta"][ykor//40][xkor//40] = "5"
        elif miinat == 6:
            tila["kentta"][ykor//40][xkor//40] = "6"
        elif miinat == 7:
            tila["kentta"][ykor//40][xkor//40] = "7"
        elif miinat == 8: 
            tila["kentta"][ykor//40][xkor//40] = "8"
        tila["vuorot"] += 1
    if voitto_tarkistus():
        haravasto.lopeta()
        voitto()
    # käytetään //, koska ruudut 40x40 pixeliä. 
    #Eli painettaisiin kord 120,80 painetaan oikeasti ruutua (3,2)

def miinoita(miinakentta, miinoitettavat, miinalkm, alkux, alkuy):
    """
    Sijoittaa miinoja ja samalla poistaa mahdollisuuden sijoittaa uudestaan samaan kohtaan.
    """
    ensimmainen_ruutu = (alkux, alkuy)
    miinoitettavat.remove(ensimmainen_ruutu)
    for i in range(miinalkm):
        miinakohta = random.choice(miinoitettavat)
        miinoitettavat.remove(miinakohta)
        xkord, ykord = miinakohta
        miinakentta[ykord-1][xkord-1] = "x"

def tulvataytto(lista, xaloitus, yaloitus):
    """
    Merkitsee kentan olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """  
    tuntematon = " "
    turvallinen = "0"
    uusilista = [(xaloitus, yaloitus)]

    while uusilista:
        xaloitus, yaloitus = uusilista.pop(-1)
        if lista[yaloitus][xaloitus] == tuntematon:
            miinat = laske_miinat(xaloitus, yaloitus, lista) 
            #laske_miinat täällä, jotta tulvatäyttö ei mene liian pitkälle
            #Eli, katsotaan montako miinaa vieressä, jos on miinoja, ei tulvatäyttöä
            if miinat == 0 and tila["räjähdys"] is False:
                lista[yaloitus][xaloitus] = turvallinen 
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        xkord = xaloitus + i
                        ykord = yaloitus + j
                        if 0 <= xkord < len(lista[0]) and 0 <= ykord < len(lista):
                            if lista[ykord][xkord] == tuntematon:
                                uusilista.append((xkord, ykord))
            elif miinat > 0 and tila["räjähdys"] is False:
                lista[yaloitus][xaloitus] = str(miinat)
                 #muutetaan luku stringiksi, jotta se voidaan esittää graafisesti

def laske_miinat(valx, valy, huone_rakenne):
    """
Laskee annetussa ruudussa sen ympärillä olevat miinat ja palauttaa
niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
ole miinaa - jos on, sekin lasketaan mukaan.
"""
    miinat = 0
    korkeus = len(huone_rakenne)
    leveys = len(huone_rakenne[0])
#Otetaan range(-1,2) uusille kordinaateille, koska 3x3 gridi
# nii ympärillä olevan koordinaatti joka yhden pienempi tai suurempi
# -1  [ ][ ][ ]
#  0  [ ][x][ ]
#  1  [ ][ ][ ]
#     -1  0  1
    if huone_rakenne[valy][valx] == "x":
        tila["räjähdys"] = True
        haravasto.lopeta()
        havio()
    else:    
        for i in range(-1, 2):
            for j in range(-1, 2):
                xkord = valx + i
                ykord = valy + j
                if 0 <= xkord < leveys and 0 <= ykord < korkeus:
                    if huone_rakenne[ykord][xkord] == 'x':
                        miinat += 1
    return miinat

def havio():
    "havio ruudun piirto ja tiedostojen tallentaminen"
    lopetusaika = datetime.datetime.now()
    koko_aika = int((lopetusaika - tila["aika"]).total_seconds() // 60)
    haravasto.luo_ikkuna(600, 200)
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aseta_piirto_kasittelija(piirra_lopetus)
    haravasto.aseta_hiiri_kasittelija(sulje)
    haravasto.aloita()
    #Tallennuksessa kentta on väärin päin, joten tässä sitä käännettään oikein.
    tallennus["kentta"] = reversed(tila["kentta"])
    with open("tallaaja-tilastot.txt", "a") as tilastot:
        tilastot.write("\n")
        tilastot.write(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        tilastot.write("Häviö \n")
        tilastot.write(f"Peli kesti: {tila['vuorot']} vuoroa ja {koko_aika} minuuttia \n")
        tilastot.write("Pelikenttä \n")
        for rivi in tallennus["kentta"]:
            tilastot.write(f"{', '.join(rivi)}\n")

def voitto():
    "voitto ruudun piirto ja tilastojen tallentaminen"
    lopetusaika = datetime.datetime.now()
    koko_aika = int((lopetusaika - tila["aika"]).total_seconds() // 60)
    haravasto.luo_ikkuna(600, 200)
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aseta_piirto_kasittelija(piirra_voitto)
    haravasto.aseta_hiiri_kasittelija(sulje)
    haravasto.aloita()
    #Tallennuksessa kentta on väärin päin, joten tässä sitä käännettään oikein.
    tallennus["kentta"] = reversed(tila["kentta"])
    with open("tallaaja-tilastot.txt", "a") as tilastot:
        tilastot.write("\n")
        tilastot.write(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        tilastot.write("Voitto \n") 
        tilastot.write(f"Peli kesti: {tila['vuorot']} vuoroa ja {koko_aika} minuuttia \n")
        tilastot.write("Pelikenttä \n")
        for rivi in tallennus["kentta"]:
            tilastot.write(f"{', '.join(rivi)}\n")

def voitto_tarkistus():
    "Tutkii kentän tilaa. Jos tyhjiä ruutuja ei ole jäljellä, voitto on saavutettu."
    for rivi in tila["kentta"]:
        for ruutu in rivi:
            if ruutu == " ":
                return False
    return True

def sulje(x, y, nappi, modit):
    "Sulkee ruudun, vau"
    haravasto.lopeta()

def main(kentan_korkeus, kentan_leveys):
    "Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän."
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(kentan_leveys*40, kentan_korkeus*40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()

def aloitus():
    "Luo aloitus ruudun, joka sulkeutuu hiiren inputista"
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna()
    haravasto.aseta_piirto_kasittelija(piirra_aloituskentta)
    haravasto.aseta_hiiri_kasittelija(sulje)
    haravasto.aloita()
    valikko()

def valikko():
    "Tulostetaan pelin valikko ja tehdään kenttä kysely funktion perusteella"
    while True:
        print("Tervetuloa Miinantallaajaan!")
        print("Aloita Peli: A")
        print("Katso Tilastoja: T")
        print("Lopeta: L")
        valikko_valinta = input("Anna seuraava valinta: ").strip().lower()
        if valikko_valinta == "a":
            korkeus, leveys, miina = ruutu_kysely()
            tila["kentta"] = []
            peli_ruutu = []
            for i in range(korkeus):
                peli_ruutu.append([" "] * leveys)
            tila["kentta"] = peli_ruutu
            tila["miinat"] = miina
            tila["vapaat"] = [(x, y) for x in range(leveys) for y in range(korkeus)]
            tila["miinoitus"] = False
            tila["räjähdys"] = False
            tila["vuorot"] = 0
            main(korkeus, leveys)
        elif valikko_valinta == "t":
            tilastot()
        elif valikko_valinta == "l":
            break
        else:
            print("Virheellinen syöte")

def tilastot():
    "Printtaa aiemmat pelit terminaaliin"
    with open("tallaaja-tilastot.txt", "r") as tilastot:
        faktat = tilastot.read()
        print(faktat)

aloitus()
