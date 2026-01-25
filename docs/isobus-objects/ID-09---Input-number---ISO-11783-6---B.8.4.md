# ID 9 – Input number – ISO 11783-6 – B.8.4

```{index} single: ID 9 – Input number – ISO 11783-6 – B.8.4
```

Das **Input Number** Objekt mit der **ID 9** ist eines der komplexesten und wichtigsten Eingabeobjekte. Es dient zur Eingabe und Anzeige von numerischen Werten und unterstützt automatische Skalierung, Formatierung und Grenzwertprüfung direkt im Terminal.

### Attribute und Record Format (Tabelle B.18)

Die folgende Tabelle beschreibt den Aufbau des Input Number Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 9 | 3 | Objekttyp = Input Number. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Eingabefeldes in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Eingabefeldes in Pixeln. |
| [3] | **Background colour** | Integer | 1 | 0 – 255 | 8 | Hintergrundfarbe. |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Objekt-ID eines Font Attributes Objekts (Farbe, Größe, Font). |
| [5] | **Options** | Bitmask | 1 | 0 – 15 | 11 | Bit 0: Transparent<br>Bit 1: Display leading zeros (Führende Nullen)<br>Bit 2: Display zero as blank (0 als leer)<br>Bit 3: Truncate (1=Abschneiden, 0=Runden). |
| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Verweis auf ein Number Variable Objekt für den Rohwert. Wenn NULL, wird Attribut "Value" genutzt. |
| [14] | **Value** | Integer | 4 | 0 – 2^32-1 | 14 – 17 | Rohwert (unsigned 32-bit). Nur wenn Variable Reference == NULL. |
| [7] | **Min value** | Integer | 4 | 0 – 2^32-1 | 18 – 21 | Minimaler Rohwert (unsigned). |
| [8] | **Max value** | Integer | 4 | 0 – 2^32-1 | 22 – 25 | Maximaler Rohwert (unsigned). |
| [9] | **Offset** | Signed Integer | 4 | -2^31 – 2^31-1 | 26 – 29 | Offset für die Skalierung. |
| [10] | **Scale** | Float | 4 | - | 30 – 33 | Skalierungsfaktor. |
| [11] | **Number of decimals** | Integer | 1 | 0 – 7 | 34 | Anzahl der Nachkommastellen. |
| [12] | **Format** | Boolean | 1 | 0 oder 1 | 35 | 0 = Festkomma, 1 = Exponential. |
| [13] | **Justification** | Integer | 1 | 0 – 15 | 36 | Textausrichtung: Bits 0-1 (Horiz.), Bits 2-3 (Vert.). |
| [15] | **Options 2** | Bitmask | 1 | 0 – 3 | 37 | Bit 0: Enabled (0=Deaktiviert, 1=Aktiviert)<br>Bit 1: Real time editing (1=Wert sofort senden). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 38 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | 39... | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | 40... | Makro ID des auszuführenden Makros. |

## Die Skalierungslogik
Das VT berechnet den angezeigten Wert automatisch nach folgender Formel:

**Angezeigter Wert = (Rohwert + Offset) × Skalierungsfaktor**

Dies erlaubt es, physikalische Werte (z. B. 12,5 bar) als einfache Ganzzahlen im Speicher (z. B. 125) zu verarbeiten, während das VT die Umrechnung und Kommadarstellung übernimmt.

## Validierung
Grenzwerte werden ebenfalls auf Basis der skalierten Werte geprüft. Das VT lässt das Schließen des Eingabefeldes (ENTER) nur zu, wenn der neue Wert innerhalb der skalierten Min/Max-Grenzen liegt:
`Scaled Min <= Neuer Wert <= Scaled Max`

## Ereignisse (Events - Tabelle B.15)

Das Input Number Objekt reagiert auf folgende Ereignisse:

*   **On Enable / On Disable:** Zustandsänderung des Objekts.
*   **On Input Field Selection / De-selection:** Fokus-Ereignisse.
*   **On Entry of Value:** Wenn der Bediener einen neuen Wert bestätigt. Sendet `Change Numeric Value`.
*   **On Change Value:** Wenn der Wert durch das Programm geändert wird.
*   **On ESC:** Abbruch der Eingabe.
*   **On Change Background Colour:** Farbänderung.
*   **On Change Attribute:** Allgemeine Attributänderung.

## Real Time Editing (AID 15, Bit 1)
Wenn dieses Bit gesetzt ist, sendet das VT bei jeder Änderung (z. B. bei jedem Tastendruck am Inkrementalgeber) den aktuellen Zwischenwert an die Arbeitsgruppe. Dies ermöglicht es der Maschine, sofort auf Änderungen zu reagieren (z. B. Drehzahlregelung in Echtzeit), noch bevor der Bediener die Eingabe final bestätigt.

## Bedeutung für die Implementierung
Das Input Number Objekt nimmt der Maschinensteuerung (ECU) viel Arbeit bei der Formatierung und Validierung ab. Entwickler sollten darauf achten, den Skalierungsfaktor und die Nachkommastellen so zu wählen, dass keine Rundungsfehler die Anzeige verfälschen.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Number (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-input) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*