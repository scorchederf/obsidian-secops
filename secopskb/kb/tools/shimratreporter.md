---
mitre_id: "S0445"
mitre_name: "ShimRatReporter"
mitre_type: "tool"
mitre_stix_id: "tool--115f88dd-0618-4389-83cb-98d33ae81848"
mitre_created: "2020-05-12T21:29:48.294Z"
mitre_modified: "2025-04-25T14:45:13.595Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0445/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "ShimRatReporter"
aliases:
  - "S0445"
  - "ShimRatReporter"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

[ShimRatReporter](https://attack.mitre.org/software/S0445) is a tool used by suspected Chinese adversary [Mofang](https://attack.mitre.org/groups/G0103) to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such as [ShimRat](https://attack.mitre.org/software/S0444)) as well as set up faux infrastructure which mimics the adversary's targets. [ShimRatReporter](https://attack.mitre.org/software/S0445) has been used in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development.(Citation: FOX-IT May 2016 Mofang)

## Workspace

- [[workspaces/tools/S0445-shimratreporter-note|Open workspace note]]

![[workspaces/tools/S0445-shimratreporter-note]]

## Uses Techniques

- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1020-automated_exfiltration|T1020: Automated Exfiltration]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1106-native_api|T1106: Native API]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1518-software_discovery|T1518: Software Discovery]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]

