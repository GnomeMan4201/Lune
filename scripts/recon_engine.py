import os, requests, whois, json
from fpdf import FPDF
from shodan import Shodan
from virus_total_apis import PublicApi as VirusTotalPublicApi

def enrich_url(url):
    try:
        w = whois.whois(url)
        return {"domain": url, "registrar": w.registrar, "creation_date": str(w.creation_date)}
    except Exception as e:
        return {"error": str(e)}

def enrich_ip(ip, shodan_key):
    api = Shodan(shodan_key)
    try:
        result = api.host(ip)
        return {
            "ip": ip,
            "org": result.get("org"),
            "os": result.get("os"),
            "ports": result.get("ports")
        }
    except Exception as e:
        return {"error": str(e)}

def enrich_hash(file_hash, vt_key):
    vt = VirusTotalPublicApi(vt_key)
    resp = vt.get_file_report(file_hash)
    return resp.get("results", {})

def generate_pdf_report(data, output_path="docs/intel/recon_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for section, details in data.items():
        pdf.cell(200, 10, txt=section.upper(), ln=True)
        for k, v in details.items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
        pdf.cell(200, 10, ln=True)
    pdf.output(output_path)

# Example usage (testing)
if __name__ == "__main__":
    VT_KEY = os.getenv("VIRUSTOTAL_API_KEY")
    SHODAN_KEY = os.getenv("SHODAN_API_KEY")
    results = {
        "url": enrich_url("example.com"),
        "ip": enrich_ip("8.8.8.8", SHODAN_KEY),
        "hash": enrich_hash("44d88612fea8a8f36de82e1278abb02f", VT_KEY)
    }
    Path("docs/intel").mkdir(parents=True, exist_ok=True)
    generate_pdf_report(results)