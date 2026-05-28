# IOC Report — Phishing Campaign
**Date:** 28 May 2026
**Analyst:** Anant Deore
**Case:** TechCorp Password Reset Phishing

## IOC Table
| Type   | Value                                    | Verdict     |
|--------|------------------------------------------|-------------|
| Domain | techc0rp-helpdesk.com                    | Malicious   |
| Domain | techcorp-password-reset.suspicious-domain.xyz | Malicious |
| Email  | it-support@techc0rp-helpdesk.com         | Phishing    |
| URL    | http://techcorp-password-reset.suspicious-domain.xyz/reset?id=EMP001 | Credential Harvest |
| URL    | http://83.142.209.67/shcript.sh                  | Malicious   |
| Domain | microsoft.com                            | Clean ✅    |
| Domain | google.com                               | Clean ✅    |

## Attack Technique
Typosquatting: techc0rp (0 instead of o)
Mixed safe + malicious URLs to bypass filters

## Recommendations
- Block newly registered domains
- Implement DMARC/DKIM/SPF
- User awareness training