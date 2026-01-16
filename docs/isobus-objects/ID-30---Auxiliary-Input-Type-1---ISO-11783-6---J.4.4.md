# ID 30 – Auxiliary Input Type 1 – ISO 11783-6 – J.4.4

Das **Auxiliary Input Type 1** Objekt mit der **ID 30** definiert die Eigenschaften eines physischen Bedienelements (z. B. Joystick, Schalter) eines Auxiliary Input Geräts.

*Hinweis: Dieses Objekt gilt ab VT Version 3 als veraltet (obsolete) und wird durch den Typ 2 (ID 32) ersetzt.*

## Technische Attribute (gemäß Tabelle J.3)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 30 (Auxiliary Input Type 1). |
| - | **Background colour** | Integer 1 | Hintergrundfarbe. |
| - | **Function type** | Integer 1 | 0 = Latching Boolean, 1 = Analogue, 2 = Non-latching Boolean. |
| - | **Input ID** | Integer 1 | Identifikationsnummer des Eingangs (wird in Statusmeldungen verwendet). |
| - | **Number of objects** | Integer 1 | Anzahl der Designator-Objekte. |

### Wiederholung für Designator-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID des Objekts für das Symbol. |
| **X Location** | Signed Int 2 | Relative X-Position. |
| **Y Location** | Signed Int 2 | Relative Y-Position. |

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*
