from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Secret patterns to detect
PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws_secret_access_key\s*=\s*['\"]?[A-Za-z0-9/+=]{40}['\"]?",
    "Generic API Key": r"(?i)(api_key|apikey)\s*=\s*['\"]?[A-Za-z0-9]{16,}['\"]?",
    "Generic Password": r"(?i)(password|passwd|pwd)\s*=\s*['\"]?.{6,}['\"]?",
    "Private Key Header": r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9\-]{10,}",
    "Generic Secret": r"(?i)(secret|token)\s*=\s*['\"]?[A-Za-z0-9]{8,}['\"]?",
}

RISK_LEVELS = {
    "AWS Access Key": "🔴 Critical",
    "AWS Secret Key": "🔴 Critical",
    "Private Key Header": "🔴 Critical",
    "GitHub Token": "🔴 Critical",
    "Slack Token": "🟠 High",
    "Generic API Key": "🟠 High",
    "Generic Password": "🟡 Medium",
    "Generic Secret": "🟡 Medium",
}

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    scanned = False
    if request.method == "POST":
        text = request.form.get("text", "")
        scanned = True
        for name, pattern in PATTERNS.items():
            matches = re.findall(pattern, text)
            if matches:
                results.append({
                    "type": name,
                    "risk": RISK_LEVELS.get(name, "🟡 Medium"),
                    "count": len(matches)
                })
    return render_template("index.html", results=results, scanned=scanned)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # nosec B104 - required for Docker networking
    
    