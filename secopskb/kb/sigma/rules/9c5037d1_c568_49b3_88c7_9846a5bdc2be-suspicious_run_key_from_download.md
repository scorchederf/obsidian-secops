---
sigma_id: "9c5037d1-c568-49b3-88c7-9846a5bdc2be"
title: "Suspicious Run Key from Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_susp_download_run_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_download_run_key.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "9c5037d1-c568-49b3-88c7-9846a5bdc2be"
  - "Suspicious Run Key from Download"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Detection

```yaml
selection:
  Image|contains:
  - \AppData\Local\Packages\Microsoft.Outlook_
  - \AppData\Local\Microsoft\Olk\Attachments\
  - \Downloads\
  - \Temporary Internet Files\Content.Outlook\
  - \Local Settings\Temporary Internet Files\
  TargetObject|contains:
  - \Software\Microsoft\Windows\CurrentVersion\Run
  - \Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
condition: selection
```

## False Positives

- Software installers downloaded and used by users

## References

- https://app.any.run/tasks/c5bef5b7-f484-4c43-9cf3-d5c5c7839def/
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_download_run_key.yml)
