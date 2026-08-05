# Insert Bitmaps
!!! Note
ISO 11783-6 does not support PNG graphics for VT3/UT2.
See also [ISOBUS-Objects-Versions](ISOBUS-Objekte-Versionen.md)]


## Find PNG

<https://www.iso.org/obp/>

Download PNG

Right-click on the icon and save it, ideally in the following folder:
...
C:\git\ms\4diac_training1\Valve Control\ISO-DesignerProjects\Workspace\DefaultPool\img

Other folders are possible, but this one is recommended for the sake of organization.

## ImageMagick®

<https://imagemagick.org/> can simplify the conversion process; it can convert hundreds of images with a single mouse click, if needed.
...
<https://imagemagick.org/script/download.php#windows> Download for Windows

at:

<https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/script>

You will find a script that (assuming ImageMagick is installed)

executes the following processes when double-clicked:

Original:
...
![image](https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png)

by `https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png`

### 1. All files under img_original will be cropped by 2 pixels on all sides:

To the folder: [img_original](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_original)

| Before | | After |

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_original/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) |

| 200x200 | | 196x196 |

This removes the 2px crop marks from <https://www.iso.org/obp/>. These are generally undesirable for aesthetic reasons.

...
The cropped images are then located under "img_cropped"

### 2. All files under img_cropped are scaled to 64x64

to the folder: [img_cropped](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped)

| before | | after |

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized/Tractor_wheel_slip_200.png) |

| 196x196 | | 64x64 |

The cropped images are then located under "img_resized"

### 3. Conversion to 2 colors (monochrome)

to the folder: [img_resized](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized)

| before | | after |

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome/Tractor_wheel_slip_200.png) |

| 64x64 | | 64x64 

The images are then located under "img_monochrome"

### 4. Conversion to BMP format

to the folder: [img_monochrome](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome)

| before | | after |

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img/Tractor_wheel_slip_200.bmp) |

| 64x64 | | 64x64 

The images are then located under "img"

to the folder: [img](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img)

## Paint

Converting PNG to BMP is very easy with Microsoft Paint, which is included in every Windows installation.

However, if you want to convert many files, the effort becomes considerable.

### Convert PNG to BMP

Name the bitmap appropriately; ISO filenames are often not very descriptive.

(no spaces, no umlauts) See: <https://docs.ms-muc-docs.de/projects/visual-programming-languages-docs/de/latest/Allgemeines.html#namen>

### Scaling BMP

### BMP Scaling ...
Size matters:

| where | size | | | |

|----------|-------------|---|---|---|

| Softkey | 72x72 pixels | | | |

| Datamask | free | | | |

| CCI A3 | 64x64 pixels | | | |

Thoughts:

80x80 --> as a button, resulting in an inner area of 72x72

72x72 --> as a button, creates an inner area of 64x64

!!! Note

Tip: Use these sizes for buttons as well; it creates a clean look.

For larger buttons, use multiples of this size, e.g., 80x160, 160x160, etc.

Recommendation:

If the symbol is to be used as a softkey and as a CCI A3 symbol, then make it 64x64 pixels.
...
You can also crop the images before scaling them.
...
### Reduce BMP Color Depth

###
For faster loading, reduce the color depth as much as possible.

Windows Paint offers the following color depths:
...
![image](https://github.com/user-attachments/assets/e8f49c00-4a94-4d6f-b1e2-3ce32dc89c61)

| Format | Colors | Bit | Note |

-------------------|------------------------------|-----|--------------------------------|

| Monochrome Bitmap | 2<sup>1</sup> = 2 | 1 | |

| 16-Color Bitmap | 2<sup>4</sup> = 16 | 4 | |

| 256-Color Bitmap | 2<sup>8</sup> = 256 | 8 | |

| 24-Bit Bitmap | 2<sup>24</sup> = 16,777,216 | 24 | not present in ISO 11783-6 |

## Insert BMP into ISO Designer

The images can now be used in ISO Designer.

In the case of monochrome, white can be set as a transparent background.

In the case of other color depths, pink is often used.

---

### 🌐 Related topic subpages on ms-muc-docs.de
* [🌐 Eclipse 4diac IDE & Color Reference on ms-muc-docs.de](https://www.ms-muc-docs.de/iec-61499/eclipse-4diac/)
