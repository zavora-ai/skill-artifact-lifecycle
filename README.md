# Artifact Lifecycle Skill

> Governed artifact management — versioned storage, provenance tracking, integrity verification, derivation chains, and export packaging for build outputs and documents.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Store | 2 | Write + create version with provenance |
| Verify | 1 | SHA-256 integrity check |
| Derive | 2 | Transform + link to source |
| Export | 1 | Package for distribution |

### Without this skill:
- Artifacts overwritten without versioning
- No provenance (who built this? from what commit?)
- Integrity unverified (could be tampered)
- No derivation chain (can't trace lineage)

### With this skill:
- Every artifact versioned (never overwrite)
- Full provenance (source, pipeline, commit, timestamp)
- Integrity verified via SHA-256 before use
- Derivation chains link outputs to inputs

## Installation

```bash
git clone https://github.com/zavora-ai/skill-artifact-lifecycle.git \
  ~/.skills/skills/artifact-lifecycle
```

## Requirements

**Required:** `mcp-artifact-store` (10 tools)
**Cross-MCP:** mcp-cicd (store build outputs), mcp-environment (deploy from store)

## Example

**User:** "Verify the billing service artifact before deploying"

**Result:**
```
Artifact: billing-v2.3.1.tar.gz
Provenance: pipeline run_200, commit abc123
Integrity: SHA-256 verified ✅ (matches stored hash)
Safe to deploy.
```

## Scripts

### `verify_integrity.py`
```bash
python scripts/verify_integrity.py '{"stored_hash": "abc123...", "content": "file contents"}'
# → {"valid": true, "match": true}
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on relevant queries |
| Compliance | 100% governed actions evaluated |
| Audit trail | Every action logged with actor + reason |

## Related Skills

See the full [ADK-Rust Enterprise Skills Registry](https://github.com/zavora-ai) for all 35 skills.
