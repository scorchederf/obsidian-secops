---
id: S0633
name: Sliver
created: 2021-07-30 15:43:17.770000+00:00
modified: 2025-03-24 16:00:41.005000+00:00
type: tool
x_mitre_version: 2.0
x_mitre_domains: enterprise-attack
---

# Sliver

[Sliver](https://attack.mitre.org/software/S0633) is an open source, cross-platform, red team command and control (C2) framework written in Golang. [Sliver](https://attack.mitre.org/software/S0633) includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: Cybereason Sliver Undated)

## Uses Techniques

- [[T1001-data_obfuscation|T1001: Data Obfuscation]]
    - [[T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027004-compile-after-delivery|T1027.004: Compile After Delivery]]
    - [[T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
    - [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1132-data_encoding|T1132: Data Encoding]]
    - [[T1132-data_encoding#^t1132001-standard-encoding|T1132.001: Standard Encoding]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

