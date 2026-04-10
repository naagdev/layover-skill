# Setup & Deployment Guide

Complete instructions for pushing the skill to GitHub and registering as a Claude skill.

---

## Step 1: Push to GitHub

### Option A: Create New GitHub Repository

1. **Create repo on GitHub.com**
   - Go to github.com/new
   - Repository name: `layover-skill` (or your preferred name)
   - Description: "AI-powered layover destination planner using multi-agent framework"
   - Choose Public or Private
   - Click "Create repository"

2. **Add remote and push**

```bash
cd /path/to/layover-skill-package

# Add GitHub as remote
git remote add origin https://github.com/yourusername/layover-skill.git

# Rename branch to main (optional but recommended)
git branch -M main

# Push to GitHub
git push -u origin main
```

3. **Verify push**
   - Visit https://github.com/yourusername/layover-skill
   - Should see all files uploaded ✓

### Option B: Push to Existing Repository

```bash
cd /path/to/layover-skill-package

# Add existing repo as remote
git remote add origin https://github.com/yourusername/existing-repo.git

# Push this skill as subdirectory
git subtree push --prefix layover-skill origin main

# Or merge as folder
git remote add layover-origin https://github.com/yourusername/layover-skill.git
git push layover-origin main
```

---

## Step 2: Add as Claude Skill to Claude.ai

### For Claude.ai Users

1. **Access Skills Directory** (Coming soon with Claude.ai update)
   - Go to claude.ai → Settings → Skills
   - Click "Browse Skills"
   - Search "Layover Destination"
   - Click "Add to Claude"

2. **Or Import Manually**

   a. **Copy the GitHub raw content link:**
      ```
      https://raw.githubusercontent.com/yourusername/layover-skill/main/SKILL.md
      ```

   b. **In Claude.ai:**
      - Go to Settings → Import Skill
      - Paste URL above
      - Click "Import"

   c. **Or paste SKILL.md content directly:**
      - Copy SKILL.md content
      - In Claude.ai, paste: "I have a skill definition. Here it is:"
      - Paste SKILL.md
      - Claude learns the skill

### For Claude API Users

Reference in your API calls:

```python
from anthropic import Anthropic

client = Anthropic()

# Load skill definition from file or URL
with open('SKILL.md', 'r') as f:
    skill_definition = f.read()

# Use in system prompt
response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    system=f"""You are a layover destination planning assistant.

Here's the skill specification:
{skill_definition}

When users ask for help planning a layover, follow this framework...""",
    messages=[{"role": "user", "content": "Help me plan my Europe layover"}]
)

print(response.content[0].text)
```

---

## Step 3: Register with Claude Skills Registry (Official)

### Submit to Anthropic Skills Registry

1. **Prepare skill metadata:**

Create `skill-manifest.json`:

```json
{
  "id": "layover-destination-planner",
  "name": "Optimal Layover Destination Planner",
  "version": "1.0.0",
  "description": "AI-powered skill for discovering perfect 2-6 day layover destinations using multi-agent framework",
  "author": "Your Name",
  "license": "MIT",
  "repository": "https://github.com/yourusername/layover-skill",
  "documentation": "https://github.com/yourusername/layover-skill#readme",
  "categories": ["travel", "planning", "recommendations"],
  "tags": ["layover", "destination", "multi-agent", "youtube", "transport-pricing"],
  "models_supported": ["claude-3-5-haiku", "claude-3-5-sonnet", "claude-opus-4"],
  "interaction_type": "multi-turn_conversation",
  "features": [
    "Progressive adaptive questioning",
    "Complexity detection and escalation",
    "Reddit/forum research",
    "Destination clustering",
    "YouTube video curation",
    "Real transport pricing",
    "Budget breakdowns",
    "Interactive comparisons"
  ],
  "estimated_duration": "15-20 minutes",
  "success_metrics": [
    "User feels understood",
    "Recommendation matches preferences",
    "Clear trade-offs explained",
    "Actionable next steps"
  ]
}
```

2. **Submit to skills registry:**

```bash
# Visit Anthropic Developer Console
# https://console.anthropic.com/skills

# Or submit via email:
# skills@anthropic.com
# Subject: "Skill Submission: Optimal Layover Destination Planner"
# Attach skill-manifest.json and skill repository link
```

3. **What Anthropic reviews:**
   - ✓ Code quality and documentation
   - ✓ User value and uniqueness
   - ✓ Safety and ethical considerations
   - ✓ Performance and reliability
   - ✓ Community benefit

---

## Step 4: Set Up Continuous Integration

### GitHub Actions for Testing

Create `.github/workflows/test.yml`:

```yaml
name: Test Layover Skill

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ -v
      - name: Check code quality
        run: |
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          black --check .
```

### GitHub Actions for Documentation

Create `.github/workflows/docs.yml`:

```yaml
name: Build Documentation

on: [push]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build README
        run: |
          # Auto-generate table of contents
          python scripts/generate_toc.py
      - name: Validate markdown
        run: |
          # Check for broken links, formatting
          markdownlint "*.md"
```

---

## Step 5: Create Release

### Version and Tag

