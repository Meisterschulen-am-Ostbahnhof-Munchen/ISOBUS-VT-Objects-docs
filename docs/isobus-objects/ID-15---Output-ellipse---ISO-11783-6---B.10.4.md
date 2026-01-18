# ID 15 – Output ellipse – ISO 11783-6 – B.10.4

```{index} single: ID 15 – Output ellipse – ISO 11783-6 – B.10.4
```

Das **Output Ellipse** Objekt mit der **ID 15** dient zum Zeichnen von Kreisen, Ellipsen sowie Kreisbögen, Segmenten und Sektoren (Tortendiagramm-Stücke).

## Technische Attribute (gemäß Tabelle B.31)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 15 (Ellipse). |
| 1 | **Line attributes** | Integer 2 | Verweis auf ein **Line Attributes** Objekt (Umriss). |
| 2 | **Width** | Integer 2 | Breite des umschließenden virtuellen Rechtecks. |
| 3 | **Height** | Integer 2 | Höhe des umschließenden virtuellen Rechtecks. |
| 4 | **Ellipse type** | Integer 1 | **0:** Geschlossen, **1:** Offen (Bogen), **2:** Segment, **3:** Sektor. |
| 5 | **Start angle** | Integer 1 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 6 | **End angle** | Integer 1 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 7 | **Fill attributes** | Integer 2 | Verweis auf ein **Fill Attributes** Objekt (Füllung). |

## Ellipsentypen und Geometrie
Die Ellipse wird in ein virtuelles Rechteck (`Width` x `Height`) eingepasst.

*   **Closed Ellipse (0):** Eine vollständige Ellipse oder ein Kreis (wenn Width = Height).
*   **Open Ellipse (1):** Nur der Bogen zwischen Start- und Endwinkel wird gezeichnet.
*   **Segment (2):** Ein Kreisabschnitt (die Sehne zwischen den Winkelpunkten wird geschlossen).
*   **Sektor (3):** Ein Kreisausschnitt (die Winkelpunkte werden mit dem Mittelpunkt verbunden, ideal für Tortendiagramme).

## Winkelberechnung (Wichtig!)
Die Winkelwerte in AID 5 und 6 werden **halbiert** übertragen (Bereich 0-180 entspricht 0-360°).
*   **90° (Oben):** Wert 45
*   **180° (Links):** Wert 90
*   **270° (Unten):** Wert 135

**Besonderheit bei skalierten Ellipsen:** Wenn die Ellipse kein Kreis ist (Width != Height), muss das VT sicherstellen, dass die Winkel mathematisch korrekt gezeichnet werden und nicht nur ein skalierter Kreisbogen dargestellt wird (siehe ISO-Norm Figure B.8).

## Ereignisse (Events - Tabelle B.30)
*   **On Change Size:** Wird ausgelöst, wenn sich die Abmessungen der Ellipse ändern.
*   **On Change Attribute:** Wird ausgelöst, wenn sich Linien- oder Füllattribute ändern.

## Bedeutung für die Implementierung
Ellipsen und Sektoren sind unverzichtbar für die Erstellung von analogen Zeigerinstrumenten (Meters) oder Fortschrittsanzeigen. Durch die dynamische Änderung des `End angle` per ECU-Kommando lassen sich füllende Kreisbögen realisieren, die intuitiv Zustände visualisieren.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*