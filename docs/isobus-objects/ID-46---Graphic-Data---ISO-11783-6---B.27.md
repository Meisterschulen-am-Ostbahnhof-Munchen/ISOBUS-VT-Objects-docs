# ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27

```{index} single: ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27
```

Das **Graphic Data** Objekt mit der **ID 46** (ab VT Version 6) dient zur Speicherung von Rohdaten für Grafiken, insbesondere im **PNG-Format**.

## Technische Attribute (gemäß Tabelle B.74)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 46 (Graphic Data). |
| 1 | **Format** | Integer 1 | Aktuell nur 0 = PNG (32-bit RGBA maximum). |
| - | **Number of bytes** | Integer 4 | Größe der folgenden Rohdaten in Bytes. |
| - | **Raw data** | Binary | Die eigentlichen PNG-Daten. |

## Besonderheiten
Im Gegensatz zum klassischen *Picture Graphic* Objekt (ID 20), das oft auf proprietären Formaten oder einfachen Bitmaps basierte, nutzt dieses Objekt den Industriestandard PNG.
*   **Eigenständigkeit:** Das Objekt enthält seine eigene Farbpalette und wird daher **nicht** von der *Colour Map* oder *Colour Palette* der Working Set beeinflusst.

## Verwendung
Dieses Objekt wird normalerweise nicht direkt in einer Maske platziert, sondern von einem *Scaled Graphic* Objekt (ID 48) referenziert, um es anzuzeigen und ggf. zu skalieren.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.27 verwiesen.*
