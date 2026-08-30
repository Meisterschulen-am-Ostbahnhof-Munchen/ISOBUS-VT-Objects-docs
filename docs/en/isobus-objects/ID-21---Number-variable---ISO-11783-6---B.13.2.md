# ID 21 – Number variable – ISO 11783-6 – B.13.2
The **Number Variable** object with **ID 21** is a pure data object. It stores a numeric value that can be referenced by other display or input objects.
### Attributes and Record Format (Table B.43)
The following table describes the structure of the Number Variable object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 21 | 3 | Object Type = Number Variable. |
| [1] | **Value** | Integer | 4 | 0 – 2^32-1 | 4 – 7 | 32-bit unsigned integer value. |

## Functionality and Referencing
Variables are not visible objects. They are never directly inserted into a mask or container as a "child" object, but rather serve as a data source for other objects:

- **Referencing:** Objects such as *Input Number* (ID 9), *Output Number* (ID 12), or *Output Meter* (ID 17) reference the ID of a Number Variable via their attribute `Variable reference`.
- **Central Data Storage:** Multiple display objects can reference the same variable. If the value of the variable is changed, the VT automatically updates all affected displays.

## Events (Table B.42)

The Number Variable object reacts to the following events:

- **On Change Value:** Triggered when the value changes (by a command or operator input). The VT redraws all objects that reference this variable.

## Implementation Implications

Number variables are the backbone of communication between the machine and the terminal.

- **Efficiency:** Instead of updating each display object individually, the ECU only changes the value of the central variable.
- **Consistency:** Using variables ensures that the same current value is always displayed in different parts of the user interface (e.g., main screen and settings menu).

Further information and examples can be found in the [ISOBUS Wiki - Number Variable](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-variable)] by Tobias Tenberg.

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018 standard.*