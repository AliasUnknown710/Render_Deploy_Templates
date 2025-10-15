from flask import Flask, jsonify
import psutil, socket

app = Flask(__name__)

def check_cpu(): return psutil.cpu_percent(interval=1) < 85
def check_mem(): return psutil.virtual_memory().percent < 90
def check_disk(): return psutil.disk_usage("/").percent < 90
def check_dns():
    try: socket.gethostbyname("example.com"); return True
    except: return False

@app.route("/healthz")
def health():
    status = {
        "cpu_ok": check_cpu(),
        "memory_ok": check_mem(),
        "disk_ok": check_disk(),
        "dns_ok": check_dns()
    }
    return jsonify({"status": "healthy" if all(status.values()) else "unhealthy", "checks": status}), 200 if all(status.values()) else 503
