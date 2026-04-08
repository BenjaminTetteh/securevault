# 🔐 SecureVault

A DevSecOps portfolio project by Benjamin Tetteh.

SecureVault is a web-based secrets detection tool that scans text, config files,
and code snippets for exposed credentials — API keys, passwords, tokens, and more.

## Features
- Detects AWS keys, GitHub tokens, Slack tokens, passwords, and more
- Risk-rated findings (Critical / High / Medium)
- Built with Python Flask

## DevSecOps Pipeline
This project implements a full DevSecOps pipeline including:
- CI/CD with GitHub Actions
- SAST scanning with Bandit
- Dependency scanning with pip-audit
- Secrets scanning with Gitleaks
- Container scanning with Trivy
- DAST with OWASP ZAP
- Deployed on AWS