# ID 22 – String variable – ISO 11783-6 – B.13.3
The **String Variable** object with **ID 22** is used to store text strings that can be referenced by display or input objects.
### Attributes and Record Format (Table B.44)
The following table describes the structure of the String Variable object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 22 | 3 | Object type = String Variable. |
| - | **Length** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximum fixed length of the string in bytes. |
| - | **Value** | String | Length | - | 6 ... | String consisting of characters. Must be padded with spaces to reach the specified length. |

## Functionality and Special Features
Like the *Number Variable*, the *String Variable* is a pure data object without its own visual representation.

* **Fixed Length:** The length of the variable is set in the pool during creation and cannot be increased at runtime.
* **Padding:** If a string shorter than the defined length is stored, the VT automatically pads the remainder with spaces.
* **Data Types:** Supports both 8-bit characters (default) and WideStrings (for special characters). The ECU can switch the type between these formats at runtime.
* **Fixed Length:**
## Referencing and Updating
* **Referencing:** Objects such as *Input String* (ID 8) or *Output String* (ID 11) reference the ID of a string variable via their attribute `Variable reference`.
* **Automatic Redraw:** As soon as the ECU changes the value of the variable via the `Change String Value` command, the VT automatically updates all visible objects that use this variable.

## Events (Table B.42)

The string variable object reacts to the following events:

* **On Change Value:** Triggered when the value changes (by the `Change String Value` command or operator input). The VT redraws all objects that reference this variable.

## Implementation Significance
String variables are essential for dynamic text such as plain-text error messages, work order names, or driver names. Since text input and modification via the CAN bus (ISOBUS) are resource-intensive, string variables should be defined as concisely as possible.

Further information and examples can be found in the [ISOBUS Wiki - String Variable](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-variable)] by Tobias Tenberg.

----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*
