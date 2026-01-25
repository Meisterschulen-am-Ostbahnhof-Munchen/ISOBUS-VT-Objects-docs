# ID 20 – Picture graphic – ISO 11783-6 – B.12.2

```{index} single: ID 20 – Picture graphic – ISO 11783-6 – B.12.2
```

Das **Picture Graphic** Objekt mit der **ID 20** dient zur Anzeige von Rastergrafiken (Bitmaps) auf dem Virtuellen Terminal. Es ermöglicht die Integration von Logos, Icons und komplexen visuellen Elementen.

### Attribute und Record Format (Tabelle B.41)

Die folgende Tabelle beschreibt den Aufbau des Picture Graphic Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 20 | 3 | Objekttyp = Picture Graphic. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Zielbreite in Pixeln (Höhe wird proportional skaliert). |
| [4] | **Actual width** | Integer | 2 | 0 – 65535 | 6 – 7 | Tatsächliche Breite der Rohdaten. |
| [5] | **Actual height** | Integer | 2 | 0 – 65535 | 8 – 9 | Tatsächliche Höhe der Rohdaten. |
| [6] | **Format** | Integer | 1 | 0 – 2 | 10 | 0=Monochrom (1 Bit), 1=16 Farben (4 Bit), 2=256 Farben (8 Bit). |
| [2] | **Options** | Bitmask | 1 | 0 – 7 | 11 | Bit 0: Transparenz (0=Opak, 1=Transp)<br>Bit 1: Blinken<br>Bit 2: Datenformat (0=Raw, 1=Run-Length Encoded). |
| [3] | **Transparency colour** | Integer | 1 | 0 – 255 | 12 | Farbindex, der transparent dargestellt wird. |
| - | **Number of bytes in raw data** | Integer | 4 | 0 – 2^32-1 | 13 – 16 | Größe der Bilddaten. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {raw data} | Integer | 1 | 0 – 255 | 18 ... | Bilddaten (Bytes). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Bilddaten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Darstellung

Das Picture Graphic-Objekt speichert Pixelgrafiken in binärer Form innerhalb der Objektpool-Datei (.IOP).

### Skalierung und Formate
*   **Seitenverhältnis:** Das VT skaliert die Grafik basierend auf der Ziel-Breite (`Width`). Um Verzerrungen zu vermeiden, berechnet das VT die Ziel-Höhe automatisch aus dem Verhältnis von `Actual width` zu `Actual height`.
*   **Farbtiefe:** Unterstützt werden 1-Bit (Monochrom), 4-Bit (16 Farben) und 8-Bit (256 Farben).

### Transparenz und Effekte
*   **Transparency (Bit 0):** Wenn aktiviert, wird die in AID 3 definierte Farbe nicht gezeichnet; stattdessen scheint der Hintergrund durch.
*   **Flashing (Bit 1):** Das Bild kann blinken (Frequenz und Stil hängen vom VT ab).
*   **RLE-Komprimierung (Bit 2):** Run-Length Encoding kann bei einfachen Grafiken (viele gleichfarbige Flächen) Speicherplatz sparen.

## Ereignisse (Events - Tabelle B.40)

Das Picture Graphic Objekt reagiert auf folgende Ereignisse:

*   **On Refresh:** Wird ausgelöst bei Änderungen von Optionen (z.B. Transparenz, Blinken) oder bei Masken-Refresh.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Picture Graphics sind essenziell für ein modernes HMI. 
*   **Verschwendung vermeiden:** Da Bitmaps viel Speicher im VT belegen, sollten sie so klein wie möglich gehalten werden. 
*   **Ziederverwendung:** Ein Bild kann im Pool einmal definiert und von vielen Objekten (z. B. mehreren Buttons) referenziert werden.
*   **Icons:** Sie werden häufig als "Designatoren" für Softkeys (ID 5) oder als Symbole in Containern (ID 3) verwendet.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Picture Graphic object](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/picture-graphic-object) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*