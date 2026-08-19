# TokenWatch 📊
![CI](https://github.com/realMNohgee/tokenwatch/actions/workflows/ci.yml/badge.svg) ![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Real-time context window monitor.** Track token usage during agent sessions. Warn at configurable thresholds and suggest what to summarize or truncate.

> Part of the **Agentic Reliability Suite**.

## Install
```bash
git clone git@github.com:realMNohgee/tokenwatch.git
cd tokenwatch
python3 tokenwatch.py --help
```

## Quick start
```bash
python3 tokenwatch.py --input conversation.txt --limit 128000 --warn 75
```

## License
MIT — see [LICENSE](LICENSE).

🧰 **[Tool on Hermtica Marketplace](https://hermtica.com/marketplace)**
