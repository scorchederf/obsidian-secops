---
mitre_id: "T1115"
mitre_name: "Clipboard Data"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--30973a08-aed9-4edf-8604-9084ce1b5c4f"
mitre_created: "2017-05-31T21:31:25.967Z"
mitre_modified: "2025-10-24T17:48:36.079Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1115/"
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

# T1115: Clipboard Data

Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using `clip.exe` or `Get-Clipboard`.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [[T1565-data_manipulation#^t1565002-transmitted-data-manipulation|T1565.002: Transmitted Data Manipulation]]).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as `pbpaste`, to grab clipboard contents.(Citation: Operating with EmPyre)

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Tools

- [[koadic|Koadic]]
- [[remcos|Remcos]]
- [[empire|Empire]]
- [[silenttrinity|SILENTTRINITY]]

## Platforms

- Linux
- macOS
- Windows

