---
atomic_guid: "c7921449-8b62-4c4d-8a83-d9281ac0190b"
title: "Steganographic Tarball Embedding"
framework: "atomic"
generated: "true"
attack_technique_id: "T1001.002"
attack_technique_name: "Data Obfuscation via Steganography"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c7921449-8b62-4c4d-8a83-d9281ac0190b"
  - "Steganographic Tarball Embedding"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Steganographic Tarball Embedding

This atomic test, named "Steganographic Tarball Embedding", simulates the technique of data obfuscation via steganography by embedding a tar archive file (tarball) 
within an image.

The test begins by ensuring the availability of the image file and the tarball file containing data . It then generates random passwords and saves them to a 
file. Subsequently, the tarball file is created, containing the passwords file. The test executor command reads the contents of the image 
file and the tarball file as byte arrays and appends them together to form a new image file. This process effectively embeds the tarball 
file within the image, utilizing steganography techniques for data obfuscation.

This atomic test simulates the technique of data obfuscation via steganography, enabling attackers to clandestinely transfer files across systems undetected. 
By embedding the tarball file within the image, adversaries can obscure their activities, facilitating covert communication and data exfiltration.

## Metadata

- Atomic GUID: c7921449-8b62-4c4d-8a83-d9281ac0190b
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

- description: Image file which will be downloaded to be used to hide data
- type: path
- default: PathToAtomicsFolder\T1001.002\bin\T1001.002.jpg

### new_image_file

- description: new image file ready for extraction
- type: path
- default: $env:PUBLIC\Downloads\T1001.002New.jpg

### passwords_file

- description: Text file containing random passwords
- type: path
- default: $env:TEMP\random_passwords.txt

### tar_file

- description: Tarz file containing random passwords
- type: path
- default: $env:PUBLIC\Downloads\T1001.002.tarz

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
New-Item -Type Directory (split-path "#{image_file}") -ErrorAction ignore | Out-Null
Write-Output "Downloading image file..."
$imageUrl = "https://github.com/raghavsingh7/Pictures/raw/a9617d9fce289909441120a1e0366315c2c5e19d/lime.jpg"
Invoke-WebRequest -Uri $imageUrl -OutFile "#{image_file}"
```

File to hide within tarz file must exist

### Prerequisite Check

```powershell
if (!(Test-Path "#{passwords_file}")) {exit 1} else {
{exit 0}
}
```

### Get Prerequisite

```powershell
Write-Output "Generating random passwords and saving to file..."
$passwords = 1..10 | ForEach-Object { -join ((1..12) | ForEach-Object { @('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') + @('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z') + @('0','1','2','3','4','5','6','7','8','9') + @('!','@','#','$','%','^','&','*','(','(',')','-','=','+','_','[',']','{','}','|',';',';',':',',','<','>','?') | Get-Random }) }
$passwords | Out-File -FilePath "#{passwords_file}"
```

Tarz file to embed in image must exist

### Prerequisite Check

```powershell
if (!(Test-Path "#{tar_file}")) {exit 1} else {
{exit 0}
}
```

### Get Prerequisite

```powershell
Write-Output "Generating tarz file..."
tar -cvf "#{tar_file}" "#{passwords_file}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-Content "#{image_file}", "#{tar_file}" -Encoding byte -ReadCount 0 | Set-Content "#{new_image_file}" -Encoding byte
```

### Cleanup

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force -ErrorAction Ignore
Remove-Item -Path "#{new_image_file}" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml)
