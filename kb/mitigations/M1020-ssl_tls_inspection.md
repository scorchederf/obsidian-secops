---
id: M1020
name: SSL/TLS Inspection
created: 2019-06-06 20:15:34.146000+00:00
modified: 2024-12-24 13:46:05.302000+00:00
type: course-of-action
---

# SSL/TLS Inspection

SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures:

Deploy SSL/TLS Inspection Appliances:

- Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic.
- Ensure appliances are placed at critical network choke points for maximum coverage.

Configure Decryption Policies:

- Define rules to decrypt traffic for specific applications, ports, or domains.
- Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations.

Integrate Threat Intelligence:

- Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs).

Integrate with Security Tools:

- Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity.
- Example Tools: Splunk, Darktrace

Implement Certificate Management:

- Use trusted internal or third-party certificates for traffic re-encryption after inspection.
- Regularly update certificate authorities (CAs) to ensure secure re-encryption.

Monitor and Tune:

- Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.

## Mitigates Techniques

- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090004-domain-fronting|T1090.004: Domain Fronting]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

