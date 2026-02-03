#!/usr/bin/env python3
import subprocess
import time
import webbrowser

print("🚀 Starting Local LLM System...")

# Start Ollama
print("Starting Ollama service...")
subprocess.run(["sudo", "systemctl", "start", "ollama"], check=True)
time.sleep(3)

# Start Open WebUI
print("Starting Open WebUI...")
subprocess.run(["docker", "start", "open-webui"], check=True)
time.sleep(5)

# Open browser
print("🌐 Opening browser...")
webbrowser.open("http://localhost:8080")

print("✨ Ready! LLM available at http://localhost:8080")
