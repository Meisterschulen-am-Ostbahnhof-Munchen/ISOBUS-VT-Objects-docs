# ID 42 – External Reference NAME – ISO 11783-6 – B.23

```{index} single: ID 42 – External Reference NAME – ISO 11783-6 – B.23
```

Das **External Reference NAME** Objekt mit der **ID 42** (ab VT Version 5) identifiziert ein anderes Working Set auf dem Bus über seinen eindeutigen ISO-NAME.

### Attribute und Record Format (Tabelle B.68)

Die folgende Tabelle beschreibt den Aufbau des External Reference NAME Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 42 | 3 | Objekttyp = External Reference NAME. |
| [1] | **Options** | Bitmask | 1 | 0 – 1 | 4 | Bit 0: Enabled (1=Referenz aktiv, 0=Deaktiviert). |
| [2] | **NAME 0** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Byte 1–4 des NAME (ISO 11783-5) des referenzierten Working Sets. |
| [3] | **NAME 1** | Integer | 4 | 0 – 2^32-1 | 9 – 12 | Byte 5–8 des NAME des referenzierten Working Sets. |

## Funktionsweise
Dieses Objekt fungiert als "Adressbucheintrag". Wenn eine ECU ein Objekt von einer anderen ECU einbinden möchte, nutzt sie diesen Eintrag, um dem Terminal mitzuteilen, von welcher ECU (identifiziert durch den NAME) das Objekt stammt.
*   **Aktivierung:** Sollte initial deaktiviert sein. Wenn das referenzierte Working Set online ist, kann die ECU dieses Objekt aktivieren.

## Ereignisse (Events - Tabelle B.67)

Das External Reference NAME Objekt reagiert auf folgende Ereignisse:

*   **On Change Attribute:** Wird ausgelöst durch das Kommando `Change Attribute`. Das VT evaluiert alle aktuell angezeigten External Object Pointer neu, die auf dieses NAME-Objekt verweisen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.23 verwiesen.*