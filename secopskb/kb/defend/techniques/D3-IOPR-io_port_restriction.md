---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IOPR"
d3fend_name: "IO Port Restriction"
d3fend_ontology_id: "d3f:IOPortRestriction"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AIOPortRestriction/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1025"
  - "T1052"
  - "T1052.001"
  - "T1056"
  - "T1056.001"
  - "T1091"
  - "T1092"
  - "T1123"
  - "T1125"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Limiting access to computer input/output (IO) ports to restrict unauthorized devices.

## Workspace

- [[workspaces/defend/techniques/D3-IOPR-io_port_restriction-note|Open workspace note]]

![[workspaces/defend/techniques/D3-IOPR-io_port_restriction-note]]

## Parent Technique

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

## Related ATT&CK Techniques

- [[T1025-data_from_removable_media|T1025: Data from Removable Media]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1092-communication_through_removable_media|T1092: Communication Through Removable Media]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]

## Knowledge Base Article

## How It works

Software-based restriction uses agent software installed on a computer system. The agent software monitors all IO port system traffic. The agent software is configurable to limit the use of certain devices connected to IO ports. The restriction software can also be configured to limit the access to files and applications on external storage devices connected to IO ports.

Hardware-based restriction can also be employed to limit access to IO ports. For example, a hardware USB filter device that is placed between the host system and the external devices can filter IO port connections based on configurable rules. When new devices are connected to the USB filter the type of device is determined. Using an allow list a connection determination is made for the device.

Some implementations detect when a device is connected in order to authorize the connection against a list of approved devices, in some cases by device type. For example, if the device is determined to be a storage device, then the contained files and executables are examined to more accurately identify the device type.

Types of restrictions that may be applied:
- Device connection
- Device command filtering
- Device file system read or write restrictions

## Considerations
 * Agent software will need to be installed on host systems
 * Configurations for allow/deny for devices and files will need to be maintained

## Ontology Relationships

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

