---
sigma_id: "5bac7a56-da88-4c27-922e-c81e113b20cb"
title: "Github Self-Hosted Runner Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_github_self_hosted_runner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_github_self_hosted_runner.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5bac7a56-da88-4c27-922e-c81e113b20cb"
  - "Github Self-Hosted Runner Execution"
attack_technique_ids:
  - "T1102.002"
  - "T1071"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Self-Hosted Runner Execution

Detects GitHub self-hosted runners executing workflows on local infrastructure that could be abused for persistence and code execution.
Shai-Hulud is an npm supply chain worm targeting CI/CD environments.
It installs runners on compromised systems to maintain access after credential theft, leveraging their access to secrets and internal networks.

## Metadata

- Rule ID: 5bac7a56-da88-4c27-922e-c81e113b20cb
- Status: test
- Level: medium
- Author: Daniel Koifman (KoifSec)
- Date: 2025-11-29
- Source Path: rules/windows/process_creation/proc_creation_win_github_self_hosted_runner.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102.002]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071]]

## Detection

```yaml
selection_worker_img:
- Image|endswith: \Runner.Worker.exe
- OriginalFileName: Runner.Worker.dll
selection_worker_cli:
  CommandLine|contains: spawnclient
selection_listener_img:
- Image|endswith: \Runner.Listener.exe
- OriginalFileName: Runner.Listener.dll
selection_listener_cli:
  CommandLine|contains:
  - run
  - configure
condition: all of selection_worker_* or all of selection_listener_*
```

## False Positives

- Legitimate GitHub self-hosted runner installations on designated CI/CD infrastructure
- Authorized runner deployments by DevOps/Platform teams following change management
- Scheduled runner updates or reconfigurations on existing build agents
- Self-hosted runners that follow expected/known naming patterns
- Installation via expected/known configuration management tools (reflected mostly as parent process name)

## References

- https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/
- https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_github_self_hosted_runner.yml)
