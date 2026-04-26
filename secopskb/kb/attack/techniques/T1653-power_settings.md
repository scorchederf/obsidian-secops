---
mitre_id: "T1653"
mitre_name: "Power Settings"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ea071aa0-8f17-416f-ab0d-2bab7e79003d"
mitre_created: "2023-06-05T15:52:52.467Z"
mitre_modified: "2025-10-24T17:49:33.435Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1653/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Network Devices"
mitre_tactic_ids:
  - "TA0003"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity.(Citation: Sleep, shut down, hibernate)

Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering a state, such as standby, that can terminate malicious activity.(Citation: Microsoft: Powercfg command-line options)(Citation: systemdsleep Linux)

For example, `powercfg` controls all configurable power system settings on a Windows system and can be abused to prevent an infected host from locking or shutting down.(Citation: Two New Monero Malware Attacks Target Windows and Android Users) Adversaries may also extend system lock screen timeout settings.(Citation: BATLOADER: The Evasive Downloader Malware) Other relevant settings, such as disk and hibernate timeout, can be similarly abused to keep the infected machine running even if no user is active.(Citation: CoinLoader: A Sophisticated Malware Loader Campaign)

Aware that some malware cannot survive system reboots, adversaries may entirely delete files used to invoke system shut down or reboot.(Citation: Condi-Botnet-binaries)

## Workspace

- [[workspaces/attack/techniques/T1653-power_settings-note|Open workspace note]]

![[workspaces/attack/techniques/T1653-power_settings-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## Mitigations

- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows
- Linux
- macOS
- Network Devices

