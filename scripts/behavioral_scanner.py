import sys
import re
import json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

suspicious_patterns = {
    "Reverse Shell": r"(nc|ncat|bash|sh)\s.*(\/dev\/tcp|exec|&)",
    "Obfuscated Vars": r"(eval|exec|compile)\s*\(",
    "Encoded Payload": r"base64\s*(--decode|-d)",
}

def scan_file(path):
    findings = []
    try:
        with open(path, "r") as f:
            content = f.read()
            for label, pattern in suspicious_patterns.items():
                matches = re.findall(pattern, content)
                if matches:
                    findings.append({"type": label, "matches": matches})
    except Exception as e:
        return {"error": str(e)}

    return findings

def analyze_with_gpt(code):
    prompt = f"Analyze the following code and explain any malicious behavior:\n\n{code[:2000]}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"GPT Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python behavioral_scanner.py <target_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    findings = scan_file(file_path)

    with open(file_path, "r") as f:
        code = f.read()

    gpt_result = analyze_with_gpt(code)

    output = {
        "file": file_path,
        "matches": findings,
        "gpt_analysis": gpt_result
    }

    print(json.dumps(output, indent=2))
