---
sigma_id: "1f0489be-b496-4ddf-b3a9-5900f2044e9c"
title: "Suspicious File Write to SharePoint Layouts Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_filewrite_in_sharepoint_layouts_dir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_filewrite_in_sharepoint_layouts_dir.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "1f0489be-b496-4ddf-b3a9-5900f2044e9c"
  - "Suspicious File Write to SharePoint Layouts Directory"
attack_technique_ids:
  - "T1190"
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious file writes to SharePoint layouts directory which could indicate webshell activity or post-exploitation.
This behavior has been observed in the exploitation of SharePoint vulnerabilities such as CVE-2025-49704, CVE-2025-49706 or CVE-2025-53770.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

## Detection

```yaml
selection:
  Image|endswith:
  - \cmd.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \w3wp.exe
  TargetFilename|startswith:
  - C:\Program Files\Common Files\Microsoft Shared\Web Server Extensions\
  - C:\Program Files (x86)\Common Files\Microsoft Shared\Web Server Extensions\
  TargetFilename|contains:
  - \15\TEMPLATE\LAYOUTS\
  - \16\TEMPLATE\LAYOUTS\
  TargetFilename|endswith:
  - .asax
  - .ascx
  - .ashx
  - .asmx
  - .asp
  - .aspx
  - .bat
  - .cmd
  - .cer
  - .config
  - .hta
  - .js
  - .jsp
  - .jspx
  - .php
  - .ps1
  - .vbs
condition: selection
```

## False Positives

- Unknown

## References

- https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/
- https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_filewrite_in_sharepoint_layouts_dir.yml)
