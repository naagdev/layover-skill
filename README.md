# 🌍 Optimal Layover Destination Design Skill

A powerful, reusable Claude skill for discovering the perfect layover destination (2-6 days in 1-2 countries) tailored to individual preferences using multi-agent AI orchestration.

## Features

✨ **Smart Progressive Questioning** — Haiku asks adaptive questions based on answers
✨ **Complexity Detection** — Auto-escalates to Sonnet when decisions are complex
✨ **Research-Backed Recommendations** — Analyzes Reddit, TripAdvisor, Rick Steves forums
✨ **Destination Clustering** — Groups 5-7 optimal destination pairs, not just cities
✨ **Transparent Scoring** — Weighted decision framework with clear trade-offs
✨ **YouTube Integration** — Curated, quality-filtered travel videos for each destination
✨ **Real Transport Pricing** — Flight, train, bus options with actual costs
✨ **Direct Booking Links** — Google Flights, Skyscanner, Raileurope, etc.
✨ **Budget Breakdown** — Shows per-person costs + remaining budget
✨ **Interactive Comparison** — Visual tool comparing top 3-5 recommendations

## How It Works

```
PHASE 1: Progressive Questioning (Haiku-Led)
├─ Basics: trip duration, countries, dates, experience level
├─ Adaptive: conditional questions based on answers
└─ Complexity Check: escalates to Sonnet if ambiguous

PHASE 2: Complexity Resolution (Sonnet)
└─ Frames clarifying questions when trade-offs exist

PHASE 3: Preferences Deep-Dive (Haiku-Led)
├─ Vibe & experience
├─ Safety & authenticity priority
├─ Budget & logistics
└─ Companion interests & constraints

PHASE 4: Research & Clustering (Sonnet-Led)
├─ Searches Reddit, forums, travel blogs
├─ Identifies 15-20 destination candidates
├─ Groups into 5-7 optimal clusters
└─ Scores on 10 factors (safety, budget, transport, uniqueness, etc.)

PHASE 5: Final Recommendation (Opus Decision-Making)
├─ Evaluates clusters with weighted framework
├─ Ranks top 3 recommendations
├─ Provides YouTube videos for each
├─ Shows transport options & pricing
└─ Generates interactive comparison tool
```

## Quick Start

### For Individual Users

```
1. Ask Claude: "Help me plan my layover before going to [destination]"
2. Respond to Haiku's progressive questions
3. Watch the skill cluster destinations and research options
4. Review Opus's ranked recommendations with YouTube videos
5. Choose your destination and get booking links
```

### For Developers

```bash
# Clone the repository
git clone https://github.com/yourusername/layover-skill.git
cd layover-skill

# Install dependencies (if using as API)
# See IMPLEMENTATION.md for setup instructions

# View the skill documentation
cat SKILL.md
```

## File Structure

```
layover-skill-package/
├── README.md                 # This file
├── SKILL.md                  # Full skill specification & architecture
├── IMPLEMENTATION.md         # Technical setup & API integration
├── PROMPTS.md                # Haiku/Sonnet/Opus system prompts
├── EXAMPLES.md               # Real-world usage examples
├── requirements.txt          # Dependencies (if applicable)
├── LICENSE                   # MIT License
└── tests/
    └── test_skill.py         # Unit tests for skill components
```

## Usage Examples

### Example 1: Traveler with International Connection
**Input:** 5-6 days before international travel, companion loves photography, avoid scams, historic culture

**Output:** Vienna + Budapest recommended with:
- 5 curated YouTube videos
- Train pricing: $35-70 per person
- Flight pricing: $250-600 per person
- Budget breakdown
- Booking links

### Example 2: First-Time Europe Solo Traveler
**Input:** 4 days, single traveler, first time Europe, budget-conscious, adventure-focused

**Output:** Prague + Budapest or Krakow + Budapest with:
- Safety analysis
- Budget optimization
- Active/adventure activity recommendations
- Local transportation tips

## Integration Methods

### Method 1: Direct Claude.ai Usage (Easiest)
1. Copy SKILL.md content
2. Share with Claude
3. Follow the interactive flow

### Method 2: Claude API Integration
See `IMPLEMENTATION.md` for:
- REST API endpoint setup
- System prompt configuration
- Multi-agent orchestration
- Response formatting

### Method 3: Embed in Custom App
Use the prompts and logic in `PROMPTS.md` to build custom UIs on top of the skill

## Key Features Explained

### Progressive Questioning
Unlike standard questionnaires, Haiku asks follow-up questions based on your answers:
- Simple preferences → straight to next phase
- Conflicting preferences → escalates to Sonnet for clarification
- Unusual constraints → Sonnet frames better questions

