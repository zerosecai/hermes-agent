# Privacy Posture

Kuma Agent is privacy-first by design and by audit. This document records the guarantee, names the kind of code that would violate it, and tells you exactly what to grep for if you want to verify it yourself.

## Guarantee

**Kuma Agent ships no third-party analytics, no phone-home telemetry, and no code that exfiltrates user data to ZeroSec AI, Nous Research, or any other party.**

The agent runs locally (or on infrastructure you control) and talks to the LLM providers and messaging platforms you explicitly configure. Nothing else.

## What "telemetry" means in this codebase

The word `telemetry` appears in many files. None of those usages send data off-machine. Specifically:

- **Skill usage sidecar** (`tools/skill_usage.py`) — a local file that tracks which skills the Curator feature touches, so it can self-improve them. Stored in your local skill directory; never transmitted. Bundled and hub-installed skills are explicitly excluded.
- **OAuth trace** (`hermes_cli/auth.py`) — debug logging for OAuth flows, gated behind the `HERMES_OAUTH_TRACE` environment variable (off by default). Writes to your local logger only. Token fingerprints are SHA-256 hashes truncated to 12 chars, designed to identify token rotation without leaking the token itself.
- **Internal health metrics** (`gateway/run.py`, `hermes_cli/kanban.py`, `agent/curator.py`, etc.) — diagnostic counters and timing measurements used inside running processes. Never persisted off-host.
- **Plugin HUD bars** (`plugins/strike-freedom-cockpit/`) — UI decoration that visualizes local agent state. No external calls.
- **Profiling scripts** (`scripts/profile-tui.py`) — developer perf tooling, not shipped to users.

The `/insights` slash command and the `/api/analytics/*` web-dashboard endpoints are local. They read the local SQLite session database (`~/.hermes/sessions.db`) and render token usage and model costs to the user. Nothing is sent to ZeroSec AI or Nous Research.

## Provider data flow

When Kuma calls an LLM provider (OpenRouter, Anthropic, OpenAI, NVIDIA NIM, Ollama, etc.) or sends a message via a gateway platform (Telegram, Discord, Slack, etc.), data goes from your machine directly to that third party's API under that provider's privacy policy. ZeroSec AI is not in the path.

## How to verify this yourself

```bash
# No third-party analytics SDKs in dependencies
grep -E '(posthog|mixpanel|segment|amplitude)' pyproject.toml uv.lock
# Sentry is referenced only in font-design references — not as an exception monitor
grep -rni 'sentry' --include='*.py' --include='*.toml'
# No outbound URLs to analytics endpoints
grep -rE 'https?://(api\.)?(amplitude|posthog|mixpanel|segment|datadog)' --include='*.py'
```

All three should return empty (or only documentation/comment hits) on the current commit.

## Rule for contributors

**Any pull request that adds analytics, telemetry, error reporting, or any other code that sends data to a third-party service must be opt-in by default.** Default-on telemetry will be rejected.

This applies to:
- Analytics SDKs
- Crash/exception reporters that include user data
- Update-check pings that include identifiers
- Any background HTTP request not directly serving the user's current task

Opt-in means an explicit `config.yaml` key or environment variable that defaults to `false`/unset, with the intent visible in the PR description and documented in this file.

## Reporting violations

If you find code that violates this posture, file a security issue (see [SECURITY.md](SECURITY.md)) — it's a vulnerability, not a feature request.
