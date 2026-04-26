---
sigma_id: "c2b86e67-b880-4eec-b045-50bc98ef4844"
title: "HackTool - LaZagne Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_lazagne.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_lazagne.yml"
build_date: "2026-04-26 14:14:26"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c2b86e67-b880-4eec-b045-50bc98ef4844"
  - "HackTool - LaZagne Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - LaZagne Execution

Detects the execution of the LaZagne. A utility used to retrieve multiple types of passwords stored on a local computer.
LaZagne has been leveraged multiple times by threat actors in order to dump credentials.

## Metadata

- Rule ID: c2b86e67-b880-4eec-b045-50bc98ef4844
- Status: experimental
- Level: medium
- Author: Nasreddine Bencherchali, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2024-06-24
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_lazagne.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img_metadata:
  Image|endswith: \lazagne.exe
selection_img_cli:
  Image|contains:
  - :\PerfLogs\
  - :\ProgramData\
  - :\Temp\
  - :\Tmp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \$Recycle.bin
  - \AppData\
  - \Desktop\
  - \Downloads\
  - \Favorites\
  - \Links\
  - \Music\
  - \Photos\
  - \Pictures\
  - \Saved Games\
  - \Searches\
  - \Users\Contacts\
  - \Users\Default\
  - \Users\Searches\
  - \Videos\
  - \Windows\addins\
  - \Windows\Fonts\
  - \Windows\IME\
  CommandLine|endswith:
  - .exe all
  - .exe browsers
  - .exe chats
  - .exe databases
  - .exe games
  - .exe git
  - .exe mails
  - .exe maven
  - .exe memory
  - .exe multimedia
  - .exe sysadmin
  - .exe unused
  - .exe wifi
  - .exe windows
selection_cli_modules:
  CommandLine|contains:
  - ' all '
  - ' browsers '
  - ' chats '
  - ' databases '
  - ' games '
  - ' mails '
  - ' maven '
  - ' memory '
  - ' multimedia '
  - ' php '
  - ' svn '
  - ' sysadmin '
  - ' unused '
  - ' wifi '
selection_cli_options:
  CommandLine|contains:
  - -1Password
  - -apachedirectorystudio
  - -autologon
  - -ChromiumBased
  - -coreftp
  - -credfiles
  - -credman
  - -cyberduck
  - -dbvis
  - -EyeCon
  - -filezilla
  - -filezillaserver
  - -ftpnavigator
  - -galconfusion
  - -gitforwindows
  - -hashdump
  - -iisapppool
  - -IISCentralCertP
  - -kalypsomedia
  - -keepass
  - -keepassconfig
  - -lsa_secrets
  - -mavenrepositories
  - -memory_dump
  - -Mozilla
  - -mRemoteNG
  - -mscache
  - -opensshforwindows
  - -openvpn
  - -outlook
  - -pidgin
  - -postgresql
  - -psi-im
  - -puttycm
  - -pypykatz
  - -Rclone
  - -rdpmanager
  - -robomongo
  - -roguestale
  - -skype
  - -SQLDeveloper
  - -squirrel
  - -tortoise
  - -turba
  - -UCBrowser
  - -unattended
  - -vault
  - -vaultfiles
  - -vnc
  - -winscp
condition: 1 of selection_img_* or all of selection_cli_*
```

## False Positives

- Some false positive is expected from tools with similar command line flags.

## References

- https://github.com/AlessandroZ/LaZagne/tree/master
- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/
- https://cloud.google.com/blog/topics/threat-intelligence/alphv-ransomware-backup/
- https://securelist.com/defttorero-tactics-techniques-and-procedures/107610/
- https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections/raw/800c0e06571993a54e39571cf27fd474dcc5c0bc/2017/2017.11.14.Muddying_the_Water/muddying-the-water-targeted-attacks.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_lazagne.yml)
