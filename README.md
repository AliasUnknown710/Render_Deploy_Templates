## 🚀 Render Deployment Templates

Secure deployment templates for Python apps on Render. Includes production-ready config, health checks, and environment variable guidance.

---

## 🔧 Files Included

| File | Description |
|------|-------------|
| `flask_deploy.yaml` | Render service definition for Flask app. |
| `env_var_notes.md` | Guidelines for secure environment variable usage. |
| `healthcheck.py` | Validates CPU, memory, disk, and DNS resolution. |

---

## 🚀 Usage

1. Add `flask_deploy.yaml` to your repo root.
2. Define secrets in Render dashboard (never in code).
3. Add `/healthz` endpoint to your app for uptime checks.

---

## 🧠 Notes

- Use `gunicorn` for production.
- Extend healthcheck with DB ping or external API reachability.
