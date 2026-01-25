# ID 2 – Alarm Mask – ISO 11783-6 – B.3

```{index} single: ID 2 – Alarm Mask – ISO 11783-6 – B.3
```

Die **Alarm Mask** (Alarmmaske) mit der **ID 2** dient zur Anzeige kritischer Informationen oder Warnungen. Sie hat Vorrang vor normalen Datenmasken und kann je nach Priorität das gesamte Display oder Teile davon überlagern.

### Attribute und Record Format (Tabelle B.6)

Die folgende Tabelle beschreibt den Aufbau des Alarm Mask Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 2 | 3 | Objekttyp = Alarm Mask. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe der Maske. |
| [2] | **Soft Key Mask** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Objekt-ID der zugehörigen Soft Key Mask (65535 = NULL). |
| [3] | **Priority** | Integer | 1 | 0 – 2 | 7 | 0 = Hoch, 1 = Mittel, 2 = Niedrig. |
| [4] | **Acoustic signal** | Integer | 1 | 0 – 3 | 8 | 0 = Höchste Prio, 1 = Mittel, 2 = Niedrig, 3 = Aus. |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 9 | Anzahl der direkt enthaltenen Objekte. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 13 + ... | X-Position relativ zur Maske (Pixel). |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 15 + ... | Y-Position relativ zur Maske (Pixel). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Prioritätsstufen und Darstellung
Die Priorität steuert nicht nur die Reihenfolge der Alarme, sondern oft auch deren visuelle Darstellung auf dem VT:

*   **High Priority (0):** Der Bediener ist in Gefahr oder es liegt eine schwere Fehlfunktion vor. Diese Alarme müssen sofort quittiert werden oder erzwingen den Fokus des Terminals.
*   **Medium Priority (1):** Normale Fehlfunktion der Maschine.
*   **Low Priority (2):** Nur zur Information (Statusmeldungen).

## Ereignisse (Events - Tabelle B.5)

Die Alarmmaske reagiert auf folgende Ereignisse:

*   **On Show:** Ausgelöst, wenn die Maske sichtbar wird. Das VT sendet eine `VT Status` Nachricht.
*   **On Hide:** Ausgelöst, wenn die Maske vom Display entfernt wird.
*   **On Refresh:** Ausgelöst bei Änderungen an Objekten innerhalb der Maske.
*   **On Change Priority:** Bei Änderung der Priorität bewertet das VT alle aktiven Alarme neu.
*   **On Change Soft Key Mask:** Wechselt die Softkey-Belegung bei aktiver Alarmmaske.
*   **On Change Child Location / Position:** Aktualisierung der Kind-Objekte.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Verhalten bei mehreren Alarmen
Wenn mehrere Alarmmasken von verschiedenen Arbeitsgruppen gleichzeitig aktiv sind, bestimmt die Priorität (AID 3), welche Maske im Vordergrund steht. Bei gleicher Priorität liegt die Entscheidung meist beim VT (oft zeitliche Abfolge).

## Bedeutung für die Implementierung
Alarmmasken sollten sparsam und nur für echte Warnungen eingesetzt werden, da sie den Arbeitsfluss des Bedieners unterbrechen. Es ist wichtig, die passende akustische Unterstützung (AID 4) zu wählen, um die Aufmerksamkeit zu steuern, ohne den Bediener zu stressen.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Alarm Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/alarm-mask) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*