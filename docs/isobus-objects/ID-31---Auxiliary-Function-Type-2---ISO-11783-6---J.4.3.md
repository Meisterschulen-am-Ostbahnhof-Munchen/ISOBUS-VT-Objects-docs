# ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3

```{index} single: ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3
```

Das **Auxiliary Function Type 2** Objekt mit der **ID 31** ist die moderne Definition für Hilfsfunktionen im ISOBUS (ab VT Version 3). Es bietet erweiterte Möglichkeiten zur Zuweisung von Bedienelementen.

### Attribute und Record Format (Tabelle J.2)

Die folgende Tabelle beschreibt den Aufbau des Auxiliary Function Type 2 Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 31 | 3 | Objekttyp = Auxiliary Function Type 2. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Function attributes** | Bitmask | 1 | - | 5 | Bitmaske für Funktionstyp und Steuerung (siehe unten). |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 6 | Anzahl der direkt enthaltenen Objekte (Designator). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 9 + ... | X-Position relativ zur oberen linken Ecke. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 11 + ... | Y-Position relativ zur oberen linken Ecke. |

### Function Attributes (Bitmaske AID 2)
*   **Bit 0–3:** Auxiliary function type (siehe Tabelle J.5)
    *   0: Boolean Latching (Schaltend)
    *   1: Analogue (Analog)
    *   2: Boolean Momentary (Tastend)
    *   3: Boolean Latching (Dual)
    *   4: Analogue (Dual)
    *   5: Boolean Momentary (Dual)
    *   ...
*   **Bit 4–5:** Reserved
*   **Bit 6:** Assignment Restriction (0 = Frei, 1 = Eingeschränkt, siehe ISO 11783-6).
*   **Bit 7:** Single Assignment (1 = Darf nur alleine auf einem Input liegen).

## Besonderheiten
Dieses Objekt wird aktiv für das "Auxiliary Mapping" im Terminal genutzt. Es erlaubt der ECU, dem Terminal mitzuteilen, welche Funktionen (z. B. "Heber auf/ab") zur Verfügung stehen, damit der Benutzer diese auf Tasten oder Joysticks legen kann.
Es ersetzt den veralteten Typ 1 (ID 29).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*