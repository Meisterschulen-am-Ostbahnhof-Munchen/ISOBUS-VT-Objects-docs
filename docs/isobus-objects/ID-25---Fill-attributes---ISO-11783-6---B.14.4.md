# ID 25 – Fill attributes – ISO 11783-6 – B.14.4

```{index} single: ID 25 – Fill attributes – ISO 11783-6 – B.14.4
```

Das **Fill Attributes** Objekt mit der **ID 25** definiert, wie geschlossene geometrische Formen (Rechtecke, Ellipsen, Polygone) gefüllt werden.

### Attribute und Record Format (Tabelle B.50)

Die folgende Tabelle beschreibt den Aufbau des Fill Attributes Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 25 | 3 | Objekttyp = Fill Attributes. |
| [1] | **Fill type** | Integer | 1 | 0 – 3 | 4 | 0=Keine Füllung, 1=Linienfarbe, 2=Füllfarbe, 3=Muster. |
| [2] | **Fill colour** | Integer | 1 | 0 – 255 | 5 | Füllfarbe (nur bei Typ 2 relevant). |
| [3] | **Fill pattern** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | Objekt-ID eines Picture Graphic Objekts für Musterfüllung (nur bei Typ 3). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Fülltypen und Logik
Über AID 1 wird gesteuert, welche Quelle für die Flächenfüllung genutzt wird:

*   **No Fill (0):** Die Fläche bleibt transparent; nur der Umriss (falls definiert) wird gezeichnet.
*   **Line Colour (1):** Die Fläche wird in derselben Farbe gefüllt wie die Umrandung (aus den Line Attributes).
*   **Specified Colour (2):** Es wird die in AID 2 definierte Farbe verwendet.
*   **Pattern (3):** Die Fläche wird mit einer sich wiederholenden Grafik gefüllt (Kachelung).

## Verwendung von Füllmustern (Wichtig!)
Wenn ein Muster (AID 3) verwendet wird, gelten strenge Regeln für die referenzierte Grafik:
*   **Ausrichtung:** Bei monochromen Grafiken muss die Breite durch 8 teilbar sein. Bei 16-Farben-Grafiken muss sie durch 2 teilbar sein.
*   **Reihenfolge:** Bei dynamischen Änderungen muss erst das `Fill pattern` und dann der `Fill type` gesetzt werden, um Fehler im VT zu vermeiden.

## Ereignisse (Events - Tabelle B.49)

Das Fill Attributes Objekt reagiert auf folgende Ereignisse:

*   **On Change Fill Attributes:** Wird ausgelöst durch das Kommando `Change Fill Attributes`. Das VT aktualisiert alle Objekte, die dieses Attribut verwenden.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Fill Attributes sind unverzichtbar für die Gestaltung der Benutzeroberfläche. Sie ermöglichen es, Flächen hervorzuheben (z. B. gelbe Füllung für einen Warnbereich in einem Balkendiagramm) oder texturierte Hintergründe zu schaffen. Durch den Wechsel des Fülltyps zur Laufzeit können Zustände (z. B. "Tank leer" -> rot blinkende Füllung) sehr auffällig visualisiert werden.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Fill Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/fill-attribute) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*