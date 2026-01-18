# ID 45 – Colour Palette – ISO 11783-6 – B.26

```{index} single: ID 45 – Colour Palette – ISO 11783-6 – B.26
```

Das **Colour Palette** Objekt mit der **ID 45** (ab VT Version 6) erlaubt es einer Working Set, die Standard-Farbpalette des Terminals vollständig durch eigene ARGB-Farbdefinitionen zu ersetzen.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.73)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 45 (Colour Palette). |
| - | **Number of ARGB values** | Integer 2 | Anzahl der folgenden Farbdefinitionen (bis zu 256). |

### Struktur der ARGB-Einträge
Jede Farbe wird durch 4 Bytes definiert:
*   **B (Blue):** 0–255.
*   **G (Green):** 0–255.
*   **R (Red):** 0–255.
*   **A (Alpha):** 0 (transparent) bis 255 (opak).

## Unterschied zur Colour Map (ID 39)
Während die *Colour Map* nur die Zuweisung (Indizierung) vorhandener Terminal-Farben ändert, definiert die *Colour Palette* die Farben selbst (RGB-Werte) neu. Dies ermöglicht echtes Branding in Firmenfarben oder eine optimierte Darstellung von Fotos.

## Wichtiger Hinweis
Die Verwendung des Alpha-Kanals (Transparenz) sollte vorsichtig erfolgen, da das Terminal die Hintergrundfarben untergelagerter Objekte oft nicht garantieren kann.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.26 verwiesen.*