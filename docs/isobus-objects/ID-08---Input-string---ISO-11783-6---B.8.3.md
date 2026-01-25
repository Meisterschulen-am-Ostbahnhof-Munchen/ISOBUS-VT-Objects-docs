# ID 8 – Input string – ISO 11783-6 – B.8.3

```{index} single: ID 8 – Input string – ISO 11783-6 – B.8.3
```

Das **Input String** Objekt mit der **ID 8** dient zur Eingabe und Anzeige von Textzeichenfolgen durch den Bediener.

### Attribute und Record Format (Tabelle B.17)

Die folgende Tabelle beschreibt den Aufbau des Input String Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 8 | 3 | Objekttyp = Input String. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Eingabefeldes in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Eingabefeldes in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [3] | **Background colour** | Integer | 1 | 0 – 255 | 8 | Hintergrundfarbe (nur bei deaktivierter Transparenz). |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Objekt-ID eines Font Attributes Objekts (Farbe, Größe, Font). |
| [5] | **Input attributes** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Objekt-ID eines Input Attributes Objekts zur Validierung oder NULL. |
| [6] | **Options** | Bitmask | 1 | 0 – 7 | 13 | Bit 0: Transparent<br>Bit 1: Auto-Wrap (Automatischer Zeilenumbruch)<br>Bit 2: Wrap on Hyphen (Umbruch bei Bindestrich). |
| [7] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 14 – 15 | Verweis auf ein String Variable Objekt. Wenn NULL, wird der Wert direkt im Attribut "Value" gespeichert. |
| [8] | **Justification** | Integer | 1 | 0 – 15 | 16 | Textausrichtung: Bits 0-1 (Horiz.): 0=Links, 1=Mitte, 2=Rechts.<br>Bits 2-3 (Vert.): 0=Oben, 1=Mitte, 2=Unten. |
| - | **Length** | Integer | 1 | 0 – 255 | 17 | Max. Länge in Bytes. Wenn Variable Reference != NULL, kann dies 0 sein. |
| - | **Value** | String | Length | - | 18 ... | Initialer Wert des Strings (nur wenn Variable Reference == NULL). |
| [9] | **Enabled** | Integer | 1 | 0 oder 1 | var. | 0 = Deaktiviert, 1 = Aktiviert. Position im Record ist abhängig von der Länge des Value-Feldes. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Optionen
Das Input String Objekt bietet flexible Möglichkeiten zur Textdarstellung:
*   **Auto-Wrap:** Wenn aktiviert (Bit 1), bricht das VT den Text automatisch um, wenn die Breite des Feldes überschritten wird.
*   **Justierung:** Über AID 8 wird sowohl die horizontale als auch die vertikale Ausrichtung gesteuert.
*   **Validierung:** Durch die Verknüpfung mit einem `Input Attributes` Objekt kann die Eingabe auf bestimmte Zeichensätze begrenzt werden.

## Ereignisse (Events - Tabelle B.15)

Das Input String Objekt reagiert auf folgende Ereignisse:

*   **On Enable:** Wenn das Objekt aktiviert wird.
*   **On Disable:** Wenn das Objekt deaktiviert wird.
*   **On Input Field Selection:** Bei Fokus/Auswahl durch den Bediener.
*   **On Input Field De-selection:** Bei Fokusverlust.
*   **On Entry of Value:** Wenn der Bediener die Texteingabe bestätigt (ENTER). Sendet `Change String Value`.
*   **On Change Value:** Wenn der Wert (z.B. durch Variable) geändert wird.
*   **On ESC:** Wenn der Bediener die Eingabe abbricht.
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Input Strings werden häufig für Namen (z. B. Feldnamen, Kundendaten) oder Passwörter verwendet. Da die Texteingabe auf Terminals ohne Tastatur (nur Touch oder Dreh-Drück-Steller) mühsam sein kann, sollten Standardwerte oder Auswahllisten (Input List) bevorzugt werden, wenn der Wertevorrat begrenzt ist.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - String (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-input) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*