```bash
cd /path/to/layover-skill

# Update version in skill-manifest.json
# Edit version: "1.0.0" → "1.1.0"

# Commit
git add skill-manifest.json
git commit -m "Bump version to 1.1.0"

# Create tag
git tag -a v1.1.0 -m "Release 1.1.0: YouTube integration + transport pricing"

# Push tag
git push origin v1.1.0
```

### Create GitHub Release

1. Go to https://github.com/yourusername/layover-skill/releases
2. Click "Draft a new release"
3. Select tag: `v1.1.0`
4. Fill in release notes:

```markdown
# Layover Destination Skill v1.1.0

## Features
- Multi-agent framework (Haiku, Sonnet, Opus)
- Progressive adaptive questioning
- YouTube video curation
- Real transport pricing integration
- Destination clustering
- Budget breakdowns

## What's New in 1.1.0
- Added YouTube video research protocol
- Integrated real-time transport pricing
- Enhanced scoring with 10 factors
- New PROMPTS.md documentation
- Real-world examples added

## Installation
```bash
git clone https://github.com/yourusername/layover-skill.git
pip install -r requirements.txt
```

## Usage
See README.md for quick start and examples

## Contributors
- Your Name (@yourusername)
- [Invite community contributions]

## License
MIT
```

---

## Step 6: Promote & Community

### Share the Skill

1. **Twitter/X:**
   ```
   🌍 Released: Optimal Layover Destination Planner Skill

   Multi-agent AI framework finds your perfect 2-6 day layover using:
   • Adaptive questioning (Haiku)
   • Research + clustering (Sonnet)  
   • Final recommendations (Opus)
   • YouTube curation
   • Real transport pricing

   👉 github.com/yourusername/layover-skill
   ```

2. **Reddit:**
   - Post to r/travel, r/backpacking, r/solotravel
   - Post to r/machinlearning, r/anthropic
   - Post to community subreddits

3. **Dev Communities:**
   - Hacker News: https://news.ycombinator.com/submit
   - Product Hunt: https://www.producthunt.com
   - Awesome Lists: Add to awesome-ai, awesome-tools

4. **Documentation Sites:**
   - GitHub Pages: Enable in repo settings
   - Read the Docs: https://readthedocs.org
   - Skill Directory Listings

---

## Step 7: Maintenance & Updates

### Regular Updates Checklist

- [ ] Monthly: Check if destination data (YouTube videos, pricing) needs refresh
- [ ] Quarterly: Test skill with new Anthropic models
- [ ] Quarterly: Review GitHub issues and community feedback
- [ ] Yearly: Major feature update (seasonal optimization, visa automation, etc.)

### Create Contributing Guidelines

Create `CONTRIBUTING.md`:

```markdown
# Contributing to Layover Destination Skill

## Ways to Contribute

1. **Add YouTube Videos**
   - Submit new travel videos for destinations
   - Update existing video links

2. **Update Pricing Data**
   - Share real flight/hotel prices
   - Update budget estimates

3. **Add Destination Clusters**
   - Research new 2-country combinations
   - Share unique pairings

4. **Improve Documentation**
   - Fix typos, clarify instructions
   - Add new examples

5. **Report Bugs**
   - Issues with recommendations
   - Broken booking links

## How to Contribute

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Make changes
4. Commit: `git commit -m "Add: [feature description]"`
5. Push: `git push origin feature/your-feature`
6. Create Pull Request

## Code Style
- Python: Black formatting, type hints
- Markdown: 80-character line limit
- JSON: 2-space indentation

## Community Standards
- Be respectful and inclusive
- Focus on traveler value
- Share knowledge generously
```

---

## Troubleshooting

### "Git push fails with authentication error"

```bash
# Use SSH instead of HTTPS
git remote remove origin
git remote add origin git@github.com:yourusername/layover-skill.git
git push -u origin main
```

### "Skill doesn't work in Claude.ai"

1. Check SKILL.md formatting (valid markdown)
2. Verify prompts are complete (check PROMPTS.md)
3. Test with Claude API first (simpler debugging)
4. Open issue on GitHub for help

### "Recommended destination doesn't match my preferences"

Add feedback mechanism to EXAMPLES.md or GitHub issues to improve the skill based on real usage.

---

## Success Checklist

- [ ] Repository created on GitHub
- [ ] All files committed and pushed
- [ ] README visible and clear on GitHub
- [ ] Skill-manifest.json prepared
- [ ] Documentation complete (all .md files)
- [ ] Tests passing (if applicable)
- [ ] License (MIT) properly attributed
- [ ] Shared on social/communities
- [ ] Anthropic skills registry notified (optional)
- [ ] First 5 users tested and feedback gathered

---

## Next Steps

1. **Use the skill:** Test it with different user profiles
2. **Gather feedback:** Ask early users for improvements
3. **Iterate:** Update based on feedback
4. **Expand:** Add new destinations, features, languages
5. **Teach:** Share how it works in blog posts
6. **Collaborate:** Invite contributors to improve it

---

**Your skill is now ready for the world! 🚀**

Questions? Create an issue on GitHub or reach out to the community.
