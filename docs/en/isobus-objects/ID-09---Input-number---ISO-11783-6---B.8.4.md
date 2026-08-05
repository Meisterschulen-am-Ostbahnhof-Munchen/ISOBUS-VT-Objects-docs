# ID 9 – Input number – ISO 11783-6 – B.8.4
The **Input Number** object with **ID 9** is one of the most complex and important input objects. It is used for inputting and displaying numeric values and supports automatic scaling, formatting, and limit checking directly in the terminal.
### Attributes and Record Format (Table B.18)
The following table describes the structure of the Input Number object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 9 | 3 | Object type = Input Number. |

[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the input field in pixels. |

[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the input field in pixels. |

[3] | **Background color** | Integer | 1 | 0 – 255 | 8 | Background color. |

[4] | **Font attributes** | Integer | 2 | 0 – 65534 | 9 – 10 | Object ID of a font attribute object (color, size, font). |

[5] | **Options** | Bitmask | 1 | 0 – 15 | 11 | Bit 0: Transparent qzmsdocs000000 qz Bit 1: Display leading zeros qzmsdocs000001 qz Bit 2: Display zero as blank qzmsdocs000002 qz Bit 3: Truncate (1=Trim, 0=Round). |

| [6] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 12 – 13 | Reference to a Number Variable object for the raw value. If NULL, the "Value" attribute is used. |

| [14] | **Value** | Integer | 4 | 0 – 2^32-1 | 14 – 17 | Raw value (unsigned 32-bit). Only if Variable Reference == NULL. |

| [7] | **Min value** | Integer | 4 | 0 – 2^32-1 | 18 – 21 | Minimum raw value (unsigned). |

[8] | **Max value** | Integer | 4 | 0 – 2^32-1 | 22 – 25 | Maximum raw value (unsigned). |

[9] | **Offset** | Signed Integer | 4 | -2^31 – 2^31-1 | 26 – 29 | Scaling offset. |

[10] | **Scale** | Float | 4 | - | 30 – 33 | Scaling factor. |

[11] | **Number of decimals** | Integer | 1 | 0 – 7 | 34 | Number of decimal places. |

[12] | **Format** | Boolean | 1 | 0 or 1 | 35 | 0 = Fixed point, 1 = Exponential. |

[13] | **Justification** | Integer | 1 | 0 – 15 | 36 | Text alignment: Bits 0-1 (Horizontal), Bits 2-3 (Vertical). |

[15] | **Options 2** | Bitmask | 1 | 0 – 3 | 37 | Bit 0: Enabled (0=Disabled, 1=Enabled)<br>Bit 1: Real-time editing (1=Send value immediately). |

[-] | **Number of macros to follow** | Integer | 1 | 0 – 255 | 38 | Number of following macro references. |

[-] | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | 39... | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | 40... | Macro ID of the macro to be executed. |

## Scaling Logic
The VT automatically calculates the displayed value using the following formula:

**Displayed Value = (Raw Value + Offset) × Scaling Factor**

This allows physical values (e.g., 12.5 bar) to be processed as simple integers in memory (e.g., 125), while the VT handles the conversion and decimal representation.

## Validation
Limit values are also checked based on the scaled values. The VT only allows the input field to be closed (ENTER) if the new value is within the scaled min/max limits:

Scaled Min <= Neuer Wert <= Scaled Max`

## Events (Table B.15)

The Input Number object responds to the following events:

* **On Enable / On Disable:** Change of object state.
* **On Input Field Selection / De-selection:** Focus events.
* **On Entry of Value:** When the operator confirms a new value. Sends `Change Numeric Value`.
* **On Change Value:** When the value is changed by the program.
* **On ESC:** Cancel input.
* **On Change Background Colour:** Change background color.
* **On Change Attribute:** General attribute change.

## Real-Time Editing (AID 15, Bit 1)

When this bit is set, the VT sends the current intermediate value to the workgroup with every change (e.g., with each key press on the incremental encoder). This allows the machine to react immediately to changes (e.g., real-time speed control) even before the operator finalizes the input.

## Implementation Implications

The Input Number object significantly reduces the workload for the machine control unit (ECU) in terms of formatting and validation. Developers should ensure that the scaling factor and number of decimal places are chosen to prevent rounding errors from distorting the display.

Further information and examples can be found in the [ISOBUS Wiki - Number (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-input)] by Tobias Tenberg.

----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018.*
