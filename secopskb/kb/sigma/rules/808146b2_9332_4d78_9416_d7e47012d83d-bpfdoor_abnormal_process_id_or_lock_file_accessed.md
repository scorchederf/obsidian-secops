---
sigma_id: "808146b2-9332-4d78-9416-d7e47012d83d"
title: "BPFDoor Abnormal Process ID or Lock File Accessed"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_bpfdoor_file_accessed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_bpfdoor_file_accessed.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "808146b2-9332-4d78-9416-d7e47012d83d"
  - "BPFDoor Abnormal Process ID or Lock File Accessed"
attack_technique_ids:
  - "T1106"
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

detects BPFDoor .lock and .pid files access in temporary file storage facility

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106: Native API]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection:
  type: PATH
  name:
  - /var/run/aepmonend.pid
  - /var/run/auditd.lock
  - /var/run/cma.lock
  - /var/run/console-kit.pid
  - /var/run/consolekit.pid
  - /var/run/daemon.pid
  - /var/run/hald-addon.pid
  - /var/run/hald-smartd.pid
  - /var/run/haldrund.pid
  - /var/run/hp-health.pid
  - /var/run/hpasmlit.lock
  - /var/run/hpasmlited.pid
  - /var/run/kdevrund.pid
  - /var/run/lldpad.lock
  - /var/run/mcelog.pid
  - /var/run/system.pid
  - /var/run/uvp-srv.pid
  - /var/run/vmtoolagt.pid
  - /var/run/xinetd.lock
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/
- https://www.elastic.co/security-labs/a-peek-behind-the-bpfdoor
- https://www.rapid7.com/blog/post/tr-bpfdoor-telecom-networks-sleeper-cells-threat-research-report/
- https://github.com/rapid7/Rapid7-Labs/blob/741c7196ec12a0a56b63463d1fd726ff14d3a97a/BPFDoor/rapid7_detect_bpfdoor.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_bpfdoor_file_accessed.yml)
