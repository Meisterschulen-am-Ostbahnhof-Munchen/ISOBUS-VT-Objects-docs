# ID 12 – Output number – ISO 11783-6 – B.9.3

```{index} single: ID 12 – Output number – ISO 11783-6 – B.9.3
```

Das **Output Number** Objekt mit der **ID 12** dient zur Anzeige von numerischen Werten. Wie das *Input Number* Objekt unterstützt es automatische Skalierung und Formatierung, ist jedoch rein für die Anzeige (Read-only für den Bediener) konzipiert.

### Attribute und Record Format (Tabelle B.23)

Die folgende Tabelle beschreibt den Aufbau des Output Number Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 12 | 3 | Objekttyp = Output Number. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Anzeigefeldes in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Anzeigefeldes in Pixeln. |
| [3] | **Background colour** | Integer | 1 | 0 – 255 | 8 | Hintergrundfarbe. |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Objekt-ID eines Font Attributes Objekts. |
| [5] | **Options** | Bitmask | 1 | 0 – 15 | 11 | Bit 0: Transparent<br>Bit 1: Display leading zeros<br>Bit 2: Display zero as blank<br>Bit 3: Truncate (1=Abschneiden, 0=Runden). |
| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Verweis auf ein Number Variable Objekt für den Rohwert. |
| [12] | **Value** | Integer | 4 | 0 – 2^32-1 | 14 – 17 | Rohwert (unsigned 32-bit). Nur wenn Variable Reference == NULL. |
| [7] | **Offset** | Signed Integer | 4 | -2^31 – 2^31-1 | 18 – 21 | Offset für die Skalierung. |
| [8] | **Scale** | Float | 4 | - | 22 – 25 | Skalierungsfaktor. |
| [9] | **Number of decimals** | Integer | 1 | 0 – 7 | 26 | Anzahl der Nachkommastellen. |
| [10] | **Format** | Boolean | 1 | 0 oder 1 | 27 | 0 = Festkomma, 1 = Exponential. |
| [11] | **Justification** | Integer | 1 | 0 – 15 | 28 | Textausrichtung: Bits 0-1 (Horiz.), Bits 2-3 (Vert.). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 29 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Die Skalierungslogik
Das VT berechnet den angezeigten Wert automatisch nach folgender Formel:

**Angezeigter Wert = (Rohwert + Offset) × Skalierungsfaktor**

Beispiel: Ein Rohwert von 2500 mit einem Offset von 0 und einem Skalierungsfaktor von 0.01 wird als **25.00** angezeigt (bei 2 Nachkommastellen).

## Formatierungsoptionen
*   **Führende Nullen (Bit 1):** Das Feld wird links mit Nullen aufgefüllt (z. B. "0012").
*   **Null als Leerzeichen (Bit 2):** Wenn der skalierte Wert exakt Null ist, bleibt das Feld komplett leer.
*   **Runden vs. Abschneiden (Bit 3):** Steuert, wie mit Werten verfahren wird, die mehr Nachkommastellen haben, als in AID 9 definiert sind.

## Ereignisse (Events)

Das Output Number Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der angezeigte Wert ändert (z.B. Variable aktualisiert oder `Change Numeric Value` Befehl). Das VT zeichnet das Objekt neu.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Change Size:** Reaktion auf Größenänderung.

## Bedeutung für die Implementierung
Output Numbers sind ideal für die Anzeige von Sensordaten (Druck, Temperatur, Geschwindigkeit). Da die ECU lediglich Ganzzahlen (Rohwerte) übertragen muss, wird die CAN-Bus-Last minimiert und die Komplexität der Formatierung auf das Terminal verlagert. Die pixelgenaue Justierung (AID 11) sorgt dafür, dass die Zahlen auch bei verschiedenen Schriftarten exakt im Designrahmen ausgerichtet sind.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Number (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-output) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*