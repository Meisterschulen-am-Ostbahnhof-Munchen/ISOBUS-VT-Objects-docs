# ID 7 – Input Boolean – ISO 11783-6 – B.8.2

The **Input Boolean** object with **ID 7** allows the operator to enter a TRUE/FALSE value (e.g., in the form of a checkbox).

### Attributes and Record Format (Table B.16)

The following table describes the structure of the Input Boolean object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 7 | 3 | Object type = Input Boolean. |
[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. |
[2] | **Width** | Integer | 2 | 0 – 65535 | 5 – 6 | Width and height of the square field in pixels. |
[3] | **Foreground color** | Integer | 2 | 0 – 65534 | 7 – 8 | Object ID of a Font Attribute object for the indicator color (only font color is relevant). |
[4] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 9 – 10 | Object ID of a Number variable to store the value. (65535 = value directly in attribute 5). |
[5] | **Value** | Integer | 1 | 0, 1 – 255 | 11 | Value: 0 = FALSE, >0 = TRUE. (Only used if variable reference is NULL). |
| [6] | **Enabled** | Integer | 1 | 0 or 1 | 12 | 0 = Disabled, 1 = Enabled. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Number of following macro references. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Display

The VT visualizes the Boolean value (e.g., as a checkbox). * **Value 0:** Background color is drawn.

- **Value > 0:** Indicator is drawn in the foreground color on the background.

## Events (Table B.15)

The Input Boolean object reacts to the following events:

- **On Enable:** When the object is enabled.
- **On Disable:** When the object is disabled.
- **On Input Field Selection:** When the operator focuses/selects the field.
- **On Input Field De-selection:** When focus is lost.
- **On Entry of Value:** When the operator confirms a new value (ENTER). Sends `Change Numeric Value`.
- **On Change Value:** When the value is changed (e.g., by a variable).
- **On Change Background Colour:** Responds to a color change.
- **On Change Attribute:** Responds to general attribute changes.

## Implementation Implementation Implementation

The Boolean input is ideal for simple yes/no options or enabling/disabling machine functions. Since the graphical representation (checkmark style) depends on the VT manufacturer, this object ensures a consistent appearance within the terminal interface.

Further information and examples can be found in the [ISOBUS Wiki - Boolean](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/boolean) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, refer to the official ISO 11783-6:2018.*
