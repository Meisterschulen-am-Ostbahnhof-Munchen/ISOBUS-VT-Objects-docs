# ID 37 – Output List – ISO 11783-6 – B.9.4

The **Output List** object with **ID 37** (from VT version 4 onwards) is used to display one of several objects from a list. Which object is currently visible is controlled by an index (value).

### Attributes and Record Format (Table B.25)

The following table describes the structure of the Output List object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 37 | 3 | Object type = Output List. |

| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the display area in pixels. Clipping occurs outside. |

| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the display area in pixels. Clipping occurs outside. |

| [3] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | Reference to a Number Variable object for the index. |

| [4] | **Value** | Integer | 1 | 0 – 255 | 10 | Current index (0-254). 255 = no display. Only if variable Ref == NULL. |

| - | **Number of list items** | Integer | 1 | 0 – 255 | 11 | Number of items in the list. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 12 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 13 + ... | Object ID of a list item (what to display). NULL = Empty placeholder. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |


## Functionality

The Output List behaves similarly to an animation, but is manually controlled via the index.

* **Index:** The displayed content is determined by the value (Value or Variable). Index 0 displays the first object in the list.

* **Special Value 255:** With a value of 255, nothing is displayed (the object is invisible).

* **NULL Pointer:** If a list entry has the ID NULL (65535), nothing is displayed for that index.

## Events (Table B.24)

The Output List object reacts to the following events:

* **On Change Value:** Triggered when the index changes. The VT updates the display.

* **On Change Attribute:** Reacts to general attribute changes.

* **On Change Size:** Reacts to size changes.

* **On Refresh:** Triggered when the VT needs to redraw the object.


Further information and examples can be found in the [ISOBUS Wiki - List (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/list-output)] by Tobias Tenberg.

----

*Note: For detailed specifications, please refer to the official ISO 11783-6:2018, B.9.4.*