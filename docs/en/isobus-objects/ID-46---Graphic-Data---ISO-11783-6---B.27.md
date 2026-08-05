# ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27
The **Graphic Data** object with **ID 46** (from VT version 6 onwards) is used to store raw data for graphics, especially in **PNG format**.
### Attributes and Record Format (Table B.74)
The following table describes the structure of the Graphic Data object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 46 | 3 | Object type = Graphic Data. |

| [1] | **Format** | Integer | 1 | 0 | 4 | Graphic format: 0 = PNG (max. 32-bit RGBA). |

| - | **Number of bytes in raw data** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Number of bytes in the raw data. |

| - | **Repeat:** {raw data} | Integer | 1 | 0 – 255 | 9 ... | Raw data of the graphic (bytes). |

## Special Features
The **Graphic Data** object (from VT version 6 onwards) is used to store raw data for graphics, especially in **PNG format**. Unlike the classic *Picture Graphic* object (ID 20), which was based on simple bitmaps, this object uses the industry standard PNG.

**Independence:** The object contains its own color palette (within the PNG data) and is therefore **not** affected by the *Color Map* (ID 39) or *Color Palette* (ID 45) of the Working Set.

## Usage

This object is not normally placed directly in a mask, but is referenced by a **Scaled Graphic** object (ID 48) to display and scale it to the desired size. It can also be referenced in an *External Object Pointer* (ID 43).

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.27.*