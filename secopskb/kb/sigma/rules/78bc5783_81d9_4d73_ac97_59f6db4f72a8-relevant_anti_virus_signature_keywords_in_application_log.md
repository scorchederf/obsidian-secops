---
sigma_id: "78bc5783-81d9-4d73-ac97-59f6db4f72a8"
title: "Relevant Anti-Virus Signature Keywords In Application Log"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/Other/win_av_relevant_match.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/Other/win_av_relevant_match.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "78bc5783-81d9-4d73-ac97-59f6db4f72a8"
  - "Relevant Anti-Virus Signature Keywords In Application Log"
attack_technique_ids:
  - "T1588"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Relevant Anti-Virus Signature Keywords In Application Log

Detects potentially highly relevant antivirus events in the application log based on known virus signature names and malware keywords.

## Metadata

- Rule ID: 78bc5783-81d9-4d73-ac97-59f6db4f72a8
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Arnim Rupp
- Date: 2017-02-19
- Modified: 2024-12-25
- Source Path: rules/windows/builtin/application/Other/win_av_relevant_match.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588]]

## Detection

```yaml
keywords:
- Adfind
- 'ASP/BackDoor '
- ATK/
- Backdoor.ASP
- Backdoor.Cobalt
- Backdoor.JSP
- Backdoor.PHP
- Blackworm
- Brutel
- BruteR
- Chopper
- Cobalt
- COBEACON
- Cometer
- CRYPTES
- Cryptor
- Destructor
- DumpCreds
- Exploit.Script.CVE
- FastReverseProxy
- Filecoder
- 'GrandCrab '
- HackTool
- HKTL
- HTool-
- /HTool
- .HTool
- IISExchgSpawnCMD
- Impacket
- 'JSP/BackDoor '
- Keylogger
- Koadic
- Krypt
- Lazagne
- Metasploit
- Meterpreter
- MeteTool
- mikatz
- Mimikatz
- Mpreter
- MsfShell
- Nighthawk
- Packed.Generic.347
- PentestPowerShell
- Phobos
- 'PHP/BackDoor '
- Potato
- PowerSploit
- PowerSSH
- PshlSpy
- PSWTool
- PWCrack
- PWDump
- Ransom
- Rozena
- Ryzerlo
- Sbelt
- Seatbelt
- 'SecurityTool '
- SharpDump
- Shellcode
- Sliver
- Splinter
- Swrort
- Tescrypt
- TeslaCrypt
- TurtleLoader
- Valyria
- Webshell
filter_optional_generic:
- anti_ransomware_service.exe
- Anti-Ransomware
- Crack
- cyber-protect-service.exe
- encryptor
- Keygen
filter_optional_information:
  Level: 4
filter_optional_restartmanager:
  Provider_Name: Microsoft-Windows-RestartManager
condition: keywords and not 1 of filter_optional_*
```

## False Positives

- Some software piracy tools (key generators, cracks) are classified as hack tools

## References

- https://www.virustotal.com/gui/file/13828b390d5f58b002e808c2c4f02fdd920e236cc8015480fa33b6c1a9300e31
- https://www.virustotal.com/gui/file/15b57c1b68cd6ce3c161042e0f3be9f32d78151fe95461eedc59a79fc222c7ed
- https://www.virustotal.com/gui/file/5092b2672b4cb87a8dd1c2e6047b487b95995ad8ed5e9fc217f46b8bfb1b8c01
- https://www.nextron-systems.com/?s=antivirus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/Other/win_av_relevant_match.yml)
