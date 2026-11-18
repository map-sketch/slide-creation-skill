# Standalone Consulting Slide Creation Skill (`consulting-slide-creator`)

A standalone Agent Skill (`SKILL.md`) designed to author, structure, and design executive-grade consulting slides using **McKinsey storyline mechanics** and **Deloitte visual design tokens**.

Dual-target compatible with:
1. **Microsoft 365 PowerPoint Copilot & Copilot Studio**
2. **Google Antigravity IDE** (`.agents/skills/`)
3. **ChatGPT Pro / Deep Research / python-pptx**

---

## Skill Overview

- **Canonical Path**: [`skills/consulting-slide-creator/SKILL.md`](skills/consulting-slide-creator/SKILL.md)
- **Specification Compliance**: Strict adherence to open Agent Skills and PowerPoint Copilot custom skill constraints:
  * Frontmatter contains only `name` and `description` between `---` delimiters.
  * Line count: **186 lines** (well under the 450-line ceiling).
  * Word count: **1,485 words** (well under the 1,800-word ceiling).

---

## Core Slide Standards Enforced

1. **Action Title Zone**: Bold 20–22pt assertion answering the "So what?" question, ending with a terminal period (`.`) rendered in Deloitte Green (`#86BC25`).
2. **Subtitle / Takeaway Line**: 12pt Cool Gray (`#53565A`) framing the core analytical finding.
3. **Structured Body Grid**: Widescreen 16:9 canvas (13.333" × 7.5") following MECE grouping, <= 15 words per bullet, and bold anchor keywords.
4. **Mandatory `Source:` Footer**: Standardized 8.5pt attribution at `Y=6.9"`.

---

## 10 Supported Layout Archetypes

1. **Cover Slide (Executive Hero)**: Dark hero (`#000000`) with practice kicker and bottom accent bar.
2. **Executive Summary / SCQA Synthesis**: 4 stacked cards (Situation, Complication, Question, Answer) + 3 large KPI callouts.
3. **3-Column Typology / Card Matrix**: 3 equal-width comparison cards with colored header bands.
4. **2×2 Risk & Prioritization Matrix**: 4 severity quadrants with Likelihood and Impact directional axes.
5. **5-Stage Process Flow**: Connected horizontal chevrons with protocol action cards below.
6. **Split Comparison Table**: Formatted comparison table with alternating tint rows.
7. **Regulatory Timeline Track**: Horizontal milestone bar with alternating above/below callouts.
8. **Case Study / Debrief**: 2-column split (Incident Facts vs. Root-Cause & Remediation).
9. **Phased Methodology / Gantt**: 3 horizontal workstream swimlanes with deliverable markers.
10. **Quantitative Waterfall Placeholder**: Framed chart placeholder with synthesis panel.

---

## Deployment & Usage

### PowerPoint Copilot
Upload the `skills/consulting-slide-creator` folder to your OneDrive/SharePoint Copilot skills library:
> *"Using consulting-slide-creator, design an executive summary slide on cloud modernization risks."*

### Google Antigravity IDE
Skills are auto-discovered from `.agents/skills/consulting-slide-creator/SKILL.md`:
> *"Use consulting-slide-creator to draft a 2x2 priority matrix slide for vendor risk."*

---

## License

MIT License.
