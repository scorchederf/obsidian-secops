---
sigma_id: "40b95d31-1afc-469e-8d34-9a3a667d058e"
title: "Suspicious Csi.exe Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_csi_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csi_execution.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "40b95d31-1afc-469e-8d34-9a3a667d058e"
  - "Suspicious Csi.exe Usage"
attack_technique_ids:
  - "T1072"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Csi.exe Usage

Csi.exe is a signed binary from Microsoft that comes with Visual Studio and provides C# interactive capabilities. It can be used to run C# code from a file passed as a parameter in command line. Early version of this utility provided with Microsoft “Roslyn” Community Technology Preview was named 'rcsi.exe'

## Metadata

- Rule ID: 40b95d31-1afc-469e-8d34-9a3a667d058e
- Status: test
- Level: medium
- Author: Konstantin Grishchenko, oscd.community
- Date: 2020-10-17
- Modified: 2022-07-11
- Source Path: rules/windows/process_creation/proc_creation_win_csi_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \csi.exe
  - \rcsi.exe
- OriginalFileName:
  - csi.exe
  - rcsi.exe
selection_cli:
  Company: Microsoft Corporation
condition: all of selection*
```

## False Positives

- Legitimate usage by software developers

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Csi/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Rcsi/
- https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/
- https://twitter.com/Z3Jpa29z/status/1317545798981324801

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csi_execution.yml)
