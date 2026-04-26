---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-HCI"
d3fend_name: "Hardware Component Inventory"
d3fend_ontology_id: "d3f:HardwareComponentInventory"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AHardwareComponentInventory/"
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
  - "T1111"
  - "T1123"
  - "T1125"
  - "T1195"
  - "T1195.003"
  - "T1200"
  - "T1619"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Hardware component inventorying identifies and records the hardware items in the organization's architecture.

## Workspace

- [[workspaces/defend/techniques/D3-HCI-hardware_component_inventory-note|Open workspace note]]

![[workspaces/defend/techniques/D3-HCI-hardware_component_inventory-note]]

## Parent Technique

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

## Related ATT&CK Techniques

- [[T1025-data_from_removable_media|T1025: Data from Removable Media]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1092-communication_through_removable_media|T1092: Communication Through Removable Media]]
- [[T1111-multi-factor_authentication_interception|T1111: Multi-Factor Authentication Interception]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise#^t1195003-compromise-hardware-supply-chain|T1195.003: Compromise Hardware Supply Chain]]
- [[T1200-hardware_additions|T1200: Hardware Additions]]
- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

## Knowledge Base Article

## How it works
Administrators collect information on hardware devices such as peripherals, NICs, processors, and memory devices that are components of the computers in their architecture using a variety of administrative and management tools that query for this information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through remote adminstration tools and system commands, either manually or using scripts.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal hardware inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Bus discovery
   * Admin-scripted PCI Bus inventory using ssh and pciutils
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)

## Ontology Relationships

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

