# ID 39 – Colour Map – ISO 11783-6 – B.17
The **Colour Map** object with **ID 39** (optional from VT version 4/5, mandatory from VT version 6) allows a working set to redefine the terminal's color table at runtime.
### Attributes and Record Format (Table B.57)
The following table describes the structure of the Colour Map object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 39 | 3 | Object type = Colour Map. |
| - | **Number of colour indexes to follow** | Integer | 2 | 2, 16, 256 | 4 – 5 | Number of following entries. Must match the VT's color depth (see Get Hardware). |
| - | **Repeat:** {Colour Map} | Integer | var. | 0 – 255 | 6 ... | List of colour indexes. |

### Structure of the entries
The entries define a redirection of the colour indexes.

* **Example:** If the entry at index 0 has the value 1, colour 1 (white) will now be displayed wherever colour 0 (black) was used in the design.
* The length of the entries depends on the VT type:
* **Type 0 (Monochrome):** 2 entries.
* **Type 1 (16 colours):** 16 entries.
* * **Type 2 (256 colors):** 256 entries.

## Functionality
Normally, a terminal uses a standard color palette (e.g., 256 colors according to ISO). With the Colour Map, a working set can define, for example, that color index 1 (default: red) should be displayed as blue instead.

* **Indirection:** This provides a level of indirection. Instead of changing each object individually, the entire application's color scheme can be changed (e.g., day/night mode) simply by toggling the Colour Map.
* **Activation:** A Colour Map is activated using the command ``Select Colour Map``.

## Note on VT Version 6
Starting with version 6, the `Colour Palette` object (ID 45) is also supported, which allows the RGB values of the colors themselves to be changed. The Colour Map maps indices to indices, while the Colour Palette maps indices to RGB values.

----
*Note: For detailed specifications, please refer to the official ISO 11783-6:2018, B.17.*