import re, json, os, subprocess
import whois
from shodan import Shodan
from virustotal_python import Virustotal

VT_KEY = os.getenv("VIRUSTOTAL_API_KEY")
SHODAN_KEY = os.getenv("SHODAN_API_KEY")
vtotal = Virustotal(API_KEY=VT_KEY)
shodan_api = Shodan(SHODAN_KEY)

def extract_iocs(content):
    domains = re.findall(r'https?://([a-zA-Z0-9.-]+\.[a-z]{2,})', content)
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)
    return list(set(domains)), list(set(ips))

def vt_lookup(domain):
    try:
        resp = vtotal.domain_report(domain)
        return {"category": resp.data.get("attributes", {}).get("categories", {})}
    except Exception as e:
        return {"error": str(e)}

def shodan_lookup(ip):
    try:
        return shodan_api.host(ip)
    except Exception as e:
        return {"error": str(e)}

def run():
    with open("dangerfile.js", "r") as f:
        content = f.read()

    domains, ips = extract_iocs(content)
    report = {"domains": {}, "ips": {}}

    for d in domains:
        report["domains"][d] = vt_lookup(d)

    for ip in ips:
        report["ips"][ip] = {
            "whois": whois.whois(ip).text,
            "shodan": shodan_lookup(ip)
        }

    with open("threat_report.json", "w") as out:
        json.dump(report, out, indent=2)

if __name__ == "__main__":
    run()
