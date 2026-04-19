---
id: M1041
name: Encrypt Sensitive Information
created: 2019-06-11 16:43:44.834000+00:00
modified: 2025-04-02 17:28:57.029000+00:00
type: course-of-action
---

# Encrypt Sensitive Information

Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:

Encrypt Data at Rest:

- Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices.
- Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives.

Encrypt Data in Transit:

- Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks.
- Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption.

Encrypt Backups:

- Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access.
- Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud.

Encrypt Application Secrets:

- Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults.
- Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets.

Database Encryption:

- Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems.
- Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security numbers.

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
- [[T1020-automated_exfiltration|T1020: Automated Exfiltration]]
    - [[T1020-automated_exfiltration#^t1020001-traffic-duplication|T1020.001: Traffic Duplication]]
- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
    - [[T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
    - [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
    - [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213006-databases|T1213.006: Databases]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
    - [[T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]
    - [[T1565-data_manipulation#^t1565002-transmitted-data-manipulation|T1565.002: Transmitted Data Manipulation]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]
- [[T1659-content_injection|T1659: Content Injection]]
- [[T1669-wi-fi_networks|T1669: Wi-Fi Networks]]

