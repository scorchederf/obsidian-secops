---
sigma_id: "cc7abbd0-762b-41e3-8a26-57ad50d2eea3"
title: "MSHTA Execution with Suspicious File Extensions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_execution.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc7abbd0-762b-41e3-8a26-57ad50d2eea3"
  - "MSHTA Execution with Suspicious File Extensions"
attack_technique_ids:
  - "T1140"
  - "T1218.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSHTA Execution with Suspicious File Extensions

Detects execution of mshta.exe with file types that looks like they do not typically represent HTA (HTML Application) content,
such as .png, .jpg, .zip, .pdf, and others, which are often polyglots. MSHTA is a legitimate Windows utility for executing HTML Applications
containing VBScript or JScript. Threat actors often abuse this lolbin utility to download and
execute malicious scripts disguised as benign files or hosted under misleading extensions to evade detection.

## Metadata

- Rule ID: cc7abbd0-762b-41e3-8a26-57ad50d2eea3
- Status: test
- Level: high
- Author: Diego Perez (@darkquassar), Markus Neis, Swisscom (Improve Rule), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2019-02-22
- Modified: 2025-05-12
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_img:
- Image|endswith: \mshta.exe
- OriginalFileName: mshta.exe
selection_cli:
  CommandLine|contains:
  - .7z
  - .avi
  - .bat
  - .bmp
  - .conf
  - .csv
  - .dll
  - .doc
  - .gif
  - .gz
  - .ini
  - .jpe
  - .jpg
  - .json
  - .lnk
  - .log
  - .mkv
  - .mp3
  - .mp4
  - .pdf
  - .png
  - .ppt
  - .rar
  - .rtf
  - .svg
  - .tar
  - .tmp
  - .txt
  - .xls
  - .xml
  - .yaml
  - .yml
  - .zip
  - vbscript
condition: all of selection_*
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- http://blog.sevagas.com/?Hacking-around-HTA-files
- https://0x00sec.org/t/clientside-exploitation-in-2018-how-pentesting-has-changed/7356
- https://learn.microsoft.com/en-us/previous-versions/dotnet/framework/data/xml/xslt/xslt-stylesheet-scripting-using-msxsl-script
- https://medium.com/tsscyber/pentesting-and-hta-bypassing-powershell-constrained-language-mode-53a42856c997
- https://twitter.com/mattifestation/status/1326228491302563846
- https://www.virustotal.com/gui/file/c1f27d9795a2eba630db8a043580a0761798f06370fb1317067805f8a845b00c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_execution.yml)
