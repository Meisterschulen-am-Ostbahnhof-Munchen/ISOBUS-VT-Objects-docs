# ID 13 – Output line – ISO 11783-6 – B.10.2

The **Output Line** object with **ID 13** is used to draw a simple line between two points within a virtual rectangle.

### Attributes and Record Format (Table B.27)

The following table describes the structure of the Output Line object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 13 | 3 | Object type = Output Line. |

| [1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Object ID of a line attribute object (color, width, style). |

| [2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Width of the bounding virtual rectangle. |

| [3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Height of the bounding virtual rectangle. |

| [4] | **Line Direction** | Integer | 1 | 0 or 1 | 10 | 0 = Top-Left to Bottom-Right <br>1 = Bottom-Left to Top-Right. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 11 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Geometry
The line is drawn within an imaginary rectangle defined by the object's position and `Width` and `Height`.

* **Line Direction 0:** The line runs diagonally downwards.

* Start point: (X, Y)

* End point: (X + Width - Line Width, Y + Height - Line Width)

* **Line Direction 1:** The line runs diagonally upwards.

* Start point: (X, Y + Height - Line Width)

* End point: (X + Width - Line Width, Y)

## Events (Events - Table B.26)

The Output Line object reacts to the following events:

* **On Change End Point:** Triggered when the geometry of the line is changed.

* **On Change Attribute:** Triggered when the line properties (e.g., color) change.

* **On Change Size:** Reacts to a change in size (e.g., by the `Change Size` command).

* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications
Lines are frequently used as separators in forms or for the simple graphical representation of relationships. By linking them to variables (via the Line Attributes), lines can change their color at runtime to indicate states (e.g., active/inactive).


Further information and examples can be found in the [ISOBUS Wiki - Line (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/line-output)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*