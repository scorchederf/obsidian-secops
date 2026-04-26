---
sigma_id: "a7af2487-9c2f-42e4-9bb9-ff961f0561d5"
title: "Audio Capture"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_audio_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_audio_capture.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "a7af2487-9c2f-42e4-9bb9-ff961f0561d5"
  - "Audio Capture"
attack_technique_ids:
  - "T1123"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Audio Capture

Detects attempts to record audio using the arecord and ecasound utilities.

## Metadata

- Rule ID: a7af2487-9c2f-42e4-9bb9-ff961f0561d5
- Status: test
- Level: low
- Author: Pawel Mazur, Milad Cheraghi
- Date: 2021-09-04
- Modified: 2025-12-05
- Source Path: rules/linux/auditd/lnx_auditd_audio_capture.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Detection

```yaml
selection_execve:
  type: EXECVE
  a0: arecord
  a1: -vv
  a2: -fdat
selection_syscall_memfd_create:
  type: SYSCALL
  exe|endswith: /ecasound
  SYSCALL: memfd_create
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://linux.die.net/man/1/arecord
- https://linuxconfig.org/how-to-test-microphone-with-audio-linux-sound-architecture-alsa
- https://manpages.debian.org/unstable/ecasound/ecasound.1.en.html
- https://ecasound.seul.org/ecasound/Documentation/examples.html#fconversions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_audio_capture.yml)
