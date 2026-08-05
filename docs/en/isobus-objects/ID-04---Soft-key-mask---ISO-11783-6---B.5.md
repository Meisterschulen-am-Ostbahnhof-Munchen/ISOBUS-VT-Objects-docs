# ID 4 – Soft Key Mask – ISO 11783-6 – B.5
The **Soft Key Mask** (softkey mask) with **ID 4** is a special container that defines the assignment of physical or virtual softkeys at the edge of the terminal. It is typically permanently assigned to a data mask or alarm mask.
### Attributes and Record Format (Table B.10)
The following table describes the structure of the Soft Key Mask object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 4 | 3 | Object type = Soft Key Mask. |

| [1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. The key object has its own background attribute, which this can override. |

| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 5 | Number of contained objects (keys or pointers). |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 6 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 7 + ... | Object ID of a contained key object or pointer. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (By Object) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Functionality and Assignment
A softkey mask contains a list of **Key Objects** (ID 5), **Object Pointers** (ID 27), or **External Object Pointers** (ID 43).

* **Order:** The assignment to the physical keys on the terminal is strictly in the order of the list.
* **NULL Pointers:** Pointers to the NULL Object ID reserve a position (the following keys do not move up). Pointers to NULL at the end of the list are not displayed and are not considered for paging.
* **Paging:** If the defined keys exceed the capacity of the terminal, it automatically creates navigation aids (arrow keys) for page turning.
* ## Events (Table B.9)

The softkey mask reacts to the following events:

* **On Show:** Triggered when the mask becomes visible. The VT draws all child objects in the defined order.
* **On Hide:** Triggered when the mask is removed.
* **On Change Background Colour:** Reacts to a change in the background color of the bar.
* **On Change Attribute:** Reacts to general attribute changes.

## Interaction with Data Masks
Each data mask (ID 1) references a softkey mask (ID 4).

* If the data mask is changed, the VT automatically changes the softkey assignments.
* The key assignments can also be changed at runtime without changing the main mask using the command `Change Soft Key Mask`.

## Importance for Implementation
The design of the softkey masks is crucial for ergonomics. Developers should ensure that important functions (e.g., "Back" or "Home") are always in the same position. Using NULL pointers can prevent keys from jumping when switching between different screens.

Further information and examples can be found in the [ISOBUS Wiki - Softkey Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/softkey-mask) by Tobias Tenberg.]

## 🎧 Podcast
* [ISO 11783-6: Understanding Softkeys and the Virtual Terminal – Your Key to Agricultural Machinery Mechatronics](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)

----
*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*