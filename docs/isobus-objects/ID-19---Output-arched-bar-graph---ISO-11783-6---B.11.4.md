# ID 19 – Output arched bar graph – ISO 11783-6 – B.11.4

```{index} single: ID 19 – Output arched bar graph – ISO 11783-6 – B.11.4
```

Das **Output Arched Bar Graph** Objekt mit der **ID 19** ist eine bogenförmige Balkenanzeige. Es kombiniert die Eigenschaften eines linearen Balkendiagramms mit der kreisförmigen Geometrie eines Meter-Objekts.

### Attribute und Record Format (Tabelle B.39)

Die folgende Tabelle beschreibt den Aufbau des Output Arched Bar Graph Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 19 | 3 | Objekttyp = Arched Bar Graph. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des umschließenden Rechtecks in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des umschließenden Rechtecks in Pixeln. |
| [3] | **Colour** | Integer | 1 | 0 – 255 | 8 | Farbe der Balkenfüllung und des Rahmens. |
| [4] | **Target line colour** | Integer | 1 | 0 – 255 | 9 | Farbe der Zielwert-Linie (falls gezeichnet). |
| [5] | **Options** | Bitmask | 1 | 0 – 31 | 10 | Bit 0: Draw Border<br>Bit 1: Draw Target Line<br>Bit 3: Type (0=Gefüllt, 1=Line/Zeiger)<br>Bit 4: Deflection (0=Gegen Uhrzeigersinn, 1=Im Uhrzeigersinn). |
| [6] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [7] | **End angle** | Integer | 1 | 0 – 180 | 12 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| [8] | **Bar graph width** | Integer | 2 | 0 – 65535 | 13 – 14 | Dicke des Bogens in Pixeln. |
| [9] | **Min value** | Integer | 2 | 0 – 65535 | 15 – 16 | Minimalwert. |
| [10] | **Max value** | Integer | 2 | 0 – 65535 | 17 – 18 | Maximalwert. |
| [11] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 19 – 20 | Verweis auf eine Number Variable für den aktuellen Wert. |
| [14] | **Value** | Integer | 2 | 0 – 65535 | 21 – 22 | Aktueller Rohwert. Nur wenn Variable Reference == NULL. |
| [12] | **Target value var.** | Integer | 2 | 0 – 65534, 65535 | 23 – 24 | Verweis auf eine Number Variable für den Zielwert. |
| [13] | **Target value** | Integer | 2 | 0 – 65535 | 25 – 26 | Aktueller Zielwert. Nur wenn Target value variable ref == NULL. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 27 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Geometrie
Der bogenförmige Balken wird basierend auf einem virtuellen Ellipsenobjekt innerhalb des umschließenden Rechtecks gezeichnet.

*   **Balkendicke (AID 8):** Definiert, wie breit der Bogen selbst ist.
*   **Winkel-Logik:** Die Winkelwerte werden (wie beim Meter-Objekt) halbiert übertragen (z. B. 45 für 90°).
*   **Deflektion (AID 5, Bit 4):** Steuert, ob der Balken im Uhrzeigersinn (Clockwise) oder gegen den Uhrzeigersinn (Anticlockwise) "wächst".
*   **Transparenz:** Das Objekt ist transparent, was die Überlagerung mit Hintergrundbildern ermöglicht.

## Ereignisse (Events - Tabelle B.38)

Das Output Arched Bar Graph Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der `Value` oder der `Target value` ändert. Das VT aktualisiert die Grafik.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Attribute ändern.
*   **On Change Size:** Reaktion auf Größenänderung.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Arched Bar Graphs sind ideal für moderne Cockpit-Designs, bei denen mehrere Skalen platzsparend ineinander verschachtelt werden (z. B. Temperatur und Kraftstoff). Durch die `Target line` kann dem Bediener ein Sollbereich visualisiert werden, während die bogenförmige Form eine intuitive Erfassung des Füllstandes ermöglicht.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Arched Bar Graph](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/arched-bar-graph) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*