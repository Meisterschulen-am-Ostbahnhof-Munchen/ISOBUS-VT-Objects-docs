# ID 28 – Macro – ISO 11783-6 – B.16

The **Macro** object with **ID 28** allows you to store a sequence of commands in the Virtual Terminal and execute them automatically upon certain events. This reduces the necessary communication via ISOBUS, as simple UI logic runs directly in the terminal.

### Attributes and Record Format (Table B.56)

The following table describes the structure of the Macro object in the object pool.

| AID | Name | Type | Size (Bytes) | Range / Value | Record Byte | Description |

| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| - | **Object ID** | Integer | 2 | 0 – 255 (VT v4)<br>0 – 65534 (VT v5+) | 1 – 2 | Unique ID in the object pool. |

| [0] | **Type** | Integer | 1 | 28 | 3 | Object type = Macro. |

| - | **Number of bytes to follow** | Integer | 2 | 0 – 65535 | 4 – 5 | Number of bytes for the command list. |

| - | **Repeat:** {Command} | Binary | 6 – n | - | 6 ... | List of command packages. Each command must be a multiple of 8 bytes long (padding with FFh). |

## Functionality and Structure
A macro consists of a list of VT commands (see ISO 11783-6, Annex F).


* **Padding:** Each command within a macro must be padded to a length of **8 bytes** (using `0xFF`) if the actual command is shorter (e.g., Change Numeric Value).

* **Execution:** Macros can be started by events (e.g., `On Press` of a button) or by the ECU command `Execute Macro`.

* **Consistency:** The ECU is responsible for ensuring that macros only reference objects that actually exist in the pool.

## Available Macro Commands (Excerpt)

Macros can use almost all commanding VT functions:

* **Visibility:** `Hide/Show Object` (show/hide containers).

* **Interaction:** `Enable/Disable Object` (Locking buttons/input), `Select Input Object` (Setting focus).

* **Values:** `Change Numeric Value` (Changing variables or pointers), `Change String Value`.

* **Geometry:** `Change Child Location/Position` (Moving/scrolling objects), `Change Size`, `Change End Point`.

* **Display:** `Change Background Color`, `Change Font/Line/Fill Attributes`.

* **Navigation:** `Change Active Mask` (Screen change), `Change Soft Key Mask`.

* **Audio:** `Control Audio Device` (Emit beeps).

* **Lists:** `Change List Item` (Change the content of input lists).

## Events

Macros do not trigger events themselves, but are started by events from other objects.

The Macro object supports the following commands:
* `Execute Macro`
* `Execute Extended Macro`
* `Get Attribute Value`

## Implementation Implementation Significance
Macros are a powerful tool for **performance optimization**:

1. **Response Time:** A screen change immediately after a key press occurs via macro without CAN delay. 2. **Relief:** The ECU doesn't have to handle purely graphical tasks (e.g., toggling an icon when a button is pressed).

3. **Complexity:** Multiple actions can be combined into a single macro (e.g., "Set variable to 0" AND "Show success message" AND "Play sound").

----

*Note: For detailed specifications of the individual command codes, refer to the official ISO 11783-6:2018, Annex F.*