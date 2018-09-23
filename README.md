# snips.ai + OpenHAB2 + mqtt 

I started this Project to get my snips.ai voice controll 
to get work with my openHAB2 Items.

Snips.ai Apps:
* [Heater/Heizung](https://console.snips.ai/store/de/bundle_ZaVvk54e52rD) 
* More is coming

### Configuration

#### Devices and Rooms
You have to add the Items you want to use and tag them the right way.
##### Light:


    {
      "Wohnzimmer Stehlampe": {     << Name of item from openHAB2
        "type": "light",            << Type we use light or heater
        "room": "Wohnzimmer",       << Roomsource from list
        "light_source": "Stehlampe" << Lightsource from list
      }
    }
    
##### Heater:

    {
      "Wohnzimmer Stehlampe": {     << Name of item from openHAB2
        "type": "light",            << Type we use light or heater
        "room": "Wohnzimmer",       << Roomsource from list
      }
    }
    
##### Config for room and light_source
Lightsources we know:
* Leuchtturm
* Kerze
* Feuerwerk
* Fahrzeugbeleuchtung
* Flutlicht
* Lampe
* Positionslicht
* Laterne
* Lagerfeuer
* Stehlampe
* Nachttischlampe
* Deckenleuchte
* Schreibtischlampe
* Ambientlight
* Küchenlicht
* Leuchte
* Lichterkette

Rooms we know:
* Atrium
* Foyer
* Vestibül
* Büro
* Atelier
* Wintergarten
* Waschküche
* Galerie
* Aula
* Dachboden
* Leitstand
* Cella
* Kommandozentrale
* Konferenzraum
* Kesselhaus
* Speisekammer
* Sonderisolierstation
* Umkleideraum
* Esszimmer
* Monteurzimmer
* Wartehalle
* Keller
* Küche
* Arbeitszimmer
* Badezimmer
* Kinderzimmer
* Wohnzimmer
* Schlafzimmer
* Balkon
* Garten
* Garage
* Spielzimmer
* Esszimmer
* Abstellkammer
