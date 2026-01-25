# ID 23 – Font attributes – ISO 11783-6 – B.14.2

```{index} single: ID 23 – Font attributes – ISO 11783-6 – B.14.2
```

Das **Font Attributes** Objekt mit der **ID 23** definiert das Erscheinungsbild von Texten (Schriftart, Größe, Farbe, Stil). Es ist ein zentrales Attribut-Objekt, das von allen textbasierten Anzeige- und Eingabeobjekten referenziert wird.

## Technische Attribute (gemäß Tabelle B.46)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 23 (Font Attributes). |
| 1 | **Font colour** | Integer 1 | Textfarbe (Farbindex 0-255). |
| 2 | **Font size** | Integer 1 | Schriftgröße (0-14 für Fixfonts, oder Pixelhöhe für Proportionalfonts). |
| 3 | **Font type** | Integer 1 | Schriftart-Index (siehe ISO-Norm Tabelle K.1). |
| 4 | **Font style** | Bitmask 1 | Stil-Optionen (Fett, Kursiv, Unterstrichen, Blinken, Proportional). |

## Schriftgrößen und Render-Modi
Die Interpretation von AID 2 hängt stark von Bit 7 in den `Font style` Optionen ab:

### Nicht-proportionale Schriftarten (Bit 7 = 0)
Hier werden vordefinierte Rastergrößen verwendet (Breite x Höhe in Pixeln):
*   **0:** 6x8, **1:** 8x8, **2:** 8x12, **3:** 12x16, **4:** 16x16, **5:** 16x24, **6:** 24x32, ..., **14:** 128x192.

### Proportionale Schriftarten (Bit 7 = 1)
In diesem Modus repräsentiert der Wert in AID 2 direkt die **Schrifthöhe in Pixeln**. Die Breite der einzelnen Zeichen variiert (ein 'i' ist schmaler als ein 'W'). Dies ermöglicht eine modernere und besser lesbare Textdarstellung.

## Stil-Optionen (AID 4)
Mehrere Stile können durch Kombination der Bits gleichzeitig aktiviert werden:
*   **Bit 0:** Fett (Bold)
*   **Bit 3:** Kursiv (Italic)
*   **Bit 2:** Unterstrichen (Underlined)
*   **Bit 4:** Invertiert (Tauscht Vorder- und Hintergrundfarbe)
*   **Bit 5/6:** Blinken (In verschiedenen Varianten)
*   **Bit 7:** Proportionaler Modus (Wichtig für modernes Design)

## Ereignisse (Events - Tabelle B.45)
*   **On Change Font Attributes:** Wird ausgelöst, wenn die Schrifteigenschaften per ECU-Kommando `Change Font Attributes` geändert werden. Das VT aktualisiert daraufhin alle betroffenen Textobjekte.

## Bedeutung für die Implementierung
Font Attributes erlauben ein konsistentes Design. Anstatt bei jedem Textobjekt Farbe und Größe einzeln zu definieren, verweisen alle Objekte auf ein gemeinsames Attribut-Objekt. Ändert man dieses eine Objekt (z. B. von weißer auf gelbe Schrift), ändert sich das gesamte HMI-Erscheinungsbild sofort.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Font Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/font-attribute) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*