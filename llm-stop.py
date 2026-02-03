#!/usr/bin/env python3
import subprocess

print("🛑 Stopping Local LLM System...")

# Stop Open WebUI
print("Stopping Open WebUI...")
subprocess.run(["docker", "stop", "open-webui"])

# Stop Ollama
print("Stopping Ollama...")
subprocess.run(["sudo", "systemctl", "stop", "ollama"])

print("✓ All services stopped. RAM freed up!")
