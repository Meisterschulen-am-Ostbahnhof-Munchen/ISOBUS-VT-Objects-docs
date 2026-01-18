# ID 13 – Output line – ISO 11783-6 – B.10.2

```{index} single: ID 13 – Output line – ISO 11783-6 – B.10.2
```

Das **Output Line** Objekt mit der **ID 13** wird verwendet, um eine einfache Linie zwischen zwei Punkten innerhalb eines virtuellen Rechtecks zu zeichnen.

## Technische Attribute (gemäß Tabelle B.27)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 13 (Output Line). |
| 1 | **Line attributes** | Integer 2 | Verweis auf ein **Line Attributes** Objekt (Farbe, Breite, Stil). |
| 2 | **Width** | Integer 2 | Breite des umschließenden virtuellen Rechtecks. |
| 3 | **Height** | Integer 2 | Höhe des umschließenden virtuellen Rechtecks. |
| 4 | **Line Direction** | Integer 1 | **0:** Oben-Links nach Unten-Rechts, **1:** Unten-Links nach Oben-Rechts. |

## Funktionsweise und Geometrie
Die Linie wird innerhalb eines gedachten Rechtecks gespannt, das durch die Position des Objekts sowie `Width` und `Height` definiert ist.

*   **Line Direction 0:** Die Linie verläuft diagonal fallend.
    *   Startpunkt: (X, Y)
    *   Endpunkt: (X + Width - Line Width, Y + Height - Line Width)
*   **Line Direction 1:** Die Linie verläuft diagonal steigend.
    *   Startpunkt: (X, Y + Height - Line Width)
    *   Endpunkt: (X + Width - Line Width, Y)

## Darstellung (Line Attributes)
Die eigentliche Erscheinungsform der Linie (Dicke, Farbe, gestrichelt/durchgezogen) wird über das verknüpfte **Line Attributes** Objekt (ID 24) gesteuert.
*   **Line Width:** Bei einer Linienbreite > 1 Pixel wächst die Dicke je nach VT-Implementierung nach innen, nach außen oder zentriert.
*   **Clipping:** Das virtuelle Rechteck (`Width` x `Height`) definiert gleichzeitig die Clipping-Grenzen. Teile der Linie, die durch eine sehr große `Line Width` über dieses Rechteck hinausgehen würden, werden abgeschnitten.

## Ereignisse (Events - Tabelle B.26)
*   **On Change End Point:** Wird ausgelöst, wenn die Endpunkte der Linie durch ein Kommando verschoben werden.
*   **On Change Attribute:** Wird ausgelöst, wenn sich die Linien-Eigenschaften (z. B. Farbe) ändern.

## Bedeutung für die Implementierung
Linien werden häufig als Trennelemente in Masken oder zur einfachen grafischen Darstellung von Zusammenhängen genutzt. Durch die Verknüpfung mit Variablen (über die Line Attributes) können Linien zur Laufzeit ihre Farbe ändern, um Zustände (z. B. Aktiv/Inaktiv) zu signalisieren.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*