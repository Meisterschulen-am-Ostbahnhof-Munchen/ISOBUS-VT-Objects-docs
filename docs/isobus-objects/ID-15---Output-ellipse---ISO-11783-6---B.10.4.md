# ID 15 – Output ellipse – ISO 11783-6 – B.10.4

```{index} single: ID 15 – Output ellipse – ISO 11783-6 – B.10.4
```

Das **Output Ellipse** Objekt mit der **ID 15** dient zum Zeichnen von Kreisen, Ellipsen sowie Kreisbögen, Segmenten und Sektoren (Tortendiagramm-Stücke).

### Attribute und Record Format (Tabelle B.31)

Die folgende Tabelle beschreibt den Aufbau des Output Ellipse Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 15 | 3 | Objekttyp = Ellipse. |
| [1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Objekt-ID eines Line Attributes Objekts (für den Umriss). |
| [2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Breite des umschließenden virtuellen Rechtecks. |
| [3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Höhe des umschließenden virtuellen Rechtecks. |
| [4] | **Ellipse type** | Integer | 1 | 0 – 3 | 10 | 0=Closed Ellipse, 1=Open Ellipse (Bogen), 2=Segment (Sehne), 3=Sector (Tortestück). |
| [5] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [6] | **End angle** | Integer | 1 | 0 – 180 | 12 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [7] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 13 – 14 | Objekt-ID eines Fill Attributes Objekts (für die Füllung) oder NULL für keine Füllung. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 15 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Ellipsentypen und Geometrie
Die Ellipse wird in ein virtuelles Rechteck (`Width` x `Height`) eingepasst.

*   **Closed Ellipse (0):** Eine vollständige Ellipse oder ein Kreis (wenn Width = Height).
*   **Open Ellipse (1):** Nur der Bogen zwischen Start- und Endwinkel wird gezeichnet.
*   **Segment (2):** Ein Kreisabschnitt (die Sehne zwischen den Winkelpunkten wird geschlossen).
*   **Sektor (3):** Ein Kreisausschnitt (die Winkelpunkte werden mit dem Mittelpunkt verbunden, ideal für Tortendiagramme).

## Winkelberechnung (Wichtig!)
Die Winkelwerte in AID 5 und 6 werden **halbiert** übertragen (Bereich 0-180 entspricht 0-360°).
*   **90° (Oben):** Wert 45
*   **180° (Links):** Wert 90
*   **270° (Unten):** Wert 135

**Besonderheit bei skalierten Ellipsen:** Wenn die Ellipse kein Kreis ist (Width != Height), muss das VT sicherstellen, dass die Winkel mathematisch korrekt gezeichnet werden und nicht nur ein skalierter Kreisbogen dargestellt wird (siehe ISO-Norm Figure B.8).

## Ereignisse (Events - Tabelle B.30)

Das Output Ellipse Objekt reagiert auf folgende Ereignisse:

*   **On Change Size:** Wird ausgelöst, wenn die Größe des Rechtecks zur Laufzeit geändert wird.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Linien- oder Füllattribute (z. B. Farben) ändern.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Ellipsen und Sektoren sind unverzichtbar für die Erstellung von analogen Zeigerinstrumenten (Meters) oder Fortschrittsanzeigen. Durch die dynamische Änderung des `End angle` per ECU-Kommando lassen sich füllende Kreisbögen realisieren, die intuitiv Zustände visualisieren.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Ellipse](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/ellipse) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*