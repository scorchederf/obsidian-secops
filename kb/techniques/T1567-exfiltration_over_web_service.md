---
id: T1567
name: Exfiltration Over Web Service
created: 2020-03-09 12:51:45.570000+00:00
modified: 2025-10-24 17:48:42.061000+00:00
type: attack-pattern
x_mitre_version: 1.5
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Properties

- id: T1567
- name: Exfiltration Over Web Service
- created: 2020-03-09 12:51:45.570000+00:00
- modified: 2025-10-24 17:48:42.061000+00:00
- type: attack-pattern
- x_mitre_version: 1.5
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1567.001: Exfiltration to Code Repository

^t1567001-exfiltration-to-code-repository

**Parent Technique**
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

Exfiltration to a code repository can also provide a significant amount of cover to the adversary if it is a popular service already used by hosts within the network. 

#### Properties

- id: T1567.001
- name: Exfiltration to Code Repository
- created: 2020-03-09 14:51:11.772000+00:00
- modified: 2025-10-24 17:49:04.207000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1567.002: Exfiltration to Cloud Storage

^t1567002-exfiltration-to-cloud-storage

**Parent Technique**
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

Examples of cloud storage services include Dropbox and Google Docs. Exfiltration to these cloud storage services can provide a significant amount of cover to the adversary if hosts within the network are already communicating with the service. 

#### Properties

- id: T1567.002
- name: Exfiltration to Cloud Storage
- created: 2020-03-09 15:04:32.767000+00:00
- modified: 2025-10-24 17:49:19.048000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

### T1567.003: Exfiltration to Text Storage Sites

^t1567003-exfiltration-to-text-storage-sites

**Parent Technique**
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as <code>pastebin[.]com</code>, are commonly used by developers to share code and other information.  

Text storage sites are often used to host malicious code for C2 communication (e.g., [Stage Capabilities](https://attack.mitre.org/techniques/T1608)), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely.(Citation: Pastebin EchoSec)

**Note:** This is distinct from [Exfiltration to Code Repository](https://attack.mitre.org/techniques/T1567/001), which highlight access to code repositories via APIs.

#### Properties

- id: T1567.003
- name: Exfiltration to Text Storage Sites
- created: 2023-02-27 22:51:27.101000+00:00
- modified: 2025-04-15 19:59:01.716000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1567.004: Exfiltration Over Webhook

^t1567004-exfiltration-over-webhook

**Parent Technique**
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control channel. Webhooks are simple mechanisms for allowing a server to push data over HTTP/S to a client without the need for the client to continuously poll the server.(Citation: RedHat Webhooks) Many public and commercial services, such as Discord, Slack, and `webhook.site`, support the creation of webhook endpoints that can be used by other services, such as Github, Jira, or Trello.(Citation: Discord Intro to Webhooks) When changes happen in the linked services (such as pushing a repository update or modifying a ticket), these services will automatically post the data to the webhook endpoint for use by the consuming application. 

Adversaries may link an adversary-owned environment to a victim-owned SaaS service to achieve repeated [Automated Exfiltration](https://attack.mitre.org/techniques/T1020) of emails, chat messages, and other data.(Citation: Push Security SaaS Attacks Repository Webhooks) Alternatively, instead of linking the webhook endpoint to a service, an adversary can manually post staged data directly to the URL in order to exfiltrate it.(Citation: Microsoft SQL Server)

Access to webhook endpoints is often over HTTPS, which gives the adversary an additional level of protection. Exfiltration leveraging webhooks can also blend in with normal network traffic if the webhook endpoint points to a commonly used SaaS application or collaboration service.(Citation: CyberArk Labs Discord)(Citation: Talos Discord Webhook Abuse)(Citation: Checkmarx Webhooks)

#### Properties

- id: T1567.004
- name: Exfiltration Over Webhook
- created: 2023-07-20 15:30:55.763000+00:00
- modified: 2025-04-15 19:58:26.901000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Office Suite
- SaaS
- Windows

## Tools

- [[S0508-ngrok|S0508: ngrok]]

