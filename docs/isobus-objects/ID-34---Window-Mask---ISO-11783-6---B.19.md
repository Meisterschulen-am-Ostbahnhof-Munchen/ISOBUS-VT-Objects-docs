# ID 34 – Window Mask – ISO 11783-6 – B.19

```{index} single: ID 34 – Window Mask – ISO 11783-6 – B.19
```

Das **Window Mask** Objekt mit der **ID 34** (eingeführt mit VT Version 4) ermöglicht es, einen Teilbereich des Bildschirms zu definieren, der unabhängig von der Haupt-Datenmaske aktualisiert oder von anderen Working Sets mit Inhalten gefüllt werden kann.

### Attribute und Record Format (Tabelle B.61)

Die folgende Tabelle beschreibt den Aufbau des Window Mask Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 34 | 3 | Objekttyp = Window Mask. |
| - | **Width** | Integer | 1 | 1 – 2 | 4 | Breite in User-Layout-Spalten (nur für Typ 0 Free Form relevant, sonst ignoriert). |
| - | **Height** | Integer | 1 | 1 – 6 | 5 | Höhe in User-Layout-Zeilen (nur für Typ 0 Free Form relevant, sonst ignoriert). |
| - | **Window Type** | Integer | 1 | 0 – 18 | 6 | Typ des Fensters (siehe unten). |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 7 | Hintergrundfarbe (nur für Typ 0 relevant). |
| [2] | **Options** | Bitmask | 1 | 0 – 3 | 8 | Bit 0: Available (0=Nicht verfügbar/geblankt, 1=Verfügbar)<br>Bit 1: Transparent (1=Hintergrund transparent, nur Typ 0). |
| [3] | **Name** | Integer | 2 | 0 – 65534 | 9 – 10 | Objekt-ID eines Output String (Name für Mapping-Screen). |
| - | **Window Title** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Objekt-ID eines Output String (Titel im Fenster). |
| - | **Window Icon** | Integer | 2 | 0 – 65534, 65535 | 13 – 14 | Objekt-ID eines Output Objects (Icon für Mapping-Screen). |
| - | **Number of object references to follow** | Integer | 1 | 0 – 2 | 15 | Anzahl der referenzierten Objekte (abhängig vom Window Type). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 16 | Anzahl der direkt enthaltenen Objekte (nur für Typ 0 Free Form). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65535 | 18 + ... | Referenzierte Objekte (für vordefinierte Typen). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | var. | Enthaltene Objekte (für Typ 0 Free Form). |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | var. | X-Position relativ zum Fenster. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | var. | Y-Position relativ zum Fenster. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Fenstertypen (Auszug aus B.19.2)
*   **0:** Free Form (Freie Gestaltung, Working Set definiert Inhalt).
*   **1:** 1x1 Numeric Output mit Einheiten.
*   **2:** 1x1 Numeric Output ohne Einheiten.
*   **3:** 1x1 String Output.
*   **4:** 1x1 Numeric Input mit Einheiten.
*   **...**
*   **7:** 1x1 Horizontal Linear Bargraph.
*   **8:** 1x1 Single Button.
*   **...**
*   **10:** 2x1 Numeric Output mit Einheiten.

## Ereignisse (Events - Tabelle B.60)

Das Window Mask Objekt reagiert auf folgende Ereignisse:

*   **On Show:** Wenn das Fenster als Teil einer User-Layout Maske sichtbar wird.
*   **On Hide:** Wenn das Fenster ausgeblendet wird.
*   **On Refresh:** Bei Änderungen an Kind-Objekten.
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Child Location / Position:** Aktualisierung der Kind-Objekte.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Pointing Event:** Touch-Ereignisse (nur bei Free Form Window).

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Window Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/window-mask) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.19 verwiesen.*