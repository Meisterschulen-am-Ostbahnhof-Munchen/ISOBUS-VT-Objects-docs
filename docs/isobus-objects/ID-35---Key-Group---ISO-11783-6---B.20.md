# ID 35 – Key Group – ISO 11783-6 – B.20

```{index} single: ID 35 – Key Group – ISO 11783-6 – B.20
```

Das **Key Group** Objekt mit der **ID 35** dient dazu, eine Gruppe von Softkeys zusammenzufassen. Dies wird primär in Verbindung mit **User-Layout Soft Key Masks** verwendet (ab VT Version 4).

### Attribute und Record Format (Tabelle B.63)

Die folgende Tabelle beschreibt den Aufbau des Key Group Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 35 | 3 | Objekttyp = Key Group. |
| [1] | **Options** | Bitmask | 1 | 0 – 3 | 4 | Bit 0: Available (0=Nicht verfügbar/geblankt, 1=Verfügbar)<br>Bit 1: Transparent (1=Hintergrundfarbe der Keys wird ignoriert). |
| [2] | **Name** | Integer | 2 | 0 – 65534 | 5 – 6 | Objekt-ID eines Output String oder Object Pointers (Name für Mapping-Screen). |
| - | **Key Group Icon** | Integer | 2 | 0 – 65534, 65535 | 7 – 8 | Objekt-ID eines Output Objects (Icon für Mapping-Screen). |
| - | **Number of objects to follow** | Integer | 1 | 1 – 4 | 9 | Anzahl der Key-Objekte in dieser Gruppe. Max. 4. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Objekt-ID eines Key-Objekts oder Object Pointers auf Key. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Ereignisse (Events - Tabelle B.62)

Das Key Group Objekt reagiert auf folgende Ereignisse:

*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

## Bedeutung und Funktionsweise
Das Key Group Objekt dient dazu, eine logisch zusammengehörige Gruppe von Softkeys zu definieren (z.B. "Hydraulikfunktionen"). Diese Gruppe wird primär in **User-Layout Soft Key Masks** verwendet.
*   **User-Mapping:** Der Benutzer kann am Terminal entscheiden, an welcher Position er diese Gruppe von Tasten in seiner Softkey-Leiste haben möchte. Das VT zwingt den Benutzer, die Gruppe *als Ganzes* zu platzieren, um die logische Zusammengehörigkeit nicht zu zerstören.
*   **Transparenz:** Es wird empfohlen, Key Groups transparent zu gestalten, damit das VT die Hintergrundfarbe der Tasten einheitlich setzen kann.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.20 verwiesen.*