---
sigma_id: "78cc2dd2-7d20-4d32-93ff-057084c38b93"
title: "Antivirus Password Dumper Detection"
framework: "sigma"
generated: "true"
source_path: "rules/category/antivirus/av_password_dumper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_password_dumper.yml"
build_date: "2026-04-26 17:03:18"
status: "stable"
level: "critical"
logsource: "antivirus"
aliases:
  - "78cc2dd2-7d20-4d32-93ff-057084c38b93"
  - "Antivirus Password Dumper Detection"
attack_technique_ids:
  - "T1003"
  - "T1558"
  - "T1003.001"
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Antivirus Password Dumper Detection

Detects a highly relevant Antivirus alert that reports a password dumper.
This event must not be ignored just because the AV has blocked the malware but investigate, how it came there in the first place.

## Metadata

- Rule ID: 78cc2dd2-7d20-4d32-93ff-057084c38b93
- Status: stable
- Level: critical
- Author: Florian Roth (Nextron Systems), Arnim Rupp
- Date: 2018-09-09
- Modified: 2024-11-02
- Source Path: rules/category/antivirus/av_password_dumper.yml

## Logsource

- category: antivirus

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
- Signature|startswith: PWS
- Signature|contains:
  - Certify
  - DCSync
  - DumpCreds
  - DumpLsass
  - DumpPert
  - HTool/WCE
  - Kekeo
  - Lazagne
  - LsassDump
  - Mimikatz
  - MultiDump
  - Nanodump
  - NativeDump
  - Outflank
  - PShlSpy
  - PSWTool
  - PWCrack
  - PWDump
  - PWS.
  - PWSX
  - pypykatz
  - Rubeus
  - SafetyKatz
  - SecurityTool
  - SharpChrome
  - SharpDPAPI
  - SharpDump
  - SharpKatz
  - SharpS.
  - ShpKatz
  - TrickDump
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.nextron-systems.com/?s=antivirus
- https://www.virustotal.com/gui/file/5fcda49ee7f202559a6cbbb34edb65c33c9a1e0bde9fa2af06a6f11b55ded619
- https://www.virustotal.com/gui/file/a4edfbd42595d5bddb442c82a02cf0aaa10893c1bf79ea08b9ce576f82749448

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_password_dumper.yml)
