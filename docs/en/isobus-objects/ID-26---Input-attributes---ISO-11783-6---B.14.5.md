# ID 26 – Input attributes – ISO 11783-6 – B.14.5
The **Input Attributes** object with **ID 26** is used to validate text input. It defines which characters an operator is allowed to enter into a linked *Input String* object.
### Attribute and Record Format (Table B.52)
The following table describes the structure of the Input Attributes object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 26 | 3 | Object type = Input Attributes. |
| [1] | **Validation type** | Integer | 1 | 0 – 1 | 4 | 0 = Allowed characters (list), 1 = Forbidden characters (list). |
| - | **Length** | Integer | 1 | 0 – 255 | 5 | Length of the validation string in bytes. |
| - | **Validation string** | String | Length | - | 6 ... | List of characters (8-bit string). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Number of following macro references. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Validation

This object acts as a filter for keyboard input on the VT:

- **Referencing:** An *Input String* object (ID 8) references this object.
- **Filter Logic:** If `Validation type` is set to 0, the VT only allows the characters contained in `Validation string`. If it is set to 1, all characters except those listed are accepted.
- **Limitation:** This object only supports **8-bit strings**. If the linked input field uses a WideString, no validation takes place.

## Events (Table B.51)

The Input Attributes object reacts to the following events:

- **On Change Value:** Triggered by the command `Change String Value`. The VT updates the validation string.

## Implementation Implications
Input attributes are an important tool for preventing user errors.

- **Example Numeric:** A validation string "0123456789." restricts a text field to purely numeric characters.
- **Example Special Characters:** Prohibits characters such as ";" or "'", which could cause problems in databases or file systems.

### Note: Extended Input Attributes (ID 38)
For validating WideStrings (Unicode), the *Extended Input Attributes* object must be used, which allows the definition of entire code planes.

----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*