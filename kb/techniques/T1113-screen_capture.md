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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0009"
---

# T1113: Screen Capture

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as `CopyFromScreen`, `xwd`, or `screencapture`.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)


## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Tools

- [[pupy|Pupy]]
- [[powersploit|PowerSploit]]
- [[remcos|Remcos]]
- [[empire|Empire]]
- [[connectwise|ConnectWise]]
- [[remoteutilities|RemoteUtilities]]
- [[sliver|Sliver]]
- [[silenttrinity|SILENTTRINITY]]
- [[pcshare|PcShare]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[asyncrat|AsyncRAT]]
- [[quick_assist|Quick Assist]]

## Platforms

- Linux
- Windows
- macOS

