---
mitre_id: "M1029"
mitre_name: "Remote Data Storage"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--20a2baeb-98c2-4901-bad7-dc62d0a03dea"
mitre_created: "2019-06-06T21:21:13.027Z"
mitre_modified: "2024-12-18T19:03:10.800Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1029/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:

Centralized Log Management:

- Configure endpoints to forward security logs to a centralized log collector or SIEM.
- Use tools like Splunk Graylog, or Security Onion to aggregate and store logs.
- Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514`

Remote File Storage Solutions:

- Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data.
- Ensure proper encryption at rest and access control policies (IAM roles, ACLs).

Intrusion Detection Log Forwarding:

- Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system.
- Example for Suricata log forwarding:
`outputs:
  - type: syslog
    protocol: tls
    address: <remote-syslog-server>`

Immutable Backup Configurations:

- Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data.
- Example: AWS S3 Object Lock.

Data Encryption:

- Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit.
Tools: OpenSSL, BitLocker, LUKS for Linux.

## Workspace

- [[workspaces/attack/mitigations/M1029-remote_data_storage-note|Open workspace note]]

![[workspaces/attack/mitigations/M1029-remote_data_storage-note]]

## Mitigates Techniques

- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
    - [[T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]
    - [[T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]
    - [[T1070-indicator_removal#^t1070007-clear-network-connection-history-and-configurations|T1070.007: Clear Network Connection History and Configurations]]
    - [[T1070-indicator_removal#^t1070008-clear-mailbox-data|T1070.008: Clear Mailbox Data]]
    - [[T1070-indicator_removal#^t1070009-clear-persistence|T1070.009: Clear Persistence]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
    - [[T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]

