---
sigma_id: "3ce8e9a4-bc61-4c9b-8e69-d7e2492a8781"
title: "OpenSSH Server Listening On Socket"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/openssh/win_sshd_openssh_server_listening_on_socket.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/openssh/win_sshd_openssh_server_listening_on_socket.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / openssh"
aliases:
  - "3ce8e9a4-bc61-4c9b-8e69-d7e2492a8781"
  - "OpenSSH Server Listening On Socket"
attack_technique_ids:
  - "T1021.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenSSH Server Listening On Socket

Detects scenarios where an attacker enables the OpenSSH server and server starts to listening on SSH socket.

## Metadata

- Rule ID: 3ce8e9a4-bc61-4c9b-8e69-d7e2492a8781
- Status: test
- Level: medium
- Author: mdecrevoisier
- Date: 2022-10-25
- Source Path: rules/windows/builtin/openssh/win_sshd_openssh_server_listening_on_socket.yml

## Logsource

- product: windows
- service: openssh

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.004]]

## Detection

```yaml
selection:
  EventID: 4
  process: sshd
  payload|startswith: 'Server listening on '
condition: selection
```

## False Positives

- Legitimate administrator activity

## References

- https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack/tree/master/TA0008-Lateral%20Movement/T1021.004-Remote%20Service%20SSH
- https://winaero.com/enable-openssh-server-windows-10/
- https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse
- https://virtualizationreview.com/articles/2020/05/21/ssh-server-on-windows-10.aspx
- https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/openssh/win_sshd_openssh_server_listening_on_socket.yml)
