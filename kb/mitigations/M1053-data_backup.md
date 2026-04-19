---
id: M1053
name: Data Backup
created: 2019-07-19 14:33:33.543000+00:00
modified: 2024-12-10 15:32:14.846000+00:00
type: course-of-action
---

# Data Backup

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

## Properties

- id: M1053
- name: Data Backup
- created: 2019-07-19 14:33:33.543000+00:00
- modified: 2024-12-10 15:32:14.846000+00:00
- type: course-of-action

## Mitigates Techniques

- [[T1485-data_destruction|T1485: Data Destruction]]
    - [[T1485-data_destruction#^t1485001-lifecycle-triggered-deletion|T1485.001: Lifecycle-Triggered Deletion]]
- [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1491-defacement|T1491: Defacement]]
    - [[T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]]
    - [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
    - [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
    - [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]

