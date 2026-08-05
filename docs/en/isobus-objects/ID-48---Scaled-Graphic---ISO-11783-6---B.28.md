# ID 48 – Scaled Graphic – ISO 11783-6 – B.28

The **Scaled Graphic** object with **ID 48** (from VT version 6 onwards) is used to display and scale graphic objects.

### Attributes and Record Format (Table B.76)

The following table describes the structure of the Scaled Graphic object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 48 | 3 | Object type = Scaled Graphic. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Target width in pixels. |

| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Target height in pixels. |

| [3] | **ScaleType** | Integer | 1 | 0 – 127 | 8 | Scaling mode and adjustment (see below). |

| [4] | **Options** | Bitmask | 1 | 0 – 1 | 9 | Bit 0: Flashing (0=Normal, 1=Blinking). |

| [5] | **Value** | Integer | 2 | 0 – 65535 | 10 – 11 | Object ID of the graphic object to be displayed (Graphic Data ID 46 or Picture Graphic ID 20) or pointer. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 12 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Scaling Types (Bits 0-2 of ScaleType)
* **0:** No scaling (use original size from the raw data).

* **1:** Scale to width (maintain aspect ratio).

* **2:** Scale to height (maintain aspect ratio).

* **3:** Scale to both width and height (distortion possible).

* **4:** Fit to area (Best Fit, maintain aspect ratio, graphic becomes as large as possible).

### Adjustment (Bits 3-6 of ScaleType)
Defines the position within the area defined by `Width` and `Height`:
* **Horizontal (Bits 3-4):** 0=Left, 1=Center, 2=Right.

* **Vertical (Bits 5-6):** 0=Top, 1=Center, 2=Bottom.

## Events (Events - Table B.75)

The Scaled Graphic object responds to the following events:

* **On Refresh:** Triggered on a mask refresh or option change.

* **On Change Attribute:** Responds to general attribute changes.

* **On Change Value:** Triggered when the referenced graphic object (value) is changed. The VT loads and scales the new image.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.28.*