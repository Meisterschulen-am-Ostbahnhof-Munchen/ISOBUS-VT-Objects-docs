# ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6

The **Extended Input Attributes** object with **ID 38** (from VT version 4 onwards) is used to validate text input (input string) when using **WideStrings** (Unicode).

### Attribute and Record Format (Table B.53)

The following table describes the structure of the Extended Input Attributes object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 38 | 3 | Object type = Extended Input Attributes. |

| [1] | **Validation type** | Integer | 1 | 0 – 1 | 4 | 0 = Allowed characters (whitelist), 1 = Forbidden characters (blacklist). |

| - | **Number of code planes to follow** | Integer | 1 | 1 – 17 | 5 | Number of defined Unicode planes. |

| - | **Repeat:** {Code plane number} | Integer | 1 | 0 – 16 | 6 ... | Unicode plane number (0 = BMP). |

| - | {Number of character ranges to follow} | Integer | 1 | 1 – 255 | 7 ... | Number of ranges in this plane. |

| - | **Repeat:** {{First character}} | Integer | 2 | 0 – 65535 | 8 ... | Start character of the range (WideChar). |

| - | {{Last character}} | Integer | 2 | 0 – 65535 | 10 ... | End character of the range (WideChar). |

## Functionality
While the simple *Input Attributes* object (ID 26) only supports 8-bit characters, this object allows for fine-grained control of allowed Unicode characters (WideString). This is necessary for languages with more than 256 characters (e.g., Asian, Cyrillic).

Validation is performed by defining ranges within Unicode layers.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.14.6.*