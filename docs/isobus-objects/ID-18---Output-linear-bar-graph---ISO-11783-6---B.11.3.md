# ID 18 – Output linear bar graph – ISO 11783-6 – B.11.3

Das **Output Linear Bar Graph** Objekt mit der **ID 18** dient zur Anzeige von Werten in Form eines Balkens oder Thermometers. Es unterstützt verschiedene Ausrichtungen und bietet die Möglichkeit, einen Zielwert (Target) markant hervorzuheben.

## Technische Attribute (gemäß Tabelle B.37)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 18 (Linear Bar Graph). |
| 1 | **Width** | Integer 2 | Breite des umschließenden Rechtecks in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des umschließenden Rechtecks in Pixeln. |
| 3 | **Colour** | Integer 1 | Farbe der Balkenfüllung und des Rahmens. |
| 4 | **Target line colour** | Integer 1 | Farbe der Zielwert-Linie. |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Rahmen zeichnen, **Bit 1:** Zielwert-Linie zeichnen, **Bit 2:** Ticks zeichnen, **Bit 3:** Typ (0=Gefüllter Balken, 1=Einzelne Linie/Zeiger), **Bit 4:** Ausrichtung (0=Vertikal, 1=Horizontal), **Bit 5:** Richtung (0=Links/Unten, 1=Rechts/Oben). |
| 6 | **Number of ticks** | Integer 1 | Anzahl der Skalenstriche (0-255). |
| 7 | **Min value** | Integer 2 | Minimalwert (Balken ist leer). |
| 8 | **Max value** | Integer 2 | Maximalwert (Balken ist voll). |
| 9 | **Variable reference**| Integer 2 | Verweis auf eine **Number Variable** für den aktuellen Wert. |
| 12 | **Value** | Integer 2 | Aktueller Rohwert (0-65535). Nur wenn AID 9 = NULL. |
| 10 | **Target value var.** | Integer 2 | Verweis auf eine **Number Variable** für den Zielwert. |
| 11 | **Target value** | Integer 2 | Aktueller Zielwert. Nur wenn AID 10 = NULL. |

## Funktionsweise und Optionen
Der Balkengrafik wird in ein Rechteck eingepasst und ist standardmäßig transparent, sodass Hintergrundgrafiken sichtbar bleiben.

*   **Ausrichtung (AID 5, Bit 4 & 5):** Ermöglicht horizontale (links-nach-rechts) oder vertikale (unten-nach-oben) Balken.
*   **Darstellungstyp (Bit 3):** Neben dem klassischen füllenden Balken kann das Objekt auch als "Einzelzeiger" fungieren, bei dem nur eine Linie an der aktuellen Position gezeichnet wird.
*   **Target Line:** Eine zusätzliche Markierung (z. B. ein roter Strich), die einen Sollwert oder einen Warnbereich kennzeichnet.

## Skalierung
Der Balken wird proportional zum aktuellen `Value` zwischen `Min value` und `Max value` berechnet. Liegt der Wert außerhalb dieses Bereichs, wird der Balken entweder komplett leer oder komplett voll gezeichnet.

## Ereignisse (Events - Tabelle B.36)
*   **On Change Value:** Wird ausgelöst, wenn sich der `Value` oder der `Target value` ändert. Das VT aktualisiert die Grafik.

## Bedeutung für die Implementierung
Balkendiagramme sind ideal für Füllstandsanzeigen (Kraftstoff, Saatgut), Temperaturanzeigen oder Lastanzeigen. Durch die Option der `Target line` kann dem Bediener sofort visualisiert werden, ob er sich im optimalen Arbeitsbereich befindet. Die Kombination mit Skalenstrichen (Ticks) erhöht die Ablesbarkeit.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*
