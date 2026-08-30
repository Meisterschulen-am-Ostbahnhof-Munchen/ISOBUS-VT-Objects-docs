# ID 11 – Output string – ISO 11783-6 – B.9.2
The **Output String** object with **ID 11** is used for the purely visual display of text strings on the Virtual Terminal. Unlike the *Input String*, this object does not allow direct editing by the user.
### Attributes and Record Format (Table B.22)
The following table describes the structure of the Output String object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 11 | 3 | Object type = Output String. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the text field in pixels. Clipping occurs outside this range. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the text field in pixels. Clipping occurs outside this range. |
| [3] | **Background color** | Integer | 1 | 0 – 255 | 8 | Background color (only when transparency is disabled). |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Object ID of a font attribute object (color, size, font). |
| [5] | **Options** | Bitmask | 1 | 0 – 7 | 11 | Bit 0: Transparent qzmsdocs000000 qz Bit 1: Auto-Wrap qzmsdocs000001 qz Bit 2: Wrap on Hyphen |
| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Reference to a string variable object. If NULL, the value is stored directly in the "Value" attribute. |
| [7] | **Justification** | Integer | 1 | 0 – 15 | 14 | Text alignment: Bits 0-1 (Horizontal): 0=Left, 1=Middle, 2=Right. Bits 2-3 (Vertical): 0=Top, 1=Middle, 2=Bottom. |
| - | **Length** | Integer | 2 | 0 – 65535 | 15 – 16 | Length of the fixed text value in bytes. If variable Ref != NULL, this can be 0. |
| - | **Value** | String | Length | - | 17... | Static text content (only if variable Reference == NULL). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Number of following macro references. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Special Features
- **Transparency:** When bit 0 is set, the background of the text field is transparent, and the background color of the mask or an underlying object remains visible.
- **Auto-Wrap:** Enables the display of multi-line text within the defined `Width` and `Height`.
- **Alignment:** Alignment is pixel-perfect within the frame. This is especially important for vertical centering with different fonts.
- * **Clipping:** Text that extends beyond the defined `Width` or `Height` is clipped by the VT.

## Static Text vs. Dynamic Variable
- **Static Text:** The text is defined directly in the object pool and its properties can only be changed at runtime using the command `Change Attribute` (AID 5 or 7).
- **Dynamic Text:** By linking it to a **string variable** (AID 6), the control unit (ECU) can update the text content at any time using `Change String Value` without having to reload the object itself.

## Events (Events - Table B.21)

The output string object reacts to the following events:

- **On Change Value:** Triggered when the displayed value changes (e.g., variable updated). The VT redraws the object.
- **On Refresh:** Triggered when the VT needs to redraw the object (e.g., mask change).
- **On Change Background Colour:** Responds to a color change.
- **On Change Attribute:** Responds to general attribute changes.
- **On Change Size:** Responds to a size change.

## Implementation Implementation Implementation Implementation (IM)
Output strings are the primary method for status messages, labels, and unit displays. For texts available in multiple languages, it is recommended to control the text via variables or to maintain a separate mask/pool for each language.

Further information and examples can be found in the [ISOBUS Wiki - String (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-output) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*