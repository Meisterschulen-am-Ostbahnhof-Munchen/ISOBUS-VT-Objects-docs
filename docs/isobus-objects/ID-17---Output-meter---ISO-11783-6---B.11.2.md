# ID 17 – Output meter – ISO 11783-6 – B.11.2

```{index} single: ID 17 – Output meter – ISO 11783-6 – B.11.2
```

Das **Output Meter** Objekt mit der **ID 17** ist eine Rundanzeige (Zeigerinstrument). Es visualisiert einen Zahlenwert durch die Position einer Nadel auf einem kreisförmigen Bogen.

### Attribute und Record Format (Tabelle B.35)

Die folgende Tabelle beschreibt den Aufbau des Output Meter Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 17 | 3 | Objekttyp = Output Meter. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite und Höhe des umschließenden Quadrats. |
| [2] | **Needle colour** | Integer | 1 | 0 – 255 | 6 | Farbe der Nadel. |
| [3] | **Border colour** | Integer | 1 | 0 – 255 | 7 | Farbe des Rahmens (wenn gezeichnet). |
| [4] | **Arc and tick colour** | Integer | 1 | 0 – 255 | 8 | Farbe des Bogens und der Ticks. |
| [5] | **Options** | Bitmask | 1 | 0 – 15 | 9 | Bit 0: Draw Arc<br>Bit 1: Draw Border<br>Bit 2: Draw Ticks<br>Bit 3: Deflection Direction (0=min->max gegen Uhrz., 1=min->max im Uhrz.). |
| [6] | **Number of ticks** | Integer | 1 | 0 – 255 | 10 | Anzahl der Skalenstriche. |
| [7] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [8] | **End angle** | Integer | 1 | 0 – 180 | 12 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [9] | **Min value** | Integer | 2 | 0 – 65535 | 13 – 14 | Wert am Startwinkel. |
| [10] | **Max value** | Integer | 2 | 0 – 65535 | 15 – 16 | Wert am Endwinkel. |
| [11] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 17 – 18 | Verweis auf ein Number Variable Objekt. |
| [12] | **Value** | Integer | 2 | 0 – 65535 | 19 – 20 | Aktueller Wert. Nur wenn Variable Reference == NULL. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 21 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Darstellung
Das Instrument wird in ein Quadrat eingepasst. Die Nadel bewegt sich auf einem Bogen, der durch Start- und Endwinkel definiert ist.
*   **Winkel-Logik:** Wie bei der Ellipse werden Winkel halbiert übertragen (z. B. 45 für 90°).
*   **Ticks (AID 6):** Bei zwei oder mehr Ticks wird einer am Anfang und einer am Ende des Bogens gezeichnet; weitere Ticks werden gleichmäßig dazwischen verteilt. Empfohlene Länge: 10 % der Meter-Breite.
*   **Transparenz:** Das Meter-Objekt selbst ist transparent. Dadurch können Bitmaps (z. B. ein schönes Zifferblatt) dahinter platziert werden.

## Deflektionsrichtung (AID 5, Bit 3)
Dies ist ein kritisches Attribut für die intuitive Bedienung:
*   **0 (Anticlockwise):** Der Wert steigt gegen den Uhrzeigersinn.
*   **1 (Clockwise):** Der Wert steigt im Uhrzeigersinn (Standard für die meisten analogen Instrumente).

## Ereignisse (Events - Tabelle B.34)

Das Output Meter Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der anzuzeigende Wert ändert (z.B. Variable aktualisiert). Das VT bewegt die Nadel.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Attribute ändern.
*   **On Change Size:** Reaktion auf Größenänderung.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Das Output Meter ist ideal für die Visualisierung von Motordrehzahlen, Füllständen oder Druckwerten. Da es transparent ist, lassen sich durch Kombination mit Hintergrundgrafiken (ID 20) und verschiedenen Masken sehr ansprechende, analog wirkende Cockpit-Anzeigen gestalten.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Meter](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/meter) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*