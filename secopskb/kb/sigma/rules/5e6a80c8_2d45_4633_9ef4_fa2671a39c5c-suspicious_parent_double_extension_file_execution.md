---
sigma_id: "5e6a80c8-2d45-4633-9ef4-fa2671a39c5c"
title: "Suspicious Parent Double Extension File Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_double_extension_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_double_extension_parent.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5e6a80c8-2d45-4633-9ef4-fa2671a39c5c"
  - "Suspicious Parent Double Extension File Execution"
attack_technique_ids:
  - "T1036.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Parent Double Extension File Execution

Detect execution of suspicious double extension files in ParentCommandLine

## Metadata

- Rule ID: 5e6a80c8-2d45-4633-9ef4-fa2671a39c5c
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-06
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_susp_double_extension_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.007]]

## Detection

```yaml
selection:
- ParentImage|endswith:
  - .doc.lnk
  - .docx.lnk
  - .xls.lnk
  - .xlsx.lnk
  - .ppt.lnk
  - .pptx.lnk
  - .rtf.lnk
  - .pdf.lnk
  - .txt.lnk
  - .doc.js
  - .docx.js
  - .xls.js
  - .xlsx.js
  - .ppt.js
  - .pptx.js
  - .rtf.js
  - .pdf.js
  - .txt.js
- ParentCommandLine|contains:
  - .doc.lnk
  - .docx.lnk
  - .xls.lnk
  - .xlsx.lnk
  - .ppt.lnk
  - .pptx.lnk
  - .rtf.lnk
  - .pdf.lnk
  - .txt.lnk
  - .doc.js
  - .docx.js
  - .xls.js
  - .xlsx.js
  - .ppt.js
  - .pptx.js
  - .rtf.js
  - .pdf.js
  - .txt.js
condition: selection
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/7872d8845a332dce517adae9c3389fde5313ff2fed38c2577f3b498da786db68/behavior
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bluebottle-banks-targeted-africa

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_double_extension_parent.yml)
