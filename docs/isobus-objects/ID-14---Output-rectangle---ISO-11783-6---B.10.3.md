# ID 14 – Output rectangle – ISO 11783-6 – B.10.3

```{index} single: ID 14 – Output rectangle – ISO 11783-6 – B.10.3
```

Das **Output Rectangle** Objekt mit der **ID 14** dient zum Zeichnen von Rechtecken, die entweder nur als Umriss, gefüllt oder in Kombination dargestellt werden können.

### Attribute und Record Format (Tabelle B.29)

Die folgende Tabelle beschreibt den Aufbau des Output Rectangle Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 14 | 3 | Objekttyp = Output Rectangle. |
| [1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Objekt-ID eines Line Attributes Objekts für den Rahmen. |
| [2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Breite des Rechtecks in Pixeln. |
| [3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Höhe des Rechtecks in Pixeln. |
| [4] | **Line suppression** | Bitmask | 1 | 0 – 15 | 10 | Unterdrückung von Seiten: Bit 0=Oben, Bit 1=Rechts, Bit 2=Unten, Bit 3=Links. (1 = nicht zeichnen). |
| [5] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Objekt-ID eines Fill Attributes Objekts (für die Füllung) oder NULL für keine Füllung. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Darstellung und Eigenschaften
Das Rechteck kombiniert Linien- und Fülleigenschaften:

*   **Umriss:** Wenn AID 1 verlinkt ist, wird ein Rahmen gemäß den Line Attributes gezeichnet.
*   **Füllung:** Wenn AID 5 verlinkt ist, wird das Innere des Rechtecks gemäß den Fill Attributes gefüllt.
*   **Linienunterdrückung (AID 4):** Ermöglicht es, gezielt einzelne Kanten des Rechtecks nicht zu zeichnen. Dies ist nützlich für Tabellenstrukturen oder offene Rahmen.
*   **Clipping:** Das Rechteck definiert durch `Width` und `Height` seine eigenen grafischen Grenzen.

## Geometrische Berechnung
Die Ecken des Rechtecks ergeben sich aus der Startposition (StartX, StartY) des Objekts:
*   **Ecke Oben-Links:** (StartX, StartY)
*   **Ecke Unten-Rechts:** (StartX + Width - 1, StartY + Height - 1)
Die Linienstärke (Line Width) muss bei der Planung berücksichtigt werden, da sie je nach VT-Implementierung nach innen oder außen wachsen kann.

## Ereignisse (Events - Tabelle B.28)

Das Output Rectangle Objekt reagiert auf folgende Ereignisse:

*   **On Change Size:** Wird ausgelöst, wenn die Größe des Rechtecks zur Laufzeit geändert wird.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Linien- oder Füllattribute (z. B. Farben) ändern.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Rechtecke sind die am häufigsten verwendeten grafischen Primitiven. Sie dienen als Hintergrund für Textfelder, als Umrandung von Gruppen oder zur Erstellung von Balken (z. B. durch dynamische Änderung der `Width` oder `Height` per ECU-Kommando). In Kombination mit transparenten Hintergründen lassen sich so komplexe Layouts realisieren.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Rectangle](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/rectangle) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*