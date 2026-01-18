# ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2

```{index} single: ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2
```

Das **Auxiliary Function Type 1** Objekt mit der **ID 29** definiert die Attribute und das Design eines Hilfsfunktions-Bedienelements (Auxiliary Function). 

*Hinweis: Dieses Objekt gilt ab VT Version 3 als veraltet (obsolete) und wird durch den Typ 2 (ID 31) ersetzt. Es sollte in neuen Projekten nicht mehr verwendet werden.*

## Technische Attribute (gemäß Tabelle J.1)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 29 (Auxiliary Function Type 1). |
| - | **Background colour** | Integer 1 | Hintergrundfarbe. |
| - | **Function type** | Integer 1 | 0 = Latching Boolean (schaltend), 1 = Analogue, 2 = Non-latching Boolean (tastend). |
| - | **Number of objects** | Integer 1 | Anzahl der folgenden Objekte, die das Designator-Symbol bilden. |

### Wiederholung für Designator-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID eines Grafik-, Form- oder Ausgabefelds. |
| **X Location** | Signed Int 2 | Relative X-Position im Designator-Bereich. |
| **Y Location** | Signed Int 2 | Relative Y-Position im Designator-Bereich. |

## Funktionsweise
Das VT nutzt diese Attribute, um die Zuweisung zu einem kompatiblen Auxiliary Input zu erzwingen. Das Designator-Symbol muss in den Bereich eines Softkeys passen; überstehende Teile werden abgeschnitten (Clipped).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*