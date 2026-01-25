# ID 23 – Font attributes – ISO 11783-6 – B.14.2

```{index} single: ID 23 – Font attributes – ISO 11783-6 – B.14.2
```

Das **Font Attributes** Objekt mit der **ID 23** definiert das Erscheinungsbild von Texten (Schriftart, Größe, Farbe, Stil). Es ist ein zentrales Attribut-Objekt, das von allen textbasierten Anzeige- und Eingabeobjekten referenziert wird.

### Attribute und Record Format (Tabelle B.46)

Die folgende Tabelle beschreibt den Aufbau des Font Attributes Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 23 | 3 | Objekttyp = Font Attributes. |
| [1] | **Font colour** | Integer | 1 | 0 – 255 | 4 | Textfarbe. |
| [2] | **Font size** | Integer | 1 | 0 – 255 | 5 | Schriftgröße (siehe unten). |
| [3] | **Font type** | Integer | 1 | 0 – 255 | 6 | Zeichensatz (siehe ISO-Tabelle K.1). |
| [4] | **Font style** | Bitmask | 1 | 0 – 255 | 7 | Bit 0: Bold<br>Bit 1: Crossed Out<br>Bit 2: Underlined<br>Bit 3: Italic<br>Bit 4: Inverted<br>Bit 5: Flashing (Inverted/Style)<br>Bit 6: Flashing (Hidden/Style)<br>Bit 7: Proportional (0=Fixfont, 1=Prop.). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Schriftgrößen und Render-Modi
Die Interpretation von AID 2 hängt stark von Bit 7 in den `Font style` Optionen ab:

### Nicht-proportionale Schriftarten (Bit 7 = 0)
Hier werden vordefinierte Rastergrößen verwendet (Breite x Höhe in Pixeln):
*   **0:** 6x8
*   **1:** 8x8
*   **2:** 8x12
*   ...
*   **14:** 128x192

### Proportionale Schriftarten (Bit 7 = 1)
In diesem Modus repräsentiert der Wert in AID 2 direkt die **Schrifthöhe in Pixeln**. Die Breite der einzelnen Zeichen variiert.

## Ereignisse (Events - Tabelle B.45)

Das Font Attributes Objekt reagiert auf folgende Ereignisse:

*   **On Change Font Attributes:** Wird ausgelöst durch das Kommando `Change Font Attributes`. Das VT aktualisiert alle Objekte, die diese Attribute verwenden.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Font Attributes erlauben ein konsistentes Design. Anstatt bei jedem Textobjekt Farbe und Größe einzeln zu definieren, verweisen alle Objekte auf ein gemeinsames Attribut-Objekt. Ändert man dieses eine Objekt (z. B. von weißer auf gelbe Schrift), ändert sich das gesamte HMI-Erscheinungsbild sofort.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Font Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/font-attribute) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*