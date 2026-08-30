# ID 3 – Container – ISO 11783-6 – B.4

The **Container** object with **ID 3** is used to logically group multiple objects. A container itself is not visible, but it allows you to move, show/hide, or split an entire group of objects.

### Attributes and Record Format (Table B.8)

The following table describes the structure of the Container object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 3 | 3 | Object type = Container. |
[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximum width of the container in pixels. Clipping occurs outside this range. |
[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Maximum height of the container in pixels. Clipping occurs outside this range. |
[3] | **Hidden** | Boolean | 1 | 0 or 1 | 8 | 0 = FALSE (Visible), 1 = TRUE (Hidden). Indicates whether the container is initially hidden. |
[-] | **Number of objects to follow** | Integer | 1 | 0 – 255 | 9 | Number of objects directly contained within. |
[-] | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Number of subsequent macro references. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Object ID of a contained object. |
| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 13 + ... | X-position relative to the container (pixels). |
| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 15 + ... | Y-position relative to the container (pixels). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Relative Positioning and Clipping

Within a container, a **separate coordinate system** begins:

- **Relative Coordinates:** The X and Y positions of child objects are referenced to the upper left corner of the container.
- **Clipping:** All objects or parts of objects that lie outside the area defined by `Width` and `Height` are clipped by the container and not displayed.
- **Group Move:** When the container is moved (e.g., via `Change Child Position`), all objects within it move automatically.

## Events (Table B.7)

The container reacts to the following events:

- **On Show:** Triggered by the command `Show Object` (even if the container is already visible). The VT redraws the contained objects.
- **On Hide:** Triggered by the command `Hide Object`. The container is overdrawn with the background color of the parent mask.
- **On Refresh:** Triggered when changes are made to child objects that require redrawing.
- **On Change Child Location / Position:** Updates the position of child objects.
- **On Change Size:** Reacts to changes in the container's size.

## Practical Use

Containers are essential for dynamic user interfaces:

- **Show/Hide:** Complex control panels or status indicators can be shown or hidden at the touch of a button using the command `IsoVtcCmd_ObjHideShow`.
- **Space Saving:** Multiple containers can reside in the same location; by cleverly switching their visibility, different "tabs" or modes can be implemented.

### Examples from the ISO Designer

![ISOBUS Container (ID 3) ISO-Designer view 1 (Examples from the ISO Designer)](https://user-images.githubusercontent.com/69573151/94602403-17f13b00-0295-11eb-8216-34070ca1bca8.png)
![ISOBUS Container (ID 3) ISO-Designer view 2 (Examples from the ISO Designer)](https://user-images.githubusercontent.com/69573151/94606853-5f7ac580-029b-11eb-9293-18570b481dbf.png)

## Implementation Implications

Since the container is a logical element, it consumes very little processing power itself, but is powerful in controlling the Z-order and grouping. Developers should ensure that `Width` and `Height` are set correctly to avoid unwanted clipping.

Further information and examples can be found in the [ISOBUS Wiki - Container](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/container) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*
