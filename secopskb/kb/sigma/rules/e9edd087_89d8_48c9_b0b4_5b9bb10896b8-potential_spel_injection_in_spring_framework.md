---
sigma_id: "e9edd087-89d8-48c9-b0b4-5b9bb10896b8"
title: "Potential SpEL Injection In Spring Framework"
framework: "sigma"
generated: "true"
source_path: "rules/application/spring/spring_spel_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/spring/spring_spel_injection.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "spring / application"
aliases:
  - "e9edd087-89d8-48c9-b0b4-5b9bb10896b8"
  - "Potential SpEL Injection In Spring Framework"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential SpEL Injection In Spring Framework

Detects potential SpEL Injection exploitation, which may lead to RCE.

## Metadata

- Rule ID: e9edd087-89d8-48c9-b0b4-5b9bb10896b8
- Status: test
- Level: high
- Author: Moti Harmats
- Date: 2023-02-11
- Source Path: rules/application/spring/spring_spel_injection.yml

## Logsource

- category: application
- definition: Requirements: application error logs must be collected (with LOG_LEVEL=ERROR and above)
- product: spring

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- org.springframework.expression.ExpressionException
condition: keywords
```

## False Positives

- Application bugs

## References

- https://owasp.org/www-community/vulnerabilities/Expression_Language_Injection
- https://www.wix.engineering/post/threat-and-vulnerability-hunting-with-application-server-error-logs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/spring/spring_spel_injection.yml)
