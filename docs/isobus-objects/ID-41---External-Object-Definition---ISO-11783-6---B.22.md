# ID 41 – External Object Definition – ISO 11783-6 – B.22

```{index} single: ID 41 – External Object Definition – ISO 11783-6 – B.22
```

Das **External Object Definition** Objekt mit der **ID 41** (ab VT Version 5) ist Teil des Mechanismus für **Working-Set-übergreifende Objektreferenzen**. Es definiert, welche Objekte eines eigenen Pools von anderen Working Sets referenziert werden dürfen.

### Attribute und Record Format (Tabelle B.66)

Die folgende Tabelle beschreibt den Aufbau des External Object Definition Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 41 | 3 | Objekttyp = External Object Definition. |
| [1] | **Options** | Bitmask | 1 | 0 – 1 | 4 | Bit 0: Enabled (1=Freigabe aktiv, 0=Deaktiviert). |
| [2] | **NAME 0** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Byte 1–4 des NAME (ISO 11783-5) des berechtigten Working Sets. |
| [3] | **NAME 1** | Integer | 4 | 0 – 2^32-1 | 9 – 12 | Byte 5–8 des NAME des berechtigten Working Sets. |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 13 | Anzahl der freigegebenen Objekte. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 14 + ... | Objekt-ID eines Objekts aus dem eigenen Pool, das für das externe WS freigegeben wird. |

## Funktionsweise
Damit Working Set A ein Objekt von Working Set B anzeigen kann (via *External Object Pointer*), muss Working Set B dieses Objekt explizit in einer *External Object Definition* für Working Set A freigeben. Dies dient der Sicherheit und Kontrolle über die eigenen Pool-Ressourcen.
*   **Empfehlung:** Das `Enabled`-Bit sollte beim Laden des Pools zunächst auf 0 gesetzt sein und erst zur Laufzeit aktiviert werden, wenn der NAME des Partners bekannt und aktuell ist.

## Ereignisse (Events - Tabelle B.65)

Das External Object Definition Objekt reagiert auf folgende Ereignisse:

*   **On Change Attribute:** Wird ausgelöst durch das Kommando `Change Attribute` (z. B. Aktivieren/Deaktivieren). Das VT evaluiert alle aktuell angezeigten External Object Pointer neu, die auf Objekte dieses WS verweisen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.22 verwiesen.*