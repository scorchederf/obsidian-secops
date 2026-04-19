---
id: S0445
name: ShimRatReporter
created: 2020-05-12 21:29:48.294000+00:00
modified: 2025-04-25 14:45:13.595000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# ShimRatReporter

[ShimRatReporter](https://attack.mitre.org/software/S0445) is a tool used by suspected Chinese adversary [Mofang](https://attack.mitre.org/groups/G0103) to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such as [ShimRat](https://attack.mitre.org/software/S0444)) as well as set up faux infrastructure which mimics the adversary's targets. [ShimRatReporter](https://attack.mitre.org/software/S0445) has been used in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development.(Citation: FOX-IT May 2016 Mofang)

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

