# ID 30 – Auxiliary Input Type 1 – ISO 11783-6 – J.4.4
The **Auxiliary Input Type 1** object with **ID 30** defines the properties of a physical control element (e.g., joystick, switch) of an auxiliary input device.
*Note: This object is considered obsolete as of VT version 3 and is replaced by Type 2 (ID 32).*
### Attributes and Record Format (Table J.3)
The following table describes the structure of the Auxiliary Input Type 1 object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

[0] | **Type** | Integer | 1 | 30 | 3 | Object type = Auxiliary Input Type 1. |

[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. |

[2] | **Function type** | Integer | 1 | 0 – 2 | 5 | 0 = Latching Boolean, 1 = Analog, 2 = Non-latching Boolean. |

[3] | **Input ID** | Integer | 1 | 0 – 255 | 6 | ID of the physical input to which this object refers. |

[-] | **Number of objects to follow** | Integer | 1 | 1 – 255 | 7 | Number of directly contained objects (designator). |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Object ID of a contained object. |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 10 + ... | X position relative to the upper left corner. |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 12 + ... | Y position relative to the upper left corner. |

## Functionality
This object describes a physical input element (e.g., a button or a joystick axis) on an Auxiliary Input Device. It is provided by the Auxiliary Input Device so that the VT knows the available inputs and their properties.

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 12 + ... | Y position relative to the upper left corner. |

## Functionality

This object describes a physical input element (e.g., a button or a joystick axis) on an Auxiliary Input Device. It is provided by the Auxiliary Input Device so that the VT knows the available inputs and their properties.

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 12 + ... | The ``Input ID`` attribute links this object to the device's status messages.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, Annex J.*