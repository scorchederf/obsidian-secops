---
id: T1608
name: Stage Capabilities
created: 2021-03-17 20:04:09.331000+00:00
modified: 2025-10-24 17:49:03.444000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[resource_development|Resource Development]]

Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting. To support their operations, an adversary may need to take capabilities they developed ([Develop Capabilities](https://attack.mitre.org/techniques/T1587)) or obtained ([Obtain Capabilities](https://attack.mitre.org/techniques/T1588)) and stage them on infrastructure under their control. These capabilities may be staged on infrastructure that was previously purchased/rented by the adversary ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or was otherwise compromised by them ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)). Capabilities may also be staged on web services, such as GitHub or Pastebin, or on Platform-as-a-Service (PaaS) offerings that enable users to easily provision applications.(Citation: Volexity Ocean Lotus November 2020)(Citation: Dragos Heroku Watering Hole)(Citation: Malwarebytes Heroku Skimmers)(Citation: Netskope GCP Redirection)(Citation: Netskope Cloud Phishing)

Staging of capabilities can aid the adversary in a number of initial access and post-compromise behaviors, including (but not limited to):

* Staging web resources necessary to conduct [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) when a user browses to a site.(Citation: FireEye CFR Watering Hole 2012)(Citation: Gallagher 2015)(Citation: ATT ScanBox)
* Staging web resources for a link target to be used with spearphishing.(Citation: Malwarebytes Silent Librarian October 2020)(Citation: Proofpoint TA407 September 2019)
* Uploading malware or tools to a location accessible to a victim network to enable [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105).(Citation: Volexity Ocean Lotus November 2020)
* Installing a previously acquired SSL/TLS certificate to use to encrypt command and control traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)).(Citation: DigiCert Install SSL Cert)

## Subtechniques

### T1608.001: Upload Malware

^t1608001-upload-malware

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may upload malware to third-party or adversary controlled infrastructure to make it accessible during targeting. Malicious software can include payloads, droppers, post-compromise tools, backdoors, and a variety of other malicious content. Adversaries may upload malware to support their operations, such as making a payload available to a victim network to enable [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105) by placing it on an Internet accessible web server.

Malware may be placed on infrastructure that was previously purchased/rented by the adversary ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or was otherwise compromised by them ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)). Malware can also be staged on web services, such as GitHub or Pastebin; hosted on the InterPlanetary File System (IPFS), where decentralized content storage makes the removal of malicious files difficult; or saved on the blockchain as smart contracts, which are resilient against takedowns that would affect traditional infrastructure.(Citation: Volexity Ocean Lotus November 2020)(Citation: Talos IPFS 2022)(Citation: Guardio Etherhiding 2023)(Citation: Bleeping Computer Binance Smart Chain 2023)

Adversaries may upload backdoored files, such as software packages, application binaries, virtual machine images, or container images, to third-party software stores, package libraries, extension marketplaces, or repositories (ex: GitHub, CNET, AWS Community AMIs, Docker Hub, PyPi, NPM).(Citation: Datadog Security Labs Malicious PyPi Packages 2024) By chance encounter, victims may directly download/install these backdoored files via [User Execution](https://attack.mitre.org/techniques/T1204). Masquerading, including typo-squatting legitimate software, may increase the chance of users mistakenly executing these files. 

### T1608.002: Upload Tool

^t1608002-upload-tool

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may upload tools to third-party or adversary controlled infrastructure to make it accessible during targeting. Tools can be open or closed source, free or commercial. Tools can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). Adversaries may upload tools to support their operations, such as making a tool available to a victim network to enable [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105) by placing it on an Internet accessible web server.

Tools may be placed on infrastructure that was previously purchased/rented by the adversary ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or was otherwise compromised by them ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).(Citation: Dell TG-3390) Tools can also be staged on web services, such as an adversary controlled GitHub repo, or on Platform-as-a-Service offerings that enable users to easily provision applications.(Citation: Dragos Heroku Watering Hole)(Citation: Malwarebytes Heroku Skimmers)(Citation: Intezer App Service Phishing)

Adversaries can avoid the need to upload a tool by having compromised victim machines download the tool directly from a third-party hosting location (ex: a non-adversary controlled GitHub repo), including the original hosting site of the tool.

### T1608.003: Install Digital Certificate

^t1608003-install-digital-certificate

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may install SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are files that can be installed on servers to enable secure communications between systems. Digital certificates include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate securely with its owner. Certificates can be uploaded to a server, then the server can be configured to use the certificate to enable encrypted communication with it.(Citation: DigiCert Install SSL Cert)

Adversaries may install SSL/TLS certificates that can be used to further their operations, such as encrypting C2 traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)) or lending credibility to a credential harvesting site. Installation of digital certificates may take place for a number of server types, including web servers and email servers. 

