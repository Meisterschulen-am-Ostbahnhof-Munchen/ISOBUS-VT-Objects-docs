# ID 10 – Input list – ISO 11783-6 – B.8.5
The **Input List** object with **ID 10** allows the operator to select an item from a predefined list of objects. It is frequently used for drop-down menus or selection lists.
### Attributes and Record Format (Table B.20)
The following table describes the structure of the Input List object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 10 | 3 | Object type = Input List. |

[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the field (when closed). |

[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the field (when closed). |

[3] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | Reference to a Number Variable object for the index. |

[4] | **Value** | Integer | 1 | 0 – 255 | 10 | Currently selected index (0-254). 255 = no selection. (Only if Variable Reference == NULL). |

- | **Number of list items** | Integer | 1 | 0 – 255 | 11 | Number of objects in the list. |

| [5] | **Options** | Bitmask | 1 | 0 – 3 | 12 | Bit 0: Enabled (0=Disabled, 1=Enabled)<br>Bit 1: Real-time editing (1=Send value on change). |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 14 + ... | Object ID of a list entry (displayed as an option). |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (By Object) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Display
In its normal state, the Input List displays only the currently selected item.

* **Selection:** When the user opens the object, the Input List displays the list of available entries.
* **Index:** The transmitted value is the **zero-based index** of the selected item in the list.
* **Special value 255:** Signals "no selection".

## Events (Events - Table B.19)

The Input List object reacts to the following events:

* **On Enable / On Disable:** Change of the object's state.
* **On Input Field Selection / De-selection:** Focus events.
* **On Entry of Value:** When the user confirms a selection (ENTER). Sends `Change Numeric Value`.
* **On Change Value:** When the index is changed by the program.
* **On Entry of New Value:** Triggered when the value changes (often redundant to "On Entry of Value").
* **On ESC:** Cancels the selection.
* **On Change Attribute:** General attribute change.
* **On Change Size:** Responds to a size change.

## Implementation Implications
Input lists are ideally suited to prevent incorrect entries, as the operator can only select from valid options. Since the display (e.g., font size in the expanded list) is controlled by the VT, good readability is ensured on various devices.

Further information and examples can be found in the [ISOBUS Wiki - List (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/list-input) by Tobias Tenberg.

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*