# ID 16 – Output polygon – ISO 11783-6 – B.10.5

The **Output Polygon** object with **ID 16** allows the drawing of complex, polygonal shapes by defining a list of vertices.

### Attributes and Record Format (Table B.33)

The following table describes the structure of the Output Polygon object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 16 | 3 | Object type = Polygon. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the enclosing virtual rectangle. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the enclosing virtual rectangle. |
| [3] | **Line attributes** | Integer | 2 | 0 – 65534 | 8 – 9 | Object ID of a Line Attributes object (for the outline). |
| [4] | **Fill attributes** | Integer | 2 | 0 – 65534, 65535 | 10 – 11 | Object ID of a Fill Attributes object (fill) or NULL. |
| [5] | **Polygon type** | Integer | 1 | 0 – 3 | 12 | 0=Convex, 1=Non-convex, 2=Complex, 3=Open. |
| - | **Number of points** | Integer | 1 | 3 – 255 | 13 | Number of vertices (minimum 3). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 14 | Number of following macro references. |
| - | **Repeat:** {Point X} | Integer | 2 | 0 – 65535 | 15 + ... | X-position of the point relative to the top left corner of the object. |
| - | {Point Y} | Integer | 2 | 0 – 65535 | 17 + ... | Y-position of the point relative to the top left corner of the object. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (By Points) Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Polygon Types and Fill Rules

The polygon type (AID 5) informs the VT about the complexity of the shape, which affects drawing efficiency:

- **Convex (0):** Simple shapes (e.g., triangle, hexagon) where each horizontal line intersects the edges only twice.
- **Non-Convex (1):** Indentations are possible, but edges do not intersect.
- **Complex (2):** Edges may intersect (e.g., a star). Here, the **even-odd rule** is applied for filling.
- **Open (3):** The points are only connected by lines; the polygon is not closed and not filled.

## Geometry and Points

- **Relative Position:** All points (`Point X`, `Point Y`) are referenced to the upper left corner of the polygon object.
- **Automatic Closing:** If the type is not "Open" and the last point is not identical to the first, the VT automatically closes the polygon with a line from the last to the first point.
- **Number of Points:** Up to 255 points can be defined.

## Events (Table B.32)

The output polygon object responds to the following events:

- **On Refresh:** Triggered by the `Change Polygon Point` or `Change Polygon Scale` command.
- **On Change Attribute:** Triggered when line or fill attributes change.
- **On Change Size:** Responds to a change in size (of the enclosing rectangle).

## Implementation Implementation Implementation

Polygons are very powerful for representing irregular shapes, such as tank contents in asymmetrical containers or for visualizing field outlines. Due to the computational load of complex polygons, ECU developers should, where possible, prefer convex polygon types if the shape allows it.

Further information and examples can be found in the ISOBUS Wiki - Polygon](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/polygon) by Tobias Tenberg.

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*
