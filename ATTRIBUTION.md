# Attribution

## Direct ancestor: Hermes Agent

**Repository:** https://github.com/NousResearch/hermes-agent
**License:** MIT
**Authors:** Nous Research and 142+ contributors

Kuma Agent is a fork of Hermes Agent. The agent runtime, skill system, memory system, gateway, CLI, and the fundamental architecture come from Hermes. Nous Research built the engine; Kuma re-skins and extends it.

Specific things we inherit nearly unchanged from Hermes:

- Agent runtime + tool execution loop
- Skills system + agentskills.io standard support
- Memory + learning loop
- Multi-platform gateway (Telegram, Discord, Slack, WhatsApp, Signal)
- Provider abstraction (OpenRouter, Anthropic, OpenAI, local)
- Cron + automation
- Subagent spawning
- Trajectory recording

## What Kuma adds

Over time, Kuma will diverge from Hermes via:

- **Skill packs format** — chunk-based, auto-indexed packs (~1GB each).
  Initial pack: `kuma-pack-tsreact` (TypeScript + React + Vite).
- **Hybrid LLM routing** — local-first with cloud burst (Ollama Cloud, Local Ollama, LM Studio).
- **Multi-agent pipeline** — Planner → Coder → Reviewer. Scalable to 10 parallel coders.
- **Brand and identity** — Kuma cyber-bear + Cyan/Black palette.
- **Privacy-first defaults** — telemetry off by default, transparent.

Where these features make Kuma more useful upstream, contributions flow back to Hermes when appropriate.

## License

All upstream code (Hermes Agent + dependencies) remains under its original MIT license. Kuma additions are also MIT.

Original copyright is preserved in [LICENSE](LICENSE) alongside ZeroSec AI's.

## Thank you

Open-source forks live or die on the goodwill of the projects they're forked from. Hermes Agent chose MIT and chose to build in public. We're grateful for that, and we try to repay it by being explicit about what we took, what we changed, and where we got it from.
