# ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27

```{index} single: ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27
```

Das **Graphic Data** Objekt mit der **ID 46** (ab VT Version 6) dient zur Speicherung von Rohdaten für Grafiken, insbesondere im **PNG-Format**.

### Attribute und Record Format (Tabelle B.74)

Die folgende Tabelle beschreibt den Aufbau des Graphic Data Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 46 | 3 | Objekttyp = Graphic Data. |
| [1] | **Format** | Integer | 1 | 0 | 4 | Grafikformat: 0 = PNG (max. 32-bit RGBA). |
| - | **Number of bytes in raw data** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Anzahl der Bytes in den Rohdaten. |
| - | **Repeat:** {raw data} | Integer | 1 | 0 – 255 | 9 ... | Rohdaten der Grafik (Bytes). |

## Besonderheiten
Das **Graphic Data** Objekt (ab VT Version 6) dient zur Speicherung von Rohdaten für Grafiken, insbesondere im **PNG-Format**. Im Gegensatz zum klassischen *Picture Graphic* Objekt (ID 20), das auf einfachen Bitmaps basierte, nutzt dieses Objekt den Industriestandard PNG.
*   **Eigenständigkeit:** Das Objekt enthält seine eigene Farbpalette (innerhalb der PNG-Daten) und wird daher **nicht** von der *Colour Map* (ID 39) oder *Colour Palette* (ID 45) der Working Set beeinflusst.

## Verwendung
Dieses Objekt wird normalerweise nicht direkt in einer Maske platziert, sondern von einem **Scaled Graphic** Objekt (ID 48) referenziert, um es anzuzeigen und auf die gewünschte Größe zu skalieren. Es kann auch in einem *External Object Pointer* (ID 43) referenziert werden.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.27 verwiesen.*