# ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3
The **Auxiliary Function Type 2** object with **ID 31** is the modern definition for auxiliary functions in ISOBUS (from VT version 3 onwards). It offers extended possibilities for assigning controls.
### Attributes and Record Format (Table J.2)
The following table describes the structure of the Auxiliary Function Type 2 object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 31 | 3 | Object type = Auxiliary Function Type 2. |

[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. |

[2] | **Function attributes** | Bitmask | 1 | - | 5 | Bitmask for function type and control (see below). |

[[[]] | **Number of objects to follow** | Integer | 1 | 1 – 255 | 6 | Number of directly contained objects (designator). |

[[]] | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Object ID of a contained object. |

[]] | {X Location} | Signed Integer | 2 | -32768 to +32767 | 9 + ... | X position relative to the upper left corner. |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 11 + ... | Y position relative to the upper left corner. |

### Function Attributes (Bitmask AID 2)
* **Bits 0–3:** Auxiliary function type (see Table J.5)
* 0: Boolean Latching
* 1: Analogue
* 2: Boolean Momentary
* 3: Boolean Latching (Dual)
* 4: Analogue (Dual)
* 5: Boolean Momentary (Dual)
* ...
* **Bits 4–5:** Reserved
* **Bit 6:** Assignment Restriction (0 = Free, 1 = Restricted, see ISO 11783-6).
* **Bit 7:** Single Assignment (1 = May only be assigned to one input).

## Special Features

This object is actively used for "Auxiliary Mapping" in the terminal. It allows the ECU to inform the terminal which functions (e.g., "Lift up/down") are available so that the user can assign them to buttons or joysticks.

It replaces the obsolete Type 1 (ID 29).

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, Annex J.*