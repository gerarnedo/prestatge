#!/usr/bin/env python3
"""Serveix l'app Prestatge per HTTPS a la xarxa local, perquè el mòbil pugui fer servir la càmera.
Ús:  python3 serveix.py   (Ctrl+C per aturar)
"""
import http.server, os, socket, ssl, subprocess, sys

PORT = 8443
HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "cert.pem")
KEY = os.path.join(HERE, "key.pem")

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80)); return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()

ip = lan_ip()
if not (os.path.exists(CERT) and os.path.exists(KEY)):
    print("Creant un certificat autosignat (només cal el primer cop)…")
    subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "3650",
                    "-keyout", KEY, "-out", CERT, "-subj", "/CN=prestatge.local",
                    "-addext", f"subjectAltName=IP:{ip},DNS:localhost,IP:127.0.0.1"], check=True)

class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=HERE, **k)
    def end_headers(self):
        self.send_header("Cache-Control", "no-store"); super().end_headers()
    def log_message(self, *a): pass

httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Quiet)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER); ctx.load_cert_chain(CERT, KEY)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
print("\nApp Prestatge en marxa.")
print(f"  Al mòbil (mateixa WiFi):  https://{ip}:{PORT}/")
print(f"  En aquest Mac:            https://localhost:{PORT}/")
print("El navegador avisarà que el certificat no és de confiança: accepta'l un cop (Avançat → Continua).")
print("Ctrl+C per aturar.\n")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nAturat.")
