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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as `CopyFromScreen`, `xwd`, or `screencapture`.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)


## Workspace

- [[workspaces/attack/techniques/T1113-screen_capture-note|Open workspace note]]

![[workspaces/attack/techniques/T1113-screen_capture-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/0f47ceb1_720f_4275_96b8_21f0562217ac-screencapture|Screencapture (bash; macos)]]
- [[kb/atomic/tests/18397d87_38aa_4443_a098_8a48a8ca5d8d-capture_linux_desktop_using_import_tool_freebsd|Capture Linux Desktop using Import Tool (freebsd) (sh; linux)]]
- [[kb/atomic/tests/3c898f62_626c_47d5_aad2_6de873d69153-windows_screencapture|Windows Screencapture (powershell; windows)]]
- [[kb/atomic/tests/562f3bc2_74e8_46c5_95c7_0e01f9ccc65c-x_windows_capture_freebsd|X Windows Capture (freebsd) (sh; linux)]]
- [[kb/atomic/tests/5a496325_0115_4274_8eb9_755b649ad0fb-windows_recall_feature_enabled_disableaidataanalysis_value_deleted|Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted (powershell; windows)]]
- [[kb/atomic/tests/8206dd0c_faf6_4d74_ba13_7fbe13dce6ac-x_windows_capture|X Windows Capture (bash; linux)]]
- [[kb/atomic/tests/98f19852_7348_4f99_9e15_6ff4320464c7-rdp_bitmap_cache_extraction_via_bmc_tools|RDP Bitmap Cache Extraction via bmc-tools (powershell; windows)]]
- [[kb/atomic/tests/9cd1cccb_91e4_4550_9139_e20a586fcea1-capture_linux_desktop_using_import_tool|Capture Linux Desktop using Import Tool (bash; linux)]]
- [[kb/atomic/tests/deb7d358_5fbd_4dc4_aecc_ee0054d2d9a4-screencapture_silent|Screencapture (silent) (bash; macos)]]
- [[kb/atomic/tests/e9313014_985a_48ef_80d9_cde604ffc187-windows_screen_capture_copyfromscreen|Windows Screen Capture (CopyFromScreen) (powershell; windows)]]

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-psr_exe|Psr.exe (Reconnaissance)]]

<!-- generated-detection-validation-end -->

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

