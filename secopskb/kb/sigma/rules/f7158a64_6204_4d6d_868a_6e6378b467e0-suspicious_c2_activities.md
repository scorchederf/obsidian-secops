---
sigma_id: "f7158a64-6204-4d6d-868a-6e6378b467e0"
title: "Suspicious C2 Activities"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_susp_c2_commands.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_susp_c2_commands.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "f7158a64-6204-4d6d-868a-6e6378b467e0"
  - "Suspicious C2 Activities"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious C2 Activities

Detects suspicious activities as declared by Florian Roth in its 'Best Practice Auditd Configuration'.
This includes the detection of the following commands; wget, curl, base64, nc, netcat, ncat, ssh, socat, wireshark, rawshark, rdesktop, nmap.
These commands match a few techniques from the tactics "Command and Control", including not exhaustively the following; Application Layer Protocol (T1071), Non-Application Layer Protocol (T1095), Data Encoding (T1132)

## Metadata

- Rule ID: f7158a64-6204-4d6d-868a-6e6378b467e0
- Status: test
- Level: medium
- Author: Marie Euler
- Date: 2020-05-18
- Modified: 2021-11-27
- Source Path: rules/linux/auditd/lnx_auditd_susp_c2_commands.yml

## Logsource

- definition: Required auditd configuration:
-w /usr/bin/wget -p x -k susp_activity
-w /usr/bin/curl -p x -k susp_activity
-w /usr/bin/base64 -p x -k susp_activity
-w /bin/nc -p x -k susp_activity
-w /bin/netcat -p x -k susp_activity
-w /usr/bin/ncat -p x -k susp_activity
-w /usr/bin/ss -p x -k susp_activity
-w /usr/bin/netstat -p x -k susp_activity
-w /usr/bin/ssh -p x -k susp_activity
-w /usr/bin/scp -p x -k susp_activity
-w /usr/bin/sftp -p x -k susp_activity
-w /usr/bin/ftp -p x -k susp_activity
-w /usr/bin/socat -p x -k susp_activity
-w /usr/bin/wireshark -p x -k susp_activity
-w /usr/bin/tshark -p x -k susp_activity
-w /usr/bin/rawshark -p x -k susp_activity
-w /usr/bin/rdesktop -p x -k susp_activity
-w /usr/local/bin/rdesktop -p x -k susp_activity
-w /usr/bin/wlfreerdp -p x -k susp_activity
-w /usr/bin/xfreerdp -p x -k susp_activity
-w /usr/local/bin/xfreerdp -p x -k susp_activity
-w /usr/bin/nmap -p x -k susp_activity
(via https://github.com/Neo23x0/auditd/blob/ddf2603dbc985f97538d102f13b4e4446b402bae/audit.rules#L336)

- product: linux
- service: auditd

## Detection

```yaml
selection:
  key: susp_activity
condition: selection
```

## False Positives

- Admin or User activity

## References

- https://github.com/Neo23x0/auditd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_susp_c2_commands.yml)
