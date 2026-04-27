---
sigma_id: "cd8b36ac-8e4a-4c2f-a402-a29b8fbd5bca"
title: "Suspicious File Creation Activity From Fake Recycle.Bin Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_recycle_bin_fake_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_recycle_bin_fake_exec.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "cd8b36ac-8e4a-4c2f-a402-a29b8fbd5bca"
  - "Suspicious File Creation Activity From Fake Recycle.Bin Folder"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects file write event from/to a fake recycle bin folder that is often used as a staging directory for malware

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
- Image|contains:
  - RECYCLERS.BIN\
  - RECYCLER.BIN\
- TargetFilename|contains:
  - RECYCLERS.BIN\
  - RECYCLER.BIN\
condition: selection
```

## False Positives

- Unknown

## References

- https://www.mandiant.com/resources/blog/infected-usb-steal-secrets
- https://unit42.paloaltonetworks.com/cloaked-ursa-phishing/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_recycle_bin_fake_exec.yml)
