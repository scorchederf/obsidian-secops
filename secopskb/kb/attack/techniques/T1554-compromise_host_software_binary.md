---
mitre_id: "T1554"
mitre_name: "Compromise Host Software Binary"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--960c3c86-1480-4d72-b4e0-8c242e84a5c5"
mitre_created: "2020-02-11T18:18:34.279Z"
mitre_modified: "2025-10-24T17:49:07.572Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1554/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "ESXi"
mitre_tactic_ids:
  - "TA0003"
d3fend_ids:
  - "D3-AVE"
  - "D3-RS"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]).(Citation: Google Cloud Mandiant UNC3886 2024)

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)(Citation: Unit42 Banking Trojans Hooking 2022) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.(Citation: ESET FontOnLake Analysis 2021)

After modifying a binary, an adversary may attempt to [[T1562-impair_defenses|T1562: Impair Defenses]] by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).(Citation: Google Cloud Mandiant UNC3886 2024)

## Workspace

- [[workspaces/attack/techniques/T1554-compromise_host_software_binary-note|Open workspace note]]

![[workspaces/attack/techniques/T1554-compromise_host_software_binary-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0ee4d8a5_4e67_4faf_acfa_62a78457d1f2-hybridconnectionmanager_service_installation|HybridConnectionManager Service Installation (high; windows / security)]]
- [[kb/sigma/rules/7bd3902d_8b8b_4dd4_838a_c6862d40150d-dns_hybridconnectionmanager_service_bus|DNS HybridConnectionManager Service Bus (high; windows / dns_query)]]
- [[kb/sigma/rules/b55d23e5_6821_44ff_8a6e_67218891e49f-hybridconnectionmanager_service_running|HybridConnectionManager Service Running (high; windows / microsoft-servicebus-client)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Mitigations

- [[M1045-code_signing|M1045: Code Signing]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

