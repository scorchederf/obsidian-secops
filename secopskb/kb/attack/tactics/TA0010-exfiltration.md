---
mitre_id: "TA0010"
mitre_name: "Exfiltration"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--9a4e74ab-5008-408c-84bf-a10dfbc53462"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-04-25T14:45:34.933Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0010/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "exfiltration"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

## Workspace

- [[notes/attack/tactics/TA0010-exfiltration-note|Open workspace note]]

![[notes/attack/tactics/TA0010-exfiltration-note]]

## Related Techniques

- [[T1011-exfiltration_over_other_network_medium|T1011: Exfiltration Over Other Network Medium]]
    - [[T1011-exfiltration_over_other_network_medium#^t1011001-exfiltration-over-bluetooth|T1011.001: Exfiltration Over Bluetooth]]
- [[T1020-automated_exfiltration|T1020: Automated Exfiltration]]
    - [[T1020-automated_exfiltration#^t1020001-traffic-duplication|T1020.001: Traffic Duplication]]
- [[T1029-scheduled_transfer|T1029: Scheduled Transfer]]
- [[T1030-data_transfer_size_limits|T1030: Data Transfer Size Limits]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol|T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
    - [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1537-transfer_data_to_cloud_account|T1537: Transfer Data to Cloud Account]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
    - [[T1567-exfiltration_over_web_service#^t1567001-exfiltration-to-code-repository|T1567.001: Exfiltration to Code Repository]]
    - [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]]
    - [[T1567-exfiltration_over_web_service#^t1567003-exfiltration-to-text-storage-sites|T1567.003: Exfiltration to Text Storage Sites]]
    - [[T1567-exfiltration_over_web_service#^t1567004-exfiltration-over-webhook|T1567.004: Exfiltration Over Webhook]]

