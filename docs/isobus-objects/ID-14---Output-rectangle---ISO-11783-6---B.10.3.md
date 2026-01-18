# ID 14 – Output rectangle – ISO 11783-6 – B.10.3

```{index} single: ID 14 – Output rectangle – ISO 11783-6 – B.10.3
```

Das **Output Rectangle** Objekt mit der **ID 14** dient zum Zeichnen von Rechtecken, die entweder nur als Umriss, gefüllt oder in Kombination dargestellt werden können.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.29)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 14 (Output Rectangle). |
| 1 | **Line attributes** | Integer 2 | Verweis auf ein **Line Attributes** Objekt (für den Umriss). |
| 2 | **Width** | Integer 2 | Gesamtbreite des Rechtecks in Pixeln. |
| 3 | **Height** | Integer 2 | Gesamthöhe des Rechtecks in Pixeln. |
| 4 | **Line suppression**| Bitmask 1 | Unterdrückung einzelner Seiten (Bit 0: Oben, Bit 1: Rechts, Bit 2: Unten, Bit 3: Links). |
| 5 | **Fill attributes** | Integer 2 | Verweis auf ein **Fill Attributes** Objekt (für die Füllung). |

## Darstellung und Eigenschaften
Das Rechteck kombiniert Linien- und Fülleigenschaften:

*   **Umriss:** Wenn AID 1 verlinkt ist, wird ein Rahmen gemäß den Line Attributes gezeichnet.
*   **Füllung:** Wenn AID 5 verlinkt ist, wird das Innere des Rechtecks gemäß den Fill Attributes gefüllt.
*   **Linienunterdrückung (AID 4):** Ermöglicht es, gezielt einzelne Kanten des Rechtecks nicht zu zeichnen. Dies ist nützlich für Tabellenstrukturen oder offene Rahmen.
*   **Clipping:** Das Rechteck definiert durch `Width` und `Height` seine eigenen grafischen Grenzen.

## Geometrische Berechnung
Die Ecken des Rechtecks ergeben sich aus der Startposition (StartX, StartY) des Objekts:
*   **Ecke Oben-Links:** (StartX, StartY)
*   **Ecke Unten-Rechts:** (StartX + Width - 1, StartY + Height - 1)
Die Linienstärke (Line Width) muss bei der Planung berücksichtigt werden, da sie je nach VT-Implementierung nach innen oder außen wachsen kann.

## Ereignisse (Events - Tabelle B.28)
*   **On Change Size:** Wird ausgelöst, wenn die Größe des Rechtecks zur Laufzeit geändert wird.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Linien- oder Füllattribute (z. B. Farben) ändern.

## Bedeutung für die Implementierung
Rechtecke sind die am häufigsten verwendeten grafischen Primitiven. Sie dienen als Hintergrund für Textfelder, als Umrandung von Gruppen oder zur Erstellung von Balken (z. B. durch dynamische Änderung der `Width` oder `Height` per ECU-Kommando). In Kombination mit transparenten Hintergründen lassen sich so komplexe Layouts realisieren.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*