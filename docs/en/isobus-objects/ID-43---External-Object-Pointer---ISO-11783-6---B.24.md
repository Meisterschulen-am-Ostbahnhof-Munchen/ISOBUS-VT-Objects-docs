# ID 43 – External Object Pointer – ISO 11783-6 – B.24

The **External Object Pointer** object with **ID 43** (from VT version 5 onwards) allows a working set to display objects that are physically located in the object pool of **another** working set.

### Attributes and Record Format (Table B.70)

The following table describes the structure of the External Object Pointer object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 43 | 3 | Object type = External Object Pointer. |
[1] | **Default Object ID** | Integer | 2 | 0 – 65534, 65535 | 4 – 5 | ID of a local fallback object if external access fails. |
[2] | **External Reference NAME ID** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | ID of an External Reference NAME object that identifies the target worksheet. |
[3] | **External Object ID** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | ID of the object in the external pool. |

## Functionality and Rules

This object allows the display of objects from external object pools.

- **Display:** The terminal searches for the object in the pool of the ECU identified by the NAME and draws it at the pointer's location.
- **Context:** Events (e.g., Button Press) and macros are executed in the context of the **original working set** (owner of the object). Messages (e.g., Button Activation) are sent to the owner.
- **Fallback:** If the external object is not found, is not released, or is invalid, `Default Object` is displayed.
- **Security:** The target object must have been released by the owning ECU via *External Object Definition* (ID 41).

## Events (Events - Table B.69)

The External Object Pointer object reacts to the following events:

- **On Change Attribute:** Triggered by the command `Change Attribute`. The VT re-evaluates the pointer and redraws it if necessary.

## Application Example

A tractor (Working Set A) wants to display the fill level of a trailed fertilizer spreader (Working Set B) in its main interface. It uses an *External Object Pointer* that points to the fill level indicator in the spreader's reservoir.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.24.*
