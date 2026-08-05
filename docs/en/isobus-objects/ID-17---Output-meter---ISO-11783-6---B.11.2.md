# ID 17 – Output meter – ISO 11783-6 – B.11.2
The **Output Meter** object with **ID 17** is a circular display (pointer instrument). It visualizes a numerical value by the position of a needle on a circular arc.
### Attributes and Record Format (Table B.35)
The following table describes the structure of the Output Meter object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 17 | 3 | Object type = Output Meter. |

[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width and height of the enclosing square. |

[2] | **Needle color** | Integer | 1 | 0 – 255 | 6 | Needle color. |

[3] | **Border color** | Integer | 1 | 0 – 255 | 7 | Border color (when drawn). |

[4] | **Arc and tick color** | Integer | 1 | 0 – 255 | 8 | Arc and tick color. |

[5] | **Options** | Bitmask | 1 | 0 – 15 | 9 | Bit 0: Draw Arc<br> Bit 1: Draw Border<br> Bit 2: Draw Ticks<br> Bit 3: Deflection Direction (0 = min->max counterclockwise, 1 = min->max clockwise). |

[6] | **Number of ticks** | Integer | 1 | 0 – 255 | 10 | Number of scale markings. |

[7] | **Start angle** | Integer | 1 | 0 – 180 | 11 | Start angle / 2 (in degrees, counterclockwise from the positive x-axis). |

[8] | **End angle** | Integer | 1 | 0 – 180 | 12 | End angle / 2 (in degrees, counterclockwise from the positive x-axis).
| [9] | **Min value** | Integer | 2 | 0 – 65535 | 13 – 14 | Value at the start angle. |

| [10] | **Max value** | Integer | 2 | 0 – 65535 | 15 – 16 | Value at the end angle. |

| [11] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 17 – 18 | Reference to a Number Variable object. |

| [12] | **Value** | Integer | 2 | 0 – 65535 | 19 – 20 | Current value. Only if Variable Reference == NULL. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 21 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Display
The instrument is fitted into a square. The needle moves along an arc defined by start and end angles.

* **Angle Logic:** As with the ellipse, angles are bisected (e.g., 45 for 90°).
* **Ticks (AID 6):** With two or more ticks, one is drawn at the beginning and one at the end of the arc; additional ticks are evenly distributed in between. Recommended length: 10% of the meter width.
* **Transparency:** The meter object itself is transparent. This allows bitmaps (e.g., a nice clock face) to be placed behind it.

## Deflection Direction (AID 5, Bit 3)

This is a critical attribute for intuitive operation:

* **0 (Anticlockwise):** The value increases counterclockwise.
* **1 (Clockwise):** The value increases clockwise (standard for most analog instruments).

## Events (Table B.34)

The Output Meter object reacts to the following events:

* **On Change Value:** Triggered when the value to be displayed changes (e.g., variable updated). The VT moves the needle.
* **On Change Attribute:** Triggered when attributes change.
* **On Change Size:** Reacts to a change in size.
* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications

The Output Meter is ideal for visualizing engine speeds, fill levels, or pressure values. Because it is transparent, very attractive, analog-looking cockpit displays can be created by combining it with background graphics (ID 20) and various masks.

Further information and examples can be found in the [ISOBUS Wiki - Meter](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/meter) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*