# 🎛️ Input-Attribute, Key-Events & Interaktionsdiagnose

> 📌 **Quellennachweis & Rechtsgrundlage:**  
> **Quelle:** *Rahmenlehrplan für die Vorbereitung auf die Meisterprüfung im Land- und Baumaschinenmechatroniker-Handwerk*  
> **Herausgeber:** LandBauTechnik-Bundesverband e. V., Alfredstraße 102, 45131 Essen (Stand: 25.02.2025)  
> **Verordnung:** *Meisterprüfungsverordnung (LandBauMechMstrV)* vom 09.09.2024 (BGBl. 2024 I Nr. 277, in Kraft ab 01.08.2025)

**Rahmenlehrplan-Kategorie:** Teil I LE 2.2 (40 UE) | Teil II LE 1.1 & 1.3  
**Relevanz:** Eingabeverarbeitung, Tasten-Events und Diagnose von HMI-Kommunikationsfehlern.

---

## 1. Interaktive Objekte & Eingabefelder

- **Input Number / Input String:** Eingabe von Zielparametern (z. B. Ausbringmenge in l/ha, Arbeitsbreite in m).
- **Button Objects:** Taster und Schalter zur Auslösung von Maschinenaktionen (z. B. Klappung starten, Pumpe ein).
- **Key Events:** Verarbeitung von `VT_KEY_EVENT` (Button Pressed, Button Released, Value Changed).

---

## 2. Fehlerdiagnose an VT-Oberflächen

- **Objektpool-Upload-Fehler:** Diagnose bei Übertragungsabbrüchen (Memory Overflow, Version Incompatibility).
- **CAN-Bus-Nachrichten:** Analyse von VT-to-ECU und ECU-to-VT Botschaften mit CAN-Trace-Tools.
