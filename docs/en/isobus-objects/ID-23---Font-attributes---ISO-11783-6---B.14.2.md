# ID 23 – Font attributes – ISO 11783-6 – B.14.2
The **Font Attributes** object with **ID 23** defines the appearance of text (font, size, color, style). It is a central attribute object referenced by all text-based display and input objects.
### Attribute and Record Format (Table B.46)
The following table describes the structure of the Font Attributes object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 23 | 3 | Object type = Font Attributes. |

[1] | **Font colour** | Integer | 1 | 0 – 255 | 4 | Text color. |

[2] | **Font size** | Integer | 1 | 0 – 255 | 5 | Font size (see below). |

[3] | **Font type** | Integer | 1 | 0 – 255 | 6 | Character set (see ISO Table K.1). |

[4] | **Font style** | Bitmask | 1 | 0 – 255 | 7 | Bit 0: Bold<br>Bit 1: Crossed Out<br>Bit 2: Underlined<br>Bit 3: Italic<br>Bit 4: Inverted<br>Bit 5: Flashing (Inverted/Style)<br>Bit 6: Flashing (Hidden/Style)<br>Bit 7: Proportional (0=Fixfont, 1=Prop.). |
| - | **Number of macros to follow** | Integers | 1 | 0 – 255 | 8 | Number of following macro references. |
| - | **Repeat:** {Event ID} | Integers | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Font Sizes and Render Modes
The interpretation of AID 2 depends heavily on bit 7 in the `Font style` options:

### Non-proportional fonts (bit 7 = 0)
Here, predefined grid sizes are used (width x height in pixels):

* **0:** 6x8
* **1:** 8x8
* **2:** 8x12
* ...
* **14:** 128x192

### Proportional fonts (bit 7 = 1)
In this mode, the value in AID 2 directly represents the **font height in pixels**. The width of individual characters varies.

## Events (Table B.45)

The Font Attributes object responds to the following events:

* **On Change Font Attributes:** Triggered by the command `Change Font Attributes`. The VT updates all objects that use these attributes.
* **On Change Attribute:** Responds to general attribute changes.

## Implementation Implications
Font attributes allow for a consistent design. Instead of defining color and size individually for each text object, all objects reference a common attribute object. If this single object is changed (e.g., from white to yellow font), the entire HMI appearance changes immediately.

Further information and examples can be found in the [ISOBUS Wiki - Font Attributes](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/font-attribute) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*