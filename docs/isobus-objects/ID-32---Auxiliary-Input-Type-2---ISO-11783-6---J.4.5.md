# ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5

```{index} single: ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5
```

Das **Auxiliary Input Type 2** Objekt mit der **ID 32** definiert ein physisches Bedienelement eines Auxiliary Input Geräts (z. B. eine Taste auf einem Joystick) ab VT Version 3.

### Attribute und Record Format (Tabelle J.4)

Die folgende Tabelle beschreibt den Aufbau des Auxiliary Input Type 2 Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 32 | 3 | Objekttyp = Auxiliary Input Type 2. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Function attributes** | Bitmask | 1 | - | 5 | Bitmaske für Funktionstyp und Steuerung (siehe unten). |
| [3] | **Input ID** | Integer | 1 | 0 – 255 | 6 | ID des physikalischen Eingangs. |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 7 | Anzahl der direkt enthaltenen Objekte (Designator). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 10 + ... | X-Position relativ zur oberen linken Ecke. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 12 + ... | Y-Position relativ zur oberen linken Ecke. |

### Function Attributes (Bitmaske AID 2)
*   **Bit 0–3:** Auxiliary function type (siehe Tabelle J.5)
    *   0: Boolean Latching (Schaltend)
    *   1: Analogue (Analog)
    *   2: Boolean Momentary (Tastend)
    *   3: Boolean Latching (Dual)
    *   ...
*   **Bit 4–5:** Reserved
*   **Bit 6:** Reserved
*   **Bit 7:** Single Assignment (1 = Darf nur einer Funktion zugewiesen werden).

## Funktionsweise
Das Terminal nutzt diese Informationen, um dem Benutzer die verfügbaren Tasten und deren physikalische Eigenschaften anzuzeigen. Wenn der Benutzer eine Taste drückt, sendet das Eingabegerät eine Statusmeldung mit dem aktuellen Wert (Boolean oder Analog) und der `Input ID` an den ISOBUS.
Es ersetzt den veralteten Typ 1 (ID 30).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*