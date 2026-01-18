# ID 24 – Line attributes – ISO 11783-6 – B.14.3

```{index} single: ID 24 – Line attributes – ISO 11783-6 – B.14.3
```

Das **Line Attributes** Objekt mit der **ID 24** definiert die grafischen Eigenschaften von Linien und Umrissen (Farbe, Breite, Stil). Es wird von allen geometrischen Objekten wie *Line* (ID 13), *Rectangle* (ID 14), *Ellipse* (ID 15) und *Polygon* (ID 16) referenziert.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.48)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 24 (Line Attributes). |
| 1 | **Line colour** | Integer 1 | Farbe der Linie (Farbindex 0-255). |
| 2 | **Line width** | Integer 1 | Linienstärke in Pixeln (Standard = 1). |
| 3 | **Line art** | Bitmask 2 | Bitmuster für den Linienstil (z. B. gestrichelt). |

## Linienstärken und Darstellung
Das VT verwendet einen quadratischen "Pinsel" der Größe `Line width` x `Line width`, um die Linie zu zeichnen.
*   **Breite = 0:** Die Linie wird nicht gezeichnet.
*   **Breite > 1:** Die Linie erscheint dicker. Je nach VT wächst die Dicke nach innen, nach außen oder zentriert zum geometrischen Pfad.

## Linienstil (Line Art - AID 3)
Über eine 16-Bit-Maske wird definiert, ob eine Linie durchgezogen, gestrichelt oder punktiert erscheint:
*   Jedes gesetzte Bit (1) steht für einen gezeichneten Pinselstrich.
*   Jedes nicht gesetzte Bit (0) steht für eine Lücke (Hintergrund scheint durch).
*   **Beispiel 0xFFFF:** Durchgezogene Linie (alle Bits 1).
*   **Beispiel 0xCCCC (11001100...):** Gestrichelte Linie (zwei Pixel an, zwei Pixel aus).
*   **Besonderheit:** Die Länge eines Strichs skaliert mit der `Line width`. Bei einer Breite von 2 Pixeln entspricht jedes Bit einem 2x2 Pixel Block.

## Ereignisse (Events - Tabelle B.47)
*   **On Change Line Attributes:** Wird ausgelöst, wenn die Eigenschaften per ECU-Kommando `Change Line Attributes` geändert werden. Alle referenzierenden Objekte werden daraufhin neu gezeichnet.

## Bedeutung für die Implementierung
Line Attributes ermöglichen eine effiziente Steuerung der grafischen Darstellung. Durch das Ändern eines einzigen Attribut-Objekts können beispielsweise alle Umrandungen in einer Maske gleichzeitig von "Dünn/Schwarz" auf "Dick/Rot" umgeschaltet werden, um einen Alarmzustand zu visualisieren.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*