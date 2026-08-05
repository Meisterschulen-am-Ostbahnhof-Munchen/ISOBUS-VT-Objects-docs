# ID 1 – Data mask – ISO 11783-6 – B.2
![](https://user-images.githubusercontent.com/69573151/94337364-35e74300-ffea-11ea-8342-cb8bd452b89d.png)
----
The **Data Mask** with **ID 1** is the primary display element for the user interface of a workgroup. It serves as the main container for all visual objects (buttons, number fields, graphics) displayed to the operator on the Virtual Terminal (VT).
### Attributes and Record Format (Table B.4)
The following table describes the structure of the Data Mask object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

[0] | **Type** | Integer | 1 | 1 | 3 | Object type = Data mask. |

[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color of the mask. |

[2] | **Soft Key Mask** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Object ID of the associated soft key mask (65535 = NULL). |

[-] | **Number of objects to follow** | Integer | 1 | 0 – 255 | 7 | Number of directly contained objects. |

[-] | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Number of following macro references. |

[-] **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 9 + ... | Object ID of a contained object. |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 11 + ... | X-position relative to the mask (pixels). |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 13 + ... | Y-position relative to the mask (pixels). |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Structure and Child Objects

The data mask serves as a container for all visible elements.

* **Object List:** Each child object is defined by its ID and its position (X/Y). Each set of ID and position occupies 6 bytes.
* **Order:** Objects are drawn in the listed order (Z-order). Higher indices are positioned above lower ones.
* **Coordinates:** Positioning is absolute in VT pixels, relative to the upper left corner of the mask (0,0).

## Events (Table B.3)

The data mask responds to the following events:

* **On Show:** Triggered when the mask becomes visible. The VT draws the background, the children, and the soft key mask.
* **On Hide:** Triggered when the mask is removed from the display.
* **On Refresh:** Triggered when changes are made to child objects that require redrawing.
* **On Change Background Colour:** Response to a change in the background colour.
* **On Change Soft Key Mask:** Response to a change in the assigned soft key mask.
* **Pointing Events:** `press` and `release` during touch operation on the mask area.

## Behavior and Limitations
* **Relationship with Softkeys:** Every data mask "has" a softkey mask. When the data mask is changed, the VT usually also changes the softkey layout.
* **Refresh:** When a child object is changed, the VT redraws the affected areas.
* **Visibility:** Only one data mask (or alarm mask) per workgroup can be active and in focus at any given time.

## Implementation Importance

The data mask is the core of the HMI design. Developers must ensure that the mask resolution matches the capabilities of the VT (standard minimum resolution is often 200x200 pixels, but modern VTs offer significantly higher resolutions). Efficient use of macros on mask events (e.g., `On Show`) can facilitate initializations directly within the VT.

Further information and examples can be found in the ISOBUS Wiki - Data Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/datamask) by Tobias Tenberg.

----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*