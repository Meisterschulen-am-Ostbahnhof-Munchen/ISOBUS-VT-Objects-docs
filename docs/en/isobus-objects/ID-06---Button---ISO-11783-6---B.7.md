# ID 6 – Button – ISO 11783-6 – B.7
![](https://user-images.githubusercontent.com/69573151/94337426-7d6dcf00-ffea-11ea-8ab0-ca710054a888.png)
**Annex B.7 – Button**
Annex B.7 of ISO 11783-6:2018 is dedicated to the detailed definition of the "button" object in the context of the Virtual Terminal (VT). Buttons are basic interactive user interface elements that allow the operator to trigger actions or send commands to the agricultural machine or implement.
**Overview of the Button Object**
The button object, as defined in B.7, is a graphical element displayed on the VT's data screen. It is designed so that the operator can interact with it by touch (on touchscreens) or selection using a navigation tool (such as cursor keys). Each button is associated with a specific function or command that is executed when the button is pressed.

**Overview of the Button Object**

The button object, as defined in B.7, is a graphical element displayed on the VT's data screen.
### Attributes and Record Format (Table B.14)

The following table describes the structure of the Button object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Unique ID in the object pool. |
| [0] | **Type** | Integer | 1 | 6 | 3 | Object type = Button. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximum width of the button area in pixels. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Maximum height of the button area in pixels. |
[3] | **Background color** | Integer | 1 | 0 – 255 | 8 | Background color. |
[4] | **Border color** | Integer | 1 | 0 – 255 | 9 | Border color (if not suppressed). |
[5] | **Key Code** | Integer | 1 | 0 – 255 | 10 | Code sent in the `Button Activation` message. |
[6] | **Options** | Bitmask | 1 | 0 – 63 | 11 | Bit 0: Latchable (0=Buttoning, 1=Hanging) qzmsdocs000002 Bit 1: State (only for Latchable: 0=Released, 1=Pressed) qzmsdocs000003 Bit 2: Suppress Border (1=No border drawn) qzmsdocs000004 Bit 3: Transparent (1=Background transparent) qzmsdocs000005 Bit 4: Disabled (1=Disabled/Grayed out) qzmsdocs000006 Bit 5: No Border (1=Border area omitted, Button Face = Button Area). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 12 | Number of directly contained objects (symbols, text). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Number of subsequent macro references. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 14 + ... | Object ID of a contained object. |
| - | {X Location} | Signed Integer | 2 | -32768 to +32767 | 16 + ... | X position relative to the upper left corner of the button face. |
| - | {Y Location} | Signed Integer | 2 | -32768 to +32767 | 18 + ... | Y position relative to the upper left corner of the button face. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (After objects) Event ID that triggers the macro. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Macro ID of the macro to be executed. |

### Structure and Appearance
The button consists of three areas:

1. **Button Area:** The entire area defined by Width/Height.

2. **Button Border:** A proprietary 8-pixel border (unless removed by Option Bit 5).

3. **Button Face:** The inner area for content (Button Area minus Border).

### Container Structure
The button is a container. It can contain other objects, which are displayed in the **Button Face**. Objects that extend beyond this area are clipped.

## Events (Events - Table B.13)

The button responds to the following events:

- **On Key Press:** Triggered when the button is pressed. Sends `Button Activation`.
- **On Key Release:** Triggered when the button is released. Sends `Button Activation`.
- **On Enable:** When the button is enabled by a command.
- **On Disable:** When the button is disabled.
- **On Input Field Selection:** When the button is focused (navigation).
- **On Input Field De-selection:** When focus is lost.
- **On Change Background Colour:** Responds to a change in background color.
- **On Change Size:** Responds to a change in size (deletes the old area, redraws).
- **On Change Attribute:** Responds to general attribute changes.

**Role of the Button Object in the Virtual Terminal**

Buttons are crucial for the operator's interaction with the Virtual Terminal and connected agricultural equipment. They enable:

- **Triggering Functions:** Starting or stopping processes, activating implements, switching operating modes.
- **Sending commands:** Controlling actuators, adjusting settings, navigating menus.
- **Confirming entries:** Acknowledging alarms, confirming settings.

The standardized definition of the Button object in Annex B.7 ensures that buttons function and are displayed consistently across different virtual terminals and from different manufacturers. This contributes to the interoperability and user-friendliness of the ISO 11783 system.

**Implementation implications:**

For developers of virtual terminals, attachments, or software components that work with the ISO 11783 standard, a thorough understanding of the specifications in Annex B.7 is essential. They must ensure that their implementation of the Button object complies with the normative requirements to guarantee correct functionality and compatibility within the ISO 11783 network.

**Note**

For complete and detailed specifications of all attributes and properties of the Button object, including the exact data types, value ranges, and linking mechanisms, please refer to the official document "ISO 11783-6:2018". Annex B.7 provides the normative basis for implementing buttons in the Virtual Terminal.

Button Evaluation:

When the button is pressed, the following messages are sent to the ISOBUS:

- BUTTON_STATE_PRESSED
- at the moment the button was pressed
- BUTTON_STATE_HELD
- if the button was held down for a longer period
- TODO: Reference to ISO
- BUTTON_STATE_RELEASED
- when the button was released
- BUTTON_STATE_ABORTED
- if the button was pressed but then released
- TODO: Describe better.

This results in the following:

Normal button presses may only be evaluated as "released" or "held,"

because evaluating "pressed" would eliminate the possibility of aborting.

TODO: Reference to international standards, safety, etc.

There are two evaluation methods:

1. Macro (ISO Designer)

2. Via a callback in C code (Eclipse)

Call Hierarchy:

![](https://user-images.githubusercontent.com/69573151/94337621-210baf00-ffec-11ea-9ec0-fe4a7e7c418b.png)

```c
iso_u32 Tageszaehler = 0;
iso_u32 Gesamtzaehler = 0;
iso_u32 Hugo = 0;

void VTC_handleSoftkeysAndButtons_RELEASED(const struct ButtonActivation_S *pButtonData) {

// what button was released
switch (pButtonData->objectIdOfButtonObject) {

case SoftKey_PlusPlus:
case Button_PlusPlus:
Tageszaehler++;
Gesamtzaehler++;
break;

case SoftKey_Reset_Gesamtzaehler:
case Button_Reset_Gesamtzaehler:
Gesamtzaehler = 0;
break;

case SoftKey_Reset_Tageszaehler:
case Button_Reset_Tageszaehler:
Tageszaehler = 0;
break;

default:
break;
}
IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Tageszaehler, Tageszaehler);
IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Gesamtzaehler, Gesamtzaehler);
setU32("CF-A", "Tageszaehler", Tageszaehler);
setU32("CF-A", "Gesamtzaehler", Gesamtzaehler);
}
```

![](https://user-images.githubusercontent.com/69573151/94602909-cbf2c600-0295-11eb-946a-a68b45b3eccc.png)

Further information and examples can be found in the [ISOBUS Wiki - Button](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/button)] by Tobias Tenberg.
