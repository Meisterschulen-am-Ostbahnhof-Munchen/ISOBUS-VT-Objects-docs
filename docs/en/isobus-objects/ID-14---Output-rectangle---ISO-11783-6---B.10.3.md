# ID 14 – Output Rectangle – ISO 11783-6 – B.10.3

The **Output Rectangle** object with **ID 14** is used to draw rectangles, which can be displayed as outlines, filled, or in combination.

### Attributes and Record Format (Table B.29)

The following table describes the structure of the Output Rectangle object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 14 | 3 | Object type = Output Rectangle. |

[1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Object ID of a Line Attributes object for the frame. |

[2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Width of the rectangle in pixels. |

[3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Height of the rectangle in pixels. |

[4] | **Line suppression** | Bitmask | 1 | 0 – 15 | 10 | Suppression of sides: Bit 0=Top, Bit 1=Right, Bit 2=Bottom, Bit 3=Left. (1 = do not draw). |

[5] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 11 – 12 | Object ID of a Fill Attribute object (for filling) or NULL for no fill. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Appearance and Properties
The rectangle combines line and fill properties:

* **Outline:** If AID 1 is linked, a border is drawn according to the Line Attributes.


**Repeat:** * **Fill:** If AID 5 is linked, the interior of the rectangle is filled according to the Fill attributes.

* **Line Suppression (AID 4):** Allows you to selectively omit drawing individual edges of the rectangle. This is useful for table structures or open frames.

* **Clipping:** The rectangle defines its own graphic boundaries using `Width` and `Height`.

## Geometric Calculation
The corners of the rectangle are determined by the object's starting position (StartX, StartY):

* **Top-Left Corner:** (StartX, StartY)

* **Bottom-Right Corner:** (StartX + Width - 1, StartY + Height - 1)
The line width must be considered during planning, as it can grow inwards or outwards depending on the VT implementation.


## Events (Table B.28)

The output Rectangle object responds to the following events:

* **On Change Size:** Triggered when the size of the rectangle changes at runtime.

* **On Change Attribute:** Triggered when line or fill attributes (e.g., colors) change.

* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications

Rectangles are the most frequently used graphic primitives. They serve as backgrounds for text fields, as borders for groups, or for creating bars (e.g., by dynamically changing the `Width` or `Height` via an ECU command). In combination with transparent backgrounds, complex layouts can be implemented.

Further information and examples can be found in the [ISOBUS Wiki - Rectangle](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/rectangle) by Tobias Tenberg].


``` ----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*