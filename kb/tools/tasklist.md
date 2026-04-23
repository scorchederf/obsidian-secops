---
mitre_id: "S0057"
mitre_name: "Tasklist"
mitre_type: "tool"
mitre_stix_id: "tool--2e45723a-31da-4a7e-aaa6-e01998a6788f"
mitre_created: "2017-05-31T21:32:39.233Z"
mitre_modified: "2024-02-12T19:14:37.984Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0057/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_aliases:
  - "Tasklist"
---

# Tasklist

The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist)

## Uses Techniques

- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1518-software_discovery|T1518: Software Discovery]]
- [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

