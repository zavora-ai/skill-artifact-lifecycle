---
name: artifact-lifecycle
description: Manage governed artifacts — store versioned artifacts, track provenance, derive new artifacts, link related items, redact sensitive content, and export packages. Use when storing build outputs, versioning artifacts, checking provenance, linking related artifacts, or exporting for distribution.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [list_folders, list_artifacts, get_artifact_metadata, read_artifact, write_artifact, create_artifact_version, redact_artifact, derive_artifact, link_artifacts, export_artifact_package]
tags: [infrastructure, artifacts, provenance, versioning, governance]
metadata:
  author: Zavora AI
  mcp-server: mcp-artifact-store
  success-criteria:
    trigger-rate: "90% on artifact queries"
    provenance-tracking: "Every artifact has source + lineage"
---

# Artifact Lifecycle Management

You manage governed artifacts with provenance. Every artifact is versioned, traceable, and linked to its source. Never overwrite — always create new versions.

## Decision Tree
```
├── "store", "save", "upload"? → write_artifact + create_artifact_version
├── "find", "list", "what artifacts"? → list_artifacts / list_folders
├── "read", "download", "get"? → read_artifact
├── "version", "history"? → get_artifact_metadata
├── "derive", "transform", "from"? → derive_artifact + link_artifacts
├── "redact", "remove sensitive"? → redact_artifact
├── "export", "package"? → export_artifact_package
```

## MUST DO
- Always create new versions (never overwrite)
- Track provenance (source, creator, pipeline)
- Link derived artifacts to their sources
- Redact sensitive content before sharing externally

## MUST NOT DO
- Never overwrite existing artifact versions
- Don't store without provenance metadata
- Don't export without checking for sensitive content
