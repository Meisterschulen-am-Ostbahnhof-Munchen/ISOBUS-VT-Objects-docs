# 🖥️ ISOBUS VT Object Pools & HMI (ISO 11783-6)

> 📌 **Source & Legal Basis:**
> **Source:** *Framework Curriculum for the Preparation for the Master Craftsman Examination in Agricultural and Construction Machinery Mechatronics*
> **Publisher:** German Association of Agricultural and Construction Machinery Mechatronics Engineers (LandBauTechnik-Bundesverband e. V.), Alfredstraße 102, 45131 Essen (as of February 25, 2025)

> **Regulation:** *Master Craftsman Examination Regulation (LandBauMechMstrV)* of September 9, 2024 (Federal Law Gazette 2024 I No. 277, effective August 1, 2025)

**Framework Curriculum Category:** Part I LE 1.4 (80 teaching units) | Part II LE 1.1 (120 hours)

**Relevance:** Object-based user interfaces for ISOBUS implements according to ISO 11783-6.

--

## 1. Fundamentals of the Virtual Terminal (VT / UT)

- **ISO 11783 Part 6:** Specification of the communication between the implement (ECU) and the Universal Terminal (UT).

- **Object Pool Concept:** The implement transmits a binary object pool to the terminal at system startup. The terminal renders the graphical elements independently.

- **ISO Designer:** Visual development tool for creating and managing VT object pools (XML / IOP files).

--

## 2. Core Objects in the Object Pool

- **Working Set Object:** Represents the implement in the terminal menu.

- **Data Mask Object:** The actual display mask / main screen on the terminal.

- **SoftKey Mask Object:** Sidebar with function keys (softkeys) that can be dynamically adjusted.

- **Alarm Mask Object:** Prioritized warning and emergency messages for security events.


**SoftKey Mask Object:**