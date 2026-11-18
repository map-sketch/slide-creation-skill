---
name: consulting-slide-creator
description: >-
  Guides the agent to design and author standalone consulting slides and complete executive presentations
  using structured storyline mechanics and executive visual design tokens. Use this skill when the user
  asks to create, draft, design, or layout any standalone slide, slide blueprint, executive summary,
  process flow, matrix, or comparison visual.
---

## When to Activate

The agent should activate this skill when the user:

- Asks to create a **standalone slide** or single visual artifact (e.g., "build me a slide on cloud migration risks", "create a 2x2 matrix slide", "draft an executive summary slide").
- Requests a **slide blueprint**, layout wireframe, or structured outline for any business, technology, risk, or strategic presentation.
- Asks for advice on which **visual layout archetype** best represents a specific business problem, data breakdown, or strategic process.
- Wants to translate raw bullet points, meeting notes, or unstructured data into an executive-ready slide format compliant with top-tier management consulting standards.

---

## The Non-Negotiable Anatomy of a Consulting Slide

Every standalone slide crafted with this skill consists of four mandatory vertical zones:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. ACTION TITLE ZONE (Top, 20–22pt Bold, Left-Aligned + Accent Green Dot)  │
│    Subtitle / Core Takeaway Line (12pt Cool Gray 11)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. STRUCTURED BODY GRID (Governed by 1 of 10 Layout Archetypes)             │
│    - 16:9 Widescreen Canvas (13.333" × 7.5")                                │
│    - Margins: Left 0.5", Right 0.5", Top 0.9", Bottom 0.5"                  │
│    - Bullets strictly <= 15 words; MECE grouping; bold anchor words         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. SOURCE FOOTER (Bottom-Left, Y=6.9", 8.5pt Cool Gray 11)                  │
│    "Source: [Author / Organization], [Report / System], [Year]"             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. SLIDE NUMBER (Bottom-Right, Y=6.9", 8.5pt Cool Gray 11)                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Action Title Rule

Never use passive, descriptive topic headers. Every slide title must be an **Action Title**:
- ❌ **Topic Title (Forbidden)**: *Cloud Migration Challenges*
- ✅ **Action Title (Required)**: *Legacy architecture and compliance silos delay enterprise cloud migration by an average of 9 months.*
- ❌ **Topic Title (Forbidden)**: *Vendor Spend Analysis*
- ✅ **Action Title (Required)**: *Top three third-party suppliers represent 68% of unmonitored accounts payable disbursements.*

> [!IMPORTANT]
> Every Action Title MUST end with a terminal period (`.`). In visual rendering, this period is colored in **Accent Green (`#86BC25`)**.

### The Source Footer Rule

Every slide presenting empirical figures, industry benchmarks, or internal metrics MUST include a bottom attribution line:
- Format: `Source: [Data Source or Internal System], [Year / Timeframe]`
- Example: `Source: Enterprise ERP Database Extracts, FY2024–FY2026; Industry Benchmark Study`

---

## Visual Design Tokens Reference

When generating slide specifications or code, adhere strictly to these parameters:

| Element | Specification | Value / Hex Code |
|---|---|---|
| **Canvas Ratio** | 16:9 Widescreen | 13.333" Width × 7.5" Height |
| **Primary Black** | Slide headers, cover background | `#000000` |
| **Canvas White** | Content slide background, white cards | `#FFFFFF` |
| **Accent Green** | Action Title terminal dot, primary accent bar, active stage | `#86BC25` |
| **Mid Green** | Secondary accent, positive status, low-risk | `#26890D` |
| **Cool Gray 11** | Subtitles, body text, footer attribution | `#53565A` |
| **Cool Gray 2** | Card borders, table grid lines, connecting stems | `#D0D0CE` |
| **Tint** | Card fill, alternating table row shading | `#F5F6F7` |
| **Chart Teal** | Series 1, card header accent 1 | `#0097A9` |
| **Chart Blue** | Series 2, card header accent 3 | `#0076A8` |
| **Font Family** | Primary: `Aptos` \| Fallback: `Calibri` \| Safe: `Open Sans` | System Standard |

---

## The 10 Consulting Layout Archetypes

Match the user's objective to the exact visual archetype:

### 1. Cover Slide (Executive Hero)
- **Best For**: Presentation kickoff, major project milestones, board presentations.
- **Visual Mechanics**: Solid black background (`#000000`), practice kicker in Accent Green, large 36pt title with green period, 14pt subtitle, metadata block, and full-width bottom green accent bar (0.12" height).

### 2. Executive Summary / SCQA Synthesis
- **Best For**: High-level alignment, steering committee briefings, project kickoffs.
- **Visual Mechanics**: Split layout. Left 60% contains 4 stacked cards for Situation, Complication, Question, and Answer. Right 40% contains 3 prominent KPI callout blocks (36pt bold metric + label + explanation).

### 3. 3-Column Typology / Comparative Matrix
- **Best For**: Categorizing schemes, comparing options, classifying risk domains, 3-pillar strategies.
- **Visual Mechanics**: Three equal-width cards on `#F5F6F7` tint with colored top header bands (Teal, Mid Green, Blue), frequency/impact badge, and 4 structured bullet points per column.

### 4. 2x2 Risk & Prioritization Matrix
- **Best For**: Prioritizing initiatives, assessing risks, mapping market positioning.
- **Visual Mechanics**: Four colored quadrants (Amber top-left, Red top-right, Green bottom-left, Yellow bottom-right) anchored by Likelihood (Y-axis) and Impact (X-axis) directional indicators.

### 5. 5-Stage Process Flow / Lifecycle
- **Best For**: Operational runbooks, investigation lifecycles, customer journeys, implementation roadmaps.
- **Visual Mechanics**: Five horizontal chevrons across the canvas. Active or initial stage highlighted in Accent Green; subsequent stages in Cool Gray 2. Structured action cards positioned beneath each chevron.

### 6. Split Comparison Table
- **Best For**: Red Flags vs. Control Gaps, Current State vs. Future State, Pros vs. Cons.
- **Visual Mechanics**: Formatted 3-column table (Category, Column A, Column B) with black header row, white bold text, and alternating `#F5F6F7` tint rows.

### 7. Regulatory & Milestone Timeline
- **Best For**: Multi-year enforcement history, regulatory compliance evolution, corporate transformation history.
- **Visual Mechanics**: Continuous horizontal center axis with circular milestone nodes, alternating above-and-below callout cards connected by thin vertical stems.

### 8. Case Study & Root-Cause Debrief
- **Best For**: Incident reviews, post-mortems, forensic investigations, training lessons.
- **Visual Mechanics**: 2-column split layout. Left panel: Incident Facts (black banner header). Right panel: Root-Cause Analysis & Remediation (green banner header).

### 9. Phased Methodology & Deliverables Grid
- **Best For**: Project proposals, 12-week workplans, multi-phase transformation roadmaps.
- **Visual Mechanics**: Three distinct phase columns (Phase 1, Phase 2, Phase 3), each displaying timeline duration, workstream bullet points, and an enclosed deliverable box at the bottom.

### 10. Quantitative Chart Placeholder + Synthesis Callout
- **Best For**: Financial waterfall analysis, volume distribution, cost leakage bridges.
- **Visual Mechanics**: Framed 8.5" chart placeholder on left with axis watermarks; 3.5" callout panel on right synthesizing key quantitative takeaways.

---

## Step-by-Step Slide Creation Protocol

When asked to create a standalone slide, follow this 6-step protocol:

1. **Clarify Objective & Target Audience**: Determine who is viewing the slide (Board, General Counsel, Operating Team) and the single core decision required.
2. **Select the Archetype**: Pick the layout archetype from the 10 options above that best fits the data shape.
3. **Draft the Action Title**: Apply the "So What?" test. State the primary empirical or strategic finding as an assertive sentence ending with a period.
4. **Structure Body Content using MECE**:
   - Ensure points are Mutually Exclusive and Collectively Exhaustive.
   - Limit bullets to 3–5 items per section.
   - Restrict each bullet to <= 15 words.
   - Bold the first 2–4 anchor words of each bullet for scannability.
5. **Assign Visual Tokens**: Specify exact hex colors, card dimensions, and layout coordinates.
6. **Ground with Source Attribution**: Provide a realistic, defensible source line. Never fabricate empirical statistics; use bracketed tokens like `[INSERT ERP EXTRACT DATE]` if unverified.

---

## Standard Slide Blueprint Output Template

When outputting a slide design for the user, use this standardized markdown format:

```markdown
### Slide Blueprint: [Slide Title]
- **Target Archetype**: Archetype [X] ([Archetype Name])
- **Canvas Aspect Ratio**: 16:9 Widescreen (13.333" × 7.5")

#### Header Zone
- **Action Title**: [Assertive takeaway sentence ending with a period.]
- **Subtitle**: [1-sentence takeaway contextualizing the analytical finding.]

#### Layout Grid Specifications
- **Left Column / Zone**: [Dimensions & content elements]
- **Center / Right Zone**: [Dimensions & content elements]
- **Key Visual Elements**: [Chevrons / Quadrants / Tables / KPI blocks with token hex colors]

#### Body Content (MECE Structured)
- **[Category 1]**:
  - **[Anchor Words]**: [Crisp assertion <= 15 words]
  - **[Anchor Words]**: [Crisp assertion <= 15 words]
- **[Category 2]**:
  - **[Anchor Words]**: [Crisp assertion <= 15 words]

#### Footer Zone
- **Source Citation**: Source: [Organization / Publication / Database], [Year]
- **Slide Number**: [X]
```

---

## Quality Checklist Before Finalizing Any Slide

- [ ] Action Title answers "So what?" and ends with a period (`.`).
- [ ] Subtitle provides supporting context without duplicating the title.
- [ ] Body content strictly follows one of the 10 consulting archetypes.
- [ ] Bullet points are <= 15 words each with bold anchor words.
- [ ] Categories satisfy the MECE principle (no overlap, no gaps).
- [ ] Colors strictly follow the consulting palette tokens (`#86BC25`, `#000000`, `#53565A`, `#F5F6F7`).
- [ ] Bottom `Source:` footer is present and properly formatted.
- [ ] Zero fabricated figures, fake percentages, or simulated client names.
