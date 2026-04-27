---
sigma_id: "9cfe4b27-1e56-48b4-b7a8-d46851c91a44"
title: "MMC Executing Files with Reversed Extensions Using RTLO Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mmc_rlo_abuse_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_rlo_abuse_pattern.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9cfe4b27-1e56-48b4-b7a8-d46851c91a44"
  - "MMC Executing Files with Reversed Extensions Using RTLO Abuse"
attack_technique_ids:
  - "T1204.002"
  - "T1218.014"
  - "T1036.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MMC Executing Files with Reversed Extensions Using RTLO Abuse

Detects malicious behavior where the MMC utility (`mmc.exe`) executes files with reversed extensions caused by Right-to-Left Override (RLO) abuse, disguising them as document formats.

## Metadata

- Rule ID: 9cfe4b27-1e56-48b4-b7a8-d46851c91a44
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_mmc_rlo_abuse_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.014]]
- [[kb/attack/techniques/T1036-masquerading|T1036.002]]

## Detection

```yaml
selection_image:
- Image|endswith: \mmc.exe
- OriginalFileName: MMC.exe
selection_commandline:
  CommandLine|contains:
  - cod.msc
  - fdp.msc
  - ftr.msc
  - lmth.msc
  - slx.msc
  - tdo.msc
  - xcod.msc
  - xslx.msc
  - xtpp.msc
condition: all of selection_*
```

## False Positives

- Legitimate administrative actions using MMC to execute misnamed `.msc` files.
- Unconventional but non-malicious usage of RLO or reversed extensions.

## References

- https://www.unicode.org/versions/Unicode5.2.0/ch02.pdf
- https://en.wikipedia.org/wiki/Right-to-left_override
- https://tria.ge/241015-l98snsyeje/behavioral2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_rlo_abuse_pattern.yml)
