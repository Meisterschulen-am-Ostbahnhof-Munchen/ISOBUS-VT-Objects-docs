# ID 16 – Output polygon – ISO 11783-6 – B.10.5

```{index} single: ID 16 – Output polygon – ISO 11783-6 – B.10.5
```

Das **Output Polygon** Objekt mit der **ID 16** ermöglicht das Zeichnen komplexer, mehreckiger Formen durch die Definition einer Liste von Eckpunkten.

### Attribute und Record Format (Tabelle B.33)

Die folgende Tabelle beschreibt den Aufbau des Output Polygon Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 16 | 3 | Objekttyp = Polygon. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des umschließenden virtuellen Rechtecks. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des umschließenden virtuellen Rechtecks. |
| [3] | **Line attributes** | Integer | 2 | 0 – 65534 | 8 – 9 | Objekt-ID eines Line Attributes Objekts (für den Umriss). |
| [4] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 10 – 11 | Objekt-ID eines Fill Attributes Objekts (Füllung) oder NULL. |
| [5] | **Polygon type** | Integer | 1 | 0 – 3 | 12 | 0=Konvex, 1=Nicht-konvex, 2=Komplex, 3=Offen. |
| - | **Number of points** | Integer | 1 | 3 – 255 | 13 | Anzahl der Eckpunkte (mindestens 3). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 14 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Point X} | Integer | 2 | 0 – 65535 | 15 + ... | X-Position des Punktes relativ zur linken oberen Ecke des Objekts. |
| - | {Point Y} | Integer | 2 | 0 – 65535 | 17 + ... | Y-Position des Punktes relativ zur linken oberen Ecke des Objekts. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Punkten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Polygontypen und Füllregeln
Der Polygontyp (AID 5) informiert das VT über die Komplexität der Form, was die Effizienz des Zeichnens beeinflusst:

*   **Convex (0):** Einfache Formen (z. B. Dreieck, Sechseck), bei denen jede horizontale Linie die Kanten nur zweimal schneidet.
*   **Non-Convex (1):** Einbuchtungen sind möglich, aber Kanten überschneiden sich nicht.
*   **Complex (2):** Kanten dürfen sich überschneiden (z. B. ein Stern). Hier wird die **Even-Odd-Regel** zur Füllung angewendet.
*   **Open (3):** Die Punkte werden nur durch Linien verbunden; das Polygon wird nicht geschlossen und nicht gefüllt.

## Geometrie und Punkte
*   **Relative Position:** Alle Punkte (`Point X`, `Point Y`) beziehen sich auf die obere linke Ecke des Polygon-Objekts.
*   **Automatisches Schließen:** Wenn der Typ nicht "Open" ist und der letzte Punkt nicht mit dem ersten identisch ist, schließt das VT das Polygon automatisch durch eine Linie vom letzten zum ersten Punkt.
*   **Anzahl der Punkte:** Es können bis zu 255 Punkte definiert werden.

## Ereignisse (Events - Tabelle B.32)

Das Output Polygon Objekt reagiert auf folgende Ereignisse:

*   **On Refresh:** Wird ausgelöst bei `Change Polygon Point` oder `Change Polygon Scale` Kommando.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Linien- oder Füllattribute ändern.
*   **On Change Size:** Reaktion auf Größenänderung (des umschließenden Rechtecks).

## Bedeutung für die Implementierung
Polygone sind sehr mächtig für die Darstellung von unregelmäßigen Flächen, wie z. B. Tankinhalten in asymmetrischen Behältern oder zur Visualisierung von Feldumrissen. Aufgrund der Rechenlast bei komplexen Polygonen sollten ECU-Entwickler nach Möglichkeit "konvexe" Typen bevorzugen, wenn die Form dies zulässt.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Polygon](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/polygon) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*