---
sigma_id: "0ba1da6d-b6ce-4366-828c-18826c9de23e"
title: "Potential Defense Evasion Via Rename Of Highly Relevant Binaries"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_binary_highly_relevant.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_binary_highly_relevant.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0ba1da6d-b6ce-4366-828c-18826c9de23e"
  - "Potential Defense Evasion Via Rename Of Highly Relevant Binaries"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Defense Evasion Via Rename Of Highly Relevant Binaries

Detects the execution of a renamed binary often used by attackers or malware leveraging new Sysmon OriginalFileName datapoint.

## Metadata

- Rule ID: 0ba1da6d-b6ce-4366-828c-18826c9de23e
- Status: test
- Level: high
- Author: Matthew Green - @mgreen27, Florian Roth (Nextron Systems), frack113
- Date: 2019-06-15
- Modified: 2026-02-12
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_binary_highly_relevant.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
- Description: Execute processes remotely
- Product: Sysinternals PsExec
- Description|startswith:
  - Windows PowerShell
  - pwsh
- OriginalFileName:
  - certutil.exe
  - cmstp.exe
  - cscript.exe
  - IE4UINIT.EXE
  - finger.exe
  - mshta.exe
  - msiexec.exe
  - msxsl.exe
  - powershell_ise.exe
  - powershell.exe
  - psexec.c
  - psexec.exe
  - psexesvc.exe
  - pwsh.dll
  - reg.exe
  - regsvr32.exe
  - rundll32.exe
  - WerMgr
  - wmic.exe
  - wscript.exe
filter:
  Image|endswith:
  - \certutil.exe
  - \cmstp.exe
  - \cscript.exe
  - \ie4uinit.exe
  - \finger.exe
  - \mshta.exe
  - \msiexec.exe
  - \msxsl.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \psexec.exe
  - \psexec64.exe
  - \PSEXESVC.exe
  - \pwsh.exe
  - \reg.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wermgr.exe
  - \wmic.exe
  - \wscript.exe
condition: selection and not filter
```

## False Positives

- Custom applications use renamed binaries adding slight change to binary name. Typically this is easy to spot and add to whitelist
- PsExec installed via Windows Store doesn't contain original filename field (False negative)

## References

- https://mgreen27.github.io/posts/2019/05/12/BinaryRename.html
- https://mgreen27.github.io/posts/2019/05/29/BinaryRename2.html
- https://www.trendmicro.com/vinfo/hk-en/security/news/cybercrime-and-digital-threats/megacortex-ransomware-spotted-attacking-enterprise-networks
- https://twitter.com/christophetd/status/1164506034720952320
- https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/
- https://www.huntress.com/blog/malicious-browser-extention-crashfix-kongtuke

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_binary_highly_relevant.yml)
