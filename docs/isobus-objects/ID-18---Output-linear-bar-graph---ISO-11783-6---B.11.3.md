# ID 18 – Output linear bar graph – ISO 11783-6 – B.11.3

```{index} single: ID 18 – Output linear bar graph – ISO 11783-6 – B.11.3
```

Das **Output Linear Bar Graph** Objekt mit der **ID 18** dient zur Anzeige von Werten in Form eines Balkens oder Thermometers. Es unterstützt verschiedene Ausrichtungen und bietet die Möglichkeit, einen Zielwert (Target) markant hervorzuheben.

### Attribute und Record Format (Tabelle B.37)

Die folgende Tabelle beschreibt den Aufbau des Output Linear Bar Graph Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 18 | 3 | Objekttyp = Linear Bar Graph. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des umschließenden Rechtecks in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des umschließenden Rechtecks in Pixeln. |
| [3] | **Colour** | Integer | 1 | 0 – 255 | 8 | Farbe der Balkenfüllung und des Rahmens. |
| [4] | **Target line colour** | Integer | 1 | 0 – 255 | 9 | Farbe der Zielwert-Linie (wenn gezeichnet). |
| [5] | **Options** | Bitmask | 1 | 0 – 63 | 10 | Bit 0: Draw Border<br>Bit 1: Draw Target Line<br>Bit 2: Draw Ticks<br>Bit 3: Type (0=Filled, 1=Line)<br>Bit 4: Axis Orientation (0=Vertical, 1=Horizontal)<br>Bit 5: Direction (0=Negativ/Absteigend, 1=Positiv/Aufsteigend). |
| [6] | **Number of ticks** | Integer | 1 | 0 – 255 | 11 | Anzahl der Skalenstriche. |
| [7] | **Min value** | Integer | 2 | 0 – 65535 | 12 – 13 | Minimalwert. |
| [8] | **Max value** | Integer | 2 | 0 – 65535 | 14 – 15 | Maximalwert. |
| [9] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 16 – 17 | Verweis auf eine Number Variable für den aktuellen Wert. |
| [12] | **Value** | Integer | 2 | 0 – 65535 | 18 – 19 | Aktueller Wert. Nur wenn Variable Reference == NULL. |
| [10] | **Target value var.** | Integer | 2 | 0 – 65534, 65535 | 20 – 21 | Verweis auf eine Number Variable für den Zielwert. |
| [11] | **Target value** | Integer | 2 | 0 – 65535 | 22 – 23 | Aktueller Zielwert. Nur wenn Target value variable ref == NULL. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 24 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Optionen
Der Balkengrafik wird in ein Rechteck eingepasst und ist standardmäßig transparent, sodass Hintergrundgrafiken sichtbar bleiben.

*   **Ausrichtung (AID 5, Bit 4 & 5):** Ermöglicht horizontale (links-nach-rechts) oder vertikale (unten-nach-oben) Balken.
*   **Darstellungstyp (Bit 3):** Neben dem klassischen füllenden Balken kann das Objekt auch als "Einzelzeiger" fungieren, bei dem nur eine Linie an der aktuellen Position gezeichnet wird.
*   **Target Line:** Eine zusätzliche Markierung (z. B. ein roter Strich), die einen Sollwert oder einen Warnbereich kennzeichnet.

## Skalierung
Der Balken wird proportional zum aktuellen `Value` zwischen `Min value` und `Max value` berechnet. Liegt der Wert außerhalb dieses Bereichs, wird der Balken entweder komplett leer oder komplett voll gezeichnet.

## Ereignisse (Events - Tabelle B.36)

Das Output Linear Bar Graph Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der `Value` oder der `Target value` ändert. Das VT aktualisiert die Grafik.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Attribute ändern.
*   **On Change Size:** Reaktion auf Größenänderung.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Balkendiagramme sind ideal für Füllstandsanzeigen (Kraftstoff, Saatgut), Temperaturanzeigen oder Lastanzeigen. Durch die Option der `Target line` kann dem Bediener sofort visualisiert werden, ob er sich im optimalen Arbeitsbereich befindet. Die Kombination mit Skalenstrichen (Ticks) erhöht die Ablesbarkeit.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*