---
sigma_id: "fcc6d700-68d9-4241-9a1a-06874d621b06"
title: "Suspicious File Created Via OneNote Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_onenote_susp_dropped_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_onenote_susp_dropped_files.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "fcc6d700-68d9-4241-9a1a-06874d621b06"
  - "Suspicious File Created Via OneNote Application"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious files created via the OneNote application. This could indicate a potential malicious ".one"/".onepkg" file was executed as seen being used in malware activity in the wild

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \onenote.exe
  - \onenotem.exe
  - \onenoteim.exe
  TargetFilename|contains: \AppData\Local\Temp\OneNote\
  TargetFilename|endswith:
  - .bat
  - .chm
  - .cmd
  - .dll
  - .exe
  - .hta
  - .htm
  - .html
  - .js
  - .lnk
  - .ps1
  - .vbe
  - .vbs
  - .wsf
condition: selection
```

## False Positives

- False positives should be very low with the extensions list cited. Especially if you don't heavily utilize OneNote.
- Occasional FPs might occur if OneNote is used internally to share different embedded documents

## References

- https://www.bleepingcomputer.com/news/security/hackers-now-use-microsoft-onenote-attachments-to-spread-malware/
- https://blog.osarmor.com/319/onenote-attachment-delivers-asyncrat-malware/
- https://twitter.com/MaD_c4t/status/1623414582382567424
- https://labs.withsecure.com/publications/detecting-onenote-abuse
- https://www.trustedsec.com/blog/new-attacks-old-tricks-how-onenote-malware-is-evolving/
- https://app.any.run/tasks/17f2d378-6d11-4d6f-8340-954b04f35e83/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_onenote_susp_dropped_files.yml)