### Destination Clustering
Instead of recommending individual cities, the skill groups optimal 2-country pairs:
- Geographic proximity (easy transport)
- Complementary vibes
- Similar safety/authenticity profiles
- Budget alignment

### YouTube Video Curation
Recommends 15-20 specific videos categorized by:
- **Watch First** — Overview & orientation (20-30 min)
- **Deep Dive** — Specific interests like photography, food, safety (30-45 min)
- **Practical** — Scams to avoid, transport tips, logistics (10-15 min)
- **Aesthetic** — Inspiration & beautiful locations (10-20 min)

Filtering ensures:
- Published within 12 months (current information)
- 100K+ views (crowd-tested)
- Recent comments confirming tips are still valid

### Real Transport Pricing
Includes:
- International flights: $250-600 USD per person
- Inter-city trains: $30-100 USD per person
- Budget buses: $15-50 USD per person
- Direct booking links with live pricing

### Budget Breakdown
Shows exactly where your money goes:
```
International flights:    $500-1,200
Inter-city transport:     $35-100
Local transport:          $50-100
Hotels (est.):            $400-800
Food & activities:        $215-865 (remaining)
────────────────────────────────────
TOTAL:                    $1,500-3,000
```

## Weighted Scoring Framework

Final recommendations evaluated on:

| Factor | Weight | Example |
|--------|--------|---------|
| Safety & Scam Avoidance | 30% | Vienna: 9.5/10 |
| Authentic Culture | 25% | Budapest: 8.5/10 |
| Budget Fit | 15% | Both: 8.5/10 |
| Girlfriend/Companion Match | 15% | Museums, photography: 8.5/10 |
| Logistics & Transport | 10% | 2.5-hour train: 9.0/10 |
| Crowds & Uniqueness | 5% | Less touristy than Prague: 8.0/10 |

## Research Sources

The skill pulls insights from:
- **Reddit**: r/travel, r/backpacking, r/solotravel, city-specific subreddits
- **TripAdvisor**: Trip Forums, reviews, traveler experiences
- **Rick Steves**: Travel Forums (culture-focused discussions)
- **Nomad List**: Digital nomad perspectives, cost data
- **YouTube**: Travel vlogs analyzed for quality & relevance
- **Booking Platforms**: Real flight/train pricing data

## Customization

### For Different Use Cases

**Solo Travelers:**
- Emphasize safety
- Highlight solo-friendly activities
- Focus on social/nightlife options

**Couples:**
- Highlight romantic experiences
- Include date night recommendations
- Suggest intimate activities

**Families:**
- Prioritize kid-friendly activities
- Consider napping/rest times
- Recommend family-oriented transport

**Budget Travelers:**
- Maximize cost optimization
- Recommend free activities
- Suggest local food spots over restaurants

**Luxury Travelers:**
- Recommend upscale experiences
- Include spa/wellness options
- Suggest private guides

Edit `PROMPTS.md` to customize for your audience.

## Limitations & Future Enhancements

### Current Limitations
- Requires user input (not fully autonomous)
- YouTube videos may become outdated
- Transport pricing changes seasonally

### Future Enhancements
- [ ] Seasonal optimization ("Best time to visit for X")
- [ ] Visa/documentation automation
- [ ] Real-time pricing integration
- [ ] Traveler matching ("89% like you chose this")
- [ ] Auto-generate 5-6 day itineraries
- [ ] Activity pre-booking integration
- [ ] Travel insurance recommendations
- [ ] Meal planning with restaurant links

## Contributing

Contributions are welcome! Areas we need help with:

1. **Video Database** — Add more curated YouTube videos for destinations
2. **Pricing Data** — Help update flight/train/bus price ranges
3. **Destination Expansion** — Add clusters for Asia, Americas, Africa
4. **UI/UX** — Build interactive web interface for the skill
5. **Testing** — Add unit & integration tests
6. **Documentation** — Improve guides & examples

## License

MIT License — Feel free to use, modify, and distribute!

## Support & Feedback

- **Found a bug?** Open an issue
- **Have a feature idea?** Submit a discussion
- **Want to contribute?** Fork the repo and submit a PR
- **Need help?** Check EXAMPLES.md or open a discussion

## Citation

If you use this skill in your project, please cite:

```bibtex
@software{layover_skill_2025,
  title = {Optimal Layover Destination Design Skill},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/yourusername/layover-skill}
}
```

## Status

✅ **Skill v1.0 Released** — Fully functional
🚀 **Active Development** — New features planned
💬 **Community Driven** — Your feedback shapes the roadmap

---

**Made with ❤️ for travelers who want to discover the perfect layover destination**
