---
car_id: "CAR-2013-09-005"
title: "Service Outlier Executables"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-09-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-09-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-09-005"
  - "Service Outlier Executables"
attack_technique_ids:
  - "T1543"
  - "T1543.003"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Sigma"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2013-09-005: Service Outlier Executables

## Metadata

- CAR ID: CAR-2013-09-005
- Submission Date: 2013/09/23
- Information Domain: Host
- Analytic Type: Detection
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

New executables that are started as a service are suspicious. This analytic looks for anomalous service executables.

## ATT&CK Coverage

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Implementations

### pseudocode

Create a baseline of services seen over the last 30 days and a list of services seen today. Remove services in the baseline from services seen today, leaving a list of new services.

```pseudocode
processes = search Process:Create
services = filter processes where (parent_image_path == "C:\Windows\System32\services.exe")
historic_services = filter services (where timestamp < now - 1 day AND timestamp > now - 1 day)
current_services = filter services (where timestamp >= now - 1 day)
new_services = historic_services - current_services
output new_services
```

### Sigma

[Sigma/Windows Event Log](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_rare_service_installs.yml) rule with similar logic to the above pseudocode

### LogPoint

LogPoint version of the above sigma rule.

- Data Model: LogPoint native

```logpoint
norm_id=WinServer event_id=7045
| chart count() as cnt by file
| search cnt < 5
```

## Data Model References

- process/create/parent_image_path

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-09-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-09-005.yaml)
