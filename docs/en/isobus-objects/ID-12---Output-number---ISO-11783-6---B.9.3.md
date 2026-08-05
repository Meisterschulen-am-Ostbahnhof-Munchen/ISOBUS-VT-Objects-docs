# ID 12 – Output number – ISO 11783-6 – B.9.3
The **Output Number** object with **ID 12** is used to display numeric values. Like the *Input Number* object, it supports automatic scaling and formatting, but is designed purely for display (read-only for the operator).
### Attributes and Record Format (Table B.23)
The following table describes the structure of the Output Number object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 12 | 3 | Object type = Output Number. |

[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the display field in pixels. |

[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the display field in pixels. |

[3] | **Background color** | Integer | 1 | 0 – 255 | 8 | Background color. |

[4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Object ID of a font attribute object. |

[5] | **Options** | Bitmask | 1 | 0 – 15 | 11 | Bit 0: Transparent <br> Bit 1: Display leading zeros <br> Bit 2: Display zero as blank <br> Bit 3: Truncate (1=Trim, 0=Round). |

| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Reference to a Number Variable object for the raw value. |

| [12] | **Value** | Integer | 4 | 0 – 2^32-1 | 14 – 17 | Raw value (unsigned 32-bit). Only if Variable Reference == NULL. |

| [7] | **Offset** | Signed Integer | 4 | -2^31 – 2^31-1 | 18 – 21 | Scaling offset. |

| [8] | **Scale** | Float | 4 | - | 22 – 25 | Scaling factor. |

| [9] | **Number of decimals** | Integer | 1 | 0 – 7 | 26 | Number of decimal places. |

| [10] | **Format** | Boolean | 1 | 0 or 1 | 27 | 0 = Fixed point, 1 = Exponential. |

| [11] | **Justification** | Integer | 1 | 0 – 15 | 28 | Text alignment: Bits 0-1 (horizontal), Bits 2-3 (vertical). |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 29 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Scaling Logic
The VT automatically calculates the displayed value using the following formula:

**Displayed Value = (Raw Value + Offset) × Scaling Factor**

Example: A raw value of 2500 with an offset of 0 and a scaling factor of 0.01 is displayed as **25.00** (with 2 decimal places).

## Formatting Options
* **Leading Zeros (Bit 1):** The field is padded with zeros on the left (e.g., "0012").
* **Zero as Space (Bit 2):** If the scaled value is exactly zero, the field remains completely empty.
* **Round vs. Truncate (Bit 3):** Controls how to handle values with more decimal places than defined in AID 9.

## Events

The Output Number object responds to the following events:

* **On Change Value:** Triggered when the displayed value changes (e.g., variable updated or `Change Numeric Value` command). The VT redraws the object.
* **On Refresh:** Triggered when the VT needs to redraw the object.
* **On Change Background Colour:** Responds to a change in background color.
* **On Change Attribute:** Responds to general attribute changes.
* **On Change Size:** Responds to a change in size.

## Implementation Implementation Implementation
Output Numbers are ideal for displaying sensor data (pressure, temperature, speed). Since the ECU only needs to transmit integers (raw values), the CAN bus load is minimized and the formatting complexity is shifted to the terminal. Pixel-precise alignment (AID 11) ensures that the numbers are perfectly aligned within the design frame, even with different fonts.

Further information and examples can be found in the [ISOBUS Wiki - Number (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-output)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*