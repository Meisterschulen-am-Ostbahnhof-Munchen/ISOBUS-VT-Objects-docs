# ID 48 – Scaled Graphic – ISO 11783-6 – B.28

```{index} single: ID 48 – Scaled Graphic – ISO 11783-6 – B.28
```

Das **Scaled Graphic** Objekt mit der **ID 48** (ab VT Version 6) dient zur Anzeige und Skalierung von Grafikobjekten.

### Attribute und Record Format (Tabelle B.76)

Die folgende Tabelle beschreibt den Aufbau des Scaled Graphic Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 48 | 3 | Objekttyp = Scaled Graphic. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Zielbreite in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Zielhöhe in Pixeln. |
| [3] | **ScaleType** | Integer | 1 | 0 – 127 | 8 | Skalierungsmodus und Justierung (siehe unten). |
| [4] | **Options** | Bitmask | 1 | 0 – 1 | 9 | Bit 0: Flashing (0=Normal, 1=Blinkend). |
| [5] | **Value** | Integer | 2 | 0 – 65535 | 10 – 11 | Objekt-ID des anzuzeigenden Grafikobjekts (Graphic Data ID 46 oder Picture Graphic ID 20) oder Pointer. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 12 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Skalierungstypen (Bits 0-2 von ScaleType)
*   **0:** Keine Skalierung (Originalgröße aus den Rohdaten verwenden).
*   **1:** Auf Breite skalieren (Seitenverhältnis beibehalten).
*   **2:** Auf Höhe skalieren (Seitenverhältnis beibehalten).
*   **3:** Auf Breite und Höhe skalieren (Verzerrung möglich).
*   **4:** In Bereich einpassen (Best Fit, Seitenverhältnis beibehalten, Grafik wird so groß wie möglich).

### Justierung (Bits 3-6 von ScaleType)
Definiert die Position innerhalb des durch `Width` und `Height` definierten Bereichs:
*   **Horizontal (Bits 3-4):** 0=Links, 1=Mitte, 2=Rechts.
*   **Vertikal (Bits 5-6):** 0=Oben, 1=Mitte, 2=Unten.

## Ereignisse (Events - Tabelle B.75)

Das Scaled Graphic Objekt reagiert auf folgende Ereignisse:

*   **On Refresh:** Wird ausgelöst bei Masken-Refresh oder Optionsänderung.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Change Value:** Wird ausgelöst, wenn das referenzierte Grafikobjekt (Value) geändert wird. Das VT lädt und skaliert das neue Bild.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.28 verwiesen.*