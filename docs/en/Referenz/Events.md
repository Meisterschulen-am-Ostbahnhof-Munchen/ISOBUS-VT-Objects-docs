# Event IDs (ISO 11783-6 Table A.3)
This table lists all event IDs that can be used in macros (`Macro object`, ID 28) or as triggers for attributes.
*Note:* Starting with VT version 5, 16-bit macro references are supported.
| Event ID | Event Name | Trigger (Occurs when) |
| :--- | :--- | :--- |
| **0** | Reserved | - |
| **1** | On Activate | Working set becomes active. |
| **2** | On Deactivate | Working set becomes inactive. |
| **3** | On Show | Container/mask becomes visible. |
| **4** | On Hide | Container/mask becomes invisible. |
| **5** | On Enable | Object is enabled (input enabled). |
| **6** | On Disable | Object is disabled (Input disabled). |
**7** | On Change Active Mask | The active data mask has been changed. |
**8** | On Change Soft Key Mask | The soft key mask has been changed. |
**9** | On Change Attribute | An attribute has been changed. |
**10** | On Change Background Colour | Background color has been changed. |
**11** | On Change Font Attributes | Font attributes have been changed. |
**12** | On Change Line Attributes | Line attributes have been changed. |
**13** | On Change Fill Attributes | Fill attributes have been changed. |
**14** | On Change Child Location | The position of a child object has been changed. |
**15** | On Change Size | The size of an object has been changed. |
**16** | On Change Value | The value (number/string) has changed. |
**17** | On Change Priority | The alarm priority has changed. |
**18** | On Change End Point | The endpoint of a line has been changed. |
**19** | On Input Field Selection | Focus retained (navigation). |
**20** | On Input Field Deselection | Focus lost. |
**21** | On ESC | Input canceled (ESC). |
**22** | On entry of a value | Value confirmed (ENTER), no change needed. |
**23** | On entry of a new value | Value confirmed (ENTER) AND changed. |
**24** | On Key Press | Key/button pressed. |
**25** | On Key Release | Key/button released. |
**26** | On Change Child Position | Relative position changed in the container (scrolling). |
**27** | On Pointing Event Press | Touch display pressed. |
**28** | On Pointing Event Release | Touch display released. |
**29-239**| Reserved | - |
| **240-254**| Proprietary Events | Manufacturer-specific events. |
| **255** | Reserved | - |
| **255** | Use Extended Macro Ref. | (Only in byte stream) Indicates 16-bit macro ID. |
