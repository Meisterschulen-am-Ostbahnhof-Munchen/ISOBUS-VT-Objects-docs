# ID 5 – Key (Soft Key) – ISO 11783-6 – B.6
![](https://user-images.githubusercontent.com/69573151/95071971-c7e9fc80-070a-11eb-8261-f87394d32fb4.png)
## 🎧 Podcast
* [ISO 11783-6: Understanding Softkeys and the Virtual Terminal – Your Key to Agricultural Machinery Mechatronics ](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
----
The **Key Object** (ID 5) defines the appearance and functional code of a softkey. It is the interactive element within a softkey interface.

### Attributes and Record Format (Table B.12)

The following table describes the structure of the Key Object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 5 | 3 | Object type = Key. |

| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Background color of the key. |

| [2] | **Key code** | Integer | 1 | 1 – 255 | 5 | Code sent in the `Soft Key Activation` message. (0 is reserved for ACK). |

| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 6 | Number of directly included objects (symbols, text). |

| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 7 | Number of subsequent macro references. |

| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Object ID of a contained object. |

| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 10 + ... | X position relative to the button (pixels). |

| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 12 + ... | Y position relative to the button (pixels). |

| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |

| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Designator and Child Objects

A Key object acts as a container for the graphical content of the key (e.g., icons or text).

* **Coordinates:** The X and Y positions of the child objects are relative to the upper left corner of the softkey designator.
* **Clipping:** Any objects that lie outside the physical area of the softkey are clipped by the VT. Since softkey sizes vary, content should be placed centrally.

## Events (Events - Table B.11)

The Key object responds to the following events:

* **On Key Press:** Triggered when the key is pressed. Sends `Soft Key Activation`.
* **On Key Release:** Triggered when the key is released. Sends `Soft Key Activation`.
* **On Change Background Colour:** Responds to a change in the key color.
* **On Change Child Location / Position:** Updates the graphical content.
* **On Change Attribute:** Responds to general attribute changes.
* **On Input Field Selection / De-selection:** Triggered when the key receives or loses focus (during navigation via encoder/cursor).

## The Key Code

The **Key Code** (AID 2) is the crucial link to the software logic (C code). While `Object ID` identifies the key in the graphics pool, the application uses `Key Code` to assign the function. This allows different graphical keys (different IDs) to be assigned the same functional code.

## Implementation Implementation Implications

Since the actual size and shape of softkeys can vary from VT to VT (e.g., portrait vs. landscape, touch vs. hardware buttons), it is best practice to choose sufficiently small graphical content (bitmaps) within the key and center it. A key object without child objects appears as an empty area in the chosen background color.

Further information and examples can be found in the [ISOBUS Wiki - Softkey](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/softkey) by Tobias Tenberg].

----

*Note: For detailed specifications on data types and message formats, please refer to the official ISO 11783-6:2018.*
