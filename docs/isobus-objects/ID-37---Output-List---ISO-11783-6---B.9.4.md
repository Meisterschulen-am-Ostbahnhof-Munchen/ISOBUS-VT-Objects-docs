# ID 37 – Output List – ISO 11783-6 – B.9.4

```{index} single: ID 37 – Output List – ISO 11783-6 – B.9.4
```

Das **Output List** Objekt mit der **ID 37** (ab VT Version 4) wird verwendet, um eines von mehreren Objekten aus einer Liste anzuzeigen. Welches Objekt aktuell sichtbar ist, wird über einen Index (Value) gesteuert.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.25)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 37 (Output List). |
| 1 | **Width** | Integer 2 | Breite des Anzeigebereichs. |
| 2 | **Height** | Integer 2 | Höhe des Anzeigebereichs. |
| - | **Value** | Integer 1 | Aktueller Index des anzuzeigenden Objekts (0-254). 255 = nichts anzeigen. |
| - | **Number of objects** | Integer 1 | Anzahl der in der Liste enthaltenen Objekte. |

## Funktionsweise
Die Output List verhält sich ähnlich wie eine Animation, wird aber manuell über den Index gesteuert. Sie eignet sich hervorragend für:
*   **Statusanzeigen:** z. B. verschiedene Symbole für "Bereit", "In Betrieb", "Fehler".
*   **Sprachumschaltung:** Anzeige unterschiedlicher Grafiken je nach Zustand.

## Besonderheiten
Wenn der Index auf ein Objekt verweist, das größer als die definierte `Width`/`Height` der Liste ist, wird es abgeschnitten (Clipped).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.9.4 verwiesen.*