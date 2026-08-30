# ID 34 – Window Mask – ISO 11783-6 – B.19
The **Window Mask** object with **ID 34** (introduced with VT version 4) allows you to define a portion of the screen that can be updated independently of the main data mask or populated with content from other working sets.
### Attributes and Record Format (Table B.61)
The following table describes the structure of the Window Mask object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 34 | 3 | Object type = Window Mask. |
| - | **Width** | Integer | 1 | 1 – 2 | 4 | Width in user layout columns (only relevant for Type 0 Free Form, otherwise ignored). |
| - | **Height** | Integer | 1 | 1 – 6 | 5 | Height in user layout rows (only relevant for Type 0 Free Form, otherwise ignored). |
| - | **Window Type** | Integer | 1 | 0 – 18 | 6 | Window type (see below). |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 7 | Background color (only relevant for Type 0). |
| [2] | **Options** | Bitmask | 1 | 0 – 3 | 8 | Bit 0: Available (0=Not available/blanked, 1=Available) <br>Bit 1: Transparent (1=Transparent background, type 0 only). |
| [3] | **Name** | Integer | 2 | 0 – 65534 | 9 – 10 | Object ID of an output string (name for mapping screen). |
| - | **Window Title** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Object ID of an output string (title in the window). |
| - | **Window Icon** | Integer | 2 | 0 – 65534, 65535 | 13 – 14 | Object ID of an output object (icon for mapping screen). |
| - | **Number of object references to follow** | Integer | 1 | 0 – 2 | 15 | Number of referenced objects (depending on the window type). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 16 | Number of directly contained objects (only for Type 0 Free Form). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Number of following macro references. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65535 | 18 + ... | Referenced objects (for predefined types). |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | var. | Contained objects (for Type 0 Free Form). |
| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | var. | X-position relative to the window. |
| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | var. | Y-position relative to the window. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Window Types (Excerpt from B.19.2)
- **0:** Free Form (Free design, working set defines content).
- **1:** 1x1 Numeric Output with units.
- **2:** 1x1 Numeric Output without units.
- **3:** 1x1 String Output.
- **4:** 1x1 Numeric Input with Units.
- **...**
- **7:** 1x1 Horizontal Linear Bargraph.
- **8:** 1x1 Single Button.
- **...**
- **10:** 2x1 Numeric Output with Units.

## Events (Events - Table B.60)

The Window Mask object responds to the following events:

- **On Show:** When the window becomes visible as part of a user layout mask.
- **On Hide:** When the window is hidden.
- **On Refresh:** When child objects are changed.
- **On Change Background Colour:** Responds to a color change.
- **On Change Child Location / Position:** Updates child objects.
- **On Change Attribute:** Responds to general attribute changes.
- **On Pointing Event:** Touch events (only for Free Form Windows).

Further information and examples can be found in the [ISOBUS Wiki - Window Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/window-mask)] by Tobias Tenberg.

----

*Note: For detailed specifications, please refer to the official ISO 11783-6:2018, B.19.*