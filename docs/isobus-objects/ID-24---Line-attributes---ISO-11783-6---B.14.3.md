# ID 24 – Line attributes – ISO 11783-6 – B.14.3

```{index} single: ID 24 – Line attributes – ISO 11783-6 – B.14.3
```

Das **Line Attributes** Objekt mit der **ID 24** definiert die grafischen Eigenschaften von Linien und Umrissen (Farbe, Breite, Stil). Es wird von allen geometrischen Objekten wie *Line* (ID 13), *Rectangle* (ID 14), *Ellipse* (ID 15) und *Polygon* (ID 16) referenziert.

## Technische Attribute (gemäß Tabelle B.48)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 24 (Line Attributes). |
| 1 | **Line colour** | Integer 1 | Farbe der Linie (Farbindex 0-255). |
| 2 | **Line width** | Integer 1 | Linienstärke in Pixeln (Standard = 1). |
| 3 | **Line art** | Bitmask 2 | Bitmuster für den Linienstil (z. B. gestrichelt). |

## Linienstärken und Darstellung
Das VT verwendet einen quadratischen "Pinsel" der Größe `Line width` x `Line width`, um die Linie zu zeichnen.
*   **Breite = 0:** Die Linie wird nicht gezeichnet.
*   **Breite > 1:** Die Linie erscheint dicker. Je nach VT wächst die Dicke nach innen, nach außen oder zentriert zum geometrischen Pfad.

## Linienstil (Line Art - AID 3)
Über eine 16-Bit-Maske wird definiert, ob eine Linie durchgezogen, gestrichelt oder punktiert erscheint:
*   Jedes gesetzte Bit (1) steht für einen gezeichneten Pinselstrich.
*   Jedes nicht gesetzte Bit (0) steht für eine Lücke (Hintergrund scheint durch).
*   **Beispiel 0xFFFF:** Durchgezogene Linie (alle Bits 1).
*   **Beispiel 0xCCCC (11001100...):** Gestrichelte Linie (zwei Pixel an, zwei Pixel aus).
*   **Besonderheit:** Die Länge eines Strichs skaliert mit der `Line width`. Bei einer Breite von 2 Pixeln entspricht jedes Bit einem 2x2 Pixel Block.

## Ereignisse (Events - Tabelle B.47)
*   **On Change Line Attributes:** Wird ausgelöst, wenn die Eigenschaften per ECU-Kommando `Change Line Attributes` geändert werden. Alle referenzierenden Objekte werden daraufhin neu gezeichnet.

## Bedeutung für die Implementierung
Line Attributes ermöglichen eine effiziente Steuerung der grafischen Darstellung. Durch das Ändern eines einzigen Attribut-Objekts können beispielsweise alle Umrandungen in einer Maske gleichzeitig von "Dünn/Schwarz" auf "Dick/Rot" umgeschaltet werden, um einen Alarmzustand zu visualisieren.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*
