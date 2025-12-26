# Vexa – Modular Voice Assistant (Python)

Vexa is a **Python-based voice assistant** designed with a **modular, intent-driven architecture**.
The project focuses on **clean design, robustness, and extensibility**, rather than just adding features.

This repository represents the project up to Phase 3 (Stateful Commands & Automation Workflows).

## Key Objectives

- Build a voice assistant with **clear separation of concerns**
- Avoid tightly coupled `if-else` command logic
- Handle real-world failures like silence, noise, and partial input
- Design the system so new commands can be added **without modifying core logic**

## Architecture Overview

Vexa follows a layered architecture:

```
User (Voice)
   ↓
Listener (Speech → Text, retries, silence handling)
   ↓
Normalizer (cleans spoken input)
   ↓
Intent Classifier (decides user intent)
   ↓
Processor (coordinates flow)
   ↓
Command Registry (Intent → Feature mapping)
   ↓
Feature Execution
```

### Core Design Principles

- **Intent ≠ Execution**
- **Processor coordinates, features execute**
- **All commands follow a unified execution contract**
- **Safe failure by default**

## Implemented Features

### Voice & Core

- Speech recognition with retry logic
- Ambient noise handling
- Silence detection
- Text-to-speech responses
- Structured logging

### Commands

- Open websites (YouTube, Google, GitHub, etc.)
- Launch desktop applications (Chrome, Calculator, VS Code, Notepad)
- Tell current time and date
- Tell jokes
- Notes system:
  - Write notes
  - Read recent notes
  - Clear notes with confirmation
- Automation workflows:
  - Coding setup (launches development tools and workspace)

## Current Development Phases

### Phase 1 – Stability & Reliability (Implemented)

- Speech recognition
- Retry logic
- Silence handling
- Logging
- Command normalization

### Phase 2 – Core Architecture (Implemented)

- Intent classification
- Command registry
- Decoupled processor
- Unified command execution
- Context-based command interface

### Phase 3 – Feature Hardening (Implemented)

- Multi-turn notes using pending intent
- Note cancellation handling
- Safer destructive actions

### Phase 4 – Advanced Behavior (Planned)

- Interruptible speech
- Event-driven / async execution
- Context-aware AI fallback (optional)

## Project Structure (Simplified)

```
vexa/
│
├── core/
|   ├── command_registry.py
|   ├── confirmation.py
│   ├── context.py
│   ├── intent_classifier.py
│   ├── intents.py
│   ├── listener.py
│   ├── logger.py
│   ├── normalizer.py
│   ├── processor.py
│   ├── session_context.py
│   ├── speaker.py
│   └── utils.py
│
├── features/
│   ├── open_web.py
│   ├── launch_apps.py
│   ├── get_datetime.py
│   ├── tell_joke.py
│   └── notes.py
|
├── setups/
│   └── coding_setup.py
|
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the assistant:

```bash
python main.py
```

## Design Decisions (Why This Matters)

- **Rule-based intent classification** was chosen for transparency and debuggability
- **Command registry** allows adding new commands without modifying the processor
- **Context-based execution** prevents feature crashes and supports future multi-turn logic
- **Logging over print statements** for traceability and debugging

## Limitations (Current)

- Most commands are single-turn (notes support multi-turn interaction)
- No async or interrupt handling yet
- Entity extraction is basic
- Notes are stored locally in a text file

These are **intentional trade-offs** to keep the core stable before moving to Phase 3.

## Roadmap

- Generalized multi-turn command framework
- Improved entity extraction
- Interruptible speech
- Async execution loop
- Optional LLM-based fallback for unknown intents

## Disclaimer

This project prioritizes **engineering correctness and architecture clarity** over feature quantity.
Each phase is validated before moving to the next.
