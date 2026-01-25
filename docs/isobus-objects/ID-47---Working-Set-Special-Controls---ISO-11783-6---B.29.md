# ID 47 – Working Set Special Controls – ISO 11783-6 – B.29

```{index} single: ID 47 – Working Set Special Controls – ISO 11783-6 – B.29
```

Das **Working Set Special Controls** Objekt mit der **ID 47** (ab VT Version 6) dient zur zentralen Steuerung von pool-weiten Einstellungen wie Farben und Sprachen.

### Attribute und Record Format (Tabelle B.78)

Die folgende Tabelle beschreibt den Aufbau des Working Set Special Controls Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 47 | 3 | Objekttyp = Working Set Special Controls. |
| [1] | **Number of Bytes to follow** | Integer | 2 | 5 – 65535 | 4 – 5 | Anzahl der Bytes in diesem Objekt nach diesem Attribut. Ermöglicht Parsing-Kompatibilität. |
| [2] | **Object ID of Colour Map object** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | ID der initial zu verwendenden Colour Map (ID 39) oder NULL. |
| [3] | **Object ID of Colour Palette object** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | ID der initial zu verwendenden Colour Palette (ID 45) oder NULL. |
| - | **Number of languages pairs to follow** | Integer | 1 | 0 – 255 | 10 | Anzahl der folgenden Sprach/Länder-Code-Paare. |
| - | **Repeat:** {Language Code} | String | 2 | - | 11 – 12 ... | 2-Buchstaben Code gemäß ISO 639-1 (z. B. "de"). |
| - | {Country Code} | String | 2 | - | 13 – 14 ... | 2-Buchstaben Code gemäß ISO 3166-1 (z. B. "DE") oder "20 20" (Hex) falls nicht anwendbar. |

## Bedeutung und Funktionsweise
Dieses Objekt ist der zentrale Anlaufpunkt für das Terminal beim Laden des Pools (ab VT Version 6).
*   **Farben:** Es definiert, welche *Colour Map* und *Colour Palette* **initial** beim Aktivieren des Pools verwendet werden sollen.
*   **Sprachen:** Es definiert eine Liste von unterstützten Sprachen, die die Liste im *Working Set* Objekt (ID 0) **ersetzt**. Durch die Kombination von Sprach- und Ländercode (z. B. `pt` + `BR` vs. `pt` + `PT`) ist eine präzisere Auswahl möglich.
*   **Erweiterbarkeit:** Das Attribut `Number of Bytes to follow` erlaubt es, das Objekt in Zukunft um neue Attribute zu erweitern, ohne ältere VTs zu verwirren (diese überspringen einfach die unbekannten Bytes).

Es darf maximal **ein** Working Set Special Controls Objekt pro Objektpool geben.

## Ereignisse (Events - Tabelle B.77)

Das Objekt reagiert auf folgende Ereignisse:

*   **On Refresh:** Wird ausgelöst, wenn sich Einstellungen ändern, die einen kompletten Neuaufbau der Darstellung erfordern (z. B. Farbpalette).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.29 verwiesen.*