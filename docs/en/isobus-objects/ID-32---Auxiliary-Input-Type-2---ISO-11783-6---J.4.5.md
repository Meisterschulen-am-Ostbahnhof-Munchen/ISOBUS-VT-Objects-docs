# ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5
The **Auxiliary Input Type 2** object with **ID 32** defines a physical control element of an auxiliary input device (e.g., a button on a joystick) from VT version 3 onwards.
### Attributes and Record Format (Table J.4)
The following table describes the structure of the Auxiliary Input Type 2 object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 32 | 3 | Object type = Auxiliary Input Type 2. |
[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color. |
[2] | **Function attributes** | Bitmask | 1 | - | 5 | Bitmask for function type and control (see below). |
[3] | **Input ID** | Integer | 1 | 0 – 255 | 6 | ID of the physical input. |
[-] | **Number of objects to follow** | Integer | 1 | 1 – 255 | 7 | Number of directly contained objects (designator). |
[-] | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Object ID of a contained object. |
[-] {X Location} | Signed Integer | 2 | -32768 to +32767 | 10 + ... | X position relative to the upper left corner. |
| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 12 + ... | Y position relative to the upper left corner. |

### Function Attributes (Bitmask AID 2)
* **Bits 0–3:** Auxiliary function type (see Table J.5)
* 0: Boolean Latching
* 1: Analogue
* 2: Boolean Momentary
* 3: Boolean Latching
* ...
* **Bits 4–5:** Reserved
* **Bit 6:** Reserved
* **Bit 7:** Single Assignment (1 = May only be assigned to one function).

## Functionality

The terminal uses this information to display the available keys and their physical properties to the user. When the user presses a key, the input device sends a status message with the current value (Boolean or Analog) and the `Input ID` to the ISOBUS.

It replaces the obsolete Type 1 (ID 30).

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, Annex J.*