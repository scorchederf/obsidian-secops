---
mitre_id: "T1583"
mitre_name: "Acquire Infrastructure"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0458aab9-ad42-4eac-9e22-706a95bafee2"
mitre_created: "2020-09-30T16:37:40.271Z"
mitre_modified: "2025-10-24T17:48:20.468Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1583/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services.(Citation: TrendmicroHideoutsLease) Some infrastructure providers offer free trial periods, enabling infrastructure acquisition at limited to no cost.(Citation: Free Trial PurpleUrchin) Additionally, botnets are available for rent or purchase.

Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure to support [[T1090-proxy|T1090: Proxy]], including from residential proxy services.(Citation: amnesty_nso_pegasus)(Citation: FBI Proxies Credential Stuffing)(Citation: Mandiant APT29 Microsoft 365 2022) Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

## Workspace

- [[workspaces/attack/techniques/T1583-acquire_infrastructure-note|Open workspace note]]

![[workspaces/attack/techniques/T1583-acquire_infrastructure-note]]

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1583.001: Domains

^t1583001-domains

Adversaries may acquire domains that can be used during targeting. Domain names are the human readable names used to represent one or more IP addresses. They can be purchased or, in some cases, acquired for free.

Adversaries may use acquired domains for a variety of purposes, including for [[T1566-phishing|T1566: Phishing]], [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], and Command and Control.(Citation: CISA MSS Sep 2020) Adversaries may choose domains that are similar to legitimate domains, including through use of homoglyphs or use of a different top-level domain (TLD).(Citation: FireEye APT28)(Citation: PaypalScam) Typosquatting may be used to aid in delivery of payloads via [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]. Adversaries may also use internationalized domain names (IDNs) and different character sets (e.g. Cyrillic, Greek, etc.) to execute "IDN homograph attacks," creating visually similar lookalike domains used to deliver malware to victim machines.(Citation: CISA IDN ST05-016)(Citation: tt_httrack_fake_domains)(Citation: tt_obliqueRAT)(Citation: httrack_unhcr)(Citation: lazgroup_idn_phishing)

Different URIs/URLs may also be dynamically generated to uniquely serve malicious content to victims (including one-time, single use domain names).(Citation: iOS URL Scheme)(Citation: URI)(Citation: URI Use)(Citation: URI Unique)

Adversaries may also acquire and repurpose expired domains, which may be potentially already allowlisted/trusted by defenders based on an existing reputation/history.(Citation: Categorisation_not_boundary)(Citation: Domain_Steal_CC)(Citation: Redirectors_Domain_Fronting)(Citation: bypass_webproxy_filtering)

Domain registrars each maintain a publicly viewable database that displays contact information for every registered domain. Private WHOIS services display alternative information, such as their own company data, rather than the owner of the domain. Adversaries may use such private WHOIS services to obscure information about who owns a purchased domain. Adversaries may further interrupt efforts to track their infrastructure by using varied registration information and purchasing domains with different domain registrars.(Citation: Mandiant APT1)

In addition to legitimately purchasing a domain, an adversary may register a new domain in a compromised environment. For example, in AWS environments, adversaries may leverage the Route53 domain service to register a domain and create hosted zones pointing to resources of the threat actor’s choosing.(Citation: Invictus IR DangerDev 2024)

### T1583.002: DNS Server

^t1583002-dns-server

Adversaries may set up their own Domain Name System (DNS) servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]). Instead of hijacking existing DNS servers, adversaries may opt to configure and run their own DNS servers in support of operations.

