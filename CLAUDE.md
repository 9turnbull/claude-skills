# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a **comprehensive skills library** for Claude AI and Claude Code - reusable, production-ready skill packages that bundle domain expertise, best practices, analysis tools, and strategic frameworks. The repository provides modular skills that teams can download and use directly in their workflows.

**Current Scope:** 177 production-ready skills across 9 domains with 254+ Python automation tools, 357 reference guides, 17 agents, and 22 slash commands.

**Key Distinction**: This is NOT a traditional application. It's a library of skill packages meant to be extracted and deployed by users into their own Claude workflows.

## Navigation Map

This repository uses **modular documentation**. For domain-specific guidance, see:

| Domain | CLAUDE.md Location | Focus |
|--------|-------------------|-------|
| **Agent Development** | [agents/CLAUDE.md](agents/CLAUDE.md) | cs-* agent creation, YAML frontmatter, relative paths |
| **Marketing Skills** | [marketing-skill/CLAUDE.md](marketing-skill/CLAUDE.md) | Content creation, SEO, ASO, demand gen, campaign analytics |
| **Product Team** | [product-team/CLAUDE.md](product-team/CLAUDE.md) | RICE, OKRs, user stories, UX research, SaaS scaffolding |
| **Engineering (Core)** | [engineering-team/CLAUDE.md](engineering-team/CLAUDE.md) | Fullstack, AI/ML, DevOps, security, data, QA tools |
| **Engineering (POWERFUL)** | [engineering/](engineering/) | Agent design, RAG, MCP, CI/CD, database, observability |
| **C-Level Advisory** | [c-level-advisor/CLAUDE.md](c-level-advisor/CLAUDE.md) | CEO/CTO strategic decision-making |
| **Project Management** | [project-management/CLAUDE.md](project-management/CLAUDE.md) | Atlassian MCP, Jira/Confluence integration |
| **RA/QM Compliance** | [ra-qm-team/CLAUDE.md](ra-qm-team/CLAUDE.md) | ISO 13485, MDR, FDA, GDPR, ISO 27001 compliance |
| **Business & Growth** | [business-growth/CLAUDE.md](business-growth/CLAUDE.md) | Customer success, sales engineering, revenue operations |
| **Finance** | [finance/CLAUDE.md](finance/CLAUDE.md) | Financial analysis, DCF valuation, budgeting, forecasting, SaaS metrics |
| **Standards Library** | [standards/CLAUDE.md](standards/CLAUDE.md) | Communication, quality, git, security standards |
| **Templates** | [templates/CLAUDE.md](templates/CLAUDE.md) | Template system usage |

## Architecture Overview

### Repository Structure

```
claude-code-skills/
├── .claude/                   # Claude Code integration configs
├── .claude-plugin/            # Plugin registry (marketplace.json, 19 plugins)
├── .codex/                    # OpenAI Codex integration configs
├── .gemini/                   # Google Gemini CLI integration configs
├── .github/                   # GitHub Actions (10 workflows) + issue templates
├── agents/                    # 17 cs-* prefixed agents + 3 personas across 11 domains
├── commands/                  # 17 slash commands (changelog, tdd, saas-health, prd, rice, retro, etc.)
├── custom-gpt/                # Custom GPT configurations
├── engineering-team/          # 24 core engineering skills + Playwright Pro + Self-Improving Agent
├── engineering/               # 25 POWERFUL-tier advanced skills
├── product-team/              # 12 product skills + Python tools
├── marketing-skill/           # 43 marketing skills (7 pods) + Python tools
├── c-level-advisor/           # 28 C-level advisory skills (10 roles + orchestration)
├── project-management/        # 6 PM skills + Atlassian MCP
├── ra-qm-team/                # 12 RA/QM compliance skills
├── business-growth/           # 4 business & growth skills + Python tools
├── finance/                   # 2 finance skills + Python tools
├── eval-workspace/            # Skill evaluation results (Tessl)
├── orchestration/             # Orchestration protocol (ORCHESTRATION.md)
├── standards/                 # 5 standards library files
├── templates/                 # Reusable templates
├── docs/                      # MkDocs Material documentation site
├── scripts/                   # Build/distribution scripts (9 files)
└── documentation/             # Implementation plans, sprints, delivery
```

