import email
import re
import sys

def analyze_email(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)
    
    print("=" * 50)
    print("PHISHING EMAIL ANALYSIS REPORT")
    print("=" * 50)
    print(f"From:        {msg['From']}")
    print(f"To:          {msg['To']}")
    print(f"Subject:     {msg['Subject']}")
    print(f"Reply-To:    {msg['Reply-To']}")
    print(f"Return-Path: {msg['Return-Path']}")
    print(f"Date:        {msg['Date']}")
    print()
    
    # Extract URLs from body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += str(part.get_payload(decode=True))
    else:
        body = str(msg.get_payload(decode=True))
    
    urls = re.findall(r'https?://[^\s<>"]+', body)
    print(f"URLs Found:")
    for url in urls:
        print(f"  → {url}")
    
    print()
    print("Next Steps:")
    print("1. Check sender IP on abuseipdb.com")
    print("2. Submit URLs to virustotal.com")
    print("3. Check SPF/DKIM at mxtoolbox.com")

analyze_email('evidence/emails/phishing-sample.eml')