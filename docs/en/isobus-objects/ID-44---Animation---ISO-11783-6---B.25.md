# ID 44 – Animation – ISO 11783-6 – B.25

The **Animation** object with **ID 44** (from VT version 5 onwards) enables the automatic or manual playback of a sequence of objects (frames).

### Attributes and Record Format (Table B.72)

The following table describes the structure of the Animation object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 44 | 3 | Object type = Animation. |

| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Width of the animation area in pixels. |

[2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Height of the animation area in pixels. |

[3] | **Refresh Interval** | Integer | 2 | 0 – 65535 | 8 – 9 | Time in ms between frames (0 = Timer off). |

[4] | **Value** | Integer | 1 | 0 – 255 | 10 | Current list index of the displayed object (0-254). |

[5] | **Enabled** | Integer | 1 | 0 or 1 | 11 | 0 = Stopped (Disabled), 1 = Animating (Enabled). |

[6] | **First Child Index** | Integer | 1 | 0 – 254 | 12 | Start index of the animation sequence. |

[7] | **Last Child Index** | Integer | 1 | 0 – 254 | 13 | End index of the animation sequence. |

[8] | **Default Child Index** | Integer | 1 | 0 – 254 | 14 | Index of the object displayed when the animation is disabled (depending on Options). |

[9] | **Options** | Bitmask | 1 | 0 – 7 | 15 | Bit 0: Sequence (0=Single Shot, 1=Loop) | Bits 1–2: Disabled Behavior (0=Pause, 1=Reset to First, 2=Default Object, 3=Blank). |


- | **Number of objects to follow** | Integer | 1 | 0 – 255 | 16 | Number of frames (objects) included. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 18 + ... | Object ID of a frame (child object). |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 20 + ... | X position relative to the animation. |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 22 + ... | Y position relative to the animation. |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

## Functionality
The animation object manages a list of child objects. When `Enabled` is 1, the terminal automatically increments `Value` (index) at the same rate as `Refresh Interval`.

* **Loop:** After reaching `Last Child Index`, the loop starts again at `First Child Index`.

* **Single Shot:** The animation stops at the last frame.

* **Deactivation:** The behavior when stopping (pause, reset to frame 1, default image, or blank) is controlled via the options.

## Events (Events - Table B.71)

The animation object reacts to the following events:

* **On Enable / On Disable:** State change.

* **On Change Value:** When the index is changed (manually or automatically). The VT draws the new object.

* **On Change Attribute:** Reacts to general attribute changes.

* **On Change Size:** Reacts to size changes.

* **On Refresh:** Triggered by the timer (refresh interval) or other refresh conditions.

## Recommendation
To avoid overloading the terminal's performance, individual objects should be kept small. A refresh interval of at least 200 ms is recommended.


----

*Note: For detailed specifications, please refer to the official ISO 11783-6:2018, B.25.*