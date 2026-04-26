---
sigma_id: "3a716279-c18c-4488-83be-f9ececbfb9fc"
title: "Linux Setgid Capability Set on a Binary via Setcap Utility"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_cap_setgid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_cap_setgid.yml"
build_date: "2026-04-26 14:14:28"
status: "experimental"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "3a716279-c18c-4488-83be-f9ececbfb9fc"
  - "Linux Setgid Capability Set on a Binary via Setcap Utility"
attack_technique_ids:
  - "T1548"
  - "T1554"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Setgid Capability Set on a Binary via Setcap Utility

Detects the use of the 'setcap' utility to set the 'setgid' capability (cap_setgid) on a binary file.
This capability allows a non privileged process to make arbitrary manipulations of group IDs (GIDs), including setting its current GID to a value that would otherwise be restricted (i.e. GID 0, the root group).
This behavior can be used by adversaries to backdoor a binary in order to escalate privileges again in the future if needed.

## Metadata

- Rule ID: 3a716279-c18c-4488-83be-f9ececbfb9fc
- Status: experimental
- Level: low
- Author: Luc Génaux
- Date: 2026-01-24
- Source Path: rules/linux/process_creation/proc_creation_lnx_cap_setgid.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]
- [[kb/attack/techniques/T1554-compromise_host_software_binary|T1554]]

## Detection

```yaml
selection:
  Image|endswith: /setcap
  CommandLine|contains: cap_setgid
condition: selection
```

## False Positives

- Unknown

## References

- https://man7.org/linux/man-pages/man8/setcap.8.html
- https://dfir.ch/posts/linux_capabilities/
- https://juggernaut-sec.com/capabilities/#cap_setgid

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_cap_setgid.yml)
