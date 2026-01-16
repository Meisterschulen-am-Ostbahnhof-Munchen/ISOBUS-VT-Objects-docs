# ID 48 – Scaled Graphic – ISO 11783-6 – B.28

Das **Scaled Graphic** Objekt mit der **ID 48** (ab VT Version 6) dient zur Anzeige und Skalierung von Grafikobjekten.

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
