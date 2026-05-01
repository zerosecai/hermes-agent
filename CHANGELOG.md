# Changelog

All notable Kuma-specific changes are documented here. Upstream Hermes Agent changes are tracked separately in `RELEASE_v*.md` (historical) and at [NousResearch/hermes-agent/releases](https://github.com/NousResearch/hermes-agent/releases) (ongoing).

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) once Kuma cuts its own release tags. Until then, individual rebrand commits land on `main` and are summarised below.

## [Unreleased] — Day-1 surface rebrand

Forked from `NousResearch/hermes-agent` at upstream commit `e5dad4ac` (2026-04-30). Sync'd to upstream HEAD before any Kuma commits landed.

### Added
- **`ATTRIBUTION.md`** — credits Nous Research and the upstream Hermes Agent contributors; documents what Kuma inherits and what it plans to add.
- **`kuma`, `kuma-agent`, `kuma-acp`** console-script entry points alongside the existing `hermes*` triplet. Both names work after `pip install -e .`.
- **`./kuma`** repo-root launcher mirroring `./hermes` (mode 100755).
- **`kuma_cli`** Python package alias. `from kuma_cli.main import main` resolves to the same code as `from hermes_cli.main import main` via the standard `sys.modules` swap pattern. No existing imports are affected.
- **`CHANGELOG.md`** — this file.

### Changed
- **`README.md`** — rewritten with Kuma identity, honest "Day-1 status" disclosure that the CLI command, Python module names, and documentation URLs still use `hermes`. Links upstream Hermes docs as authoritative until Kuma has its own docs site.
- **`LICENSE`** — appended `Copyright (c) 2026 ZeroSec AI (Kuma Agent additions)` alongside the original `Copyright (c) 2025 Nous Research`. Both copyrights preserved; license text unchanged (MIT).
- **`SECURITY.md`** — title and intro retitled; vulnerability reporting routes Kuma-specific issues to `zerosecai` GHSA / `sam@zerosec-ai.com`, upstream-runtime issues stay with Nous (with a CC ask). All technical content (trust model, sandbox, redaction, subagent isolation) is upstream-equivalent and untouched.
- **`AGENTS.md`** — title + a Day-1 note pointing dev-tool readers at `ATTRIBUTION.md` for the path-rename plan. The 762-line dev guide body is upstream-equivalent and untouched.
- **`CONTRIBUTING.md`** — title + a "where to send PRs" callout that routes runtime work upstream and Kuma-specific work here. The 658-line guide body is upstream-equivalent and untouched.
- **`pyproject.toml`** — `[project] name`: `hermes-agent` → `kuma-agent`. Authors: Nous Research kept, ZeroSec AI added. Description rewritten with Kuma framing. 27 self-references in `[termux]` and `[all]` extras updated from `hermes-agent[X]` → `kuma-agent[X]` so extras still resolve. `[tool.setuptools.packages.find]` now discovers both `hermes_cli` and `kuma_cli`.
- **`.github/ISSUE_TEMPLATE/*.yml`** and **`.github/PULL_REQUEST_TEMPLATE.md`** — URLs that pointed at `NousResearch/hermes-agent` (for issues, PRs, CONTRIBUTING in *this* repo) now point at `zerosecai/hermes-agent`. User-facing labels reference Kuma where it improves accuracy. Discord stays linked to Nous (no Kuma server yet). The skill template still references `hermes` commands because both `hermes` and `kuma` invocations resolve to the same code.

### Intentionally NOT changed (planned for later)
- **Source dirs / files** — `hermes_cli/`, `hermes_state.py`, `hermes_constants.py`, `hermes_logging.py`, `hermes_time.py` etc. remain canonical. Renaming would require shimming ~960 imports and a full pytest sweep. Will land in a later batch once shims and a CI gate are in place.
- **`~/.hermes/` user config dir** — unchanged. Renaming would orphan every existing install's settings, sessions DB, and skill installs.
- **`website/`** — Docusaurus site is upstream-equivalent. Will diverge once Kuma has its own docs deployment target.
- **`RELEASE_v*.md`** (11 files, ~360KB) — historical Hermes release notes. Left as artifact; rewriting would be revisionist.
- **`hermes-already-has-routines.md`** — upstream marketing artifact, left untouched.
- **CI workflows** (`.github/workflows/`) — unchanged. Rebranding the runtime here without first verifying no test references break would be unsafe.
- **Banner asset** (`assets/banner.png`) — original Hermes banner. Awaiting a Kuma cyber-bear PNG.
- **Skill packs, hybrid LLM routing, multi-agent pipeline, telemetry-off defaults, Kuma cyan/black palette** — these are the substantive Kuma additions and are scheduled for incremental work over weeks 2-7. None are shipped yet.

### Inherited
The full Hermes Agent runtime: agent loop, tool execution, skills system + agentskills.io standard, memory + learning loop, multi-platform gateway (Telegram/Discord/Slack/WhatsApp/Signal/etc.), provider abstraction, cron scheduler, subagent spawning, trajectory recording. Kuma re-skins and extends this engine.
