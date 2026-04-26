---
sigma_id: "fd435618-981e-4a7c-81f8-f78ce480d616"
title: "Django Framework Exceptions"
framework: "sigma"
generated: "true"
source_path: "rules/application/django/appframework_django_exceptions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/django/appframework_django_exceptions.yml"
build_date: "2026-04-26 14:14:24"
status: "stable"
level: "medium"
logsource: "django / application"
aliases:
  - "fd435618-981e-4a7c-81f8-f78ce480d616"
  - "Django Framework Exceptions"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Django Framework Exceptions

Detects suspicious Django web application framework exceptions that could indicate exploitation attempts

## Metadata

- Rule ID: fd435618-981e-4a7c-81f8-f78ce480d616
- Status: stable
- Level: medium
- Author: Thomas Patzke
- Date: 2017-08-05
- Modified: 2020-09-01
- Source Path: rules/application/django/appframework_django_exceptions.yml

## Logsource

- category: application
- product: django

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- SuspiciousOperation
- DisallowedHost
- DisallowedModelAdminLookup
- DisallowedModelAdminToField
- DisallowedRedirect
- InvalidSessionKey
- RequestDataTooBig
- SuspiciousFileOperation
- SuspiciousMultipartForm
- SuspiciousSession
- TooManyFieldsSent
- PermissionDenied
condition: keywords
```

## False Positives

- Application bugs

## References

- https://docs.djangoproject.com/en/1.11/ref/exceptions/
- https://docs.djangoproject.com/en/1.11/topics/logging/#django-security

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/django/appframework_django_exceptions.yml)
