# ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27

```{index} single: ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27
```

Das **Graphic Data** Objekt mit der **ID 46** (ab VT Version 6) dient zur Speicherung von Rohdaten für Grafiken, insbesondere im **PNG-Format**.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.74)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 46 (Graphic Data). |
| 1 | **Format** | Integer 1 | Aktuell nur 0 = PNG (32-bit RGBA maximum). |
| - | **Number of bytes** | Integer 4 | Größe der folgenden Rohdaten in Bytes. |
| - | **Raw data** | Binary | Die eigentlichen PNG-Daten. |

## Besonderheiten
Im Gegensatz zum klassischen *Picture Graphic* Objekt (ID 20), das oft auf proprietären Formaten oder einfachen Bitmaps basierte, nutzt dieses Objekt den Industriestandard PNG.
*   **Eigenständigkeit:** Das Objekt enthält seine eigene Farbpalette und wird daher **nicht** von der *Colour Map* oder *Colour Palette* der Working Set beeinflusst.

## Verwendung
Dieses Objekt wird normalerweise nicht direkt in einer Maske platziert, sondern von einem *Scaled Graphic* Objekt (ID 48) referenziert, um es anzuzeigen und ggf. zu skalieren.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.27 verwiesen.*