# ID 24 – Line attributes – ISO 11783-6 – B.14.3
The **Line Attributes** object with **ID 24** defines the graphic properties of lines and outlines (color, width, style). It is referenced by all geometric objects such as *Line* (ID 13), *Rectangle* (ID 14), *Ellipse* (ID 15), and *Polygon* (ID 16).
### Attribute and Record Format (Table B.48)
The following table describes the structure of the Line Attributes object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

[0] | **Type** | Integer | 1 | 24 | 3 | Object type = Line Attributes. |

[1] | **Line colour** | Integer | 1 | 0 – 255 | 4 | Line color. |

[2] | **Line width** | Integer | 1 | 0 – 255 | 5 | Line thickness in pixels. 0 = do not draw. |

[3] | **Line art** | Bitmask | 2 | 0 – 65535 | 6 – 7 | Bit pattern for line style (1 = draw, 0 = background). |

[-] | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Number of following macro references. |

[-] **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Line Thickness and Appearance
The VT uses a square "brush" of size `Line width` x `Line width` to draw the line.

* **Width = 0:** The line is not drawn.
* **Width > 1:** The line appears thicker.

## Line Style (Line Art - AID 3)
A 16-bit mask defines whether a line appears solid, dashed, or dotted:

* Each set bit (1) represents a drawn brushstroke.
* Each unset bit (0) represents a gap (background shows through).
* **Example 0xFFFF:** Solid line (all bits 1).
* **Example 0xCCCC (11001100...):** Dashed line.
* **Special Feature:** The length of a line scales with the `Line width`.

## Events (Table B.47)

The Line Attributes object reacts to the following events:

* **On Change Line Attributes:** Triggered by the `Change Line Attributes` command. The VT updates all objects that use this attribute.
* **On Change Attribute:** Reacts to general attribute changes.

## Implementation Implementation Implementation
Line attributes enable efficient control of the graphical display. By changing a single attribute object, for example, all borders in a mask can be switched simultaneously from "Thin/Black" to "Thick/Red" to visualize an alarm condition.

Further information and examples can be found in the [ISOBUS Wiki - Line Attribute](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/line-attribute)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*