# Empty Objects (Minimum Child Objects)
The ISO 11783-6 standard makes an important distinction for container objects (objects that contain other objects): **Can the object be empty or not?**
This rule is defined by the permissible range of values for the attribute **"Number of objects to follow"**.
## Objects that MUST NOT be empty (Minimum 1 Child)
These objects must contain at least one child object, as they cannot fulfill their function in the system without content (usually because they must be visible to the user as a **designator** / icon).
| Object ID | Name | Reason | Standard Reference |

| :--- | :--- | :--- | :--- |

**0** | **Working Set** | Must be displayed for selection in the VT menu. Without a graphical designator, the device would be invisible to the operator and could not be selected. | Table B.2 |

| **29** | **Auxiliary Function Type 1** | Must be displayed on the mapping screen so the user can assign the function (e.g., "Lift") to a switch. | Table J.1 |

**30** | **Auxiliary Input Type 1** | Must be displayed on the mapping screen to represent the physical input (e.g., "Joystick Button A"). | Table J.3 |

**31** | **Auxiliary Function Type 2** | See ID 29. | Table J.2 |

**32** | **Auxiliary Input Type 2** | See ID 30. | Table J.4 |

**Error Case:** If such an object is defined with `0` child objects in the object pool, the pool is **invalid** and will be rejected by the VT (or a validation tool).

** ---

## Objects that may be empty (Minimum 0 children)

For most other containers, content such as `0` is permitted. This can be quite useful.

| Object ID | Name | Behavior with 0 children |

| :--- | :--- | :--- |

| **1** | **Data Mask** | Displays only the background color. |

| **2** | **Alarm Mask** | Displays only the background color (warning without content). |

| **3** | **Container** | Is effectively invisible and takes up no space (unless an area with a background color is defined by Width/Height). |

| **4** | **Soft Key Mask** | Hides all soft keys or leaves them unlabeled. |

| **5** | **Key** | Displays an empty key in the defined background color. |

| **6** | **Button** | Displays an empty button in the defined background color. |

**35** | **Key Group** | Technically allowed, but functionally pointless (an empty group). |

**44** | **Animation** | An animation without frames displays nothing. |

### Special Feature: Input List (ID 10)
Even a `Input List` can theoretically be empty (`Number of list items` = 0). In this case, the list exists but contains no selectable options.

**35** | **Key Group** | Technically, an animation without frames displays nothing.