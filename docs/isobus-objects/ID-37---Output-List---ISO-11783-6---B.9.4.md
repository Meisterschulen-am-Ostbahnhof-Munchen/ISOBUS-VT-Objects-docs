# ID 37 – Output List – ISO 11783-6 – B.9.4

```{index} single: ID 37 – Output List – ISO 11783-6 – B.9.4
```

Das **Output List** Objekt mit der **ID 37** (ab VT Version 4) wird verwendet, um eines von mehreren Objekten aus einer Liste anzuzeigen. Welches Objekt aktuell sichtbar ist, wird über einen Index (Value) gesteuert.

### Attribute und Record Format (Tabelle B.25)

Die folgende Tabelle beschreibt den Aufbau des Output List Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 37 | 3 | Objekttyp = Output List. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Anzeigebereichs in Pixeln. Clipping erfolgt außerhalb. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Anzeigebereichs in Pixeln. Clipping erfolgt außerhalb. |
| [3] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | Verweis auf ein Number Variable Objekt für den Index. |
| [4] | **Value** | Integer | 1 | 0 – 255 | 10 | Aktueller Index (0-254). 255 = keine Anzeige. Nur wenn Variable Ref == NULL. |
| - | **Number of list items** | Integer | 1 | 0 – 255 | 11 | Anzahl der Objekte in der Liste. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 12 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 13 + ... | Objekt-ID eines Listenelements (was angezeigt werden soll). NULL = Leerer Platzhalter. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise
Die Output List verhält sich ähnlich wie eine Animation, wird aber manuell über den Index gesteuert.
*   **Index:** Der angezeigte Inhalt wird durch den Wert (Value oder Variable) bestimmt. Index 0 zeigt das erste Objekt in der Liste.
*   **Spezialwert 255:** Bei Wert 255 wird nichts angezeigt (das Objekt ist unsichtbar).
*   **NULL-Pointer:** Wenn ein Listeneintrag die ID NULL (65535) hat, wird für diesen Index ebenfalls nichts angezeigt.

## Ereignisse (Events - Tabelle B.24)

Das Output List Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der Index ändert. Das VT aktualisiert die Anzeige.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Change Size:** Reaktion auf Größenänderung.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - List (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/list-output) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.9.4 verwiesen.*