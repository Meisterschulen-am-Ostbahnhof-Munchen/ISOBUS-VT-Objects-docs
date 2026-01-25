# ID 24 – Line attributes – ISO 11783-6 – B.14.3

```{index} single: ID 24 – Line attributes – ISO 11783-6 – B.14.3
```

Das **Line Attributes** Objekt mit der **ID 24** definiert die grafischen Eigenschaften von Linien und Umrissen (Farbe, Breite, Stil). Es wird von allen geometrischen Objekten wie *Line* (ID 13), *Rectangle* (ID 14), *Ellipse* (ID 15) und *Polygon* (ID 16) referenziert.

### Attribute und Record Format (Tabelle B.48)

Die folgende Tabelle beschreibt den Aufbau des Line Attributes Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 24 | 3 | Objekttyp = Line Attributes. |
| [1] | **Line colour** | Integer | 1 | 0 – 255 | 4 | Linienfarbe. |
| [2] | **Line width** | Integer | 1 | 0 – 255 | 5 | Linienstärke in Pixeln. 0 = nicht zeichnen. |
| [3] | **Line art** | Bitmask | 2 | 0 – 65535 | 6 – 7 | Bitmuster für Linienstil (1=Zeichnen, 0=Hintergrund). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Linienstärken und Darstellung
Das VT verwendet einen quadratischen "Pinsel" der Größe `Line width` x `Line width`, um die Linie zu zeichnen.
*   **Breite = 0:** Die Linie wird nicht gezeichnet.
*   **Breite > 1:** Die Linie erscheint dicker.

## Linienstil (Line Art - AID 3)
Über eine 16-Bit-Maske wird definiert, ob eine Linie durchgezogen, gestrichelt oder punktiert erscheint:
*   Jedes gesetzte Bit (1) steht für einen gezeichneten Pinselstrich.
*   Jedes nicht gesetzte Bit (0) steht für eine Lücke (Hintergrund scheint durch).
*   **Beispiel 0xFFFF:** Durchgezogene Linie (alle Bits 1).
*   **Beispiel 0xCCCC (11001100...):** Gestrichelte Linie.
*   **Besonderheit:** Die Länge eines Strichs skaliert mit der `Line width`.

## Ereignisse (Events - Tabelle B.47)

Das Line Attributes Objekt reagiert auf folgende Ereignisse:

*   **On Change Line Attributes:** Wird ausgelöst durch das Kommando `Change Line Attributes`. Das VT aktualisiert alle Objekte, die dieses Attribut verwenden.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Line Attributes ermöglichen eine effiziente Steuerung der grafischen Darstellung. Durch das Ändern eines einzigen Attribut-Objekts können beispielsweise alle Umrandungen in einer Maske gleichzeitig von "Dünn/Schwarz" auf "Dick/Rot" umgeschaltet werden, um einen Alarmzustand zu visualisieren.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Line Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/line-attribute) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*