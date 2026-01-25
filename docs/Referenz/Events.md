# Event IDs (ISO 11783-6 Table A.3)

```{index} single: Events
```

Diese Tabelle listet alle Ereignis-IDs (Event IDs), die in Makros (`Macro object`, ID 28) oder als Trigger für Attribute verwendet werden können.

*Hinweis:* Ab VT Version 5 werden 16-Bit Makro-Referenzen unterstützt.

| Event ID | Event Name | Auslöser (Occurs when) |
| :--- | :--- | :--- |
| **0** | Reserved | - |
| **1** | On Activate | Working Set wird aktiv. |
| **2** | On Deactivate | Working Set wird inaktiv. |
| **3** | On Show | Container/Maske wird sichtbar. |
| **4** | On Hide | Container/Maske wird unsichtbar. |
| **5** | On Enable | Objekt wird aktiviert (Input enabled). |
| **6** | On Disable | Objekt wird deaktiviert (Input disabled). |
| **7** | On Change Active Mask | Die aktive Datenmaske wurde gewechselt. |
| **8** | On Change Soft Key Mask | Die Softkey-Maske wurde gewechselt. |
| **9** | On Change Attribute | Ein Attribut wurde geändert. |
| **10** | On Change Background Colour | Hintergrundfarbe wurde geändert. |
| **11** | On Change Font Attributes | Schriftattribute wurden geändert. |
| **12** | On Change Line Attributes | Linienattribute wurden geändert. |
| **13** | On Change Fill Attributes | Füllattribute wurden geändert. |
| **14** | On Change Child Location | Die Position eines Kind-Objekts wurde geändert. |
| **15** | On Change Size | Die Größe eines Objekts wurde geändert. |
| **16** | On Change Value | Der Wert (Zahl/String) hat sich geändert. |
| **17** | On Change Priority | Die Alarm-Priorität hat sich geändert. |
| **18** | On Change End Point | Endpunkt einer Linie wurde geändert. |
| **19** | On Input Field Selection | Fokus erhalten (Navigation). |
| **20** | On Input Field Deselection | Fokus verloren. |
| **21** | On ESC | Eingabe abgebrochen (ESC). |
| **22** | On entry of a value | Wert bestätigt (ENTER), keine Änderung nötig. |
| **23** | On entry of a new value | Wert bestätigt (ENTER) UND geändert. |
| **24** | On Key Press | Taste/Button gedrückt. |
| **25** | On Key Release | Taste/Button losgelassen. |
| **26** | On Change Child Position | Relative Position im Container geändert (Scrolling). |
| **27** | On Pointing Event Press | Touch-Display gedrückt. |
| **28** | On Pointing Event Release | Touch-Display losgelassen. |
| **29-239**| Reserved | - |
| **240-254**| Proprietary Events | Herstellerspezifische Events. |
| **255** | Reserved | - |
| **255** | Use Extended Macro Ref. | (Nur in Byte-Stream) Kennzeichnet 16-Bit Makro ID. |
