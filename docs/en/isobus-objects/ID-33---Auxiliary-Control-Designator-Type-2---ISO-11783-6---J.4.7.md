# ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7
The **Auxiliary Control Designator Type 2 Object Pointer** object with **ID 33** allows a working set to graphically display the currently assigned auxiliary functions and their inputs in a dialog box.
### Attributes and Record Format (Table J.6)
The following table describes the structure of the Auxiliary Control Designator Type 2 object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

[0] | **Type** | Integer | 1 | 33 | 3 | Object type = Auxiliary Control Designator Type 2 Object Pointer. |

[1] | **Pointer Type** | Integer | 1 | 0 – 3 | 4 | Reference type (see below). |

[2] | **Auxiliary Object ID** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Object ID of an Auxiliary Function (Type 2) or an Auxiliary Input (Type 2). |

### Pointer Types (AID 1)
* **0:** The VT displays the designator of the object specified by `Auxiliary Object ID`.
* **1:** The VT displays the designator of the object assigned to the object referenced by `Auxiliary Object ID` (e.g., if AID 2 is a function, the assigned input is shown).
* **2:** The VT displays the designator of the working set that owns the object specified by `Auxiliary Object ID`.
* **3:** The VT displays the designator of the working set that owns the object assigned to the object referenced by `Auxiliary Object ID`.

## Events (Events - Table J.7)

The object responds to the following events:

* **On Change Value:** Triggered when the mapping is changed or the referenced object is modified. The VT updates the display.

## Benefits for the Developer

This object allows you to create a graphical overview that shows the user: "This function on my machine is currently controlled by button Y on joystick Z." Since the mapping is often done by the user at the terminal, this pointer allows for a dynamic display without the ECU needing prior knowledge of the actual assignment.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, Annex J.*