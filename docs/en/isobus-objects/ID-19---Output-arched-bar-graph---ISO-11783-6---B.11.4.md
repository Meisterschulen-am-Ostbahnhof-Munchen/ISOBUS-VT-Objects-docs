# ID 19 – Output Arched Bar Graph – ISO 11783-6 – B.11.4
The **Output Arched Bar Graph** object with **ID 19** is an arched bar graph. It combines the properties of a linear bar chart with the circular geometry of a meter object.
### Attributes and Record Format (Table B.39)
The following table describes the structure of the Output Arched Bar Graph object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 19 | 3 | Object type = Arched Bar Graph. |
[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the bounding rectangle in pixels. |
[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the bounding rectangle in pixels. |
[3] | **Colour** | Integer | 1 | 0 – 255 | 8 | Color of the bar fill and border. |
[4] | **Target line color** | Integer | 1 | 0 – 255 | 9 | Color of the target value line (if drawn). |
[5] | **Options** | Bitmask | 1 | 0 – 31 | 10 | Bit 0: Draw Border qzmsdocs000000 qz Bit 1: Draw Target Line qzmsdocs000001 qz Bit 3: Type (0=Filled, 1=Line/Pointer) qzmsdocs000002 qz Bit 4: Deflection (0=Counterclockwise, 1=Clockwise). |
| [6] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Start angle / 2 (in degrees, counterclockwise from the positive X-axis). |
| [7] | **End angle** | Integer | 1 | 0 – 180 | 12 | End angle / 2 (in degrees, counterclockwise from the positive X-axis). |
| [8] | **Bar graph width** | Integer | 2 | 0 – 65535 | 13 – 14 | Arc thickness in pixels. |
[9] | **Min value** | Integer | 2 | 0 – 65535 | 15 – 16 | Minimum value. |
[10] | **Max value** | Integer | 2 | 0 – 65535 | 17 – 18 | Maximum value. |
[11] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 19 – 20 | Reference to a Number variable for the current value. |
[14] | **Value** | Integer | 2 | 0 – 65535 | 21 – 22 | Current raw value. Only if Variable Reference == NULL. |
[12] | **Target value var.** | Integer | 2 | 0 – 65534, 65535 | 23 – 24 | Reference to a Number variable for the target value. |
| [13] | **Target value** | Integer | 2 | 0 – 65535 | 25 – 26 | Current target value. Only if Target value variable ref == NULL. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 27 | Number of subsequent macro references. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Geometry

The arc-shaped bar is drawn based on a virtual ellipse object within the enclosing rectangle.

* **Bar Thickness (AID 8):** Defines the width of the arc itself.
* **Angle Logic:** Angle values are transmitted in halves (as with the meter object), e.g., 45 for 90°.
* **Deflection (AID 5, Bit 4):** Controls whether the bar "grows" clockwise or counterclockwise.
* **Transparency:** The object is transparent, allowing it to be overlaid with background images.
* **Transparency:** The object is transparent, enabling it to be overlaid with background images.
## Events (Table B.38)

The output Arched Bar Graph object responds to the following events:

* **On Change Value:** Triggered when the `Value` or `Target value` changes. The VT updates the graph.
* **On Change Attribute:** Triggered when attributes change.
* **On Change Size:** Responds to a size change.
* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications
Arched bar graphs are ideal for modern cockpit designs where multiple scales are nested within each other to save space (e.g., temperature and fuel). The `Target line` allows the operator to visualize a target range, while the arc shape enables intuitive level measurement.

Further information and examples can be found in the [ISOBUS Wiki - Arched Bar Graph](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/arched-bar-graph)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*
