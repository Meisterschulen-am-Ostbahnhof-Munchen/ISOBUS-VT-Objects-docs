# Standard Farbpalette (ISO 11783-6 Table A.4)

```{index} single: Farben
```

Die VT-Standardfarbpalette definiert 256 Farben. Die ersten 16 Farben sind identisch mit der Standard-VGA-Palette.

| Index | Name / Beschreibung | R, G, B Wert | Hex Code (RGB) |
| :--- | :--- | :--- | :--- |
| **0** | **Black** | 0, 0, 0 | `#000000` |
| **1** | **White** | 255, 255, 255 | `#FFFFFF` |
| **2** | **Green** | 0, 153, 0 | `#009900` |
| **3** | **Teal** | 0, 153, 153 | `#009999` |
| **4** | **Maroon** | 153, 0, 0 | `#990000` |
| **5** | **Purple** | 153, 0, 153 | `#990099` |
| **6** | **Olive** | 153, 153, 0 | `#999900` |
| **7** | **Silver** | 204, 204, 204 | `#CCCCCC` |
| **8** | **Grey** | 153, 153, 153 | `#999999` |
| **9** | **Blue** | 0, 0, 255 | `#0000FF` |
| **10** | **Lime** | 0, 255, 0 | `#00FF00` |
| **11** | **Cyan** | 0, 255, 255 | `#00FFFF` |
| **12** | **Red** | 255, 0, 0 | `#FF0000` |
| **13** | **Magenta** | 255, 0, 255 | `#FF00FF` |
| **14** | **Yellow** | 255, 255, 0 | `#FFFF00` |
| **15** | **Navy** | 0, 0, 153 | `#000099` |
| ... | ... | ... | ... |
| **232-255**| **Proprietary** | - | VT-Hersteller spezifisch |

*Hinweis: Für die Indizes 16 bis 231 ist eine algorithmische Verteilung im Farbwürfel (6x6x6) definiert. Siehe ISO 11783-6 Table A.4 für die vollständige Liste.*

Weitere Informationen und Visualisierungen finden sich im [ISOBUS Wiki - Colours](https://isobus-studio.com/isobus-wiki/isobus-colours) von Tobias Tenberg.

### Transparenz
Der Farbindex, der im Attribut "Transparency Colour" (z. B. bei Picture Graphics) angegeben wird, wird nicht gezeichnet. Oft wird hierfür eine "Signalfarbe" wie Magenta (Index 13) verwendet, wenn diese im Bild nicht vorkommt.
