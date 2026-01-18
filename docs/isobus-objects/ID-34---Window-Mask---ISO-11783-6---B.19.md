# ID 34 – Window Mask – ISO 11783-6 – B.19

```{index} single: ID 34 – Window Mask – ISO 11783-6 – B.19
```

Das **Window Mask** Objekt mit der **ID 34** (eingeführt mit VT Version 4) ermöglicht es, einen Teilbereich des Bildschirms zu definieren, der unabhängig von der Haupt-Datenmaske aktualisiert oder von anderen Working Sets mit Inhalten gefüllt werden kann.

## Technische Attribute (gemäß Tabelle B.61)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 34 (Window Mask). |
| - | **Window Type** | Integer 1 | Vordefinierter Fenstertyp (0-18, siehe unten). |
| - | **Background colour** | Integer 1 | Hintergrundfarbe des Fensters. |
| - | **Options** | Bitmask 1 | Optionen (z. B. Rahmen, Sichtbarkeit). |
| - | **Number of objects** | Integer 1 | Anzahl der Kind-Objekte im Fenster. |

### Fenstertypen (Auszug aus B.19.2)
*   **0:** Free Form (Freie Gestaltung).
*   **1:** 1x1 Numeric Output mit Einheiten.
*   **3:** 1x1 String Output.
*   **9:** 1x1 Button.
*   (Typen 11-19 sind meist größere 2x1 Varianten).

## Funktionsweise
Window Masks sind essenziell für **User-Layout Data Masks**. Hierbei kann der Benutzer am Terminal selbst entscheiden, welche Informationen (Fenster) er an welcher Stelle sehen möchte. Eine ECU stellt die Window Masks zur Verfügung, und das Terminal übernimmt die Anordnung.

## Ereignisse (Events)
*   **On Refresh:** Wird ausgelöst, wenn das Fenster neu gezeichnet werden muss.
*   **On Change Attribute:** Bei Änderung technischer Parameter.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.19 verwiesen.*