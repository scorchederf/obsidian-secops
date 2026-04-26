---
sigma_id: "d65f37da-a26a-48f8-8159-3dde96680ad2"
title: "Process Execution Error In JVM Based Application"
framework: "sigma"
generated: "true"
source_path: "rules/application/jvm/java_rce_exploitation_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/jvm/java_rce_exploitation_attempt.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "jvm / application"
aliases:
  - "d65f37da-a26a-48f8-8159-3dde96680ad2"
  - "Process Execution Error In JVM Based Application"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Execution Error In JVM Based Application

Detects process execution related exceptions in JVM based apps, often relates to RCE

## Metadata

- Rule ID: d65f37da-a26a-48f8-8159-3dde96680ad2
- Status: test
- Level: high
- Author: Moti Harmats
- Date: 2023-02-11
- Source Path: rules/application/jvm/java_rce_exploitation_attempt.yml

## Logsource

- category: application
- definition: Requirements: application error logs must be collected (with LOG_LEVEL=ERROR and above)
- product: jvm

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- Cannot run program
- java.lang.ProcessImpl
- java.lang.ProcessBuilder
condition: keywords
```

## False Positives

- Application bugs

## References

- https://www.wix.engineering/post/threat-and-vulnerability-hunting-with-application-server-error-logs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/jvm/java_rce_exploitation_attempt.yml)
