---
mitre_id: "T1123"
mitre_name: "Audio Capture"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1035cdf2-3e5f-446f-a7a7-e8f6d7925967"
mitre_created: "2017-05-31T21:31:34.528Z"
mitre_modified: "2025-10-24T17:48:24.702Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1123/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
---

# T1123: Audio Capture

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Tools

- [[pupy|Pupy]]
- [[powersploit|PowerSploit]]
- [[remcos|Remcos]]
- [[imminent_monitor|Imminent Monitor]]

## Platforms

- Linux
- macOS
- Windows

