# ID 35 – Key Group – ISO 11783-6 – B.20

The **Key Group** object with **ID 35** is used to group softkeys. This is primarily used in conjunction with **User Layout Soft Key Masks** (from VT version 4 onwards).

### Attributes and Record Format (Table B.63)

The following table describes the structure of the Key Group object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 35 | 3 | Object type = Key Group. |

| [1] | **Options** | Bitmask | 1 | 0 – 3 | 4 | Bit 0: Available (0=Not available/blanked, 1=Available)<br>Bit 1: Transparent (1=Background color of keys is ignored). |

| [2] | **Name** | Integer | 2 | 0 – 65534 | 5 – 6 | Object ID of an output string or object pointer (name for mapping screen). |

| - | **Key Group Icon** | Integer | 2 | 0 – 65534, 65535 | 7 – 8 | Object ID of an output object (icon for mapping screen). |

| - | **Number of objects to follow** | Integer | 1 | 1 – 4 | 9 | Number of key objects in this group. Max. 4. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Object ID of a key object or object pointer to key. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |


## Events (Table B.62)

The Key Group object reacts to the following events:

* **On Change Attribute:** Reacts to general attribute changes.

## Meaning and Functionality

The Key Group object is used to define a logically related group of softkeys (e.g., "Hydraulic Functions"). This group is primarily used in **User Layout Soft Key Masks**.

* **User Mapping:** The user can decide at the terminal where they want this group of keys to be placed in their softkey bar. The VT forces the user to place the group *as a whole* to maintain logical coherence.

* **Transparency:** It is recommended to make Key Groups transparent so that the VT can set a uniform background color for the keys.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.20.*