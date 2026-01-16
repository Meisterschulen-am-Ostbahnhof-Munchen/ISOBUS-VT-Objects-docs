# ID 19 – Output arched bar graph – ISO 11783-6 – B.11.4

Das **Output Arched Bar Graph** Objekt mit der **ID 19** ist eine bogenförmige Balkenanzeige. Es kombiniert die Eigenschaften eines linearen Balkendiagramms mit der kreisförmigen Geometrie eines Meter-Objekts.

## Technische Attribute (gemäß Tabelle B.39)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 19 (Arched Bar Graph). |
| 1 | **Width** | Integer 2 | Breite des umschließenden Rechtecks in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des umschließenden Rechtecks in Pixeln. |
| 3 | **Colour** | Integer 1 | Farbe der Balkenfüllung und des Rahmens. |
| 4 | **Target line colour** | Integer 1 | Farbe der Zielwert-Linie (falls gezeichnet). |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Rahmen zeichnen, **Bit 1:** Zielwert-Linie zeichnen, **Bit 3:** Typ (0=Gefüllt, 1=Einzelzeiger), **Bit 4:** Richtung (0=Gegen Uhrzeigersinn, 1=Im Uhrzeigersinn). |
| 6 | **Start angle** | Integer 1 | Startwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 7 | **End angle** | Integer 1 | Endwinkel / 2 (in Grad, gegen den Uhrzeigersinn ab positiver X-Achse). |
| 8 | **Bar graph width** | Integer 2 | Dicke des Bogens in Pixeln. |
| 9 | **Min value** | Integer 2 | Minimalwert (Balken ist leer). |
| 10 | **Max value** | Integer 2 | Maximalwert (Balken ist voll). |
| 11 | **Variable reference**| Integer 2 | Verweis auf eine **Number Variable** für den aktuellen Wert. |
| 14 | **Value** | Integer 2 | Aktueller Rohwert (0-65535). Nur wenn AID 11 = NULL. |
| 12 | **Target value var.** | Integer 2 | Verweis auf eine **Number Variable** für den Zielwert. |
| 13 | **Target value** | Integer 2 | Aktueller Zielwert. Nur wenn AID 12 = NULL. |

## Funktionsweise und Geometrie
Der bogenförmige Balken wird basierend auf einem virtuellen Ellipsenobjekt innerhalb des umschließenden Rechtecks gezeichnet.

*   **Balkendicke (AID 8):** Definiert, wie breit der Bogen selbst ist. Eine `Bar graph width` von 0 führt dazu, dass nichts gezeichnet wird.
*   **Winkel-Logik:** Die Winkelwerte werden (wie beim Meter-Objekt) halbiert übertragen (z. B. 45 für 90°).
*   **Deflektion (AID 5, Bit 4):** Steuert, ob der Balken im Uhrzeigersinn (Clockwise) oder gegen den Uhrzeigersinn (Anticlockwise) "wächst".
*   **Transparenz:** Das Objekt ist transparent, was die Überlagerung mit Hintergrundbildern (z. B. einer Skala) ermöglicht.

## Ereignisse (Events - Tabelle B.38)
*   **On Change Value:** Wird ausgelöst, wenn sich der aktuelle Wert oder der Zielwert ändert. Das VT aktualisiert die bogenförmige Füllung.

## Bedeutung für die Implementierung
Arched Bar Graphs sind ideal für moderne Cockpit-Designs, bei denen mehrere Skalen platzsparend ineinander verschachtelt werden (z. B. Temperatur und Kraftstoff). Durch die `Target line` kann dem Bediener ein Sollbereich visualisiert werden, während die bogenförmige Form eine intuitive Erfassung des Füllstandes ermöglicht.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*
