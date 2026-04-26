---
mitre_id: "T1113"
mitre_name: "Screen Capture"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0259baeb-9f63-4c69-bf10-eb038c390688"
mitre_created: "2017-05-31T21:31:25.060Z"
mitre_modified: "2025-10-24T17:48:19.886Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1113/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as `CopyFromScreen`, `xwd`, or `screencapture`.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)


## Workspace

- [[workspaces/attack/techniques/T1113-screen_capture-note|Open workspace note]]

![[workspaces/attack/techniques/T1113-screen_capture-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[connectwise|ConnectWise (S0591)]]
- [[empire|Empire (S0363)]]
- [[pcshare|PcShare (S1050)]]
- [[powersploit|PowerSploit (S0194)]]
- [[pupy|Pupy (S0192)]]
- [[quick_assist|Quick Assist (S1209)]]
- [[remcos|Remcos (S0332)]]
- [[remoteutilities|RemoteUtilities (S0592)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- Linux
- Windows
- macOS

