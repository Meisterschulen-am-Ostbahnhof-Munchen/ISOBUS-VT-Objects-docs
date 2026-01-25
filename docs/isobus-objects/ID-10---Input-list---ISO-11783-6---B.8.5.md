# ID 10 – Input list – ISO 11783-6 – B.8.5

```{index} single: ID 10 – Input list – ISO 11783-6 – B.8.5
```

Das **Input List** Objekt mit der **ID 10** ermöglicht dem Bediener die Auswahl eines Elements aus einer vordefinierten Liste von Objekten. Es wird häufig für Dropdown-Menüs oder Auswahllisten verwendet.

### Attribute und Record Format (Tabelle B.20)

Die folgende Tabelle beschreibt den Aufbau des Input List Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 10 | 3 | Objekttyp = Input List. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Feldes (im geschlossenen Zustand). |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Feldes (im geschlossenen Zustand). |
| [3] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | Verweis auf ein Number Variable Objekt für den Index. |
| [4] | **Value** | Integer | 1 | 0 – 255 | 10 | Aktueller gewählter Index (0-254). 255 = keine Auswahl. (Nur wenn Variable Reference == NULL). |
| - | **Number of list items** | Integer | 1 | 0 – 255 | 11 | Anzahl der Objekte in der Liste. |
| [5] | **Options** | Bitmask | 1 | 0 – 3 | 12 | Bit 0: Enabled (0=Deaktiviert, 1=Aktiviert)<br>Bit 1: Real time editing (1=Wert bei Änderung senden). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 14 + ... | Objekt-ID eines Listeneintrags (angezeigt als Option). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Darstellung
Die Input List zeigt im normalen Zustand nur das aktuell ausgewählte Element an.
*   **Auswahl:** Wenn der Bediener das Objekt öffnet, zeigt das VT die Liste der verfügbaren Einträge an.
*   **Index:** Der übertragene Wert ist der **nullbasierte Index** des gewählten Elements in der Liste.
*   **Spezialwert 255:** Signalisiert "keine Auswahl".

## Ereignisse (Events - Tabelle B.19)

Das Input List Objekt reagiert auf folgende Ereignisse:

*   **On Enable / On Disable:** Zustandsänderung des Objekts.
*   **On Input Field Selection / De-selection:** Fokus-Ereignisse.
*   **On Entry of Value:** Wenn der Bediener eine Auswahl bestätigt (ENTER). Sendet `Change Numeric Value`.
*   **On Change Value:** Wenn der Index durch das Programm geändert wird.
*   **On Entry of New Value:** Ausgelöst, wenn sich der Wert ändert (oft redundant zu "On Entry of Value").
*   **On ESC:** Abbruch der Auswahl.
*   **On Change Attribute:** Allgemeine Attributänderung.
*   **On Change Size:** Reaktion auf Größenänderung.

## Bedeutung für die Implementierung
Input Lists sind hervorragend geeignet, um Fehleingaben zu vermeiden, da der Bediener nur aus gültigen Optionen wählen kann. Da die Darstellung (z. B. Schriftgröße in der aufgeklappten Liste) vom VT gesteuert wird, ist eine gute Lesbarkeit auf verschiedenen Endgeräten gewährleistet.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - List (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/list-input) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*