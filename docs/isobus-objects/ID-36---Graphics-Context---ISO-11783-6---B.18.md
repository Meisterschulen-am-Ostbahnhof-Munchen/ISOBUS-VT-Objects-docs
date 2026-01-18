# ID 36 – Graphics Context Object – ISO 11783-6 – B.18

```{index} single: ID 36 – Graphics Context Object – ISO 11783-6 – B.18
```

Das **Graphics Context Object (GCO)** mit der **ID 36** (ab VT Version 4) stellt einen dynamischen Grafikpuffer (Canvas) zur Verfügung, in den die ECU zur Laufzeit zeichnen kann. Es ist vergleichbar mit einer Bitmap, deren Inhalt pixelgenau verändert werden kann.

## 🎧 Podcast

* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [2025-03-30 16-59-57 Verknüpfung von Object ID und Objektname](https://www.youtube.com/watch?v=FuZTizT48JU)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

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