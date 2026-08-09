# ID 42 – External Reference NAME – ISO 11783-6 – B.23
The **External Reference NAME** object with **ID 42** (from VT version 5 onwards) identifies another working set on the bus via its unique ISO NAME.
### Attributes and Record Format (Table B.68)
The following table describes the structure of the External Reference NAME object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 42 | 3 | Object Type = External Reference NAME. |
| [1] | **Options** | Bitmask | 1 | 0 – 1 | 4 | Bit 0: Enabled (1=Reference active, 0=Disabled). |
| [2] | **NAME 0** | Integer | 4 | 0 – 2^32-1 | 5 – 8 | Bytes 1–4 of the NAME (ISO 11783-5) of the referenced working set. |
| [3] | **NAME 1** | Integer | 4 | 0 – 2^32-1 | 9 – 12 | Bytes 5–8 of the NAME of the referenced working set. |

## Functionality
This object functions as an "address book entry." When an ECU wants to load an object from another ECU, it uses this entry to tell the terminal which ECU (identified by the NAME) the object originates from.

* **Activation:** Should be initially disabled. When the referenced working set is online, the ECU can activate this object.

## Events (Table B.67)

The External Reference NAME object responds to the following events:

* **On Change Attribute:** Triggered by the command `Change Attribute`. The VT re-evaluates all currently displayed external object pointers that reference this NAME object.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.23.*
