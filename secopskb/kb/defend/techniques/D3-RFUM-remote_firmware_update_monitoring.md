---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RFUM"
d3fend_name: "Remote Firmware Update Monitoring"
d3fend_ontology_id: "d3f:RemoteFirmwareUpdateMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARemoteFirmwareUpdateMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Monitoring of remote firmware update commands to identify unauthorized software installations.

## Workspace

- [[workspaces/defend/techniques/D3-RFUM-remote_firmware_update_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RFUM-remote_firmware_update_monitoring-note]]

## Parent Technique

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]

## Knowledge Base Article

## How it works
By deploying sensors within the OT environment to passively monitor network traffic, tools can leverage deep packet inspection to identify protocol-specific commands and generate logs of relevant firmware activity. Additionally, these tools may incorporate behavioral and signature-based analysis to enhance detection and alerting capabilities.

## See Also

- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf

## Ontology Relationships

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]

