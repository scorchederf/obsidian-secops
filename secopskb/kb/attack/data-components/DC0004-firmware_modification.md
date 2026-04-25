---
mitre_id: "DC0004"
mitre_name: "Firmware Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--b9d031bb-d150-4fc6-8025-688201bf3ffd"
mitre_created: "2021-10-20T15:05:19.271Z"
mitre_modified: "2025-10-21T15:14:38.020Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass alterations to the Master Boot Record (MBR), Volume Boot Record (VBR), or other firmware components critical to system boot and functionality. Such modifications are often indicators of adversary activity, including malware persistence and system compromise. Examples: 

- Changes to Master Boot Record (MBR): Modifying the MBR to load malicious code during the boot process.
- Changes to Volume Boot Record (VBR): Altering the VBR to redirect boot processes to malicious locations.
- Firmware Configuration Changes: Modifying BIOS/UEFI settings such as disabling Secure Boot.
- Firmware Image Tampering: Updating firmware with a malicious or unauthorized image.
- Logs or Errors Indicating Firmware Changes: Logs showing unauthorized firmware updates or checksum mismatches.

This data component can be collected through the following measures:

- BIOS/UEFI Logs: Enable and monitor BIOS/UEFI logs to capture settings changes or firmware updates.
- Firmware Integrity Monitoring: Use tools or firmware security features to detect changes to firmware components.
- Endpoint Detection and Response (EDR) Solutions: Many EDR platforms can detect abnormal firmware activity, such as changes to MBR/VBR or unauthorized firmware updates.
- File System Monitoring: Monitor changes to MBR/VBR-related files using tools like Sysmon or auditd.
    - Windows Example (Sysmon): Monitor Event ID 7 (Raw disk access).
    - Linux Example (auditd): `auditctl -w /dev/sda -p wa -k firmware_modification`
- Network Traffic Analysis: Capture firmware updates downloaded over the network, particularly from untrusted sources. Use network monitoring tools like Zeek or Wireshark to analyze firmware-related traffic.
- Secure Boot Logs: Collect and analyze Secure Boot logs for signs of tampering or unauthorized configurations. Example: Use PowerShell to retrieve Secure Boot settings on Windows: `Confirm-SecureBootUEFI`
- Vendor-Specific Firmware Tools: Many hardware vendors provide tools for firmware integrity checks.Examples:
    - Intel Platform Firmware Resilience (PFR).
    - Lenovo UEFI diagnostics.

## Workspace

- [[notes/attack/data-components/DC0004-firmware_modification-note|Open workspace note]]

![[notes/attack/data-components/DC0004-firmware_modification-note]]

