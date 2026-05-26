# Artifact Cross-MCP Workflows

## Artifact + CI/CD: Store Build Output
```
CICD: list_artifacts(run_id: "run_200") → [{name: "billing-v2.3.1.tar.gz", size: "12MB"}]
ARTIFACT: write_artifact(folder: "releases/billing", name: "v2.3.1.tar.gz", source: "cicd_run_200")
ARTIFACT: create_artifact_version(id, version: "2.3.1", provenance: {pipeline: "run_200", commit: "abc123"})
```

## Artifact + Environment: Deploy from Store
```
ARTIFACT: get_artifact_metadata(id: "billing-v2.3.1") → {integrity: "sha256:...", verified: true}
ENVIRONMENT: promote_release(artifact_id: "billing-v2.3.1", env: "production")
```
