# ID 44 – Animation – ISO 11783-6 – B.25

```{index} single: ID 44 – Animation – ISO 11783-6 – B.25
```

Das **Animation** Objekt mit der **ID 44** (ab VT Version 5) ermöglicht die automatische oder manuelle Wiedergabe einer Sequenz von Objekten (Frames).

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.72)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 44 (Animation). |
| 1 | **Width** | Integer 2 | Breite des Animationsbereichs. |
| 2 | **Height** | Integer 2 | Höhe des Animationsbereichs. |
| 3 | **Refresh Interval** | Integer 2 | Zeit in ms zwischen den Frames (0 = Timer aus). |
| 4 | **Value** | Integer 1 | Aktueller Index des sichtbaren Objekts. |
| 5 | **Enabled** | Integer 1 | 0 = Stop, 1 = Läuft. |
| 6 | **First Child Index** | Integer 1 | Index des ersten Frames der Sequenz. |
| 7 | **Last Child Index** | Integer 1 | Index des letzten Frames der Sequenz. |
| 8 | **Default Child Index**| Integer 1 | Anzeige-Index, wenn die Animation gestoppt ist. |
| 9 | **Options** | Bitmask 1 | Bit 0: 0=Single Shot, 1=Loop. Bits 1-2: Verhalten bei Deaktivierung (Pause, Reset, etc.). |

## Funktionsweise
Das Animationsobjekt verwaltet eine Liste von Kind-Objekten. Wenn `Enabled` auf 1 steht, inkrementiert das Terminal den `Value` (Index) automatisch im Rhythmus des `Refresh Interval`.
*   **Loop:** Nach Erreichen des `Last Child Index` wird wieder beim `First Child Index` begonnen.
*   **Single Shot:** Die Animation stoppt beim letzten Frame.

## Empfehlung
Um die Performance des Terminals nicht zu überlasten, sollten die Einzelobjekte klein gehalten werden. Ein Refresh-Intervall von mindestens 200 ms wird empfohlen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.25 verwiesen.*