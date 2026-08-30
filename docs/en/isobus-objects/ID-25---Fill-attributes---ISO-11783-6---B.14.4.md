# ID 25 – Fill attributes – ISO 11783-6 – B.14.4
The **Fill Attributes** object with **ID 25** defines how closed geometric shapes (rectangles, ellipses, polygons) are filled.
### Attribute and Record Format (Table B.50)
The following table describes the structure of the Fill Attributes object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 25 | 3 | Object type = Fill Attributes. |
[1] | **Fill type** | Integer | 1 | 0 – 3 | 4 | 0=No fill, 1=Line color, 2=Fill color, 3=Pattern. |
[2] | **Fill color** | Integer | 1 | 0 – 255 | 5 | Fill color (only relevant for type 2). |
[3] | **Fill pattern** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | Object ID of a Picture Graphic object for pattern fill (only for type 3). |
[-] | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Number of following macro references. |
[-] | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Fill Types and Logic
AID 1 controls which source is used for the fill:

- **No Fill (0):** The fill remains transparent; only the outline (if defined) is drawn.
- **Line Colour (1):** The fill is the same color as the border (from the Line Attributes).
- **Specified Colour (2):** The color defined in AID 2 is used.
- **Pattern (3):** The fill is a repeating graphic (tiling).

## Using Fill Patterns (Important!)

When a pattern (AID 3) is used, strict rules apply to the referenced graphic:

- **Alignment:** For monochrome graphics, the width must be divisible by 8. For 16-color graphics, it must be divisible by 2.
- **Order:** For dynamic changes, `Fill pattern` must be set first, followed by `Fill type`, to avoid errors in the VT.

## Events (Table B.49)

The Fill Attributes object responds to the following events:

- **On Change Fill Attributes:** Triggered by the command `Change Fill Attributes`. The VT updates all objects that use this attribute.
- **On Change Attribute:** Responds to general attribute changes.

## Implementation Implementation Importance
Fill attributes are essential for user interface design. They allow you to highlight areas (e.g., yellow fill for a warning zone in a bar chart) or create textured backgrounds. By changing the fill type at runtime, states (e.g., "tank empty" -> flashing red fill) can be visualized very effectively.

Further information and examples can be found in the [ISOBUS Wiki - Fill Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/fill-attribute)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*