# Invalid Object Pools

For an ISOBUS object pool (IOP) to be accepted and loaded by the Virtual Terminal (VT), it must adhere to strict structural rules. If the pool violates any of these rules, the VT sends an error code at the end of the transmission (`End of Object Pool`) and usually discards the entire pool.

Here are the most important rules that every programmer needs to know:

## 1. Structural Integrity (Parsing Errors)

These are the most common errors that cause the VT parser to malfunction.

* **Incorrect Length Specifications:** If an object specifies "Five child objects follow," but the byte stream only contains four (or six), the VT incorrectly reads the next object byte as an attribute of the previous one. The pool is then corrupted.


``` * **Unknown Object Types:** An object type ID that is not defined in the standard (and the supported VT version).

* **Missing ID 0 Object:** Each workset **must** contain exactly one object with the **ID 0** (Working Set). If this is missing, the VT does not know who owns the pool.

## 2. Referencing Errors (Dangling Pointers)

The VT checks whether all links are valid when loading (or at the latest when activating).

* **Dead References:** An object (e.g., a container) references an object ID (e.g., 100) in its child list, but there is no object with ID 100 in the entire pool.

* *Exception:* References to `NULL` (65535 or FFFFh) are allowed and expected (e.g., empty softkeys).

* **Incorrect Object Types:** An attribute requires a specific type, but the referenced ID belongs to a different type.

* *Example:* A `Input Number` object references a `String Variable` object at `Variable Reference`. -> **Invalid!**

* *Example:* A `Output Rectangle` references a `Fill Attributes` object at `Line Attributes`. -> **Invalid!**

## 3. Logical Errors & Recursion

* **Circular References:** Container A contains Container B, and Container B contains Container A. This leads to an infinite loop during drawing. The VT detects this and rejects the pool or (in the worst case) crashes.


* **Circular References:** Container A contains Container B, and Container B contains Container A. * **Multiple Definitions:** An object ID (e.g., ID 50) may only be defined once in the pool. Duplicate IDs are prohibited.

## 4. Specific Object Rules (Hard Constraints)

Some objects have very specific rules that are often overlooked:

* **Designator Requirement:** Objects such as `Working Set`, `Auxiliary Function`, and `Auxiliary Input` **must** have at least one child object (see page [Empty Objects ](Leere_Objekte.md)]).

* **Input Lists:** The `Value` of an Input List may not be greater than `Anzahl der Listeneinträge - 1`.

* **Soft Key Masks:** May only contain `Key` objects (ID 5) or `Object Pointer` (ID 27), which in turn point to keys. A Button (ID 6) within a Soft Key Mask is invalid.

* **Variable Size:** When a String object references a String variable, the defined length in the String object should ideally match the length of the variable (although VTs are often tolerant here and will clip/pad).

## 5. Resource Limits

Even if the pool is syntactically correct, it may be rejected if it exceeds the hardware limits of the VT:

* **Memory Full:** The pool is larger than the available flash memory of the VT (Memory Out of Range).

* **Too many objects:** Some older VTs have limits on the absolute number of objects (e.g., max. 65534, which is determined by the 16-bit ID field, but actual limits are often lower).

* **Softkey limit:** A softkey mask that defines more keys than the VT can manage (although paging is required, there are often hard limits).

## Troubleshooting tips

If the VT reports "Object Pool Error" during loading:

1. Check if **ID 0** exists.

2. Check if all referenced IDs are actually in the pool.

3. Check if all `Number of objects/macros/bytes` fields exactly match the following data.

4. Check if type references (Number Var vs. String Var) are correct.

