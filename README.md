# 🧪 vuln-code-lab

A curated collection of intentionally vulnerable code snippets and mini web apps for demonstrating common web application security vulnerabilities. Each example includes a vulnerable version and, where applicable, a secure variant for comparison.

> ⚠️ **Warning:** This code is intentionally vulnerable. Run only in isolated environments for educational or testing purposes.


## 🔍 Included Vulnerabilities

| Vulnerability          | Folder                | Description                                        |
|------------------------|-----------------------|----------------------------------------------------|
| Clickjacking           | /ui-redressing         | Iframe-based UI redressing without protection      |
| Command Injection      | /command-injection    | Shell commands built from user input               |
| XML External Entity    | /xxe                  | XML parsers resolving external entities            |
| Path Traversal         | /path-traversal       | Files accessed via ../ in user input               |
| Insecure Deserialization | /insecure_deserialization         | Python pickle abuse leading to RCE                 |


## 📦 Requirements

- Python 3.7 or higher
  - Flask
  - (Optional) lxml, defusedxml for XXE-related examples
- PHP 7.0 or higher (for command injection and file upload demos)
- Go 1.18 or higher (for path traversal and other backend-related PoCs)


## 🛡️ Disclaimer

This project is for educational purposes only. Do not deploy this code to production systems. All examples are designed to demonstrate how vulnerabilities work so developers and security professionals can better understand and defend against them.

## 📚 License

MIT License – use freely for education, teaching, and awareness.