By running their own DNS servers, adversaries can have more control over how they administer server-side DNS C2 traffic ([[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]). With control over a DNS server, adversaries can configure DNS applications to provide conditional responses to malware and, generally, have more flexibility in the structure of the DNS-based C2 channel.(Citation: Unit42 DNS Mar 2019)

### T1583.003: Virtual Private Server

^t1583003-virtual-private-server

Adversaries may rent Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety of cloud service providers that will sell virtual machines/containers as a service. By utilizing a VPS, adversaries can make it difficult to physically tie back operations to them. The use of cloud infrastructure can also make it easier for adversaries to rapidly provision, modify, and shut down their infrastructure.

Acquiring a VPS for use in later stages of the adversary lifecycle, such as Command and Control, can allow adversaries to benefit from the ubiquity and trust associated with higher reputation cloud service providers. Adversaries may also acquire infrastructure from VPS service providers that are known for renting VPSs with minimal registration information, allowing for more anonymous acquisitions of infrastructure.(Citation: TrendmicroHideoutsLease)

### T1583.004: Server

^t1583004-server

Adversaries may buy, lease, rent, or obtain physical servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, such as watering hole operations in [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], enabling [[T1566-phishing|T1566: Phishing]] operations, or facilitating [[TA0011-command_and_control|TA0011: Command and Control]]. Instead of compromising a third-party [[T1584-compromise_infrastructure#^t1584004-server|T1584.004: Server]] or renting a [[T1583-acquire_infrastructure#^t1583003-virtual-private-server|T1583.003: Virtual Private Server]], adversaries may opt to configure and run their own servers in support of operations. Free trial periods of cloud servers may also be abused.(Citation: Free Trial PurpleUrchin)(Citation: Freejacked) 

Adversaries may only need a lightweight setup if most of their activities will take place using online infrastructure. Or, they may need to build extensive infrastructure if they want to test, communicate, and control other aspects of their activities on their own systems.(Citation: NYTStuxnet)

### T1583.005: Botnet

^t1583005-botnet

Adversaries may buy, lease, or rent a network of compromised systems that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Adversaries may purchase a subscription to use an existing botnet from a booter/stresser service. 

Internet-facing edge devices and related network appliances that are end-of-life (EOL) and unsupported by their manufacturers are commonly acquired for botnet activities. Adversaries may lease operational relay box (ORB) networks – consisting of virtual private servers (VPS), small office/home office (SOHO) routers, or Internet of Things (IoT) devices – to serve as a botnet.(Citation: ORB Mandiant) 

With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale [[T1566-phishing|T1566: Phishing]] or Distributed Denial of Service (DDoS).(Citation: Imperva DDoS for Hire)(Citation: Krebs-Anna)(Citation: Krebs-Bazaar)(Citation: Krebs-Booter) Acquired botnets may also be used to support Command and Control activity, such as [[T1665-hide_infrastructure|T1665: Hide Infrastructure]] through an established [[T1090-proxy|T1090: Proxy]] network.



### T1583.006: Web Services

^t1583006-web-services

Adversaries may register for web services that can be used during targeting. A variety of popular websites exist for adversaries to register for a web-based service that can be abused during later stages of the adversary lifecycle, such as during Command and Control ([[T1102-web_service|T1102: Web Service]]), [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]], or [[T1566-phishing|T1566: Phishing]]. Using common services, such as those offered by Google, GitHub, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: FireEye APT29)(Citation: Hacker News GitHub Abuse 2024) By utilizing a web service, adversaries can make it difficult to physically tie back operations to them.

### T1583.007: Serverless

^t1583007-serverless

Adversaries may purchase and configure serverless cloud infrastructure, such as Cloudflare Workers, AWS Lambda functions, or Google Apps Scripts, that can be used during targeting. By utilizing serverless infrastructure, adversaries can make it more difficult to attribute infrastructure used during operations back to them.

Once acquired, the serverless runtime environment can be leveraged to either respond directly to infected machines or to [[T1090-proxy|T1090: Proxy]] traffic to an adversary-owned command and control server.(Citation: BlackWater Malware Cloudflare Workers)(Citation: AWS Lambda Redirector)(Citation: GWS Apps Script Abuse 2021) As traffic generated by these functions will appear to come from subdomains of common cloud providers, it may be difficult to distinguish from ordinary traffic to these providers - making it easier to [[T1665-hide_infrastructure|T1665: Hide Infrastructure]].(Citation: Detecting Command & Control in the Cloud)(Citation: BlackWater Malware Cloudflare Workers)

### T1583.008: Malvertising

^t1583008-malvertising

Adversaries may purchase online advertisements that can be abused to distribute malware to victims. Ads can be purchased to plant as well as favorably position artifacts in specific locations  online, such as prominently placed within search engine results. These ads may make it more difficult for users to distinguish between actual search results and advertisements.(Citation: spamhaus-malvertising) Purchased ads may also target specific audiences using the advertising network’s capabilities, potentially further taking advantage of the trust inherently given to search engines and popular websites. 

Adversaries may purchase ads and other resources to help distribute artifacts containing malicious code to victims. Purchased ads may attempt to impersonate or spoof well-known brands. For example, these spoofed ads may trick victims into clicking the ad which could then send them to a malicious domain that may be a clone of official websites containing trojanized versions of the advertised software.(Citation: Masquerads-Guardio)(Citation: FBI-search) Adversary’s efforts to create malicious domains and purchase advertisements may also be automated at scale to better resist cleanup efforts.(Citation: sentinelone-malvertising) 

Malvertising may be used to support [[T1608-stage_capabilities#^t1608004-drive-by-target|T1608.004: Drive-by Target]] and [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], potentially requiring limited interaction from the user if the ad contains code/exploits that infect the target system's web browser.(Citation: BBC-malvertising)

Adversaries may also employ several techniques to evade detection by the advertising network. For example, adversaries may dynamically route ad clicks to send automated crawler/policy enforcer traffic to benign sites while validating potential targets then sending victims referred from real ad clicks to malicious pages. This infection vector may therefore remain hidden from the ad network as well as any visitor not reaching the malicious sites with a valid identifier from clicking on the advertisement.(Citation: Masquerads-Guardio) Other tricks, such as intentional typos to avoid brand reputation monitoring, may also be used to evade automated detection.(Citation: spamhaus-malvertising) 

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

