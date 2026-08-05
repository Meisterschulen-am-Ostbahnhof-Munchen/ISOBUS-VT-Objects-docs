# ID 0 – Working set – ISO 11783-6 – B.1
![](https://user-images.githubusercontent.com/69573151/94337326-edc82080-ffe9-11ea-93d7-61752b51d9cf.png)
----
The **Working Set** object with **ID 0** is the central management element of a workgroup (Working Set) in ISOBUS. It defines how the workgroup presents itself to the Virtual Terminal (VT) and which interface is initially displayed.

## Key properties (according to ISO 11783-6, Annex B.1)

Each workgroup must define **exactly one** Working Set object in its object pool. Only the VT can activate this object.

...
### Attributes and Record Format (Table B.2)

The following table describes the structure of the Working Set object in the object pool (byte stream).

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 0 | 3 | Object type = Working Set. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Background color. |
| [2] | **Selectable** | Boolean | 1 | 0 or 1 | 5 | 0 = FALSE, 1 = TRUE. Indicates whether the working set can be selected by the operator. |
| [3] | **Active mask** | Integer | 2 | 0 – 65534 | 6 – 7 | Object ID of the data or alarm mask displayed when the working set is active. |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 8 | Number of following child objects (designator). Must be at least 1. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 9 | Number of following macro references. |
| - | **Number of languages to follow** | Integer | 1 | 0 – 255 | 10 | Number of following language codes. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Object ID of a child object (part of the designator). List of all objects *before* the macros. |
| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 13 + ... | Relative X position of the child object (pixels). |
| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 15 + ... | Relative Y position of the child object (pixels). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After the objects) Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed (or reference to the 16-bit Macro ID). |
| - | **Repeat:** {Language Code} | String | 2 | - | var. | (After the macros) Two-letter language code according to ISO 639 (e.g., "de", "en"). |

### Designator (Child Objects)

The Working Set object serves as a container for a graphical identifier (designator) that represents the device (e.g., icon and name).

* **Structure:** The number of objects specified under `Number of objects to follow` follows directly in the record. Each child object is defined by its ID, X-Pos, and Y-Pos.
* **Space Limit:** All of these objects must fit within the area of a **softkey**. The VT truncates anything that extends beyond this area.
* **Coordinates:** Relative to the upper left corner of the Working Set object.

### Macros (Events)

The working set defines events that can trigger macros. See Table B.1 for the event definitions.

* **On Activate:** Triggered when the working set is selected by the operator.
* **On Deactivate:** Triggered when the working set is exited.
* **On Change Active Mask:** Triggered by the command `Change Active Mask`.

### Language Support

The list of language codes (`Language Code`) informs the VT which languages the working set supports. Each code consists of two ASCII characters (e.g., "de", "en", "fr"). This is for informational purposes; the actual language switching is performed by loading the corresponding language objects or texts.

### Language Support

The list of language codes (`Language Code`) informs the VT which languages the working set supports.
## Implementation Implementation Implementation Implementation

The working set object is the "anchor" of an application on the VT. Without a correctly defined object ID 0, the VT cannot identify the working group or load the first form. Developers must ensure that the `Active mask` AID points to a valid data form in the pool.

Further information and examples can be found in the [ISOBUS Wiki - Working Set](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/working-set)] by Tobias Tenberg.

ISOBUS Wiki - Working Set](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/working-set)
----

*Note: For detailed implementation information on data types and message formats, please refer to the official ISO 11783-6:2018 standard.*