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
mitre_tactic_ids:
  - "TA0009"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using `clip.exe` or `Get-Clipboard`.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [[T1565-data_manipulation#^t1565002-transmitted-data-manipulation|T1565.002: Transmitted Data Manipulation]]).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as `pbpaste`, to grab clipboard contents.(Citation: Operating with EmPyre)

## Workspace

- [[workspaces/attack/techniques/T1115-clipboard_data-note|Open workspace note]]

![[workspaces/attack/techniques/T1115-clipboard_data-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/7794fa3c_edea_4cff_bec7_267dd4770fd7-clipboard_data_collection_via_osascript|Clipboard Data Collection Via OSAScript (high; macos / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0cd14633_58d4_4422_9ede_daa2c9474ae7-utilize_clipboard_to_store_or_execute_commands_from|Utilize Clipboard to store or execute commands from (command_prompt; windows)]]
- [[kb/atomic/tests/1ac2247f_65f8_4051_b51f_b0ccdfaaa5ff-execute_commands_from_clipboard|Execute commands from clipboard (bash; macos)]]
- [[kb/atomic/tests/9c8d5a72_9c98_48d3_b9bf_da2cc43bdf52-collect_clipboard_data_via_vba|Collect Clipboard Data via VBA (powershell; windows)]]
- [[kb/atomic/tests/d6dc21af_bec9_4152_be86_326b6babd416-execute_commands_from_clipboard_using_powershell|Execute Commands from Clipboard using PowerShell (powershell; windows)]]
- [[kb/atomic/tests/ee363e53_b083_4230_aff3_f8d955f2d5bb-add_or_copy_content_to_clipboard_with_xclip|Add or copy content to clipboard with xClip (sh; linux)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Tools
- [[empire|Empire (S0363)]]
- [[koadic|Koadic (S0250)]]
- [[remcos|Remcos (S0332)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Linux
- macOS
- Windows