Adversaries can obtain digital certificates (see [Digital Certificates](https://attack.mitre.org/techniques/T1588/004)) or create self-signed certificates (see [Digital Certificates](https://attack.mitre.org/techniques/T1587/003)). Digital certificates can then be installed on adversary controlled infrastructure that may have been acquired ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or previously compromised ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).

### T1608.004: Drive-by Target

^t1608004-drive-by-target

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may prepare an operational environment to infect systems that visit a website over the normal course of browsing. Endpoint systems may be compromised through browsing to adversary controlled sites, as in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189). In such cases, the user's web browser is typically targeted for exploitation (often not requiring any extra user interaction once landing on the site), but adversaries may also set up websites for non-exploitation behavior such as [Application Access Token](https://attack.mitre.org/techniques/T1550/001). Prior to [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), adversaries must stage resources needed to deliver that exploit to users who browse to an adversary controlled site. Drive-by content can be staged on adversary controlled infrastructure that has been acquired ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or previously compromised ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).

Adversaries may upload or inject malicious web content, such as [JavaScript](https://attack.mitre.org/techniques/T1059/007), into websites.(Citation: FireEye CFR Watering Hole 2012)(Citation: Gallagher 2015) This may be done in a number of ways, including:

* Inserting malicious scripts into web pages or other user controllable web content such as forum posts
* Modifying script files served to websites from publicly writeable cloud storage buckets
* Crafting malicious web advertisements and purchasing ad space on a website through legitimate ad providers (i.e., [Malvertising](https://attack.mitre.org/techniques/T1583/008))

In addition to staging content to exploit a user's web browser, adversaries may also stage scripting content to profile the user's browser (as in [Gather Victim Host Information](https://attack.mitre.org/techniques/T1592)) to ensure it is vulnerable prior to attempting exploitation.(Citation: ATT ScanBox)

Websites compromised by an adversary and used to stage a drive-by may be ones visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is referred to a strategic web compromise or watering hole attack.

Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure ([Domains](https://attack.mitre.org/techniques/T1583/001)) to help facilitate [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).

### T1608.005: Link Target

^t1608005-link-target

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may put in place resources that are referenced by a link that can be used during targeting. An adversary may rely upon a user clicking a malicious link in order to divulge information (including credentials) or to gain execution, as in [Malicious Link](https://attack.mitre.org/techniques/T1204/001). Links can be used for spearphishing, such as sending an email accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser. Prior to a phish for information (as in [Spearphishing Link](https://attack.mitre.org/techniques/T1598/003)) or a phish to gain initial access to a system (as in [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002)), an adversary must set up the resources for a link target for the spearphishing link. 

Typically, the resources for a link target will be an HTML page that may include some client-side script such as [JavaScript](https://attack.mitre.org/techniques/T1059/007) to decide what content to serve to the user. Adversaries may clone legitimate sites to serve as the link target, this can include cloning of login pages of legitimate web services or organization login pages in an effort to harvest credentials during [Spearphishing Link](https://attack.mitre.org/techniques/T1598/003).(Citation: Malwarebytes Silent Librarian October 2020)(Citation: Proofpoint TA407 September 2019) Adversaries may also [Upload Malware](https://attack.mitre.org/techniques/T1608/001) and have the link target point to malware for download/execution by the user.

Adversaries may purchase domains similar to legitimate domains (ex: homoglyphs, typosquatting, different top-level domain, etc.) during acquisition of infrastructure ([Domains](https://attack.mitre.org/techniques/T1583/001)) to help facilitate [Malicious Link](https://attack.mitre.org/techniques/T1204/001).

Links can be written by adversaries to mask the true destination in order to deceive victims by abusing the URL schema and increasing the effectiveness of phishing.(Citation: Kaspersky-masking)(Citation: mandiant-masking)

Adversaries may also use free or paid accounts on link shortening services and Platform-as-a-Service providers to host link targets while taking advantage of the widely trusted domains of those providers to avoid being blocked while redirecting victims to malicious pages.(Citation: Netskope GCP Redirection)(Citation: Netskope Cloud Phishing)(Citation: Intezer App Service Phishing)(Citation: Cofense-redirect) In addition, adversaries may serve a variety of malicious links through uniquely generated URIs/URLs (including one-time, single use links).(Citation: iOS URL Scheme)(Citation: URI)(Citation: URI Use)(Citation: URI Unique) Finally, adversaries may take advantage of the decentralized nature of the InterPlanetary File System (IPFS) to host link targets that are difficult to remove.(Citation: Talos IPFS 2022)

### T1608.006: SEO Poisoning

^t1608006-seo-poisoning

**Parent Technique**
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]

**Tactic**
- [[resource_development|Resource Development]]

Adversaries may poison mechanisms that influence search engine optimization (SEO) to further lure staged capabilities towards potential victims. Search engines typically display results to users based on purchased ads as well as the site’s ranking/score/reputation calculated by their web crawlers and algorithms.(Citation: Atlas SEO)(Citation: MalwareBytes SEO)

To help facilitate [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), adversaries may stage content that explicitly manipulates SEO rankings in order to promote sites hosting their malicious payloads (such as [Drive-by Target](https://attack.mitre.org/techniques/T1608/004)) within search engines. Poisoning SEO rankings may involve various tricks, such as stuffing keywords (including in the form of hidden text) into compromised sites. These keywords could be related to the interests/browsing habits of the intended victim(s) as well as more broad, seasonably popular topics (e.g. elections, trending news).(Citation: ZScaler SEO)(Citation: Atlas SEO)

In addition to internet search engines (such as Google), adversaries may also aim to manipulate specific in-site searches for developer platforms (such as GitHub) to deceive users towards [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) lures. In-site searches will rank search results according to their own algorithms and metrics such as popularity(Citation: Chexmarx-seo) which may be targeted and gamed by malicious actors.(Citation: Checkmarx-oss-seo)

Adversaries may also purchase or plant incoming links to staged capabilities in order to boost the site’s calculated relevance and reputation.(Citation: MalwareBytes SEO)(Citation: DFIR Report Gootloader)

SEO poisoning may also be combined with evasive redirects and other cloaking mechanisms (such as measuring mouse movements or serving content based on browser user agents, user language/localization settings, or HTTP headers) in order to feed SEO inputs while avoiding scrutiny from defenders.(Citation: ZScaler SEO)(Citation: Sophos Gootloader)

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

