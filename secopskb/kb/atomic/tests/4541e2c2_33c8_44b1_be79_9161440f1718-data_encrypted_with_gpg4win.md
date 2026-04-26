---
atomic_guid: "4541e2c2-33c8-44b1-be79-9161440f1718"
title: "Data Encrypted with GPG4Win"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4541e2c2-33c8-44b1-be79-9161440f1718"
  - "Data Encrypted with GPG4Win"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Data Encrypted with GPG4Win

Gpg4win is a Windows tool (also called Kleopatra which is the preferred certificate manager) that uses email and file encryption packages for symmetric encryption. It is used by attackers to encrypt disks. User will need to add pass phrase to encrypt file as automation is not allowed under newer versions.

## Metadata

- Atomic GUID: 4541e2c2-33c8-44b1-be79-9161440f1718
- Technique: T1486: Data Encrypted for Impact
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1486/T1486.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Input Arguments

### File_to_Encrypt_Location

- description: Path of File
- type: path
- default: $env:temp\test.txt

### GPG_Exe_Location

- description: Path of the GPG program
- type: path
- default: C:\Program Files (x86)\GnuPG\bin\gpg.exe

## Dependencies

GPG must exist at (#{GPG_Exe_Location}). If -GetPrereqs fails, try to install GPG4WIN manually at 'https://www.gpg4win.org/download.html'. Once done, run -CheckPrereqs to confirm that it works.

### Prerequisite Check

```untitled
if (test-path '#{GPG_Exe_Location}'){exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
Set-Content -Path "#{File_to_Encrypt_Location}" -Value "populating this file with some text"  # Create the test.txt file
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://files.gpg4win.org/gpg4win-4.1.0.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\gpginstall.exe"
cmd /c "PathToAtomicsFolder\..\ExternalPayloads\gpginstall.exe" /S
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Set-Content -Path "#{File_to_Encrypt_Location}" -Value "populating this file with some text"  # Create the test.txt file again in case prereqs failed
cmd /c "`"C:\Program Files (x86)\GnuPG\bin\gpg.exe`" --passphrase 'SomeParaphraseBlah' --batch --yes -c `"#{File_to_Encrypt_Location}`""
```

### Cleanup

```powershell
Remove-Item -Path "#{File_to_Encrypt_Location}" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "#{File_to_Encrypt_Location}.gpg" -Force -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
