# Standard Color Palette (ISO 11783-6 Table A.4)

The VT standard color palette defines 256 colors. The first 16 colors are identical to the standard VGA palette.

| Index | Name / Description | R, G, B Value | Hex Code (RGB) |
| :--- | :--- | :--- | :--- |
**0** | **Black** | 0, 0, 0 | `#000000` |
**1** | **White** | 255, 255, 255 | `#FFFFFF` |
**2** | **Green** | 0, 153, 0 | `#009900` |
**3** | **Teal** | 0, 153, 153 | `#009999` |
| **4** | **Maroon** | 153, 0, 0 | `#990000` |
| **5** | **Purple** | 153, 0, 153 | `#990099` |
| **6** | **Olive** | 153, 153, 0 | `#999900` |
| **7** | **Silver** | 204, 204, 204 | `#CCCCCC` |
| **8** | **Gray** | 153, 153, 153 | `#999999` |
| **9** | **Blue** | 0, 0, 255 | `#0000FF` |
| **10** | **Lime** | 0, 255, 0 | `#00FF00` |
| **11** | **Cyan** | 0, 255, 255 | `#00FFFF` |
| **12** | **Red** | 255, 0, 0 | `#FF0000` |
| **13** | **Magenta** | 255, 0, 255 | `#FF00FF` |
| **14** | **Yellow** | 255, 255, 0 | `#FFFF00` |
| **15** | **Navy** | 0, 0, 153 | `#000099` |
| ... | ... | ... | ... |
| **232-255** | **Proprietary** | - | VT manufacturer specific |

*Note: For indices 16 to 231, an algorithmic distribution is defined in the color cube (6x6x6). See ISO 11783-6 Table A.4 for the complete list.*

Further information and visualizations can be found in the [ISOBUS Wiki - Colours](https://isobus-studio.com/isobus-wiki/isobus-colours) by Tobias Tenberg.]

### Transparency

The color index specified in the "Transparency Colour" attribute (e.g., in Picture Graphics) is not drawn. Often, a "signal color" such as magenta (index 13) is used if it is not present in the image.

