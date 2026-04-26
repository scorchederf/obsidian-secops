---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ANAA"
d3fend_name: "Administrative Network Activity Analysis"
d3fend_ontology_id: "d3f:AdministrativeNetworkActivityAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AAdministrativeNetworkActivityAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.006"
  - "T1047"
  - "T1098"
  - "T1098.001"
  - "T1110"
  - "T1110.003"
  - "T1110.004"
  - "T1207"
  - "T1546"
  - "T1546.003"
  - "T1546.008"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Detection of unauthorized use of administrative network protocols by analyzing network activity against a baseline.

## Workspace

- [[workspaces/defend/techniques/D3-ANAA-administrative_network_activity_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ANAA-administrative_network_activity_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1110-brute_force#^t1110004-credential-stuffing|T1110.004: Credential Stuffing]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

## Knowledge Base Article

## How it works
Network protocols such as RDP, IPMI, SSH, SNMP, VNC, MOSH, NX, TeamViewer, SPICE, PCoIP, and others are used by system administrators to remotely manage servers. Defenders monitor administrative network activity to determine if the use of remote protocols is malicious. Attackers can abuse administrative protocols and leverage them for initial access to various endpoints. For example, an attacker with valid credentials will remotely SSH or RDP into a server and attempt to blend in with existing traffic from system administrators. By monitoring the traffic activity, it is possible to detect when the protocols are behaving differently from a known baseline of system administration activity.

## Considerations
* Administrative traffic can be encrypted, making network protocol analysis a challenge
* False alarms can be mitigated by integration with inventory management systems

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

