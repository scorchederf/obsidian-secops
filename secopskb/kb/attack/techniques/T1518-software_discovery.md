---
mitre_id: "T1518"
mitre_name: "Software Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e3b6daca-e963-4a69-aee6-ed4fd653ad58"
mitre_created: "2019-09-16T17:52:44.147Z"
mitre_modified: "2025-10-24T17:49:31.671Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1518/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-CI"
  - "D3-CQ"
  - "D3-RC"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [[T1518-software_discovery|T1518: Software Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as [[T1072-software_deployment_tools|T1072: Software Deployment Tools]], and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]].

## Workspace

- [[workspaces/attack/techniques/T1518-software_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1518-software_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Subtechniques

### T1518.001: Security Software Discovery

^t1518001-security-software-discovery

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on a system or in a cloud environment. This may include things such as cloud monitoring agents and anti-virus. Adversaries may use the information from [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Example commands that can be used to obtain security software information are [[netsh|netsh (S0108)]], `reg query` with [[reg|Reg (S0075)]], `dir` with [[cmd|cmd (S0106)]], and [[tasklist|Tasklist (S0057)]], but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for. It is becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

Adversaries may also utilize the [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]] to discover cloud-native security software installed on compute infrastructure, such as the AWS CloudWatch agent, Azure VM Agent, and Google Cloud Monitor agent. These agents  may collect  metrics and logs from the VM, which may be centrally aggregated in a cloud-based monitoring platform.

### T1518.002: Backup Software Discovery

^t1518002-backup-software-discovery

Adversaries may attempt to get a listing of backup software or configurations that are installed on a system. Adversaries may use this information to shape follow-on behaviors, such as [[T1485-data_destruction|T1485: Data Destruction]], [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]], or [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]].  

Commands that can be used to obtain security software information are [[netsh|netsh (S0108)]], `reg query` with [[reg|Reg (S0075)]], `dir` with [[cmd|cmd (S0106)]], and [[tasklist|Tasklist (S0057)]], but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for, such as Veeam, Acronis, Dropbox, or Paragon.(Citation: Symantec Play Ransomware 2023)

## Tools

- [[shimratreporter|ShimRatReporter (S0445)]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Windows

