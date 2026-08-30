# ID 8 – Input string – ISO 11783-6 – B.8.3
The **Input String** object with **ID 8** is used for inputting and displaying text strings by the operator.
### Attributes and Record Format (Table B.17)
The following table describes the structure of the Input String object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 8 | 3 | Object type = Input String. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the input field in pixels. Clipping occurs outside this range. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the input field in pixels. Clipping occurs outside this range. |
| [3] | **Background color** | Integer | 1 | 0 – 255 | 8 | Background color (only when transparency is disabled). |
| [4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Object ID of a font attribute object (color, size, font). |
| [5] | **Input attributes** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Object ID of an input attribute object for validation or NULL. |
[6] | **Options** | Bitmask | 1 | 0 – 7 | 13 | Bit 0: Transparent <br> Bit 1: Auto-Wrap <br> Bit 2: Wrap on Hyphen. |
[7] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 14 – 15 | Reference to a string variable object. If NULL, the value is stored directly in the "Value" attribute. |
[8] | **Justification** | Integer | 1 | 0 – 15 | 16 | Text alignment: Bits 0-1 (Horizontal): 0=Left, 1=Middle, 2=Right. Bits 2-3 (Vertical): 0=Top, 1=Middle, 2=Bottom. |
| - | **Length** | Integer | 1 | 0 – 255 | 17 | Maximum length in bytes. If Variable Reference != NULL, this can be 0. |
| - | **Value** | String | Length | - | 18 ... | Initial value of the string (only if Variable Reference == NULL). |
| [9] | **Enabled** | Integer | 1 | 0 or 1 | var. | 0 = Disabled, 1 = Enabled. Position in the record depends on the length of the Value field. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Number of subsequent macro references. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Options

The Input String object offers flexible text display options:

- **Auto-Wrap:** When enabled (Bit 1), the VT automatically wraps the text if the field width is exceeded.
- **Adjustment:** Horizontal and vertical alignment are controlled via AID 8.
- **Validation:** By linking to a `Input Attributes` object, input can be restricted to specific character sets.

## Events (Table B.15)

The Input String object reacts to the following events:

- **On Enable:** When the object is enabled.
- **On Disable:** When the object is disabled.
- **On Input Field Selection:** When the operator focuses/selects the field.
- **On Input Field De-selection:** When focus is lost.
- **On Entry of Value:** When the operator confirms the text input (ENTER). Sends `Change String Value`.
- **On Change Value:** When the value is changed (e.g., by a variable).
- **On ESC:** When the operator cancels the input.
- **On Change Background Colour:** Responds to a change in background color.
- **On Change Attribute:** Responds to general attribute changes.

## Implementation Implementation Implementation Significance
Input strings are frequently used for names (e.g., field names, customer data) or passwords. Since text input on terminals without a keyboard (only touch or rotary push-button) can be cumbersome, default values or input lists should be preferred when the range of values is limited.

Further information and examples can be found in the ISOBUS Wiki - String (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-input) by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, refer to the official ISO 11783-6:2018.*