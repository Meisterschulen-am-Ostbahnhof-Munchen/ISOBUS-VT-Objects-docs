# ID 45 – Colour Palette – ISO 11783-6 – B.26

The **Colour Palette** object with **ID 45** (from VT version 6 onwards) allows a working set to completely replace the terminal's default color palette with its own ARGB color definitions.

### Attributes and Record Format (Table B.73)

The following table describes the structure of the Colour Palette object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 45 | 3 | Object type = Color Palette. |

| [1] | **Options** | Bitmask | 1 | 0 | 4 | Reserved (should be 0). |

| - | **Number of ARGB values to follow** | Integer | 2 | 0 – 256 | 5 – 6 | Number of following color definitions. |

| - | **Repeat:** {B} | Integer | 1 | 0 – 255 | 7 + ... | Blue value. |

| - | {G} | Integer | 1 | 0 – 255 | 8 + ... | Green value. |

| - | {R} | Integer | 1 | 0 – 255 | 9 + ... | Red value. |

| - | {A} | Integer | 1 | 0 – 255 | 10 + ... | Alpha value (0 = Transparent, 255 = Opaque). |

## Functionality
When a Colour Palette object is active, it replaces the default colors of the terminal for this working set. The colors are populated starting at index 0.

**Activation:** A Colour Palette can be set as the default via the *Working Set Special Controls* object (ID 47) or activated at runtime using the `Select Colour Map or Palette` command.

**Transparency:** The alpha channel enables semi-transparent colors. However, this should be used with caution, especially with overlapping objects.

## Difference to the Colour Map (ID 39)

While the *Colour Map* only changes the assignment (indexing) of existing terminal colors, the *Colour Palette* redefines the physical colors (ARGB values). This enables true branding in company colors.

## Events

The object itself does not trigger any events, but it affects the display of all objects that use colors.

* **On Change Attribute:** Triggered when attributes are changed. The virtual machine may need to redraw the entire screen.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.26.*