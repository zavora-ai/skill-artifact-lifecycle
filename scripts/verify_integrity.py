#!/usr/bin/env python3
"""Verify artifact integrity by comparing stored vs computed hash."""
import json, sys, hashlib

def verify(data):
    stored_hash = data.get("stored_hash", "")
    content = data.get("content", "")
    computed = hashlib.sha256(content.encode()).hexdigest()
    return {"valid": stored_hash == computed, "stored": stored_hash[:12], "computed": computed[:12], "match": stored_hash == computed}

if __name__ == "__main__":
    print(json.dumps(verify(json.loads(sys.argv[1])), indent=2))
