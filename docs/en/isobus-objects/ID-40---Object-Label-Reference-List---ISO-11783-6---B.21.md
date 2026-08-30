# ID 40 – Object Label Reference List – ISO 11783-6 – B.21
The **Object Label Reference List** object with **ID 40** (from VT version 5 onwards) is used to assign a list of label objects to objects (such as variables or input fields).
### Attributes and Record Format (Table B.64)
The following table describes the structure of the Object Label Reference List object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 40 | 3 | Object type = Object Label Reference List. |
| [1] | **Number of Labelled objects** | Integer | 2 | 0 – 65535 | 4 – 5 | Number of subsequent label assignments. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 6 – 7 ... | Object ID of the object to be labeled (e.g., Input Number). |
| - | {String Variable reference} | Integer | 2 | 0 – 65535 | 8 – 9 ... | Object ID of a string variable containing the label text (or FFFFh = no text). |
| - | {Font type} | Integer | 1 | 0 – 255 | 10 ... | Font type (see Annex K). Ignored for WideString or NULL. |
| - | {Object Label graphic representation} | Integer | 2 | 0 – 65535 | 11 – 12 ... | Object ID of a graphic (icon) for the label (or FFFFh = no graphic). |

## Meaning and Functionality
This object is used to assign a name (text) and an icon (graphic) to other objects (e.g., working sets, input fields). These "labels" are used by the VT:

- **Working Set Label:** The label for the working set object is displayed in the list of active workgroups.
- **Input Labels:** For input fields, the VT displays the label (text/graphic) in the popup editor so the user knows which value they are currently editing (e.g., "seed quantity" instead of just "120").

Only **one** Object Label Reference List is allowed per object pool.

----

*Note: For detailed specifications, please refer to the official ISO 11783-6:2018, B.21.*