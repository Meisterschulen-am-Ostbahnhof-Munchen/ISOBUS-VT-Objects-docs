# ID 7 – Input boolean – ISO 11783-6 – B.8.2

```{index} single: ID 7 – Input boolean – ISO 11783-6 – B.8.2
```

Das **Input Boolean** Objekt mit der **ID 7** ermöglicht dem Bediener die Eingabe eines TRUE/FALSE-Wertes (z. B. in Form eines Kontrollkästchens).

### Attribute und Record Format (Tabelle B.16)

Die folgende Tabelle beschreibt den Aufbau des Input Boolean Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 7 | 3 | Objekttyp = Input Boolean. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Width** | Integer | 2 | 0 – 65535 | 5 – 6 | Breite und Höhe des quadratischen Feldes in Pixeln. |
| [3] | **Foreground colour** | Integer | 2 | 0 – 65534 | 7 – 8 | Objekt-ID eines Font Attributes Objekts für die Farbe des Indikators (nur Schriftfarbe relevant). |
| [4] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 9 – 10 | Objekt-ID einer Number Variable zur Speicherung des Wertes. (65535 = Wert direkt in Attribut 5). |
| [5] | **Value** | Integer | 1 | 0, 1 – 255 | 11 | Wert: 0 = FALSE, >0 = TRUE. (Nur genutzt, wenn Variable reference NULL ist). |
| [6] | **Enabled** | Integer | 1 | 0 oder 1 | 12 | 0 = Deaktiviert, 1 = Aktiviert. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Darstellung
Das VT visualisiert den Booleschen Wert (z. B. als Checkbox).
*   **Wert 0:** Hintergrundfarbe wird gezeichnet.
*   **Wert > 0:** Indikator wird in Vordergrundfarbe auf Hintergrund gezeichnet.

## Ereignisse (Events - Tabelle B.15)

Das Input Boolean Objekt reagiert auf folgende Ereignisse:

*   **On Enable:** Wenn das Objekt aktiviert wird.
*   **On Disable:** Wenn das Objekt deaktiviert wird.
*   **On Input Field Selection:** Bei Fokus/Auswahl durch den Bediener.
*   **On Input Field De-selection:** Bei Fokusverlust.
*   **On Entry of Value:** Wenn der Bediener einen neuen Wert bestätigt (ENTER). Sendet `Change Numeric Value`.
*   **On Change Value:** Wenn der Wert (z.B. durch Variable) geändert wird.
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung für die Implementierung
Das Input Boolean ist ideal für einfache Ja/Nein-Optionen oder das Aktivieren/Deaktivieren von Maschinenfunktionen. Da die grafische Ausprägung (Häkchen-Stil) vom VT-Hersteller abhängt, sorgt dieses Objekt für ein konsistentes Erscheinungsbild innerhalb der Terminal-Oberfläche.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Boolean](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/boolean) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*