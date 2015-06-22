# Transports publics parisiens
Librairie Python relative aux transports publics parisiens (métro, Vélib), utilisée dans le cadre d'un projet perso de domotique.
Les services implémentés utilisent la technique de web scraping via la librairie [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/).

## Disponibilité de Vélib à proximité
### Prérequis

* Installation de [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) :

```
pip install beautifulsoup4
```

* Installation de [Geopy](https://github.com/geopy/geopy) :

```
pip install geopy
```
### Exemples d'utilisation
* Vélibs disponibles autour du **10 rue d'Astorg** dans un rayon de 270 mètres (valeur par défaut)

```
$ ./dispo_velib.py -a "10 rue d'astorg, paris" -r 350
{
    "MIROMESNIL": 32,
    "PLACE ST AUGUSTIN": 18,
    "ROQUEPINE": 36,
    "SQUARE LOUIS XVI": 19
}
```

* Vélibs disponibles autour du **10 rue d'Astorg** dans un rayon de 400 mètres :

```
$ ./dispo_velib.py -a "10 rue d'astorg, paris" -r 400
{
    "MALESHERBES PASQUIER": 61,
    "MIROMESNIL": 25,
    "PLACE ST AUGUSTIN": 18,
    "ROME SAINT LAZARE": 8,
    "ROQUEPINE": 43,
    "SAINT AUGUSTIN": 1,
    "SQUARE LOUIS XVI": 26
}
```

## Horaires des prochains passages de métro
### Prérequis
* Installation de [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) :

```
pip install beautifulsoup4
```
### Exemples d'utilisation
* Prochains passages du métro : station **Pyramides**, ligne **14**


```
$ ./passages_metro.py -s pyramides -l 14
{
    "Direction : Olympiades": [
        "0 mn",
        "3 mn"
    ],
    "Direction : Saint-Lazare": [
        "1 mn",
        "4 mn"
    ]
}
```
* Liste des **L**ignes de métro

```
$ ./passages_metro.py -L
[
    {
        "1": {
            "icon": "http://www.ratp.fr/meteo/bundles/ratpmeteo/img/lines/metro/M1_normal.png?v2",
            "infos": "Trafic normal sur l'ensemble de la ligne."
        }
    },
  ...
]
``` 
* Liste des **S**tations du réseau métropolitain

```
$ ./passages_metro.py -S | more
[
    {
        "abbesses": "Abbesses"
    },
    {
        "alexandre dumas": "Alexandre Dumas"
    },
    {
        "alma marceau": "Alma-Marceau"
    },
  ...
]    
```
