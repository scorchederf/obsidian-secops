---
sigma_id: "16c86189-b556-4ee8-b4c7-7e350a195a4f"
title: "Potential Server Side Template Injection In Velocity"
framework: "sigma"
generated: "true"
source_path: "rules/application/velocity/velocity_ssti_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/velocity/velocity_ssti_injection.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "velocity / application"
aliases:
  - "16c86189-b556-4ee8-b4c7-7e350a195a4f"
  - "Potential Server Side Template Injection In Velocity"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects exceptions in velocity template renderer, this most likely happens due to dynamic rendering of user input and may lead to RCE.

## Logsource

- category: application
- definition: Requirements: application error logs must be collected (with LOG_LEVEL=ERROR and above)
- product: velocity

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]

## Detection

```yaml
keywords:
- ParseErrorException
- VelocityException
- TemplateInitException
condition: keywords
```

## False Positives

- Application bugs
- Missing .vm files

## References

- https://antgarsil.github.io/posts/velocity/
- https://www.wix.engineering/post/threat-and-vulnerability-hunting-with-application-server-error-logs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/velocity/velocity_ssti_injection.yml)
