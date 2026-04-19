---
id: M1029
name: Remote Data Storage
created: 2019-06-06 21:21:13.027000+00:00
modified: 2024-12-18 19:03:10.800000+00:00
type: course-of-action
---

# Remote Data Storage

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

## Mitigates Techniques

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
    - [[T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]

