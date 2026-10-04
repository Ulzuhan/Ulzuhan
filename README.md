I build private AI and self-hosted software from Oviedo, Spain: tools that do useful work with your documents and files without sending them to someone else’s cloud.

I co-founded [Hesperia Labs](https://hesperialabs.com), where we design and deploy AI systems on our clients’ own infrastructure. I’m also a ServiceNow consultant at DXC Technology, where for eight years I’ve built enterprise systems for clients like Grifols, Fluidra, Generali and Sanofi. In the evenings I teach AI and data science at Upgrade Hub.

### Private AI

- **[reed](https://github.com/Ulzuhan/reed)** · Self-hosted RAG. Streams answers with citations and abstains when the documents don’t support one. Hybrid dense + BM25 retrieval, a 41-question golden set with labelled evidence, and about 300 tests behind an 85% coverage gate.
- **[reed-mcp](https://github.com/Ulzuhan/reed-mcp)** · Gives Claude Desktop, Claude Code and other MCP hosts cited evidence from your own documents. Four read-only tools.
- **[private-ai-stack](https://github.com/Ulzuhan/private-ai-stack)** · Reed, Ollama, Qdrant and Open WebUI behind one `docker compose up`. CI reinstalls it from an offline bundle with networking disabled and round-trips a backup.

### Encryption and self-hosting

- **[arveil](https://github.com/Ulzuhan/arveil)** · End-to-end encrypted messenger for families. MLS (RFC 9420) in a Rust core, a Go relay, Flutter apps for Android and macOS. A threat model with 13 invariants checked by about 620 tests. Beta, not independently audited.
- **[docdrop](https://github.com/Ulzuhan/docdrop)** · File transfer up to 10 GiB, encrypted in the browser with chunked AES-256-GCM. A single Go binary on the standard library, with the React UI embedded.
- **[secretdrop](https://github.com/Ulzuhan/secretdrop)** · One-time secret links, encrypted in the browser with AES-256-GCM; the key stays in the URL fragment. Crash-safe burn after the last view, in a single Go binary.
- **[signdrop](https://github.com/Ulzuhan/signdrop)** · PAdES signing and verification in the browser, checked against 3,409 qualified authorities from 29 EU trusted lists.
- Also: [tabup](https://github.com/Ulzuhan/tabup) (shared expenses) · [qr-forge](https://github.com/Ulzuhan/qr-forge) (editable QR codes) · [linkup](https://github.com/Ulzuhan/linkup) (URL shortener without tracking) · [pixelforge](https://github.com/Ulzuhan/pixelforge) (local background removal) · [kaicorp-account](https://github.com/Ulzuhan/kaicorp-account) (one sign-in for all of them)

All of these run on hardware I own, at [kaicorplabs.com](https://kaicorplabs.com).

### Teaching

- **[Masterclass-YOLO](https://github.com/Ulzuhan/Masterclass-YOLO)** · From CNNs to YOLO: the computer vision material I use with my bootcamp students.

<br>

[ulzuhan.github.io](https://ulzuhan.github.io) · [LinkedIn](https://www.linkedin.com/in/manulinares6) · [ulzuhan.market@gmail.com](mailto:ulzuhan.market@gmail.com)
