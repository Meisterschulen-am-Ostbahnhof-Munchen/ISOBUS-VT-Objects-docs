# ID 36 – Graphics Context Object – ISO 11783-6 – B.18

```{index} single: ID 36 – Graphics Context Object – ISO 11783-6 – B.18
```

Das **Graphics Context Object (GCO)** mit der **ID 36** (ab VT Version 4) stellt einen dynamischen Grafikpuffer (Canvas) zur Verfügung, in den die ECU zur Laufzeit zeichnen kann. Es ist vergleichbar mit einer Bitmap, deren Inhalt pixelgenau verändert werden kann.

## Technische Attribute (gemäß Tabelle B.59)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 36 (Graphics Context). |
| 1 | **Viewport Width** | Integer 2 | Breite des sichtbaren Fensters auf dem Canvas. |
| 2 | **Viewport Height** | Integer 2 | Höhe des sichtbaren Fensters. |
| 3 | **Viewport X** | Integer 2 | X-Position des Viewports auf dem Canvas. |
| 4 | **Viewport Y** | Integer 2 | Y-Position des Viewports auf dem Canvas. |
| 5 | **Canvas Width** | Integer 2 | Gesamtbreite des Grafikpuffers. |
| 6 | **Canvas Height** | Integer 2 | Gesamthöhe des Grafikpuffers. |
| 8/9 | **Cursor X/Y** | Integer 2 | Aktuelle Zeichenposition (Grafik-Cursor). |
| 10 | **Foreground Colour** | Integer 1 | Aktuelle Vordergrundfarbe zum Zeichnen. |

## Funktionsweise
Im Gegensatz zu statischen Objekten erlaubt das GCO das Zeichnen von Linien, Rechtecken und Text mittels spezieller **Graphics Context Commands** (Annex F). 
*   **Persistenz:** Der Inhalt des Canvas bleibt im Speicher des Terminals erhalten, auch wenn die Maske gewechselt wird.
*   **Panning:** Durch Verschieben des Viewports (X/Y) kann ein großer Canvas durch ein kleines Fenster betrachtet werden (Scroll-Effekt).

## Anwendungsbeispiel
Typische Anwendungen sind **GPS-Karten** (Swath-Logging), bei denen die ECU kontinuierlich die gefahrene Spur als Linie in den GCO zeichnet.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.18 verwiesen.*