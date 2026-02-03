# Local Uncensored LLM Setup

A fully private, uncensored AI assistant running locally using Dolphin Llama 3 8B with Ollama and Open WebUI.

## Features

- 🔒 **100% Private** - All data stays on your machine
- 🚫 **Zero Censorship** - Dolphin model with refusal training removed
- 💻 **Easy Control** - Simple Python scripts to start/stop
- 🌐 **Beautiful UI** - ChatGPT-like web interface via Open WebUI
- ⚡ **Resource Efficient** - ~7GB RAM when running, 0GB when stopped

## Requirements

- 32GB RAM (recommended)
- Linux (tested on Linux Mint)
- Docker
- Python 3

## Installation

### 1. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Download Dolphin Model
```bash
ollama pull dolphin-llama3:8b
```

### 3. Install Open WebUI
```bash
docker run -d \
  --network host \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  -e OLLAMA_BASE_URL=http://localhost:11434 \
  ghcr.io/open-webui/open-webui:main
```

### 4. Configure Permissions
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Allow Ollama without password (optional)
sudo visudo
# Add: username ALL=(ALL) NOPASSWD: /bin/systemctl start ollama, /bin/systemctl stop ollama
```

### 5. Clone This Repo
```bash
git clone https://github.com/YOUR_USERNAME/local-uncensored-llm.git
cd local-uncensored-llm
```

## Usage

### Start the LLM
```bash
python3 llm-start.py
```

Opens browser to http://localhost:8080

### Stop the LLM (frees RAM)
```bash
python3 llm-stop.py
```

## Resource Usage

- **RAM**: ~7GB while running (22% of 32GB)
- **Storage**: ~10GB total
- **CPU**: Spikes during responses, idle otherwise

## Model Information

- **Model**: Dolphin 2.9.2 Llama 3 8B
- **Quantization**: Q4_K_M
- **Training**: Uncensored - refusal behaviors removed
- **Creator**: Eric Hartford / Cognitive Computations

## Why Dolphin?

Dolphin models are specifically trained to remove alignment and refusal mechanisms, making them ideal for:
- Privacy-focused applications
- Research without guardrails
- Creative projects
- Learning how LLMs work without restrictions

## Troubleshooting

**Docker permission denied:**
```bash
newgrp docker
```

**Model not showing in Open WebUI:**
- Verify Ollama is running: `ollama list`
- Check Open WebUI connection in Settings

**Slow responses:**
- Consider using smaller model: `ollama pull dolphin-llama3:3b`
- Or upgrade to GPU acceleration

## License

Scripts: MIT License
Models: Check individual model licenses on HuggingFace

## Disclaimer

This setup provides an uncensored AI model. Use responsibly and in accordance with local laws.
