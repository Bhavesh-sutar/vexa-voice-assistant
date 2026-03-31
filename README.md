# Vexa – Modular Voice Assistant

A Python voice assistant built with clean architecture and extensibility in mind.

## Architecture

```
Voice Input → Listener → Normalizer → Intent Classifier → Processor → Command Registry → Feature
```

## Features

- Speech recognition with retry and silence handling
- Open websites and launch desktop apps
- Tell time, date, and jokes
- Notes (write, read, clear)
- Coding setup automation

## Project Structure

```
vexa/
├── core/        # Listener, classifier, processor, registry, etc.
├── features/    # Web, apps, datetime, jokes, notes
├── setups/      # Automation workflows
└── main.py
```

## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

## Design Philosophy

- Intent classification is rule-based for transparency
- New commands can be added without touching core logic
- Features are decoupled and follow a unified execution contract

## Roadmap

- Async / interruptible execution
- Generalized multi-turn support
- Optional LLM fallback for unknown intents
