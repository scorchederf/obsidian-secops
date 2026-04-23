---
mitre_id: "T1567"
mitre_name: "Exfiltration Over Web Service"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--40597f16-0963-4249-bf4c-ac93b7fb9807"
mitre_created: "2020-03-09T12:51:45.570Z"
mitre_modified: "2025-10-24T17:48:42.061Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1567/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
---

# T1567: Exfiltration Over Web Service

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Subtechniques

### T1567.001: Exfiltration to Code Repository

^t1567001-exfiltration-to-code-repository

Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

Exfiltration to a code repository can also provide a significant amount of cover to the adversary if it is a popular service already used by hosts within the network. 

### T1567.002: Exfiltration to Cloud Storage

^t1567002-exfiltration-to-cloud-storage

Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

Examples of cloud storage services include Dropbox and Google Docs. Exfiltration to these cloud storage services can provide a significant amount of cover to the adversary if hosts within the network are already communicating with the service. 

### T1567.003: Exfiltration to Text Storage Sites

^t1567003-exfiltration-to-text-storage-sites

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as `pastebin[.]com`, are commonly used by developers to share code and other information.  

Text storage sites are often used to host malicious code for C2 communication (e.g., [[T1608-stage_capabilities|T1608: Stage Capabilities]]), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely.(Citation: Pastebin EchoSec)

**Note:** This is distinct from [[T1567-exfiltration_over_web_service#^t1567001-exfiltration-to-code-repository|T1567.001: Exfiltration to Code Repository]], which highlight access to code repositories via APIs.

### T1567.004: Exfiltration Over Webhook

^t1567004-exfiltration-over-webhook

Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control channel. Webhooks are simple mechanisms for allowing a server to push data over HTTP/S to a client without the need for the client to continuously poll the server.(Citation: RedHat Webhooks) Many public and commercial services, such as Discord, Slack, and `webhook.site`, support the creation of webhook endpoints that can be used by other services, such as Github, Jira, or Trello.(Citation: Discord Intro to Webhooks) When changes happen in the linked services (such as pushing a repository update or modifying a ticket), these services will automatically post the data to the webhook endpoint for use by the consuming application. 

Adversaries may link an adversary-owned environment to a victim-owned SaaS service to achieve repeated [[T1020-automated_exfiltration|T1020: Automated Exfiltration]] of emails, chat messages, and other data.(Citation: Push Security SaaS Attacks Repository Webhooks) Alternatively, instead of linking the webhook endpoint to a service, an adversary can manually post staged data directly to the URL in order to exfiltrate it.(Citation: Microsoft SQL Server)

Access to webhook endpoints is often over HTTPS, which gives the adversary an additional level of protection. Exfiltration leveraging webhooks can also blend in with normal network traffic if the webhook endpoint points to a commonly used SaaS application or collaboration service.(Citation: CyberArk Labs Discord)(Citation: Talos Discord Webhook Abuse)(Citation: Checkmarx Webhooks)

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools

- [[ngrok|ngrok]]

## Platforms

- ESXi
- Linux
- macOS
- Office Suite
- SaaS
- Windows

