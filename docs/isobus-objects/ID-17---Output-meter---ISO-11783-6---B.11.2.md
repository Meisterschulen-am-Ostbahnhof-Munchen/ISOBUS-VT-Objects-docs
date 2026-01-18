# ID 17 – Output meter – ISO 11783-6 – B.11.2

```{index} single: ID 17 – Output meter – ISO 11783-6 – B.11.2
```

Das **Output Meter** Objekt mit der **ID 17** ist eine Rundanzeige (Zeigerinstrument). Es visualisiert einen Zahlenwert durch die Position einer Nadel auf einem kreisförmigen Bogen.

## 🎧 Podcast

* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.35)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 17 (Output Meter). |
| 1 | **Width** | Integer 2 | Breite und Höhe des umschließenden Quadrats. |
| 2 | **Needle colour** | Integer 1 | Farbe der Nadel (Zeiger). |
| 3 | **Border colour** | Integer 1 | Farbe des Rahmens (falls aktiviert). |
| 4 | **Arc and tick colour**| Integer 1 | Farbe des Bogens und der Skalenstriche (Ticks). |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Bogen zeichnen, **Bit 1:** Rahmen zeichnen, **Bit 2:** Ticks zeichnen, **Bit 3:** Richtung (0=Gegen Uhrzeigersinn, 1=Im Uhrzeigersinn). |
| 6 | **Number of ticks** | Integer 1 | Anzahl der Teilstriche auf der Skala (0-255). |
| 7 | **Start angle** | Integer 1 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 8 | **End angle** | Integer 1 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 9 | **Min value** | Integer 2 | Minimalwert (entspricht dem Startwinkel). |
| 10 | **Max value** | Integer 2 | Maximalwert (entspricht dem Endwinkel). |
| 11 | **Variable reference**| Integer 2 | Verweis auf ein **Number Variable** Objekt für den aktuellen Wert. |
| 12 | **Value** | Integer 2 | Aktueller Wert (0-65535). Nur wenn AID 11 = NULL. |

## Funktionsweise und Darstellung
Das Instrument wird in ein Quadrat eingepasst. Die Nadel bewegt sich auf einem Bogen, der durch Start- und Endwinkel definiert ist.
*   **Winkel-Logik:** Wie bei der Ellipse werden Winkel halbiert übertragen (z. B. 45 für 90°).
*   **Ticks (AID 6):** Bei zwei oder mehr Ticks wird einer am Anfang und einer am Ende des Bogens gezeichnet; weitere Ticks werden gleichmäßig dazwischen verteilt. Empfohlene Länge: 10 % der Meter-Breite.
*   **Transparenz:** Das Meter-Objekt selbst ist transparent. Dadurch können Bitmaps (z. B. ein schönes Zifferblatt) dahinter platziert werden.

## Deflektionsrichtung (AID 5, Bit 3)
Dies ist ein kritisches Attribut für die intuitive Bedienung:
*   **0 (Anticlockwise):** Der Wert steigt gegen den Uhrzeigersinn.
*   **1 (Clockwise):** Der Wert steigt im Uhrzeigersinn (Standard für die meisten analogen Instrumente).

## Ereignisse (Events - Tabelle B.34)
*   **On Change Value:** Wird ausgelöst, wenn sich der anzuzeigende Wert ändert. Das VT bewegt die Nadel an die neue Position.

## Bedeutung für die Implementierung
Das Output Meter ist ideal für die Visualisierung von Motordrehzahlen, Füllständen oder Druckwerten. Da es transparent ist, lassen sich durch Kombination mit Hintergrundgrafiken (ID 20) und verschiedenen Masken sehr ansprechende, analog wirkende Cockpit-Anzeigen gestalten.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*