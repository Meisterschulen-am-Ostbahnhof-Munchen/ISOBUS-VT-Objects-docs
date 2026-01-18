# ID 16 – Output polygon – ISO 11783-6 – B.10.5

```{index} single: ID 16 – Output polygon – ISO 11783-6 – B.10.5
```

Das **Output Polygon** Objekt mit der **ID 16** ermöglicht das Zeichnen komplexer, mehreckiger Formen durch die Definition einer Liste von Eckpunkten.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.33)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 16 (Polygon). |
| 1 | **Width** | Integer 2 | Breite des umschließenden virtuellen Rechtecks (Clipping-Grenze). |
| 2 | **Height** | Integer 2 | Höhe des umschließenden virtuellen Rechtecks (Clipping-Grenze). |
| 3 | **Line attributes** | Integer 2 | Verweis auf ein **Line Attributes** Objekt (Umriss). |
| 4 | **Fill attributes** | Integer 2 | Verweis auf ein **Fill Attributes** Objekt (Füllung). |
| 5 | **Polygon type** | Integer 1 | **0:** Konvex, **1:** Nicht-konvex, **2:** Komplex, **3:** Offen (keine Füllung). |
| - | **Number of points**| Integer 1 | Anzahl der Eckpunkte (mindestens 3). |
| - | **Points** | List | Liste von X/Y-Koordinatenpaaren (relativ zum Objektursprung). |

## Polygontypen und Füllregeln
Der Polygontyp (AID 5) informiert das VT über die Komplexität der Form, was die Effizienz des Zeichnens beeinflusst:

*   **Convex (0):** Einfache Formen (z. B. Dreieck, Sechseck), bei denen jede horizontale Linie die Kanten nur zweimal schneidet.
*   **Non-Convex (1):** Einbuchtungen sind möglich, aber Kanten überschneiden sich nicht.
*   **Complex (2):** Kanten dürfen sich überschneiden (z. B. ein Stern). Hier wird die **Even-Odd-Regel** zur Füllung angewendet.
*   **Open (3):** Die Punkte werden nur durch Linien verbunden; das Polygon wird nicht geschlossen und nicht gefüllt.

## Geometrie und Punkte
*   **Relative Position:** Alle Punkte (`Point X`, `Point Y`) beziehen sich auf die obere linke Ecke des Polygon-Objekts.
*   **Automatisches Schließen:** Wenn der Typ nicht "Open" ist und der letzte Punkt nicht mit dem ersten identisch ist, schließt das VT das Polygon automatisch durch eine Linie vom letzten zum ersten Punkt.
*   **Anzahl der Punkte:** Es können bis zu 255 Punkte definiert werden.

## Ereignisse (Events - Tabelle B.32)
*   **On Change Polygon Point:** Wird ausgelöst, wenn ein einzelner Punkt der Liste per ECU-Kommando verschoben wird.
*   **On Change Polygon Scale:** Wird ausgelöst, wenn das gesamte Polygon skaliert wird.

## Bedeutung für die Implementierung
Polygone sind sehr mächtig für die Darstellung von unregelmäßigen Flächen, wie z. B. Tankinhalten in asymmetrischen Behältern oder zur Visualisierung von Feldumrissen. Aufgrund der Rechenlast bei komplexen Polygonen sollten ECU-Entwickler nach Möglichkeit "konvexe" Typen bevorzugen, wenn die Form dies zulässt.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*