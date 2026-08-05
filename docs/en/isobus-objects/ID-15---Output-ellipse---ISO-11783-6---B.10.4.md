# ID 15 – Output Ellipse – ISO 11783-6 – B.10.4

The **Output Ellipse** object with **ID 15** is used to draw circles, ellipses, arcs, segments, and sectors (pie chart segments).

### Attributes and Record Format (Table B.31)

The following table describes the structure of the Output Ellipse object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 15 | 3 | Object type = Ellipse. |

| [1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Object ID of a Line Attributes object (for the outline). |

| [2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Width of the enclosing virtual rectangle. |

| [3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Height of the enclosing virtual rectangle. |

| [4] | **Ellipse type** | Integer | 1 | 0 – 3 | 10 | 0=Closed Ellipse, 1=Open Ellipse (arc), 2=Segment (chord), 3=Sector (pie slice). |

| [5] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Start angle / 2 (in degrees, counterclockwise from the positive X-axis). |

| [6] | **End angle** | Integer | 1 | 0 – 180 | 12 | End angle / 2 (in degrees, counterclockwise from the positive X-axis). |

| [7] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 13 – 14 | Object ID of a Fill Attributes object (for filling) or NULL for no filling. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 15 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Ellipse Types and Geometry
The ellipse is fitted into a virtual rectangle (`Width` x `Height`).

* **Closed Ellipse (0):** A complete ellipse or a circle (if Width = Height).

* **Open Ellipse (1):** Only the arc between the start and end angles is drawn.

* **Segment (2):** A segment of a circle (the chord between the angle points is closed).

* **Sector (3):** A sector of a circle (the angle points are connected to the center point, ideal for pie charts).


## Angle Calculation (Important!)

The angle values in AID 5 and 6 are transferred **halved** (range 0-180 corresponds to 0-360°).

* **90° (Top):** Value 45
* **180° (Left):** Value 90
* **270° (Bottom):** Value 135

**Special note for scaled ellipses:** If the ellipse is not a circle (Width != Height), the VT must ensure that the angles are drawn mathematically correctly and not just a scaled circular arc (see ISO standard Figure B.8).

## Events (Events - Table B.30)

The Output Ellipse object reacts to the following events:

* **On Change Size:** Triggered when the size of the rectangle changes at runtime.

* **On Change Attribute:** Triggered when line or fill attributes (e.g., colors) change.

* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications
Ellipses and sectors are essential for creating analog pointer instruments (meters) or progress indicators. Dynamically changing the `End angle` via ECU command allows for the creation of filled circular arcs that intuitively visualize states.

Further information and examples can be found in the [ISOBUS Wiki - Ellipse](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/ellipse) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*