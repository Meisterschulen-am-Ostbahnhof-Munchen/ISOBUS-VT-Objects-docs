# ID 30 – Auxiliary Input Type 1 – ISO 11783-6 – J.4.4

```{index} single: ID 30 – Auxiliary Input Type 1 – ISO 11783-6 – J.4.4
```

Das **Auxiliary Input Type 1** Objekt mit der **ID 30** definiert die Eigenschaften eines physischen Bedienelements (z. B. Joystick, Schalter) eines Auxiliary Input Geräts.

*Hinweis: Dieses Objekt gilt ab VT Version 3 als veraltet (obsolete) und wird durch den Typ 2 (ID 32) ersetzt.*

### Attribute und Record Format (Tabelle J.3)

Die folgende Tabelle beschreibt den Aufbau des Auxiliary Input Type 1 Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 30 | 3 | Objekttyp = Auxiliary Input Type 1. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Function type** | Integer | 1 | 0 – 2 | 5 | 0=Schaltend (Latch Boolean), 1=Analog, 2=Tastend (Non-latching Boolean). |
| [3] | **Input ID** | Integer | 1 | 0 – 255 | 6 | ID des physikalischen Eingangs, auf den sich dieses Objekt bezieht. |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 7 | Anzahl der direkt enthaltenen Objekte (Designator). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 10 + ... | X-Position relativ zur oberen linken Ecke. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 12 + ... | Y-Position relativ zur oberen linken Ecke. |

## Funktionsweise
Dieses Objekt beschreibt ein physisches Eingabeelement (z. B. einen Taster oder eine Achse eines Joysticks) an einem Auxiliary Input Device. Es wird vom Auxiliary Input Device bereitgestellt, damit das VT die verfügbaren Eingänge und deren Eigenschaften kennt.
Die `Input ID` verknüpft dieses Objekt mit den Statusnachrichten des Geräts.


----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*