# ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6

```{index} single: ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6
```

Das **Extended Input Attributes** Objekt mit der **ID 38** (ab VT Version 4) dient der Validierung von Texteingaben (Input String) bei Verwendung von **WideStrings** (Unicode).

### Attribute und Record Format (Tabelle B.53)

Die folgende Tabelle beschreibt den Aufbau des Extended Input Attributes Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 38 | 3 | Objekttyp = Extended Input Attributes. |
| [1] | **Validation type** | Integer | 1 | 0 – 1 | 4 | 0=Erlaubte Zeichen (Whitelist), 1=Verbotene Zeichen (Blacklist). |
| - | **Number of code planes to follow** | Integer | 1 | 1 – 17 | 5 | Anzahl der definierten Unicode-Ebenen. |
| - | **Repeat:** {Code plane number} | Integer | 1 | 0 – 16 | 6 ... | Nummer der Unicode-Ebene (0 = BMP). |
| - | {Number of character ranges to follow} | Integer | 1 | 1 – 255 | 7 ... | Anzahl der Bereiche in dieser Ebene. |
| - | **Repeat:** {{First character}} | Integer | 2 | 0 – 65535 | 8 ... | Startzeichen des Bereichs (WideChar). |
| - | {{Last character}} | Integer | 2 | 0 – 65535 | 10 ... | Endzeichen des Bereichs (WideChar). |

## Funktionsweise
Während das einfache *Input Attributes* Objekt (ID 26) nur 8-Bit Zeichen unterstützt, ermöglicht dieses Objekt die feingranulare Steuerung erlaubter Unicode-Zeichen (WideString). Dies wird für Sprachen benötigt, die mehr als 256 Zeichen umfassen (z. B. Asiatisch, Kyrillisch).
Die Validierung erfolgt durch Definition von Bereichen innerhalb von Unicode-Ebenen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.14.6 verwiesen.*