---
mitre_id: "T1584"
mitre_name: "Compromise Infrastructure"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7e3beebd-8bfe-4e7b-a892-e44ab06a75f9"
mitre_created: "2020-10-01T00:36:30.759Z"
mitre_modified: "2025-10-24T17:49:01.181Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1584/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0042"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing, or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle.(Citation: Mandiant APT1)(Citation: ICANNDomainNameHijacking)(Citation: Talos DNSpionage Nov 2018)(Citation: FireEye EPS Awakens Part 2) Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.

Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure can help adversary operations blend in with traffic that is seen as normal, such as contact with high reputation or trusted sites. For example, adversaries may leverage compromised infrastructure (potentially also in conjunction with [[T1588-obtain_capabilities#^t1588004-digital-certificates|T1588.004: Digital Certificates]]) to further blend in and support staged information gathering and/or [[T1566-phishing|T1566: Phishing]] campaigns.(Citation: FireEye DNS Hijack 2019) Adversaries may also compromise numerous machines to support [[T1090-proxy|T1090: Proxy]] and/or proxyware services or to form a botnet.(Citation: amnesty_nso_pegasus)(Citation: Sysdig Proxyjacking) Additionally, adversaries may compromise infrastructure residing in close proximity to a target in order to gain [[TA0001-initial_access|TA0001: Initial Access]] via [[T1669-wi-fi_networks|T1669: Wi-Fi Networks]].(Citation: Nearest Neighbor Volexity)

By using compromised infrastructure, adversaries may enable follow-on malicious operations. Prior to targeting, adversaries may also compromise the infrastructure of other adversaries.(Citation: NSA NCSC Turla OilRig)

## Workspace

- [[workspaces/attack/techniques/T1584-compromise_infrastructure-note|Open workspace note]]

![[workspaces/attack/techniques/T1584-compromise_infrastructure-note]]

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1584.001: Domains

^t1584001-domains

Adversaries may hijack domains and/or subdomains that can be used during targeting. Domain registration hijacking is the act of changing the registration of a domain name without the permission of the original registrant.(Citation: ICANNDomainNameHijacking) Adversaries may gain access to an email account for the person listed as the owner of the domain. The adversary can then claim that they forgot their password in order to make changes to the domain registration. Other possibilities include social engineering a domain registration help desk to gain access to an account, taking advantage of renewal process gaps, or compromising a cloud service that enables managing domains (e.g., AWS Route53).(Citation: Krebs DNS Hijack 2019)

Subdomain hijacking can occur when organizations have DNS entries that point to non-existent or deprovisioned resources. In such cases, an adversary may take control of a subdomain to conduct operations with the benefit of the trust associated with that domain.(Citation: Microsoft Sub Takeover 2020)

Adversaries who compromise a domain may also engage in domain shadowing by creating malicious subdomains under their control while keeping any existing DNS records. As service will not be disrupted, the malicious subdomains may go unnoticed for long periods of time.(Citation: Palo Alto Unit 42 Domain Shadowing 2022)

### T1584.002: DNS Server

^t1584002-dns-server

Adversaries may compromise third-party DNS servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]). Instead of setting up their own DNS servers, adversaries may compromise third-party DNS servers in support of operations.

By compromising DNS servers, adversaries can alter DNS records. Such control can allow for redirection of an organization's traffic, facilitating Collection and Credential Access efforts for the adversary.(Citation: Talos DNSpionage Nov 2018)(Citation: FireEye DNS Hijack 2019)  Additionally, adversaries may leverage such control in conjunction with [[T1588-obtain_capabilities#^t1588004-digital-certificates|T1588.004: Digital Certificates]] to redirect traffic to adversary-controlled infrastructure, mimicking normal trusted network communications.(Citation: FireEye DNS Hijack 2019)(Citation: Crowdstrike DNS Hijack 2019) Alternatively, they may be able to prove ownership of a domain to a SaaS service in order to assert control of the service or create a new administrative [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]].(Citation: CyberCX SaaS Domain Hijacking 2025) Adversaries may also be able to silently create subdomains pointed at malicious servers without tipping off the actual owner of the DNS server.(Citation: CiscoAngler)(Citation: Proofpoint Domain Shadowing)

### T1584.003: Virtual Private Server

^t1584003-virtual-private-server

Adversaries may compromise third-party Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety of cloud service providers that will sell virtual machines/containers as a service. Adversaries may compromise VPSs purchased by third-party entities. By compromising a VPS to use as infrastructure, adversaries can make it difficult to physically tie back operations to themselves.(Citation: NSA NCSC Turla OilRig)

Compromising a VPS for use in later stages of the adversary lifecycle, such as Command and Control, can allow adversaries to benefit from the ubiquity and trust associated with higher reputation cloud service providers as well as that added by the compromised third-party.

### T1584.004: Server

^t1584004-server

Adversaries may compromise third-party servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, including for Command and Control.(Citation: TrendMicro EarthLusca 2022) Instead of purchasing a [[T1583-acquire_infrastructure#^t1583004-server|T1583.004: Server]] or [[T1583-acquire_infrastructure#^t1583003-virtual-private-server|T1583.003: Virtual Private Server]], adversaries may compromise third-party servers in support of operations.

Adversaries may also compromise web servers to support watering hole operations, as in [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], or email servers to support [[T1566-phishing|T1566: Phishing]] operations.

### T1584.005: Botnet

^t1584005-botnet

Adversaries may compromise numerous third-party systems to form a botnet that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Instead of purchasing/renting a botnet from a booter/stresser service, adversaries may build their own botnet by compromising numerous third-party systems.(Citation: Imperva DDoS for Hire) Adversaries may also conduct a takeover of an existing botnet, such as redirecting bots to adversary-controlled C2 servers.(Citation: Dell Dridex Oct 2015) With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale [[T1566-phishing|T1566: Phishing]] or Distributed Denial of Service (DDoS).

### T1584.006: Web Services

^t1584006-web-services

Adversaries may compromise access to third-party web services that can be used during targeting. A variety of popular websites exist for legitimate users to register for web-based services, such as GitHub, Twitter, Dropbox, Google, SendGrid, etc. Adversaries may try to take ownership of a legitimate user's access to a web service and use that web service as infrastructure in support of cyber operations. Such web services can be abused during later stages of the adversary lifecycle, such as during Command and Control ([[T1102-web_service|T1102: Web Service]]), [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]], or [[T1566-phishing|T1566: Phishing]].(Citation: Recorded Future Turla Infra 2020) Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. By utilizing a web service, particularly when access is stolen from legitimate users, adversaries can make it difficult to physically tie back operations to them. Additionally, leveraging compromised web-based email services may allow adversaries to leverage the trust associated with legitimate domains.

### T1584.007: Serverless

^t1584007-serverless

Adversaries may compromise serverless cloud infrastructure, such as Cloudflare Workers, AWS Lambda functions, or Google Apps Scripts, that can be used during targeting. By utilizing serverless infrastructure, adversaries can make it more difficult to attribute infrastructure used during operations back to them. 

Once compromised, the serverless runtime environment can be leveraged to either respond directly to infected machines or to [[T1090-proxy|T1090: Proxy]] traffic to an adversary-owned command and control server.(Citation: BlackWater Malware Cloudflare Workers)(Citation: AWS Lambda Redirector)(Citation: GWS Apps Script Abuse 2021) As traffic generated by these functions will appear to come from subdomains of common cloud providers, it may be difficult to distinguish from ordinary traffic to these providers - making it easier to [[T1665-hide_infrastructure|T1665: Hide Infrastructure]].(Citation: Detecting Command & Control in the Cloud)(Citation: BlackWater Malware Cloudflare Workers)

### T1584.008: Network Devices

^t1584008-network-devices

Adversaries may compromise third-party network devices that can be used during targeting. Network devices, such as small office/home office (SOHO) routers, may be compromised where the adversary's ultimate goal is not [[TA0001-initial_access|TA0001: Initial Access]] to that environment, but rather to leverage these devices to support additional targeting.

Once an adversary has control, compromised network devices can be used to launch additional operations, such as hosting payloads for [[T1566-phishing|T1566: Phishing]] campaigns (i.e., [[T1608-stage_capabilities#^t1608005-link-target|T1608.005: Link Target]]) or enabling the required access to execute [[T1659-content_injection|T1659: Content Injection]] operations. Adversaries may also be able to harvest reusable credentials (i.e., [[T1078-valid_accounts|T1078: Valid Accounts]]) from compromised network devices.

Adversaries often target Internet-facing edge devices and related network appliances that specifically do not support robust host-based defenses.(Citation: Mandiant Fortinet Zero Day)(Citation: Wired Russia Cyberwar)

Compromised network devices may be used to support subsequent [[TA0011-command_and_control|TA0011: Command and Control]] activity, such as [[T1665-hide_infrastructure|T1665: Hide Infrastructure]] through an established [[T1090-proxy|T1090: Proxy]] and/or [[T1584-compromise_infrastructure#^t1584005-botnet|T1584.005: Botnet]] network.(Citation: Justice GRU 2024)

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

