# ID 41 – External Object Definition – ISO 11783-6 – B.22
The **External Object Definition** object with **ID 41** (from VT version 5 onwards) is part of the mechanism for **cross-working-set object references**. It defines which objects in a user's own pool may be referenced by other working sets.
### Attributes and Record Format (Table B.66)
The following table describes the structure of the External Object Definition object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 41 | 3 | Object type = External Object Definition. |
| [1] | **Options** | Bitmask | 1 | 0 – 1 | 4 | Bit 0: Enabled (1=Share active, 0=Disabled). |
| [2] | **NAME 0** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Bytes 1–4 of the NAME (ISO 11783-5) of the authorized working set. |
| [3] | **NAME 1** | Integer | 4 | 0 – 2^32-1 | 9 – 12 | Bytes 5–8 of the NAME of the authorized working set. |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 13 | Number of shared objects. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534, 65535 | 14 + ... | Object ID of an object from the local pool that is shared with the external work set. |

## Functionality
For Working Set A to display an object from Working Set B (via an *External Object Pointer*), Working Set B must explicitly share this object with Working Set A in an *External Object Definition*. This ensures security and control over the local pool resources.

**Recommendation:** The `Enabled` bit should initially be set to 0 when the pool is loaded and only activated at runtime when the partner's NAME is known and up-to-date.

## Events (Table B.65)

The External Object Definition object responds to the following events:

- **On Change Attribute:** Triggered by the command `Change Attribute` (e.g., enabling/disabling). The VT re-evaluates all currently displayed External Object Pointers that reference objects in this WS.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.22.*