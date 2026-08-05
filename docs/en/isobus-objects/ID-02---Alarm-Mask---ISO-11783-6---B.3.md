# ID 2 – Alarm Mask – ISO 11783-6 – B.3

The **Alarm Mask** with **ID 2** is used to display critical information or warnings. It takes precedence over normal data masks and, depending on its priority, can overlay the entire display or parts of it.

### Attributes and Record Format (Table B.6)

The following table describes the structure of the Alarm Mask object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 2 | 3 | Object type = Alarm Mask. |

[1] | **Background color** | Integer | 1 | 0 – 255 | 4 | Background color of the mask. |

[2] | **Soft Key Mask** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Object ID of the associated soft key mask (65535 = NULL). |

[3] | **Priority** | Integer | 1 | 0 – 2 | 7 | 0 = High, 1 = Medium, 2 = Low. |

[4] | **Acoustic signal** | Integer | 1 | 0 – 3 | 8 | 0 = Highest priority, 1 = Medium, 2 = Low, 3 = Off. |

[-] | **Number of objects to follow** | Integer | 1 | 0 – 255 | 9 | Number of directly contained objects. |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Number of following macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Object ID of a contained object. |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 13 + ... | X position relative to the mask (pixels). |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 15 + ... | Y position relative to the mask (pixels). |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (By Object) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Priority Levels and Display
The priority not only controls the order of the alarms, but often also their visual display on the VT:

* **High Priority (0):** The operator is in danger or a serious malfunction has occurred. These alarms must be acknowledged immediately or force the terminal to focus.

* **Medium Priority (1):** Normal machine malfunction.

* **Low Priority (2):** For information only (status messages).

## Events (Events - Table B.5)

The alarm screen reacts to the following events:

* **On Show:** Triggered when the screen becomes visible. The VT sends a `VT Status` message.

* **On Hide:** Triggered when the mask is removed from the display.

* **On Refresh:** Triggered when objects within the mask are changed.

* **On Change Priority:** When the priority changes, the VT re-evaluates all active alarms.

* **On Change Soft Key Mask:** Changes the softkey assignment when an alarm mask is active.

* **On Change Child Location / Position:** Updates child objects.

* **On Change Attribute:** Reacts to general attribute changes.

## Behavior with Multiple Alarms
If multiple alarm masks from different workgroups are active simultaneously, the priority (AID 3) determines which mask takes precedence. If the priority is the same, the VT usually decides (often based on chronological order).

## Implementation Implementation Implementation Implementation Masks should be used sparingly and only for genuine warnings, as they interrupt the operator's workflow. It is important to select the appropriate audible alert (AID 4) to guide attention without stressing the operator.

Further information and examples can be found in the ISOBUS Wiki - Alarm Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/alarm-mask) by Tobias Tenberg.

----

*Note: For detailed specifications regarding data types and message formats, please refer to the official ISO 11783-6:2018.*