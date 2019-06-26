## WS2812 LED Display

Dieses Repository beinhaltet Quelltextbeispiele für das 30x30 WS2812 
LED-Display, das wir auf der Maker Faire Berlin 2018 ausgestellt haben.

Die Ansteuerung fand mit Hilfe eines RaspberryPi 3 und der rpi_ws281x 
Library statt, die u.a. einen Python-Wrapper für die Adafruit NeoPixel 
Library bereitstellt.

Im Ordner ''makerfaire-demos'' findet ihr die beiden Python-Skripte, 
die wir während der Maker Faire haben laufen lassen.

### Wie man dieses Repository klont

Eventuell ist ein oder andere nicht mit den git submodules vertraut. 
Dieses Repository enthält jedoch eines - d.h. zum erfolgreichen klonen 
und benutzen des Repositories sind nach dem ``git clone`` Befehl auch 
die folgenden noch nötig:

```
git submodule init
git submodule update
```