### Skill Package Pattern

Each skill follows this structure:
```
skill-name/
├── SKILL.md              # Master documentation (YAML frontmatter required)
├── scripts/              # Python CLI tools (no ML/LLM calls)
├── references/           # Expert knowledge bases
└── assets/               # User templates
```

**SKILL.md YAML Frontmatter (required on all skills):**
```yaml
---
name: skill-name
description: "When to use, trigger keywords, related skills"
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: domain-name
  updated: YYYY-MM-DD
---
```

**Design Philosophy**: Skills are self-contained packages. Each includes executable tools (Python scripts), knowledge bases (markdown references), and user-facing templates. Teams can extract a skill folder and use it immediately.

**Key Pattern**: Knowledge flows from `references/` → into `SKILL.md` workflows → executed via `scripts/` → applied using `assets/` templates.

## Skill Production Pipeline

All new skills and major improvements **must** follow the mandatory 9-phase pipeline defined in [SKILL_PIPELINE.md](SKILL_PIPELINE.md):

```
Intent → Research → Draft → Eval → Iterate → Compliance → Package → Deploy → Verify → Rollback-Ready
```

**Key tooling:**
- **Tessl CLI** (v0.70.0) — Skill quality scoring. Target: 85%+. Max 5 iterations per skill.
- **ClawHub CLI** — Publish to ClawHub registry after compliance passes.
- **eval-workspace/** — Stores Tessl evaluation results for review.

## Git Workflow

**Branch Strategy:** feature → dev → main (PR only)

**Branch Protection Active:** Main branch requires PR approval. Direct pushes blocked.

### Quick Start

```bash
# 1. Always start from dev
git checkout dev
git pull origin dev

# 2. Create feature branch
git checkout -b feature/agents-{name}

# 3. Work and commit (conventional commits)
feat(agents): implement cs-{agent-name}
fix(tool): correct calculation logic
docs(workflow): update branch strategy

# 4. Push and create PR to dev
git push origin feature/agents-{name}
gh pr create --base dev --head feature/agents-{name}

# 5. After approval, PR merges to dev
# 6. Periodically, dev merges to main via PR
```

**Conventional Commit Types:** `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `perf`

**Branch Protection Rules:**
- ✅ Main: Requires PR approval, no direct push
- ✅ Dev: Unprotected, but PRs recommended
- ✅ All: Conventional commits enforced

See [documentation/WORKFLOW.md](documentation/WORKFLOW.md) for complete workflow guide.
See [standards/git/git-workflow-standards.md](standards/git/git-workflow-standards.md) for commit standards.

## CI/CD & Automation

**GitHub Actions (`.github/workflows/`, 10 workflows):**
| Workflow | Purpose |
|----------|---------|
| `claude.yml` | Main CI/CD pipeline |
| `ci-quality-gate.yml` | Quality checks on PRs |
| `claude-code-review.yml` | AI-powered code review |
| `enforce-pr-target.yml` | Forces PRs to target dev branch |
| `pr-issue-auto-close.yml` | Auto-closes linked issues on merge |
| `skill-security-audit.yml` | Runs security scan on skill packages |
| `smart-sync.yml` | Syncs skills to Codex/Gemini registries |
| `static.yml` | Static analysis |
| `sync-codex-skills.yml` | Codex skill index sync |
| `virustotal-scan.yml` | Malware scanning for new files |

## Multi-Platform Support

Skills are distributed across 6+ AI coding tools via platform-specific configs:

| Platform | Config Location | Install Script |
|----------|----------------|---------------|
| Claude Code | `.claude/` | `scripts/install.sh` |
| OpenAI Codex | `.codex/` | `scripts/codex-install.sh` |
| Google Gemini CLI | `.gemini/` | `scripts/gemini-install.sh` |
| OpenClaw | — | `scripts/openclaw-install.sh` |
| Cursor / Aider / Windsurf | — | `scripts/install.sh` (multi-tool) |

The `scripts/convert.sh` converts skills to all platform formats in batch.

## Agents Structure

**17 cs-* agents** organized across 11 domain subdirectories in `agents/`:

```
agents/
├── CLAUDE.md                    # Agent development guide (YAML frontmatter spec)
├── business-growth/
│   └── cs-growth-strategist.md
├── c-level/
│   ├── cs-ceo-advisor.md
│   └── cs-cto-advisor.md
├── engineering/
│   └── cs-senior-engineer.md
├── finance/
│   └── cs-financial-analyst.md
├── marketing/
│   ├── cs-content-creator.md
│   └── cs-demand-gen-specialist.md
├── personas/                    # Non-cs-* persona agents (startup-cto, growth-marketer, solo-founder)
├── product/
│   ├── cs-agile-product-owner.md
│   ├── cs-product-analyst.md
│   ├── cs-product-manager.md
│   ├── cs-product-strategist.md
│   └── cs-ux-researcher.md
├── project-management/
│   └── cs-project-manager.md
└── ra-qm-team/
    └── cs-quality-regulatory.md
```

**Agent YAML Frontmatter:**
```yaml
---
name: cs-agent-name
description: One-line description
skills: skill-folder-name
domain: domain-name
model: sonnet
tools: [Read, Write, Bash, Grep, Glob]
---
```

## Development Environment

**No build system or test frameworks** - intentional design choice for portability.

**Python Scripts:**
- Use standard library only (no pip dependencies unless documented)
- CLI-first design: all scripts support `--help` and JSON output
- No ML/LLM calls (keeps skills portable and fast)
- Python 3.10+ required
- All 254+ scripts must pass `python script.py --help` without errors

**If adding dependencies:**
- Keep scripts runnable with minimal setup (`pip install package` at most)
- Document all dependencies in SKILL.md
- Prefer standard library implementations

## Current Version

**Version:** v2.1.2 (latest stable)

**v2.1.2 Highlights (2026-03-10):**
- Landing page generator now outputs **Next.js TSX + Tailwind CSS** by default (4 design styles, 7 section generators)
- **Brand voice integration** — landing page workflow uses marketing brand voice analyzer to match copy tone to design style
- 25 Python scripts fixed across all domains (syntax, dependencies, argparse)
- 237/237 scripts verified passing `--help`
- Competitive teardown SKILL.md fixed (6 broken file references)
- Cross-domain workflows documented (product + marketing skill integration)

**v2.1.1 (2026-03-07):**
- 18 skills optimized from 66-83% to 85-100% via Tessl quality review
- YAML frontmatter (name + description) added to all SKILL.md files
- 6 new agents + 5 slash commands, Gemini CLI support, MkDocs docs site
- `SKILL_PIPELINE.md` added — mandatory 9-phase production pipeline

**v2.0.0 (2026-02-16):**
- 25 POWERFUL-tier engineering skills added (engineering/ folder)
- Plugin marketplace infrastructure (.claude-plugin/marketplace.json)
- Multi-platform support: Claude Code, OpenAI Codex, OpenClaw

**Unreleased / In Progress:**
- `engineering/skill-security-auditor` — POWERFUL-tier security scanner for skill packages (PASS/WARN/FAIL verdicts, zero dependencies)
- `engineering/git-worktree-manager` — Added `worktree_manager.py` and `worktree_cleanup.py`
- `engineering/mcp-server-builder` — Added `openapi_to_mcp.py` and `mcp_validator.py`
- `engineering/changelog-generator` — Added `generate_changelog.py` and `commit_linter.py`
- `engineering/ci-cd-pipeline-builder` — Added `stack_detector.py` and `pipeline_generator.py`
- Python Agent SDK app for skills repo exploration (most recent commit)

**Past Sprints:** See [documentation/delivery/](documentation/delivery/) and [CHANGELOG.md](CHANGELOG.md) for history.

## Roadmap

**Phase 1-2 Complete:** 177 production-ready skills deployed across 9 domains
- Engineering Core (24), Engineering POWERFUL (25), Product (12), Marketing (43), PM (6), C-Level (28), RA/QM (12), Business & Growth (4), Finance (2)
- 254+ Python automation tools, 357 reference guides, 17 agents, 22 commands
- Complete enterprise coverage from engineering through regulatory compliance, sales, customer success, and finance
- MkDocs Material docs site with 210+ indexed pages for SEO

See domain-specific roadmaps in each skill folder's README.md or roadmap files.

## Key Principles

1. **Skills are products** - Each skill deployable as standalone package
2. **Documentation-driven** - Success depends on clear, actionable docs
3. **Algorithm over AI** - Use deterministic analysis (code) vs LLM calls
4. **Template-heavy** - Provide ready-to-use templates users customize
5. **Platform-specific** - Specific best practices > generic advice

## ClawHub Publishing Constraints

This repository publishes skills to **ClawHub** (clawhub.com) as the distribution registry. The following rules are **non-negotiable**:

1. **cs- prefix for slug conflicts only.** When a skill slug is already taken on ClawHub by another publisher, publish with the `cs-` prefix (e.g., `cs-copywriting`, `cs-seo-audit`). The `cs-` prefix applies **only on the ClawHub registry** — repo folder names, local skill names, and all other tools (Claude Code, Codex, Gemini CLI) remain unchanged.
2. **Never rename repo folders or local skill names** to match ClawHub slugs. The repo is the source of truth.
3. **No paid/commercial service dependencies.** Skills must not require paid third-party API keys or commercial services unless provided by the project itself. Free-tier APIs and BYOK (bring-your-own-key) patterns are acceptable.
4. **Rate limit: 5 new skills per hour** on ClawHub. Batch publishes must respect this. Use the drip timer (`clawhub-drip.timer`) for bulk operations.
5. **plugin.json schema** — ONLY these fields: `name`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `skills: "./"`. No extra fields.
6. **Version follows repo versioning.** ClawHub package versions must match the repo release version (currently v2.1.2+).

## Anti-Patterns to Avoid

- Creating dependencies between skills (keep each self-contained)
- Adding complex build systems or test frameworks (maintain simplicity)
- Generic advice (focus on specific, actionable frameworks)
- LLM calls in scripts (defeats portability and speed)
- Over-documenting file structure (skills are simple by design)
- Hardcoding secrets or API keys in any file
- Renaming repo folders to match ClawHub slugs

## Working with This Repository

**Creating New Skills:** Follow the appropriate domain's roadmap and CLAUDE.md guide (see Navigation Map above). All new skills must go through the [SKILL_PIPELINE.md](SKILL_PIPELINE.md) 9-phase process.

**Editing Existing Skills:** Maintain consistency across markdown files. Use the same voice, formatting, and structure patterns.

**Quality Standard:** Each skill should save users 40%+ time while improving consistency/quality by 30%+. Tessl target score: 85%+.

**Compliance Check (8 points):**
1. YAML frontmatter present and valid
2. All file references resolve
3. SKILL.md under 500 lines
4. Python scripts pass `--help`
5. No hardcoded secrets
6. No LLM calls in scripts
7. Self-contained (no cross-skill dependencies)
8. Conventional commit used

## Additional Resources

- **.gitignore:** Excludes `.vscode/`, `.DS_Store`, `AGENTS.md`, `PROMPTS.md`, `.env*`
- **Plugin Registry:** [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) - 19 plugins
- **Standards Library:** [standards/](standards/) - Communication, quality, git, documentation, security
- **Skill Pipeline:** [SKILL_PIPELINE.md](SKILL_PIPELINE.md) - Mandatory 9-phase production pipeline
- **Skill Authoring:** [SKILL-AUTHORING-STANDARD.md](SKILL-AUTHORING-STANDARD.md) - Skill creation guidelines
- **Orchestration:** [orchestration/ORCHESTRATION.md](orchestration/ORCHESTRATION.md) - Multi-agent orchestration protocol
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- **Implementation Plans:** [documentation/implementation/](documentation/implementation/)
- **Sprint Delivery:** [documentation/delivery/](documentation/delivery/)
- **Python Tools Audit:** [documentation/PYTHON_TOOLS_AUDIT.md](documentation/PYTHON_TOOLS_AUDIT.md)

---

**Last Updated:** March 20, 2026
**Version:** v2.1.2
**Status:** 177 skills deployed across 9 domains, 19 marketplace plugins, docs site live
