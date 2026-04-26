---
sigma_id: "ae48ab93-45f7-4051-9dfe-5d30a3f78e33"
title: "Spring Framework Exceptions"
framework: "sigma"
generated: "true"
source_path: "rules/application/spring/spring_application_exceptions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/spring/spring_application_exceptions.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "medium"
logsource: "spring / application"
aliases:
  - "ae48ab93-45f7-4051-9dfe-5d30a3f78e33"
  - "Spring Framework Exceptions"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Spring Framework Exceptions

Detects suspicious Spring framework exceptions that could indicate exploitation attempts

## Metadata

- Rule ID: ae48ab93-45f7-4051-9dfe-5d30a3f78e33
- Status: stable
- Level: medium
- Author: Thomas Patzke
- Date: 2017-08-06
- Modified: 2020-09-01
- Source Path: rules/application/spring/spring_application_exceptions.yml

## Logsource

- category: application
- product: spring

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- AccessDeniedException
- CsrfException
- InvalidCsrfTokenException
- MissingCsrfTokenException
- CookieTheftException
- InvalidCookieException
- RequestRejectedException
condition: keywords
```

## False Positives

- Application bugs

## References

- https://docs.spring.io/spring-security/site/docs/current/api/overview-tree.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/spring/spring_application_exceptions.yml)
