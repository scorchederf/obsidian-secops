---
atomic_guid: "9f8b1c54-cb76-4d5e-bb1f-2f5c0e8f5a11"
title: "Expand CAB with expand.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "9f8b1c54-cb76-4d5e-bb1f-2f5c0e8f5a11"
  - "Expand CAB with expand.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses expand.exe to extract a file from a CAB created locally. This simulates adversarial use of expand on cabinet archives.
Upon success, art-expand-source.txt is extracted next to the CAB.

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

## Input Arguments

### cab_path

- description: Path to the CAB to expand (created if missing)
- type: path
- default: %TEMP%\art-expand-test.cab

### output_dir

- description: Destination directory
- type: path
- default: %TEMP%\art-expand-out

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
mkdir "#{output_dir}" >nul 2>&1
echo hello from atomic red team > "PathToAtomicsFolder\T1140\src\art-expand-source.txt"
makecab "PathToAtomicsFolder\T1140\src\art-expand-source.txt" "#{cab_path}"
pushd "#{output_dir}"
expand "#{cab_path}" -F:* .
popd
```

### Cleanup

```cmd
del "PathToAtomicsFolder\T1140\src\art-expand-source.txt" >nul 2>&1
del "#{cab_path}" >nul 2>&1
rmdir "#{output_dir}" /s /q >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
