# subway-itinerary

Given a starting point and destination from the Istanbul Subway Stations, get the shortest itinerary between those two stations. 

This program uses A* Search algorithm in order to find the shortest path. Implementation details can be seen from the report.pdf

When you run the `main.py`, you will be prompted to enter your starting station and destination. Station names are case sensitive, it should exactly match to name given in the list below. 

Unfortunately, importing every station including the Metrobus, Tram, Suburban Trains, Funicular etc. would have been a time consuming process given that it requires manually labeling the coordinates each of these stations. Therefore, this program only works for the M1A, M1B, M[2-7] lines, full station list is presented below. 

To run;

`$	python3 Main.py`

Example output;

```
$	python3 Main.py
Please enter the name of your starting station:Darussafaka
Please enter the name of your ending station:Siteler
You have reached to your destination!
◉ {'M2'}: Darussafaka
 ○ {'M2'}: Ataturk Oto Sanayi
 ○ {'M2'}: ITU Ayazaga
 ○ {'M2'}: Sanayi Mahallesi
 ○ {'M2'}: 4. Levent
 ○ {'M6', 'M2'}: Levent
 ➲ Tranfer to {'M2'}
 ○ {'M2'}: Gayrettepe
 ○ {'M7', 'M2'}: Sisli Mecidiyekoy
 ➲ Tranfer to {'M7'}
 ○ {'M7'}: Caglayan
 ○ {'M7'}: Kagithane
 ○ {'M7'}: Nurtepe
 ○ {'M7'}: Alibeykoy
 ○ {'M7'}: Circir Mahallesi
 ○ {'M7'}: Veysel Karani Aksemsettin
 ○ {'M7'}: Yesilpinar
 ○ {'M7'}: Kazim Karabekir
 ○ {'M7'}: Yenimahalle
 ○ {'M7'}: Karadeniz Mahallesi
 ○ {'M7'}: Tekstilkent Giyimkent
 ○ {'M7'}: Oruc Reis
 ○ {'M7'}: Goztepe Mahallesi
 ○ {'M7', 'M3'}: Mahmutbey
 ➲ Tranfer to {'M3'}
 ○ {'M3'}: ISTOC
 ○ {'M3'}: Ikitelli Sanayi
 ○ {'M3'}: Turgut Ozal
◉ {'M3'}: Siteler

```



```
Station List:

Yenikapi
Aksaray
Emniyet-Fatih
Topkapi-Ulubatli
Bayrampasa Maltepe
Sagmalcilar
Kocatepe
Otogar
Terazidere
Davutpasa YTU
Merter
Zeytinburnu
Bakirkoy Incirli
Bahcelievler
Atakoy Sirinevler
Yenibosna
DTM Congress Center
Ataturk Airport
Esenler
Menderes
Ucyuzlu
Bagcilar Meydan
Kirazli Bagcilar
Haciosman
Darussafaka
Ataturk Oto Sanayi
ITU Ayazaga
Sanayi Mahallesi
4. Levent
Levent
Gayrettepe
Sisli Mecidiyekoy
Osmanbey
Taksim
Sishane
Halic
Vezneciler
Basaksehir Metrokent
Basak Konutlari
Siteler
Turgut Ozal
Ikitelli Sanayi
ISTOC
Mahmutbey
Yenimahalle
Kadikoy
Ayrilik Cesmesi
Acibadem
Unalan
Goztepe
Yenisahra
Kozyatagi
Bostanci
Kucukyali
Maltepe
Huzurevi
Gulsuyu
Esenkent
Hastane Adliye
Soganlik
Kartal
Yakacik Adnan Kahveci
Pendik
Tavsantepe
Uskudar
Fistikagaci
Baglarbasi
Altunizade
Kisikli
Bulgurlu
Umraniye
Carsi
Yamanevler
Cakmak
Ihlamurkuyu
Altinsehir
Imam Hatip Lisesi
Dudullu
Necip Fazil
Cekmekoy
Nispetiye
Etiler
Bogazici Universitesi Hisarustu
Caglayan
Kagithane
Nurtepe
Alibeykoy
Circir Mahallesi
Veysel Karani Aksemsettin
Yesilpinar
Kazim Karabekir
Karadeniz Mahallesi
Tekstilkent Giyimkent
Oruc Reis
Goztepe Mahallesi
```

