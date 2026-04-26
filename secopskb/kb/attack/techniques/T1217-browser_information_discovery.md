---
mitre_id: "T1217"
mitre_name: "Browser Information Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--5e4a2073-9643-44cb-a0b5-e7f4048446c7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:50.561Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1217/"
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
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]] associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)

## Workspace

- [[workspaces/attack/techniques/T1217-browser_information_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1217-browser_information_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/1ca1f9c7_44bc_46bb_8c85_c50e2e94267b-list_mozilla_firefox_bookmark_database_files_on_macos|List Mozilla Firefox Bookmark Database Files on macOS (sh; macos)]]
- [[kb/atomic/tests/3a41f169_a5ab_407f_9269_abafdb5da6c2-list_mozilla_firefox_bookmark_database_files_on_freebsd_linux|List Mozilla Firefox Bookmark Database Files on FreeBSD/Linux (sh; linux)]]
- [[kb/atomic/tests/4312cdbc_79fc_4a9c_becc_53d49c734bc5-list_mozilla_firefox_bookmarks_on_windows_with_command_prompt|List Mozilla Firefox bookmarks on Windows with command prompt (command_prompt; windows)]]
- [[kb/atomic/tests/5fc528dd_79de_47f5_8188_25572b7fafe0-list_safari_bookmarks_on_macos|List Safari Bookmarks on MacOS (sh; macos)]]
- [[kb/atomic/tests/727dbcdb_e495_4ab1_a6c4_80c7f77aef85-list_internet_explorer_bookmarks_using_the_command_prompt|List Internet Explorer Bookmarks using the command prompt (command_prompt; windows)]]
- [[kb/atomic/tests/74094120_e1f5_47c9_b162_a418a0f624d5-extract_edge_browsing_history|Extract Edge Browsing History (powershell; windows)]]
- [[kb/atomic/tests/76f71e2f_480e_4bed_b61e_398fe17499d5-list_google_chrome_edge_chromium_bookmarks_on_windows_with_command_prompt|List Google Chrome / Edge Chromium Bookmarks on Windows with command prompt (command_prompt; windows)]]
- [[kb/atomic/tests/88ca025b_3040_44eb_9168_bd8af22b82fa-list_google_chromium_bookmark_json_files_on_freebsd|List Google Chromium Bookmark JSON Files on FreeBSD (sh; linux)]]
- [[kb/atomic/tests/b789d341_154b_4a42_a071_9111588be9bc-list_google_chrome_bookmark_json_files_on_macos|List Google Chrome Bookmark JSON Files on macOS (sh; macos)]]
- [[kb/atomic/tests/cfe6315c_4945_40f7_b5a4_48f7af2262af-extract_chrome_browsing_history|Extract chrome Browsing History (powershell; windows)]]
- 1 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[empire|Empire (S0363)]]

## Platforms

- Linux
- macOS
- Windows

