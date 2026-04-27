---
sigma_id: "1cdd9a09-06c9-4769-99ff-626e2b3991b8"
title: "Suspicious Double Extension File Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_double_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_double_extension.yml"
build_date: "2026-04-27 19:13:56"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1cdd9a09-06c9-4769-99ff-626e2b3991b8"
  - "Suspicious Double Extension File Execution"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spear phishing campaigns

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]

## Detection

```yaml
selection:
  Image|endswith:
  - '      .exe'
  - ______.exe
  - .doc.exe
  - .doc.js
  - .docx.exe
  - .docx.js
  - .gif.exe
  - .jpeg.exe
  - .jpg.exe
  - .mkv.exe
  - .mov.exe
  - .mp3.exe
  - .mp4.exe
  - .pdf.exe
  - .pdf.js
  - .png.exe
  - .ppt.exe
  - .ppt.js
  - .pptx.exe
  - .pptx.js
  - .rtf.exe
  - .rtf.js
  - .svg.exe
  - .txt.exe
  - .txt.js
  - .xls.exe
  - .xls.js
  - .xlsx.exe
  - .xlsx.js
  - ⠀⠀⠀⠀⠀⠀.exe
  CommandLine|contains:
  - '      .exe'
  - ______.exe
  - .doc.exe
  - .doc.js
  - .docx.exe
  - .docx.js
  - .gif.exe
  - .jpeg.exe
  - .jpg.exe
  - .mkv.exe
  - .mov.exe
  - .mp3.exe
  - .mp4.exe
  - .pdf.exe
  - .pdf.js
  - .png.exe
  - .ppt.exe
  - .ppt.js
  - .pptx.exe
  - .pptx.js
  - .rtf.exe
  - .rtf.js
  - .svg.exe
  - .txt.exe
  - .txt.js
  - .xls.exe
  - .xls.js
  - .xlsx.exe
  - .xlsx.js
  - ⠀⠀⠀⠀⠀⠀.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://blu3-team.blogspot.com/2019/06/misleading-extensions-xlsexe-docexe.html
- https://twitter.com/blackorbird/status/1140519090961825792
- https://cloud.google.com/blog/topics/threat-intelligence/cybercriminals-weaponize-fake-ai-websites

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_double_extension.yml)
