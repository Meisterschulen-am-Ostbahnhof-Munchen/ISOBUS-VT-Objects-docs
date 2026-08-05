# ID 47 – Working Set Special Controls – ISO 11783-6 – B.29
The **Working Set Special Controls** object with **ID 47** (from VT version 6 onwards) is used for the central control of pool-wide settings such as colors and languages.
### Attributes and Record Format (Table B.78)
The following table describes the structure of the Working Set Special Controls object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 47 | 3 | Object type = Working Set Special Controls. |
| [1] | **Number of Bytes to follow** | Integer | 2 | 5 – 65535 | 4 – 5 | Number of bytes in this object after this attribute. Enables parsing compatibility. |
| [2] | **Object ID of Colour Map object** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | ID of the initial Colour Map to be used (ID 39) or NULL. |
| [3] | **Object ID of Colour Palette object** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | ID of the initial Colour Palette to be used (ID 45) or NULL. |
| - | **Number of languages pairs to follow** | Integer | 1 | 0 – 255 | 10 | Number of the following language/country code pairs. |
| - | **Repeat:** {Language Code} | String | 2 | - | 11 – 12 ... | 2-letter code according to ISO 639-1 (e.g., "de"). |
| - | {Country Code} | String | 2 | - | 13 – 14 ... | 2-letter code according to ISO 3166-1 (e.g., "DE") or "20 20" (Hex) if not applicable. |

## Meaning and Functionality

This object is the central point of contact for the terminal when loading the pool (from VT version 6 onwards).

* **Colors:** It defines which *Color Map* and *Color Palette* should be used **initially** when activating the pool.

`` * **Languages:** This defines a list of supported languages that **replaces** the list in the *Working Set* object (ID 0). Combining language and country codes (e.g., `pt` + `BR` vs. `pt` + `PT`) allows for more precise selection.

* **Extensibility:** The attribute `Number of Bytes to follow` allows the object to be extended with new attributes in the future without confusing older VTs (they simply skip the unknown bytes).

There can be a maximum of **one** Working Set Special Controls object per object pool.

## Events (Table B.77)

The object responds to the following events:

* **On Refresh:** Triggered when settings change that require a complete rebuild of the display (e.g., color palette).

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.29.*
