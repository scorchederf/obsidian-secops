---
mitre_id: "M1057"
mitre_name: "Data Loss Prevention"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--65401701-019d-44ff-b223-08d520bb0e7b"
mitre_created: "2021-08-04T21:22:11.612Z"
mitre_modified: "2024-12-10T19:10:54.180Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1057/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# M1057: Data Loss Prevention

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. (Citation: PurpleSec Data Loss Prevention) This mitigation can be implemented through the following measures:

Sensitive Data Categorization:

- Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets).
- Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details.

Exfiltration Restrictions:

- Use Case: Prevent unauthorized transmission of sensitive data.
- Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage.

Data-in-Transit Monitoring:

- Use Case: Detect and prevent the transmission of sensitive data over unapproved channels.
- Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions.

Endpoint Data Protection:

- Use Case: Monitor and control sensitive data usage on endpoints.
- Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing.

Cloud Data Security:

- Use Case: Protect data stored in cloud platforms.
- Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

## Mitigates Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1020-automated_exfiltration|T1020: Automated Exfiltration]]
- [[T1020-automated_exfiltration#^t1020001-traffic-duplication|T1020.001: Traffic Duplication]]
- [[T1025-data_from_removable_media|T1025: Data from Removable Media]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1537-transfer_data_to_cloud_account|T1537: Transfer Data to Cloud Account]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1567-exfiltration_over_web_service#^t1567004-exfiltration-over-webhook|T1567.004: Exfiltration Over Webhook]]

