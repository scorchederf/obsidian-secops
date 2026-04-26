---
sigma_id: "ada3bc4f-f0fd-42b9-ba91-e105e8af7342"
title: "Server Side Template Injection Strings"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_ssti_in_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_ssti_in_access_logs.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "ada3bc4f-f0fd-42b9-ba91-e105e8af7342"
  - "Server Side Template Injection Strings"
attack_technique_ids:
  - "T1221"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Server Side Template Injection Strings

Detects SSTI attempts sent via GET requests in access logs

## Metadata

- Rule ID: ada3bc4f-f0fd-42b9-ba91-e105e8af7342
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-14
- Source Path: rules/web/webserver_generic/web_ssti_in_access_logs.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1221-template_injection|T1221]]

## Detection

```yaml
select_method:
  cs-method: GET
keywords:
- ={{
- =%7B%7B
- =${
- =$%7B
- =<%=
- =%3C%25=
- =@(
- freemarker.template.utility.Execute
- .getClass().forName('javax.script.ScriptEngineManager')
- T(org.apache.commons.io.IOUtils)
filter:
  sc-status: 404
condition: select_method and keywords and not filter
```

## False Positives

- User searches in search boxes of the respective website
- Internal vulnerability scanners can cause some serious FPs when used, if you experience a lot of FPs due to this think of adding more filters such as "User Agent" strings and more response codes

## References

- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://github.com/payloadbox/ssti-payloads

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_ssti_in_access_logs.yml)
