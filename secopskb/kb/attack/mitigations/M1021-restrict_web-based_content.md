---
mitre_id: "M1021"
mitre_name: "Restrict Web-Based Content"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--21da4fd4-27ad-4e9c-b93d-0b9b14d02c96"
mitre_created: "2019-06-06T20:52:59.206Z"
mitre_modified: "2024-12-24T13:40:41.043Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1021/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:

Deploy Web Proxy Filtering:

- Use solutions to filter web traffic based on categories, reputation, and content types.
- Enforce policies that block unsafe websites or file types at the gateway level.

Enable DNS-Based Filtering:

- Implement tools to restrict access to domains associated with malware or phishing campaigns.
- Use public DNS filtering services to enhance protection.

Enforce Content Security Policies (CSP):

- Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests.

Control Browser Features:

- Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting.
- Enforce policies through tools like Group Policy Management to control browser settings.

Monitor and Alert on Web-Based Threats:

- Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity.
- Configure alerts for access attempts to blocked domains or repeated file download failures.

## Workspace

- [[notes/attack/mitigations/M1021-restrict_web-based_content-note|Open workspace note]]

![[notes/attack/mitigations/M1021-restrict_web-based_content-note]]

## Mitigates Techniques

- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1102-web_service|T1102: Web Service]]
    - [[T1102-web_service#^t1102001-dead-drop-resolver|T1102.001: Dead Drop Resolver]]
    - [[T1102-web_service#^t1102002-bidirectional-communication|T1102.002: Bidirectional Communication]]
    - [[T1102-web_service#^t1102003-one-way-communication|T1102.003: One-Way Communication]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127002-clickonce|T1127.002: ClickOnce]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
    - [[T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218001-compiled-html-file|T1218.001: Compiled HTML File]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
    - [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
    - [[T1567-exfiltration_over_web_service#^t1567001-exfiltration-to-code-repository|T1567.001: Exfiltration to Code Repository]]
    - [[T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]]
    - [[T1567-exfiltration_over_web_service#^t1567003-exfiltration-to-text-storage-sites|T1567.003: Exfiltration to Text Storage Sites]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
    - [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1659-content_injection|T1659: Content Injection]]

