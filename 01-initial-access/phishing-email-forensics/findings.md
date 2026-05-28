# Chapter 1: Phishing Email Forensics
## Incident: TechCorp Password Reset Phishing

## Summary
A phishing email impersonating TechCorp IT
Support was received by employee@techcorp.com
attempting to steal credentials via fake
password reset page.

## Header Analysis
| Field | Value | Verdict |
|-------|-------|---------|
| From | techc0rp-helpdesk.com | FAKE - typosquat |
| SPF | FAIL | Not authorized ❌ |
| DKIM | FAIL | Not signed ❌ |

## URLs Found
| URL | Type | VirusTotal | Verdict |
|-----|------|------------|---------|
| techcorp-password-reset.xyz | Credential harvest | Suspicious | 🚨 |
| http://83.142.209.67/shcript.sh | Malware delivery | XX/90 engines | ☠️ Malicious |
| microsoft.com | Legitimacy decoy | Clean | ✅ Safe |
| google.com | Legitimacy decoy | Clean | ✅ Safe |

## Attacker Technique
Mixing safe + malicious URLs is a common
technique to bypass email filters ✅

## MITRE ATT&CK
T1566.001 - Phishing: Spearphishing Link
T1598.003 - Phishing for Information

## Screenshots
- screenshot-script-output.png
- screenshot-virustotal1.png
- screenshot-virustotal2.png
- screenshot-virustotal3.png
- screenshot-virustotal4.png
- screenshot-mxtoolbox.png

## Recommendations
1. Implement DMARC policy
2. Block newly registered domains
3. User awareness training