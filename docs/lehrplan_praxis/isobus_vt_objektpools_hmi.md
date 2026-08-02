# 🖥️ ISOBUS VT Objektpools & HMI (ISO 11783-6)

> 📌 **Quellennachweis & Rechtsgrundlage:**  
> **Quelle:** *Rahmenlehrplan für die Vorbereitung auf die Meisterprüfung im Land- und Baumaschinenmechatroniker-Handwerk*  
> **Herausgeber:** LandBauTechnik-Bundesverband e. V., Alfredstraße 102, 45131 Essen (Stand: 25.02.2025)  
> **Verordnung:** *Meisterprüfungsverordnung (LandBauMechMstrV)* vom 09.09.2024 (BGBl. 2024 I Nr. 277, in Kraft ab 01.08.2025)

**Rahmenlehrplan-Kategorie:** Teil I LE 1.4 (80 UE) | Teil II LE 1.1 (120 UStd.)  
**Relevanz:** Objektbasierte Benutzeroberflächen für ISOBUS-Anbaugeräte nach ISO 11783-6.

---

## 1. Grundlagen des Virtual Terminals (VT / UT)

- **ISO 11783 Part 6:** Spezifikation der Kommunikation zwischen Anbaugerät (ECU) und Universal Terminal (UT).
- **Objektpool-Konzept:** Das Anbaugerät überträgt beim Systemstart einen binären Objektpool an das Terminal. Das Terminal rendert die grafischen Elemente eigenständig.
- **ISO-Designer:** Visuelles Entwicklungswerkzeug zur Erstellung und Verwaltung von VT-Objektpools (XML / IOP-Dateien).

---

## 2. Kernobjekte im Objektpool

- **Working Set Object:** Repräsentiert das Anbaugerät im Terminalmenü.
- **Data Mask Object:** Die eigentliche Anzeigemaske / Hauptbildschirm auf dem Terminal.
- **SoftKey Mask Object:** Seitenleiste mit Funktionstasten (Softkeys), die sich dynamisch anpassen lassen.
- **Alarm Mask Object:** Priorisierte Warn- und Notfallmeldungen bei Sicherheitsereignissen.
