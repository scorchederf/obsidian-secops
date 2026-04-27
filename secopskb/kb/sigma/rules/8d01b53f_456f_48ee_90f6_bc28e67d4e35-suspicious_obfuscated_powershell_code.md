---
sigma_id: "8d01b53f-456f-48ee-90f6-bc28e67d4e35"
title: "Suspicious Obfuscated PowerShell Code"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_obfusc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_obfusc.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8d01b53f-456f-48ee-90f6-bc28e67d4e35"
  - "Suspicious Obfuscated PowerShell Code"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious UTF16 and base64 encoded and often obfuscated PowerShell code often used in command lines

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains:
  - IAAtAGIAeABvAHIAIAAwAHgA
  - AALQBiAHgAbwByACAAMAB4A
  - gAC0AYgB4AG8AcgAgADAAeA
  - AC4ASQBuAHYAbwBrAGUAKAApACAAfAAg
  - AuAEkAbgB2AG8AawBlACgAKQAgAHwAI
  - ALgBJAG4AdgBvAGsAZQAoACkAIAB8AC
  - AHsAMQB9AHsAMAB9ACIAIAAtAGYAI
  - B7ADEAfQB7ADAAfQAiACAALQBmAC
  - AewAxAH0AewAwAH0AIgAgAC0AZgAg
  - AHsAMAB9AHsAMwB9ACIAIAAtAGYAI
  - B7ADAAfQB7ADMAfQAiACAALQBmAC
  - AewAwAH0AewAzAH0AIgAgAC0AZgAg
  - AHsAMgB9AHsAMAB9ACIAIAAtAGYAI
  - B7ADIAfQB7ADAAfQAiACAALQBmAC
  - AewAyAH0AewAwAH0AIgAgAC0AZgAg
  - AHsAMQB9AHsAMAB9ACcAIAAtAGYAI
  - B7ADEAfQB7ADAAfQAnACAALQBmAC
  - AewAxAH0AewAwAH0AJwAgAC0AZgAg
  - AHsAMAB9AHsAMwB9ACcAIAAtAGYAI
  - B7ADAAfQB7ADMAfQAnACAALQBmAC
  - AewAwAH0AewAzAH0AJwAgAC0AZgAg
  - AHsAMgB9AHsAMAB9ACcAIAAtAGYAI
  - B7ADIAfQB7ADAAfQAnACAALQBmAC
  - AewAyAH0AewAwAH0AJwAgAC0AZgAg
condition: selection
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/fcadca91-3580-4ede-aff4-4d2bf809bf99/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_obfusc.yml)
