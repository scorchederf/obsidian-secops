---
sigma_id: "1ab3c5ed-5baf-417b-bb6b-78ca33f6c3df"
title: "AWS EC2 Startup Shell Script Change"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_ec2_startup_script_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_startup_script_change.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "1ab3c5ed-5baf-417b-bb6b-78ca33f6c3df"
  - "AWS EC2 Startup Shell Script Change"
attack_technique_ids:
  - "T1059.001"
  - "T1059.003"
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the EC2 instance startup script. The shell script will be executed as root/SYSTEM every time the specific instances are booted up.

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Detection

```yaml
selection_source:
  eventSource: ec2.amazonaws.com
  requestParameters.attribute: userData
  eventName: ModifyInstanceAttribute
condition: selection_source
```

## False Positives

- Valid changes to the startup script

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/ec2__startup_shell_script/main.py#L9

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_startup_script_change.yml)
