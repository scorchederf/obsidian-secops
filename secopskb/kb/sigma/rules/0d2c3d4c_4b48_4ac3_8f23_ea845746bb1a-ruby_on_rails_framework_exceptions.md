---
sigma_id: "0d2c3d4c-4b48-4ac3-8f23-ea845746bb1a"
title: "Ruby on Rails Framework Exceptions"
framework: "sigma"
generated: "true"
source_path: "rules/application/ruby/appframework_ruby_on_rails_exceptions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/ruby/appframework_ruby_on_rails_exceptions.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "medium"
logsource: "ruby_on_rails / application"
aliases:
  - "0d2c3d4c-4b48-4ac3-8f23-ea845746bb1a"
  - "Ruby on Rails Framework Exceptions"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ruby on Rails Framework Exceptions

Detects suspicious Ruby on Rails exceptions that could indicate exploitation attempts

## Metadata

- Rule ID: 0d2c3d4c-4b48-4ac3-8f23-ea845746bb1a
- Status: stable
- Level: medium
- Author: Thomas Patzke
- Date: 2017-08-06
- Modified: 2020-09-01
- Source Path: rules/application/ruby/appframework_ruby_on_rails_exceptions.yml

## Logsource

- category: application
- product: ruby_on_rails

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- ActionController::InvalidAuthenticityToken
- ActionController::InvalidCrossOriginRequest
- ActionController::MethodNotAllowed
- ActionController::BadRequest
- ActionController::ParameterMissing
condition: keywords
```

## False Positives

- Application bugs

## References

- http://edgeguides.rubyonrails.org/security.html
- http://guides.rubyonrails.org/action_controller_overview.html
- https://stackoverflow.com/questions/25892194/does-rails-come-with-a-not-authorized-exception
- https://github.com/rails/rails/blob/cd08e6bcc4cd8948fe01e0be1ea0c7ca60373a25/actionpack/lib/action_dispatch/middleware/exception_wrapper.rb

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/ruby/appframework_ruby_on_rails_exceptions.yml)
