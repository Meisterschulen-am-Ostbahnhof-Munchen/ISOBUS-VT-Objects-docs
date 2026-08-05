# ID 27 – Object pointer – ISO 11783-6 – B.15
The **Object Pointer** object with **ID 27** serves as a dynamic placeholder. It allows the referenced object to be replaced at runtime at a predefined location within a mask or container.
### Attributes and Record Format (Table B.55)
The following table describes the structure of the Object Pointer object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 27 | 3 | Object type = Object Pointer. |

| [1] | **Value** | Integer | 2 | 0 – 65534, 65535 | 4 – 5 | Object ID of the referenced object or NULL (65535). |

## Functionality and Application
An object pointer is integrated into a mask like a normal child object. However, instead of drawing anything itself, it "redirects" the display to the object whose ID is stored in AID 1.

* **Dynamic Exchange:** The ECU can change `Value` (AID 1) at any time using the `Change Numeric Value` command. The VT then hides the old object and displays the new one in the same position.

`` * **Placeholder Function:** It is ideal for status icons (e.g., changing symbols for different machine states) without having to layer multiple objects and hide them individually.

* **NULL Pointer:** If the value is set to 65535, nothing is drawn at this location.

## Events (Table B.54)

The Object Pointer object reacts to the following events:

* **On Change Value:** Triggered by the command `Change Numeric Value`. The VT hides the previous object and displays the new one. The parent screen is updated.

## Implementation Implementation Implementation Implementation Implementation Implementation Implementation (IMA) significantly reduces the complexity of the screen control. Instead of manually managing many objects using `Hide/Show`, the ECU only needs to change a single ID in the pointer. This saves CAN bus bandwidth and simplifies the program logic on the machine control.
* **On Change Value:** Triggered by the command `Change Numeric Value`. Further information and examples can be found in the [ISOBUS Wiki - Object Pointer](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/object-pointer)] by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*
