---
sigma_id: "e568650b-5dcd-4658-8f34-ded0b1e13992"
title: "Potential Product Class Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_product_class.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_product_class.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e568650b-5dcd-4658-8f34-ded0b1e13992"
  - "Potential Product Class Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Product Class Reconnaissance Via Wmic.EXE

Detects the execution of WMIC in order to get a list of firewall, antivirus and antispywware products.
Adversaries often enumerate security products installed on a system to identify security controls and potential ways to evade detection or disable protection mechanisms.
This information helps them plan their next attack steps and choose appropriate techniques to bypass security measures.

## Metadata

- Rule ID: e568650b-5dcd-4658-8f34-ded0b1e13992
- Status: test
- Level: medium
- Author: Michael Haag, Florian Roth (Nextron Systems), juju4, oscd.community, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2023-02-14
- Modified: 2025-03-17
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_product_class.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains:
  - AntiVirusProduct
  - AntiSpywareProduct
  - FirewallProduct
condition: all of selection_*
```

## False Positives

- Legitimate use of wmic.exe for reconnaissance of firewall, antivirus and antispywware products.

## References

- https://github.com/albertzsigovits/malware-notes/blob/c820c7fea76cf76a861b28ebc77e06100e20ec29/Ransomware/Maze.md
- https://www.hybrid-analysis.com/sample/4be06ecd234e2110bd615649fe4a6fa95403979acf889d7e45a78985eb50acf9?environmentId=1
- https://www.trendmicro.com/en_us/research/25/c/socgholishs-intrusion-techniques-facilitate-distribution-of-rans.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_product_class.yml)
