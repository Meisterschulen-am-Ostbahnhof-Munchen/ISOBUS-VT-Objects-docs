# ID 48 – Scaled Graphic – ISO 11783-6 – B.28

```{index} single: ID 48 – Scaled Graphic – ISO 11783-6 – B.28
```

Das **Scaled Graphic** Objekt mit der **ID 48** (ab VT Version 6) dient zur Anzeige und Skalierung von Grafikobjekten.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.76)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 48 (Scaled Graphic). |
| 1 | **Width** | Integer 2 | Zielbreite in Pixeln. |
| 2 | **Height** | Integer 2 | Zielhöhe in Pixeln. |
| 3 | **ScaleType** | Integer 1 | Art der Skalierung (siehe unten). |
| 4 | **Options** | Bitmask 1 | Bit 0: 1 = Flashing (Blinken). |
| 5 | **Value** | Integer 2 | ID des Grafikobjekts (ID 46 oder ID 20). |

### Skalierungstypen (Bits 0-2 von ScaleType)
*   **0:** Keine Skalierung (Originalgröße).
*   **1:** Auf Breite skalieren (Seitenverhältnis beibehalten).
*   **2:** Auf Höhe skalieren (Seitenverhältnis beibehalten).
*   **3:** Auf Breite und Höhe skalieren (Verzerrung möglich).
*   **4:** In Bereich einpassen (Best Fit, Seitenverhältnis beibehalten).

### Justierung (Bits 3-6 von ScaleType)
Definiert die Position (Links, Mitte, Rechts / Oben, Mitte, Unten) innerhalb des durch `Width` und `Height` definierten Bereichs.

## Nutzen
Im Gegensatz zum *Picture Graphic* Objekt (ID 20), das oft nur unzureichende Skalierungsmöglichkeiten bot, erlaubt dieses Objekt eine präzise Steuerung, wie Grafiken (insbesondere PNGs) auf unterschiedlichen Terminalauflösungen dargestellt werden sollen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.28 verwiesen.*