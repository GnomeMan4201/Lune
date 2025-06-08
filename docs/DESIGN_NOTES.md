# Design Notes - Lune

This file captures architectural considerations, design trade-offs, and decisions taken during the development of the Lune adversary simulation framework.

## Design Philosophy

- Keep agents minimal and cross-platform
- Use only standard libraries and common dependencies
- Modularize all components for extensibility
- Support testing and simulation of offensive operations in labs

## Key Decisions

### Communication via HTTP
- Realistic and common in threat actor C2
- Easily supports tunneling
- Replaceable transport layer in the future

### JSON for Task Format
- Simple, readable, portable
- No custom serialization needed

### Polling Model with Jitter
- Reduces signature-based detection
- Mimics realistic "check-in" behavior

## Extensibility Ideas

- Plugin system for custom commands
- Multi-agent authentication
- Covert channels (DNS, ICMP, stego)
- Task expiration and scheduling
- Result aggregation database

## Testing Strategy

- Endpoint coverage tests via \`pytest\`
- Simulate agents in test harness
- Integrate CI with coverage badges

## Known Limitations

- No encryption (yet)
- Plaintext over HTTP
- Agent detection via static signatures

## Inspirations

- MITRE ATT&CK
- Cobalt Strike
- Empire
