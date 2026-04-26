---
mitre_id: "M1053"
mitre_name: "Data Backup"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--3efe43d1-6f3f-4fcb-ab39-4a730971f70b"
mitre_created: "2019-07-19T14:33:33.543Z"
mitre_modified: "2024-12-10T15:32:14.846Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1053/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures:

Regular Backup Scheduling:
- Use Case: Ensure timely and consistent backups of critical data.
- Implementation: Schedule daily incremental backups and weekly full backups for all critical servers and systems.

Immutable Backups:
- Use Case: Protect backups from modification or deletion, even by attackers.
- Implementation: Use write-once-read-many (WORM) storage for backups, preventing ransomware from encrypting or deleting backup files.

Backup Encryption:
- Use Case: Protect data integrity and confidentiality during transit and storage.
- Implementation: Encrypt backups using strong encryption protocols (e.g., AES-256) before storing them in local, cloud, or remote locations.

Offsite Backup Storage:
- Use Case: Ensure data availability during physical disasters or onsite breaches.
- Implementation: Use cloud-based solutions like AWS S3, Azure Backup, or physical offsite storage to maintain a copy of critical data.

Backup Testing:
- Use Case: Validate backup integrity and ensure recoverability.
- Implementation: Regularly test data restoration processes to ensure that backups are not corrupted and can be recovered quickly.

## Workspace

- [[workspaces/attack/mitigations/M1053-data_backup-note|Open workspace note]]

![[workspaces/attack/mitigations/M1053-data_backup-note]]

## Mitigates Techniques

- [[T1485-data_destruction|T1485: Data Destruction]]
- [[T1485-data_destruction|T1485: Data Destruction]]
    - [[T1485-data_destruction#^t1485001-lifecycle-triggered-deletion|T1485.001: Lifecycle-Triggered Deletion]]
- [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1491-defacement|T1491: Defacement]]
- [[T1491-defacement|T1491: Defacement]]
    - [[T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]]
    - [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
    - [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
    - [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]

