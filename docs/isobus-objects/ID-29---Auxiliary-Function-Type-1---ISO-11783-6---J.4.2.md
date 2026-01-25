# ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2

```{index} single: ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2
```

Das **Auxiliary Function Type 1** Objekt mit der **ID 29** definiert die Attribute und das Design eines Hilfsfunktions-Bedienelements (Auxiliary Function). 

*Hinweis: Dieses Objekt gilt ab VT Version 3 als veraltet (obsolete) und wird durch den Typ 2 (ID 31) ersetzt. Es sollte in neuen Projekten nicht mehr verwendet werden.*

### Attribute und Record Format (Tabelle J.1)

Die folgende Tabelle beschreibt den Aufbau des Auxiliary Function Type 1 Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 29 | 3 | Objekttyp = Auxiliary Function Type 1. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Function type** | Integer | 1 | 0 – 2 | 5 | 0=Schaltend (Latch Boolean), 1=Analog, 2=Tastend (Non-latching Boolean). |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 6 | Anzahl der direkt enthaltenen Objekte (Designator). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 9 + ... | X-Position relativ zur oberen linken Ecke. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 11 + ... | Y-Position relativ zur oberen linken Ecke. |

## Funktionsweise
Das VT nutzt diese Attribute, um die Zuweisung zu einem kompatiblen Auxiliary Input zu erzwingen. Das Designator-Symbol muss in den Bereich eines Softkeys passen; überstehende Teile werden abgeschnitten (Clipped).
Das Objekt dient als Funktionsdefinition, die einem physischen Hilfseingabegerät (Auxiliary Input) zugewiesen werden kann.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*