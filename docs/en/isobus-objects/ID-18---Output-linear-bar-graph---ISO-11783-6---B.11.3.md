# ID 18 – Output Linear Bar Graph – ISO 11783-6 – B.11.3

The **Output Linear Bar Graph** object with **ID 18** is used to display values in the form of a bar graph or thermometer. It supports various orientations and offers the option of highlighting a target value.

### Attributes and Record Format (Table B.37)

The following table describes the structure of the Output Linear Bar Graph object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 18 | 3 | Object type = Linear Bar Graph. |

[1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the bounding rectangle in pixels. |

[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the bounding rectangle in pixels. |

[3] | **Colour** | Integer | 1 | 0 – 255 | 8 | Color of the bar fill and border. |

[4] | **Target line color** | Integer | 1 | 0 – 255 | 9 | Color of the target value line (when drawn). |

[5] | **Options** | Bitmask | 1 | 0 – 63 | 10 | Bit 0: Draw Border | Bit 1: Draw Target Line | Bit 2: Draw Ticks | Bit 3: Type (0=Filled, 1=Line) | Bit 4: Axis Orientation (0=Vertical, 1=Horizontal) | Bit 5: Direction (0=Negative/Descending, 1=Positive/Ascending). |

| [6] | **Number of ticks** | Integer | 1 | 0 – 255 | 11 | Number of ticks. |

| [7] | **Min value** | Integer | 2 | 0 – 65535 | 12 – 13 | Minimum value. |

| [8] | **Max value** | Integer | 2 | 0 – 65535 | 14 – 15 | Maximum value. |

| [9] | **Variable reference** | Integer | 2 | 0 – 65534, 65535 | 16 – 17 | Reference to a Number variable for the current value. |

| [12] | **Value** | Integer | 2 | 0 – 65535 | 18 – 19 | Current value. Only if Variable Reference == NULL. |

| [10] | **Target value var.** | Integer | 2 | 0 – 65534, 65535 | 20 – 21 | Reference to a Number variable for the target value. |

| [11] | **Target value** | Integer | 2 | 0 – 65535 | 22 – 23 | Current target value. Only if Target value variable ref == NULL. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 24 | Number of following macro references. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality and Options
The bar graph is fitted into a rectangle and is transparent by default, so background graphics remain visible.

* **Alignment (AID 5, Bits 4 & 5):** Allows horizontal (left-to-right) or vertical (bottom-to-top) bars.

* **Display Type (Bit 3):** In addition to the classic fill bar, the object can also function as a "single pointer," where only a line is drawn at the current position.

* **Target Line:** An additional marker (e.g., a red line) that indicates a target value or a warning range.

## Scaling
The bar is calculated proportionally to the current value between `Value` and `Min value` and `Max value`. If the value is outside this range, the bar is either completely empty or completely filled.

## Events (Events - Table B.36)

The Output Linear Bar Graph object reacts to the following events:

* **On Change Value:** Triggered when `Value` or `Target value` changes. The VT updates the graph.

* **On Change Attribute:** Triggered when attributes change.

* **On Change Size:** Responds to size changes.

* **On Refresh:** Triggered when the VT needs to redraw the object.

## Implementation Implications
Bar charts are ideal for level indicators (fuel, seeds), temperature displays, or load indicators. The `Target line` option allows the operator to immediately visualize whether they are within the optimal operating range. Combining this with scale ticks improves readability.


## 🎧 Podcast

* [ISOBUS bar chart: The Output Linear Bar Graph object of ISO 11783-6 decoded ](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*