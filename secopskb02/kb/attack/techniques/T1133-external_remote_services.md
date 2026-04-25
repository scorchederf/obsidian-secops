---
mitre_id: "T1133"
mitre_name: "External Remote Services"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--10d51417-ee35-4589-b1ff-b6df1c334e8d"
mitre_created: "2017-05-31T21:31:44.421Z"
mitre_modified: "2025-10-24T17:48:24.982Z"
mitre_version: "2.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1133/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0003"
  - "TA0001"
d3fend_ids:
  - "D3-ST"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]] and [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]] can also be used externally.(Citation: MacOS VNC software for Remote Desktop)

Access to [[T1078-valid_accounts|T1078: Valid Accounts]] to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.(Citation: Volexity Virtual Private Keylogging) Access to remote services may be used as a redundant or persistent access mechanism during an operation.

Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.(Citation: Trend Micro Exposed Docker Server)(Citation: Unit 42 Hildegard Malware)

Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access.(Citation: The BadPilot campaign) Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.(Citation: Russian threat actors dig in, prepare to seize on war fatigue)

## Workspace

- [[workspaces/attack/techniques/T1133-external_remote_services-note|Open workspace note]]

![[workspaces/attack/techniques/T1133-external_remote_services-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-ST-session_termination|D3-ST: Session Termination]]

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Containers
- Linux
- macOS
- Windows

