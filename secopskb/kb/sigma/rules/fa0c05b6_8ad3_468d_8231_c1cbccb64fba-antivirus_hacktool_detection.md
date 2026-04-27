---
sigma_id: "fa0c05b6-8ad3-468d-8231-c1cbccb64fba"
title: "Antivirus Hacktool Detection"
framework: "sigma"
generated: "true"
source_path: "rules/category/antivirus/av_hacktool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_hacktool.yml"
build_date: "2026-04-26 17:03:18"
status: "stable"
level: "high"
logsource: "antivirus"
aliases:
  - "fa0c05b6-8ad3-468d-8231-c1cbccb64fba"
  - "Antivirus Hacktool Detection"
attack_technique_ids:
  - "T1204"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Antivirus Hacktool Detection

Detects a highly relevant Antivirus alert that reports a hack tool or other attack tool.
This event must not be ignored just because the AV has blocked the malware but investigate, how it came there in the first place.

## Metadata

- Rule ID: fa0c05b6-8ad3-468d-8231-c1cbccb64fba
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems), Arnim Rupp
- Date: 2021-08-16
- Modified: 2024-11-02
- Source Path: rules/category/antivirus/av_hacktool.yml

## Logsource

- category: antivirus

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204]]

## Detection

```yaml
selection:
- Signature|startswith:
  - ATK/
  - Exploit.Script.CVE
  - HKTL
  - HTOOL
  - PWS.
  - PWSX
  - SecurityTool
- Signature|contains:
  - Adfind
  - Brutel
  - BruteR
  - Cobalt
  - COBEACON
  - Cometer
  - DumpCreds
  - FastReverseProxy
  - Hacktool
  - Havoc
  - Impacket
  - Keylogger
  - Koadic
  - Mimikatz
  - Nighthawk
  - PentestPowerShell
  - Potato
  - PowerSploit
  - PowerSSH
  - PshlSpy
  - PSWTool
  - PWCrack
  - PWDump
  - Rozena
  - Rusthound
  - Sbelt
  - Seatbelt
  - SecurityTool
  - SharpDump
  - SharpHound
  - Shellcode
  - Sliver
  - Snaffler
  - SOAPHound
  - Splinter
  - Swrort
  - TurtleLoader
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.nextron-systems.com/2021/08/16/antivirus-event-analysis-cheat-sheet-v1-8-2/
- https://www.nextron-systems.com/?s=antivirus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_hacktool.yml)
