---
sigma_id: "6640f31c-01ad-49b5-beb5-83498a5cd8bd"
title: "Potential Arbitrary Code Execution Via Node.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_node_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_node_abuse.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6640f31c-01ad-49b5-beb5-83498a5cd8bd"
  - "Potential Arbitrary Code Execution Via Node.EXE"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution node.exe which is shipped with multiple software such as VMware, Adobe...etc. In order to execute arbitrary code. For example to establish reverse shell as seen in Log4j attacks...etc

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detection

```yaml
selection_main:
  Image|endswith: \node.exe
  CommandLine|contains:
  - ' -e '
  - ' --eval '
selection_action_reverse_shell:
  CommandLine|contains|all:
  - .exec(
  - net.socket
  - .connect
  - child_process
condition: selection_main and 1 of selection_action_*
```

## False Positives

- Unlikely

## References

- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html
- https://www.sprocketsecurity.com/resources/crossing-the-log4j-horizon-a-vulnerability-with-no-return
- https://www.rapid7.com/blog/post/2022/01/18/active-exploitation-of-vmware-horizon-servers/
- https://nodejs.org/api/cli.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_node_abuse.yml)
