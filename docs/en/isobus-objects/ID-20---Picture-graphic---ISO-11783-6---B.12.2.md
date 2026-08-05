# ID 20 – Picture graphic – ISO 11783-6 – B.12.2

The **Picture Graphic** object with **ID 20** is used to display raster graphics (bitmaps) on the Virtual Terminal. It allows the integration of logos, icons, and complex visual elements.

### Attributes and Record Format (Table B.41)

The following table describes the structure of the Picture Graphic object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 20 | 3 | Object type = Picture Graphic. |

| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Target width in pixels (height is scaled proportionally). |

| [4] | **Actual width** | Integer | 2 | 0 – 65535 | 6 – 7 | Actual width of the raw data. |

| [5] | **Actual height** | Integer | 2 | 0 – 65535 | 8 – 9 | Actual height of the raw data. |

| [6] | **Format** | Integer | 1 | 0 – 2 | 10 | 0=Monochrome (1 bit), 1=16 colors (4 bits), 2=256 colors (8 bits). |

| [2] | **Options** | Bitmask | 1 | 0 – 7 | 11 | Bit 0: Transparency (0=Opaque, 1=Transparent) <br>Bit 1: Blinking <br>Bit 2: Data format (0=Raw, 1=Run-Length Encoded). |

| [3] | **Transparency color** | Integer | 1 | 0 – 255 | 12 | Color index to be displayed transparently. |

| - | **Number of bytes in raw data** | Integer | 4 | 0 – 2^32-1 | 13 – 16 | Size of image data. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Number of following macro references. |

| - | **Repeat:** {raw data} | Integer | 1 | 0 – 255 | 18 ... | Image data (bytes). |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After image data) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Display

The Picture Graphic object stores pixel graphics in binary form within the object pool file (.IOP).

### Scaling and Formats
* **Aspect Ratio:** The VT scales the graphic based on the target width (`Width`). To avoid distortion, the VT automatically calculates the target height from the ratio of `Actual width` to `Actual height`.

* **Color Depth:** 1-bit (monochrome), 4-bit (16 colors), and 8-bit (256 colors) are supported.

### Transparency and Effects

* **Transparency (Bit 0):** When enabled, the color defined in AID 3 is not drawn; instead, the background shows through.

* **Flashing (Bit 1):** The image can blink (frequency and style depend on the VT).

* **RLE Compression (Bit 2):** Run-Length Encoding can save memory for simple graphics (many areas of the same color).


### Transparency and Effects

* **Transparency (Bit 0):** When enabled, the color defined in AID 3 is not drawn; instead, the background shows through. ## Events (Events - Table B.40)

The Picture Graphic object reacts to the following events:

* **On Refresh:** Triggered when options change (e.g., transparency, blinking) or when the mask is refreshed.

* **On Change Attribute:** Reacts to general attribute changes.

## Implementation Implementation Importance
Picture graphics are essential for a modern HMI.

* **Avoid Waste:** Since bitmaps occupy a lot of memory in the VT, they should be kept as small as possible.

* **Reuse:** An image can be defined once in the pool and referenced by many objects (e.g., multiple buttons).

* **Icons:** They are frequently used as "designators" for softkeys (ID 5) or as symbols in containers (ID 3).

Further information and examples can be found in the [ISOBUS Wiki - Picture Graphic object](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/picture-graphic-object) by Tobias Tenberg].


----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*