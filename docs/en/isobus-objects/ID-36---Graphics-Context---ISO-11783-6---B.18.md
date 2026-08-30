# ID 36 – Graphics Context Object – ISO 11783-6 – B.18
The **Graphics Context Object (GCO)** with **ID 36** (from VT version 4 onwards) provides a dynamic graphics buffer (canvas) into which the ECU can draw at runtime. It is comparable to a bitmap whose content can be modified pixel-perfectly.
### Attributes and Record Format (Table B.59)
The following table describes the structure of the Graphics Context Object in the object pool.
| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 36 | 3 | Object type = Graphics Context. |
| [1] | **Viewport Width** | Integer | 2 | 0 – 32767 | 4 – 5 | Width of the visible window (display in the canvas). |
| [2] | **Viewport Height** | Integer | 2 | 0 – 32767 | 6 – 7 | Height of the visible window. |
| [3] | **Viewport X** | Signed Integer | 2 | -32768 to +32767 | 8 – 9 | X-position of the viewport relative to the canvas (0 = Left). |
| [4] | **Viewport Y** | Signed Integer | 2 | -32768 to +32767 | 10 – 11 | Y-position of the viewport relative to the canvas (0 = Top). |
[5] | **Canvas Width** | Integer | 2 | 0 – 32767 | 12 – 13 | Total width of graphics memory. |
[6] | **Canvas Height** | Integer | 2 | 0 – 32767 | 14 – 15 | Total height of graphics memory. |
[7] | **Viewport Zoom** | Float | 4 | -32.0 to +32.0 | 16 – 19 | Viewport zoom factor (see Table F.1). |
[8] | **Graphics Cursor X** | Signed Integer | 2 | -32768 to +32767 | 20 – 21 | Current X position of the drawing cursor. |
[9] | **Graphics Cursor Y** | Signed Integer | 2 | -32768 to +32767 | 22 – 23 | Current Y position of the drawing cursor. |
[10] | **Foreground Colour** | Integer | 1 | 0 – 255 | 24 | Foreground color for drawing operations. |
[11] | **Background Colour** | Integer | 1 | 0 – 255 | 25 | Background color. Used for filling during parsing. |
[12] | **Font Attributes** | Integer | 2 | 0 – 65534, 65535 | 26 – 27 | Reference to the Font Attributes object (for text commands). |
[13] | **Line Attributes** | Integer | 2 | 0 – 65534, 65535 | 28 – 29 | Reference to the Line Attributes object (for line commands). |
[14] | **Fill Attributes** | Integer | 2 | 0 – 65534, 65535 | 30 – 31 | Reference to Fill Attributes object (for fill commands). |
| [15] | **Format** | Integer | 1 | 0 – 2 | 32 | Canvas color depth: 0=1-bit, 1=4-bit, 2=8-bit. |
| [16] | **Options** | Bitmask | 1 | 0 – 3 | 33 | Bit 0: Transparency | Bit 1: Color (0=FG/BG Attribute, 1=Line/Font/Fill Attribute). |
| [17] | **Transparency Color** | Integer | 1 | 0 – 255 | 34 | Transparency color (when Options Bit 0 is set). |

## Functionality and Structure
The GCO consists of two main components:

1. **Canvas:** A persistent graphics memory (bitmap) with a defined size (`Canvas Width/Height`). The content is retained even when the object is not displayed.

2. **Viewport:** A "window" that displays a portion of the canvas. The viewport defines the size of the object on the canvas. By changing `Viewport X/Y`, the content can be scrolled (panned).

## Graphics Context Commands
The canvas is manipulated using special commands (see ISO 11783-6, Annex F), such as:

- `Set Graphics Cursor`: Sets the writing position.
- `Draw Point / Line / Rectangle / Polygon / Ellipse`: Draws geometric shapes.
- `Draw Text`: Writes text to the cursor position.
- `Copy Canvas`: Copies areas within the canvas.

## Events (Table B.58)

The Graphics Context object reacts to the following events:

- **On Change Attribute:** Triggered when attributes change (e.g., viewport position, zoom). The VT updates the display.
- **On Change Background Colour:** Fills the object (the canvas) with the new background color. **Caution:** Deletes the previous content!

## Application Example
Typical applications include **GPS maps** (swath logging), where the ECU continuously plots the driven route as a line in the GCO.

----

*Note: For detailed specifications, refer to the official ISO 11783-6:2018, B.18.*