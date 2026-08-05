# ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2
The **Auxiliary Function Type 1** object with **ID 29** defines the attributes and design of an auxiliary function control.
*Note: This object is considered obsolete as of VT version 3 and is replaced by Type 2 (ID 31). It should no longer be used in new projects.*
### Attributes and Record Format (Table J.1)
The following table describes the structure of the Auxiliary Function Type 1 object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 29 | 3 | Object type = Auxiliary Function Type 1. |

| [1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. |

| [2] | **Function type** | Integer | 1 | 0 – 2 | 5 | 0 = Latching Boolean, 1 = Analog, 2 = Non-latching Boolean. |

| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 6 | Number of directly contained objects (Designator). |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Object ID of a contained object. |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 9 + ... | X position relative to the upper left corner. |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 11 + ... | Y position relative to the upper left corner. |

## Functionality
The VT uses these attributes to enforce assignment to a compatible auxiliary input. The designator symbol must fit within the area of a softkey; any excess is clipped.

The object serves as a function definition that can be assigned to a physical auxiliary input device.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, Annex J.*