# ID 40 – Object Label Reference List – ISO 11783-6 – B.21

```{index} single: ID 40 – Object Label Reference List – ISO 11783-6 – B.21
```

Das **Object Label Reference List** Objekt mit der **ID 40** (ab VT Version 5) wird verwendet, um Objekten (wie Variablen oder Eingabefeldern) eine Liste von Beschriftungsobjekten (Labels) zuzuordnen.

## Technische Attribute (gemäß Tabelle B.64)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 40 (Object Label Reference List). |
| - | **Number of objects** | Integer 1 | Anzahl der Referenzen in der Liste. |

### Struktur der Liste (Wiederholung)
*   **Object ID:** Die ID des Objekts, dem ein Label zugewiesen werden soll (z. B. ein *Input Number* Objekt).
*   **Label String Object ID:** Die ID eines *String Variable* oder *Output String* Objekts, das als Label fungiert.
*   **Font Attributes Object ID:** Optionale Schriftattribute für das Label.

## Bedeutung
Dieses Objekt hilft dem Terminal, kontextsensitive Hilfetexte oder Beschriftungen anzuzeigen, besonders wenn das Terminal selbst Layout-Entscheidungen trifft (z. B. in User-Layouts).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.21 verwiesen.*
