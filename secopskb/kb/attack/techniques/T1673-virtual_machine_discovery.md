---
mitre_id: "T1673"
mitre_name: "Virtual Machine Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--6bc7f9aa-b91f-4b23-84b8-5e756eba68eb"
mitre_created: "2025-03-27T15:32:17.400Z"
mitre_modified: "2025-04-15T21:24:32.155Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1673/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [[T1059-command_and_scripting_interpreter#^t1059012-hypervisor-cli|T1059.012: Hypervisor CLI]] such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: TrendMicro Play) Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. 

Adversaries may use the information from [[T1673-virtual_machine_discovery|T1673: Virtual Machine Discovery]] during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as [[T1489-service_stop|T1489: Service Stop]] or [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]].(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

## Workspace

- [[workspaces/attack/techniques/T1673-virtual_machine_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1673-virtual_machine_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

