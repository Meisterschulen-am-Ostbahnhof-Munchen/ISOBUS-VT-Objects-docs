# ID 47 – Working Set Special Controls – ISO 11783-6 – B.29

Das **Working Set Special Controls** Objekt mit der **ID 47** (ab VT Version 6) dient zur zentralen Steuerung von pool-weiten Einstellungen wie Farben und Sprachen.

## Technische Attribute (gemäß Tabelle B.78)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 47 (Working Set Special Controls). |
| 1 | **Number of Bytes** | Integer 2 | Ermöglicht das Überspringen zukünftiger Erweiterungen. |
| 2 | **Colour Map ID** | Integer 2 | ID der initial zu verwendenden *Colour Map* (ID 39). |
| 3 | **Colour Palette ID** | Integer 2 | ID der initial zu verwendenden *Colour Palette* (ID 45). |
| - | **Num. of Lang. pairs** | Integer 1 | Anzahl der folgenden Sprach/Länder-Kürzel. |

### Sprachen-Liste (Wiederholung)
*   **Language Code:** 2-Buchstaben Code gemäß ISO 639-1 (z. B. "de", "en").
*   **Country Code:** 2-Buchstaben Code gemäß ISO 3166-1 (z. B. "DE", "US").

## Bedeutung
Dieses Objekt ist der zentrale Anlaufpunkt für das Terminal beim Laden des Pools. Es überschreibt beispielsweise die Sprachenliste im *Working Set* Objekt (ID 0), falls hier detailliertere Informationen hinterlegt sind. Es sorgt dafür, dass die richtigen Farben und Sprachen von der ersten Sekunde an korrekt geladen werden.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.29 verwiesen.*
