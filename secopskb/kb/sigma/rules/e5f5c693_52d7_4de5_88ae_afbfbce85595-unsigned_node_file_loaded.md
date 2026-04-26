---
sigma_id: "e5f5c693-52d7-4de5-88ae-afbfbce85595"
title: "Unsigned .node File Loaded"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_unsigned_node_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_unsigned_node_load.yml"
build_date: "2026-04-26 14:14:38"
status: "experimental"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "e5f5c693-52d7-4de5-88ae-afbfbce85595"
  - "Unsigned .node File Loaded"
attack_technique_ids:
  - "T1129"
  - "T1574.001"
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned .node File Loaded

Detects the loading of unsigned .node files.
Adversaries may abuse a lack of .node integrity checking to execute arbitrary code inside of trusted applications such as Slack.
.node files are native add-ons for Electron-based applications, which are commonly used for desktop applications like Slack, Discord, and Visual Studio Code.
This technique has been observed in the DripLoader malware, which uses unsigned .node files to load malicious native code into Electron applications.

## Metadata

- Rule ID: e5f5c693-52d7-4de5-88ae-afbfbce85595
- Status: experimental
- Level: medium
- Author: Jonathan Beierle (@hullabrian)
- Date: 2025-11-22
- Source Path: rules/windows/image_load/image_load_dll_unsigned_node_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1129-shared_modules|T1129]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]
- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection_node_extension:
  ImageLoaded|endswith: .node
selection_status:
- Signed: 'false'
- SignatureStatus: Unavailable
filter_optional_vscode_jupyter:
  Image|endswith: \Code.exe
  ImageLoaded|contains: .vscode\extensions\ms-toolsai.jupyter-
  ImageLoaded|endswith:
  - \electron.napi.node
  - \node.napi.glibc.node
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- VsCode extensions or similar legitimate tools might use unsigned .node files. These should be investigated on a case-by-case basis, and whitelisted if determined to be benign.

## References

- https://www.coreycburton.com/blog/driploader-case-study
- https://github.com/CoreyCBurton/DripLoaderNG
- https://www.electronjs.org/docs/latest/tutorial/native-code-and-electron

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_unsigned_node_load.yml)
