# ID 36 – Graphics Context Object – ISO 11783-6 – B.18

```{index} single: ID 36 – Graphics Context Object – ISO 11783-6 – B.18
```

Das **Graphics Context Object (GCO)** mit der **ID 36** (ab VT Version 4) stellt einen dynamischen Grafikpuffer (Canvas) zur Verfügung, in den die ECU zur Laufzeit zeichnen kann. Es ist vergleichbar mit einer Bitmap, deren Inhalt pixelgenau verändert werden kann.

### Attribute und Record Format (Tabelle B.59)

Die folgende Tabelle beschreibt den Aufbau des Graphics Context Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 36 | 3 | Objekttyp = Graphics Context. |
| [1] | **Viewport Width** | Integer | 2 | 0 – 32767 | 4 – 5 | Breite des sichtbaren Fensters (Anzeige im VT). |
| [2] | **Viewport Height** | Integer | 2 | 0 – 32767 | 6 – 7 | Höhe des sichtbaren Fensters. |
| [3] | **Viewport X** | Signed Integer | 2 | -32768 bis +32767 | 8 – 9 | X-Position des Viewports relativ zum Canvas (0 = Links). |
| [4] | **Viewport Y** | Signed Integer | 2 | -32768 bis +32767 | 10 – 11 | Y-Position des Viewports relativ zum Canvas (0 = Oben). |
| [5] | **Canvas Width** | Integer | 2 | 0 – 32767 | 12 – 13 | Gesamtbreite des Grafikspeichers. |
| [6] | **Canvas Height** | Integer | 2 | 0 – 32767 | 14 – 15 | Gesamthöhe des Grafikspeichers. |
| [7] | **Viewport Zoom** | Float | 4 | -32.0 bis +32.0 | 16 – 19 | Zoomfaktor des Viewports (siehe Tabelle F.1). |
| [8] | **Graphics Cursor X** | Signed Integer | 2 | -32768 bis +32767 | 20 – 21 | Aktuelle X-Position des Zeichencursors. |
| [9] | **Graphics Cursor Y** | Signed Integer | 2 | -32768 bis +32767 | 22 – 23 | Aktuelle Y-Position des Zeichencursors. |
| [10] | **Foreground Colour** | Integer | 1 | 0 – 255 | 24 | Vordergrundfarbe für Zeichenoperationen. |
| [11] | **Background Colour** | Integer | 1 | 0 – 255 | 25 | Hintergrundfarbe. Wird beim Parsen zum Füllen genutzt. |
| [12] | **Font Attributes** | Integer | 2 | 0 – 65534, 65535 | 26 – 27 | Referenz auf Font Attributes Objekt (für Textbefehle). |
| [13] | **Line Attributes** | Integer | 2 | 0 – 65534, 65535 | 28 – 29 | Referenz auf Line Attributes Objekt (für Linienbefehle). |
| [14] | **Fill Attributes** | Integer | 2 | 0 – 65534, 65535 | 30 – 31 | Referenz auf Fill Attributes Objekt (für Füllbefehle). |
| [15] | **Format** | Integer | 1 | 0 – 2 | 32 | Farbtiefe des Canvas: 0=1-Bit, 1=4-Bit, 2=8-Bit. |
| [16] | **Options** | Bitmask | 1 | 0 – 3 | 33 | Bit 0: Transparenz<br>Bit 1: Farbe (0=FG/BG Attribute, 1=Line/Font/Fill Attr). |
| [17] | **Transparency Colour** | Integer | 1 | 0 – 255 | 34 | Transparenzfarbe (wenn Options Bit 0 gesetzt). |

## Funktionsweise und Struktur
Das GCO besteht aus zwei Hauptkomponenten:
1.  **Canvas:** Ein persistenter Grafikspeicher (Bitmap) mit definierter Größe (`Canvas Width/Height`). Der Inhalt bleibt erhalten, auch wenn das Objekt nicht angezeigt wird.
2.  **Viewport:** Ein "Fenster", das einen Ausschnitt des Canvas anzeigt. Der Viewport definiert die Größe des Objekts auf der Maske. Durch Ändern von `Viewport X/Y` kann der Inhalt gescrollt (gepannt) werden.

## Graphics Context Commands
Die Manipulation des Canvas erfolgt über spezielle Befehle (siehe ISO 11783-6, Anhang F), wie z. B.:
*   `Set Graphics Cursor`: Setzt die Schreibposition.
*   `Draw Point / Line / Rectangle / Polygon / Ellipse`: Zeichnet geometrische Formen.
*   `Draw Text`: Schreibt Text an die Cursorposition.
*   `Copy Canvas`: Kopiert Bereiche innerhalb des Canvas.

## Ereignisse (Events - Tabelle B.58)

Das Graphics Context Objekt reagiert auf folgende Ereignisse:

*   **On Change Attribute:** Wird ausgelöst bei Änderungen von Attributen (z. B. Viewport-Position, Zoom). Das VT aktualisiert die Anzeige.
*   **On Change Background Colour:** Füllt das Objekt (den Canvas) mit der neuen Hintergrundfarbe. **Achtung:** Löscht den bisherigen Inhalt!

## Anwendungsbeispiel
Typische Anwendungen sind **GPS-Karten** (Swath-Logging), bei denen die ECU kontinuierlich die gefahrene Spur als Linie in den GCO zeichnet.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.18 verwiesen.*