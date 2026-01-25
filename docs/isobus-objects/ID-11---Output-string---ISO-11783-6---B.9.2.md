# ID 11 – Output string – ISO 11783-6 – B.9.2

```{index} single: ID 11 – Output string – ISO 11783-6 – B.9.2
```

Das **Output String** Objekt mit der **ID 11** dient zur rein visuellen Anzeige von Textzeichenfolgen auf dem Virtuellen Terminal. Im Gegensatz zum *Input String* erlaubt dieses Objekt keine direkte Bearbeitung durch den Bediener.

### Attribute und Record Format (Tabelle B.22)

Die folgende Tabelle beschreibt den Aufbau des Output String Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 11 | 3 | Objekttyp = Output String. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Textfeldes in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Textfeldes in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [3] | **Background colour** | Integer | 1 | 0 – 255 | 8 | Hintergrundfarbe (nur bei deaktivierter Transparenz). |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Objekt-ID eines Font Attributes Objekts (Farbe, Größe, Font). |
| [5] | **Options** | Bitmask | 1 | 0 – 7 | 11 | Bit 0: Transparent<br>Bit 1: Auto-Wrap (Automatischer Zeilenumbruch)<br>Bit 2: Wrap on Hyphen (Umbruch bei Bindestrich). |
| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Verweis auf ein String Variable Objekt. Wenn NULL, wird der Wert direkt im Attribut "Value" gespeichert. |
| [7] | **Justification** | Integer | 1 | 0 – 15 | 14 | Textausrichtung: Bits 0-1 (Horiz.): 0=Links, 1=Mitte, 2=Rechts.<br>Bits 2-3 (Vert.): 0=Oben, 1=Mitte, 2=Unten. |
| - | **Length** | Integer | 2 | 0 – 65535 | 15 – 16 | Länge des festen Textwerts in Bytes. Wenn Variable Ref != NULL, kann dies 0 sein. |
| - | **Value** | String | Length | - | 17... | Statischer Textinhalt (nur wenn Variable Reference == NULL). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Besonderheiten
*   **Transparenz:** Wenn Bit 0 gesetzt ist, ist der Hintergrund des Textfeldes transparent, und die Hintergrundfarbe der Maske oder eines darunterliegenden Objekts bleibt sichtbar.
*   **Auto-Wrap:** Ermöglicht die Darstellung mehrzeiliger Texte innerhalb der definierten `Width` und `Height`.
*   **Justierung:** Die Ausrichtung erfolgt pixelgenau innerhalb des Rahmens. Dies ist besonders wichtig für die vertikale Zentrierung bei unterschiedlichen Schriftarten.
*   **Clipping:** Text, der über die definierte `Width` oder `Height` hinausgeht, wird vom VT abgeschnitten.

## Statischer Text vs. Dynamische Variable
*   **Statischer Text:** Der Text wird direkt im Objekt-Pool definiert und kann zur Laufzeit nur über das Kommando `Change Attribute` (AID 5 oder 7) in seinen Eigenschaften geändert werden.
*   **Dynamischer Text:** Durch die Verknüpfung mit einer **String Variable** (AID 6) kann die Steuerung (ECU) den Textinhalt jederzeit per `Change String Value` aktualisieren, ohne das Objekt selbst neu laden zu müssen.

## Ereignisse (Events - Tabelle B.21)

Das Output String Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der angezeigte Wert ändert (z.B. Variable aktualisiert). Das VT zeichnet das Objekt neu.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss (z.B. Maskenwechsel).
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Change Size:** Reaktion auf Größenänderung.

## Bedeutung für die Implementierung
Output Strings sind die primäre Methode für Statusmeldungen, Beschriftungen und Einheitenanzeigen. Für Texte, die in vielen Sprachen vorliegen, empfiehlt es sich, die Texte über Variablen einzusteuern oder für jede Sprache eine eigene Maske/einen eigenen Pool vorzuhalten.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - String (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-output) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*