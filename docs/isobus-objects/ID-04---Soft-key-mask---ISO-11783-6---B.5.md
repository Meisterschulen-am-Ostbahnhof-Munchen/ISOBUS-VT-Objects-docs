# ID 4 – Soft Key Mask – ISO 11783-6 – B.5

```{index} single: ID 4 – Soft Key Mask – ISO 11783-6 – B.5
```

Die **Soft Key Mask** (Softkey-Maske) mit der **ID 4** ist ein spezieller Container, der die Belegung der physischen oder virtuellen Softkeys am Rand des Terminals definiert. Sie wird in der Regel einer Datenmaske oder Alarmmaske fest zugeordnet.

### Attribute und Record Format (Tabelle B.10)

Die folgende Tabelle beschreibt den Aufbau des Soft Key Mask Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 4 | 3 | Objekttyp = Soft Key Mask. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. Das Key-Objekt hat ein eigenes Hintergrundattribut, das dieses überschreiben kann. |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 5 | Anzahl der enthaltenen Objekte (Keys oder Pointer). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 6 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Objekt-ID eines enthaltenen Key-Objekts oder Pointers. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Funktionsweise und Zuweisung
Eine Softkey-Maske enthält eine Liste von **Key Objekten** (ID 5), **Object Pointern** (ID 27) oder **External Object Pointern** (ID 43).
*   **Reihenfolge:** Die Zuweisung zu den physischen Tasten am Terminal erfolgt strikt in der Reihenfolge der Liste.
*   **NULL-Pointer:** Pointers auf die NULL Object ID reservieren eine Position (die folgenden Keys rücken nicht nach). Pointers auf NULL am Ende der Liste werden nicht angezeigt und nicht für das Paging berücksichtigt.
*   **Paging:** Übersteigen die definierten Keys die Kapazität des VT, erstellt dieses automatisch Navigationshilfen (Pfeiltasten) zum Umblättern.

## Ereignisse (Events - Tabelle B.9)

Die Softkey-Maske reagiert auf folgende Ereignisse:

*   **On Show:** Ausgelöst, wenn die Maske sichtbar wird. Das VT zeichnet alle Kind-Objekte in der definierten Reihenfolge.
*   **On Hide:** Ausgelöst beim Entfernen der Maske.
*   **On Change Background Colour:** Reaktion auf eine Änderung der Hintergrundfarbe der Leiste.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Zusammenspiel mit Datenmasken
Jede Datenmaske (ID 1) verweist auf eine Soft Key Mask (ID 4). 
*   Wird die Datenmaske gewechselt, wechselt das VT automatisch auch die Softkey-Belegung.
*   Über das Kommando `Change Soft Key Mask` kann die Belegung der Tasten auch zur Laufzeit geändert werden, ohne die Hauptmaske zu wechseln.

## Bedeutung für die Implementierung
Das Design der Softkey-Masken ist entscheidend für die Ergonomie. Entwickler sollten darauf achten, dass wichtige Funktionen (z. B. "Zurück" oder "Home") immer an der gleichen Position liegen. Durch den Einsatz von NULL-Pointern kann ein Springen der Tasten beim Wechsel zwischen verschiedenen Masken verhindert werden.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Softkey Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/softkey-mask) von Tobias Tenberg.

## 🎧 Podcast

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*