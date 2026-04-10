# 🌍 Optimal Layover Destination Design Skill

## Overview
A robust, multi-agent framework for discovering the perfect layover destination (2-6 days in 1-2 countries) tailored to individual preferences. Uses Haiku for progressive questioning, Sonnet for complexity detection and research, and Opus for final recommendation.

---

## Framework Architecture

### Phase 1: Adaptive Preference Gathering (Haiku-Led)
**Goal**: Understand traveler's profile through progressive, dependent questions

#### Initial Context Questions (Haiku asks 3-4)
- **Trip Duration**: "How many days do you have for this layover? (2-3 / 4-5 / 5-6 / flexible)"
- **Number of Countries**: "Prefer staying in 1 country or exploring 2?"
- **Travel Dates**: "When are you traveling? (specific month important for weather/crowds)"
- **First-time Europe Indicator**: "Is this your first time in Europe?"

#### Adaptive Follow-up (Haiku asks 2-3, dependent on answers)
- **If interested in 2 countries**: "How important is easy commute between them?" (train/flight preference)
- **If flexible duration**: "What's your soft/hard deadline?"
- **If first-timer**: "Any specific regions calling you?" (Europe location preferences)

#### Complexity Detection (Haiku self-assesses)
**Haiku decision tree:**
- ✓ Clear answers, simple preferences → Continue to preferences gathering
- ✗ Conflicting priorities (e.g., "want adventure AND relaxation equally") → **ESCALATE TO SONNET**
- ✗ Ambiguous answers (e.g., "not sure what I like") → **ESCALATE TO SONNET**
- ✗ Unusual constraint combinations → **ESCALATE TO SONNET**

**Escalation Prompt for Sonnet:**
```
User's responses show complexity in [specific area].
Current understanding: [summary]
Conflicting signals: [details]
Please frame a clarifying question that helps narrow this down.
```

---

### Phase 2: Preferences Deep-Dive (Haiku-Led, Sonnet-Supported)

#### Vibe & Experience Questions (Haiku asks 3-4)
- "What appeals most for this layover?"
  - Historic cities & culture / Beach & relaxation / Adventure & nature / Food & wine / Modern cities / Mix of everything
  
- "How important is your travel companion's interests?"
  - "Tell me about them (interests, preferences)"
  
- "Daily activity pace preference?"
  - Relaxed (2-3 activities/day) / Moderate (3-5) / Fast-paced (see everything)

#### Safety & Authenticity Questions (Haiku asks 2)
- "How important is avoiding scams/tourism traps?"
  - Not important / Somewhat / Very important / Critical
  
- "Authentic local experience vs. comfort/convenience?"
  - Prioritize authenticity / Balance both / Prioritize comfort

#### Budget & Logistics (Haiku asks 2)
- "Budget for this layover?"
  - Budget ($500-1K) / Mid-range ($1K-2.5K) / Luxury (2.5K+)
  
- "Any cities/countries to avoid or MUST visit?"
  - (Open response)

#### Complexity Re-Check (Haiku evaluates)
- If responses contradict (e.g., "want authentic AND luxury, avoid scams AND visit Prague")
  - → **Escalate to Sonnet for clarification**
  - Sonnet frames: "I'm seeing you want both A and B—which matters more? Why?"

---

### Phase 3: Research & Destination Clustering (Sonnet-Led)

**Trigger**: Once all preferences gathered + no more complexity escalations

#### Sonnet's Research Mission
```json
{
  "task": "Research optimal layover destinations matching user profile",
  "method": "Search Reddit r/travel, TripAdvisor forums, Rick Steves forums, Nomad List",
  "criteria": {
    "safety": "user's safety priority",
    "scams": "user's scam-avoidance priority",
    "culture_authenticity": "user's authenticity priority",
    "budget": "user's budget",
    "crowd_level": "user's pace/crowd preference",
    "logistics": "commute time, transport ease",
    "specific_interests": "girlfriend/travel_companion interests"
  }
}
```

#### Sonnet's Analysis Output
For each destination cluster, Sonnet identifies:
1. **Safety Rating** (based on forum consensus)
2. **Scam Risk** (documented experiences)
3. **Authentic Culture Score** (locals vs tourists ratio)
4. **Girlfriend Interest Match** (% alignment with stated interests)
5. **Budget Alignment** (expected cost vs stated budget)
6. **Crowd Level** (peak vs relaxed season)
7. **Logistical Ease** (commute time, transport options)
8. **Uniqueness Score** (how different from mainstream recommendations)

#### Destination Clusters (5-7 options)
Sonnet groups similar destinations and rates each cluster:
```
Cluster A: Vienna + Budapest
- Safety: 9.5/10 | Scams: 10/10 | Authentic: 9/10 | Budget: 8/10 | Crowds: 8/10 | Unique: 8/10

Cluster B: Barcelona + Lisbon
- Safety: 7.5/10 | Scams: 7/10 | Authentic: 6/10 | Budget: 5/10 | Crowds: 4/10 | Unique: 7/10

... (continue for all clusters)
```

---

### Phase 4: Final Recommendation (Opus Decision-Making)

**Opus's Mission**: "Plan Mode" evaluation across clusters

#### Opus's Evaluation Framework
```json
{
  "decision_criteria": {
    "alignment_with_stated_goals": "40%",
    "safety_and_authenticity": "30%",
    "budget_fit": "15%",
    "logistical_feasibility": "10%",
    "uniqueness_and_surprise": "5%"
  }
}
```

#### Opus's Output
1. **Primary Recommendation** (ranked #1 cluster)
   - Why it's the best fit for THIS user specifically
   - How it aligns with their values/preferences
   - Potential challenges and how to mitigate

2. **Alternative Recommendations** (ranked #2 and #3)
   - When to choose each alternative
   - Trade-offs vs primary recommendation

3. **Detailed Reasoning** (transparent decision logic)
   - Weighted scoring for each cluster
   - Key differentiators
   - Research citations (which forums/sources informed decision)

4. **Quick-Start Comparison Tool**
   - Interactive visual comparing top 3-5 clusters
   - User can click to explore alternatives

---

## Implementation: Progressive Question Flow

### Pseudo-Code for Haiku's Question Engine

```
FUNCTION ask_adaptive_questions(user_profile):
  
  // Phase 1: Basics (always ask)
  trip_duration = ask_question("How many days? (2-3 / 4-5 / 5-6 / flexible)")
  country_count = ask_question("1 country or 2?")
  travel_dates = ask_question("When? (specific month/dates)")
  first_timer = ask_question("First time Europe? Yes/No")
  
  // Phase 2: Conditional logic
  IF country_count == "2":
    commute_pref = ask_question("Transport preference? (train/flight/flexible)")
  
  IF trip_duration == "flexible":
    min_days = ask_question("Minimum days?")
    max_days = ask_question("Maximum days?")
  
  // Phase 3: Preferences
  vibe = ask_question("Vibe appeal? [list 6 options]")
  
  // Complexity check
  IF vibe contains conflicting elements:
    ESCALATE_TO_SONNET(user_profile, vibe, "Clarify priority: A or B?")
    vibe = receive_sonnet_clarification()
  
  companion = ask_question("Tell me about your travel companion")
  
  pace = ask_question("Pace? (relaxed/moderate/fast)")
  
  // Phase 4: Safety & Authenticity
  safety_priority = ask_question("Scam avoidance importance? (not/somewhat/very/critical)")
  
  authenticity = ask_question("Authentic culture vs comfort? (authenticity/balance/comfort)")
  
  // Phase 5: Budget & Specifics
  budget = ask_question("Budget? (budget/mid/luxury)")
  
  constraints = ask_question("Must visit / avoid any cities?")
  
  // Complexity re-check
  IF contradictions_detected(user_profile):
    ESCALATE_TO_SONNET(user_profile, "Resolve contradictions")
    clarifications = receive_sonnet_clarifications()
  
  RETURN user_profile (complete)

END FUNCTION
```

---

## Escalation Protocol (Haiku → Sonnet)

### When to Escalate
1. **Conflicting preferences** (wants both A and B equally)
2. **Vague responses** ("I'm not sure" / "whatever feels right")
3. **Unusual constraint combinations** (wants authentic + luxury + budget)
4. **Ambiguous reasoning** (multiple interpretations possible)

### Sonnet's Clarification Approach
**Goal**: Frame ONE clear, high-impact question that resolves ambiguity

**Template:**
```
"I'm seeing two pulls here:
1. You want [preference A] (you said: [evidence])
2. But also [preference B] (you said: [evidence])

These sometimes trade off. For YOU specifically, if you had to choose, which matters more and why?"
```

**Then continue loop** with Haiku asking next question

---

## Research Protocol (Sonnet-Led)

### Forums to Search
- Reddit: r/travel, r/backpacking, r/solotravel, city-specific subreddits
- TripAdvisor: Trip Forums for specific cities
- Rick Steves: Travel Forums (culture-focused discussions)
- Nomad List: Digital nomad perspectives (cost, community, lifestyle)

### Search Queries per Destination
- "[City] first time? What should I know?" (authentic experiences)
- "[City] scams? Avoid?" (safety concerns)
- "[City] solo/couples travelers?" (vibe & crowd)
- "[City 1] + [City 2] itinerary [X days]" (logistics confirmation)
- "[City] vs [competitor city]" (comparative analysis)

### Data to Extract (per destination)
- Safety consensus (crime rate, traveler experiences)
- Scam prevalence (specific scams documented, frequency)
- Authenticity factor (ratio of tourists to locals in main areas)
- Crowd levels (peak vs off-season experiences)
- Budget reality (actual costs from travelers, not guide estimates)
- Girlfriend-specific experiences (fashion, photography, food, art scenes)

---

## Clustering Algorithm (Sonnet)

### Step 1: Identify Candidates
From research, extract 15-20 top destinations matching user's basic criteria

### Step 2: Group into Clusters (2-country pairs)
- Geographic proximity (train/flight < 4 hours ideally)
- Complementary vibe (e.g., relaxation + adventure)
- Similar safety/authenticity profiles
- Budget alignment

**Example clustering:**
```
Cluster A (Safe, Authentic, Budget-Friendly, Central Europe):
  - Vienna + Budapest
  - Vienna + Prague
  - Prague + Budapest

Cluster B (Beach & Relaxation, Southern Europe):
  - Barcelona + Lisbon
  - Venice + Florence
  - Lisbon + Porto

Cluster C (Modern & Trendy, Western Europe):
  - Amsterdam + Berlin
  - Paris + Brussels
  - Barcelona + Valencia

Cluster D (Off-the-beaten-path, Emerging):
  - Krakow + Budapest
  - Lisbon + Porto + Sintra
  - Athens + Istanbul
```

### Step 3: Research Transport & YouTube Content (Sonnet)

#### Flight & Transport Research
For each cluster, Sonnet researches:
```json
{
  "research_queries": [
    "flights from [origin] to [city1] [dates] 2025",
    "train [city1] to [city2] time price",
    "[city1] public transport cost",
    "[destination pair] best transport reddit",
    "cheapest way [city1] [city2] comparison"
  ],
  "sources": [
    "Google Flights (current pricing)",
    "Skyscanner (price trends)",
    "Kayak (alerts & tracking)",
    "Trainline.eu / Omio (European trains)",
    "Blablacar (coach options)",
    "Reddit r/travel (real traveler costs)",
    "Nomad List (actual expenses)"
  ],
  "data_to_extract": {
    "flights": {
      "price_range": "$X - $Y per person",
      "duration": "travel time + airport time",
      "carriers": "budget vs full-service options",
      "timing": "early morning / evening options"
    },
    "trains": {
      "price_range": "$X - $Y per person",
      "duration": "door-to-door time",
      "frequency": "how many daily connections",
      "comfort": "seating class options"
    },
    "alternative_transport": {
      "bus": "price, duration, comfort",
      "driving": "car rental cost + gas + tolls",
      "rideshare": "Blablacar, Uber Ride options"
    }
  }
}
```

#### YouTube Content Research (Sonnet)
For EACH recommended destination cluster:

```
Search queries for YouTube:
- "[City1] travel guide first time [year]" (recent, authentic)
- "[City1] scams to avoid + tips" (practical security)
- "[City1] [girlfriend interest] guide" (fashion/art/photography specific)
- "[City1] local vs tourist [X hours]" (authentic experience)
- "[City1] day trip from [city2]" (logistics confirmation)
- "[City2] travel vlog [month]" (seasonal feel)
- "[City1] to [City2] how to travel guide" (transport logistics)
- "[Destination pair] [X days] itinerary" (similar trip reports)
```

**Quality Filtering**:
- ✓ Publish date: Last 12 months (current conditions)
- ✓ Channel type: Solo travelers, couples, budget travelers
- ✓ Length: 15-45 minutes (comprehensive but digestible)
- ✓ Engagement: 100K+ views (crowd-tested, reliable)
- ✓ Comments: Check for recent comments confirming tips still valid

**Video categorization for user**:
- "Watch First" (overview, 20-30 min)
- "Deep Dive" (specific interests, 30-45 min)
- "Practical" (scams, transport, logistics, 10-15 min)
- "Aesthetic" (photography, beautiful locations, 10-20 min)

### Step 4: Score Each Cluster (with Transport & Videos integrated)
Create weighted scoring matrix:

```
Scoring Matrix (example):

                    Vienna+Bud  Barcel+Lisbom  Amsterdam+Ber  Kraków+Bud
Safety              9.5         7.5            9.0           8.0
Scam Avoidance      10.0        7.0            9.5           8.5
Authenticity        9.0         6.5            7.0           8.5
Budget Fit          8.5         5.0            6.0           9.0
Girlfriend Match    8.5         9.0            7.5           8.0
Logistics Ease      9.0         8.0            4.0           8.5
Crowds              8.0         4.0            5.0           7.5
Uniqueness          8.0         7.0            6.0           9.0
Transport Cost      9.0         6.5            4.5           7.5
Video Quality       8.5         8.0            7.5           8.0

WEIGHTED SCORE:     8.95        6.96           6.80           8.35
```

---

## Opus's Decision Output Format

### Decision Report with Transport & Videos (3-5 clusters ranked)

```json
{
  "primary_recommendation": {
    "cluster": "Vienna + Budapest",
    "rank": 1,
    "weighted_score": 8.95,
    "why_best_for_this_user": "Perfectly balances your safety priority (zero scams in Vienna), authentic culture desire (locals live in center), girlfriend's interests (museums, thermal baths, photography), and budget-friendly reality. Only 2.5-hour train makes logistics effortless for 5-6 days. Transport costs are lowest in Europe.",
    
    "alignment_breakdown": {
      "safety_authenticity": "9.25/10 - Vienna has zero documented scams; Budapest unique culture",
      "girlfriend_interests": "8.5/10 - Art museums, thermal spas, photography opportunities",
      "budget_fit": "8.5/10 - Budapest especially cheap; stays in range",
      "logistical_feasibility": "9.0/10 - Direct train, perfect timing",
      "uniqueness": "8.0/10 - Common but less crowded than Prague",
      "transport_value": "9.0/10 - Cheapest flights + direct train option"
    },
    
    "transport_recommendations": {
      "getting_to_vienna": {
        "flight_option_1": {
          "route": "Your Location → Vienna",
          "carriers": ["Lufthansa (full-service)", "Ryanair (budget)", "Austrian Airlines"],
          "price_range": "$250-600 USD per person",
          "duration": "Direct flights 9-12 hours (with connection: 12-16 hours)",
          "timing_tip": "Book 6-8 weeks in advance for best prices",
          "best_for": "Fast, comfortable, predictable",
          "booking_links": [
            "Google Flights: google.com/flights",
            "Skyscanner: skyscanner.com",
            "Kayak: kayak.com"
          ]
        },
        "flight_option_2": {
          "route": "Your Location → Prague/Budapest (budget hub)",
          "carriers": ["Wizz Air (ultra-budget)", "Ryanair"],
          "price_range": "$150-350 USD per person",
          "duration": "Similar total time but cheaper",
          "timing_tip": "May require additional local transport",
          "best_for": "Budget-conscious travelers"
        }
      },
      
      "vienna_to_budapest": {
        "train": {
          "provider": "ÖBB (Austrian Federal Railways)",
          "price_range": "$30-70 USD per person (advance booking)",
          "duration": "2.5 hours direct",
          "frequency": "10-12 daily departures",
          "comfort": "Standard or First Class available",
          "tips": "Book at raileurope.com or oebb.at",
          "best_for": "Scenic journey, on-time reliability, no luggage fees",
          "booking_links": ["raileurope.com", "omio.com", "oebb.at"]
        },
        "flight": {
          "carriers": "Wizz Air, budget airlines",
          "price_range": "$25-60 USD per person",
          "duration": "1 hour flight + airport time = 3.5-4 hours total",
          "frequency": "5-6 daily",
          "tips": "Cheaper but less convenient (airport taxes, luggage)",
          "best_for": "In a hurry, want cheapest option"
        },
        "bus": {
          "provider": "FlixBus, Eurolines",
          "price_range": "$15-40 USD per person",
          "duration": "6.5-7.5 hours",
          "frequency": "3-4 daily",
          "tips": "Cheapest but slowest; good for overnight",
          "best_for": "Budget travelers not sensitive to time"
        },
        "comparison": {
          "fastest": "Flight (3.5 hours)",
          "best_value": "Train ($35 avg, scenic, 2.5 hours)",
          "cheapest": "Bus ($25 avg but 7 hours)"
        }
      },
      
      "returning_home": {
        "from_budapest": {
          "flight_option": "Direct flights to your home city",
          "price_range": "$250-600 USD per person",
          "duration": "10-14 hours depending on destination",
          "carriers": "Wizz Air (budget), Lufthansa, national carriers",
          "booking_links": ["Google Flights", "Skyscanner", "Kayak"]
        }
      },
      
      "total_transport_budget": {
        "flights_estimate": "$500-1,200 per person (international)",
        "vienna_budapest_train": "$35-70 per person",
        "local_transport": "$50-100 per person (trams, metros, taxis)",
        "total_transport": "$585-1,370 per person",
        "note": "Leaves $130-1,415 from $1,500-3,000 budget for hotels + food + activities"
      }
    },

    "youtube_videos": {
      "watch_first": [
        {
          "title": "Vienna + Budapest 5 Days Travel Guide (2024)",
          "channel": "[Popular Travel Channel]",
          "length": "28 minutes",
          "why": "Recent overview of both cities, realistic expectations",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Best neighborhoods", "Budget tips", "Top attractions", "Local food"]
        },
        {
          "title": "How to Travel Vienna to Budapest by Train",
          "channel": "[Budget Travel Channel]",
          "length": "12 minutes",
          "why": "Practical logistics for your specific route",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Train booking", "Luggage tips", "Timing", "Ticket prices"]
        }
      ],
      
      "deep_dive_vienna": [
        {
          "title": "Vienna for First-Timers (Safety, Neighborhoods, What to Skip)",
          "channel": "[Travel Vlogger]",
          "length": "35 minutes",
          "why": "Honest guide to avoiding tourist traps, real Vienna experience",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Authentic vs touristy areas", "Scams to avoid", "Local cafes", "Museums worth visiting"]
        },
        {
          "title": "Vienna Photography Guide (Best Locations, Light, Angles)",
          "channel": "[Photography Channel]",
          "length": "18 minutes",
          "why": "Perfect for girlfriend's photography interests",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Golden hour spots", "Composition tips", "Street photography", "Architectural angles"]
        }
      ],
      
      "deep_dive_budapest": [
        {
          "title": "Budapest Thermal Baths Complete Guide (Which, Prices, Tips)",
          "channel": "[Adventure Travel]",
          "length": "22 minutes",
          "why": "Essential for your girlfriend's relaxation + adventure interests",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Széchenyi vs Gellért baths", "Booking tips", "Prices", "What to bring"]
        },
        {
          "title": "Budapest Scams & Safety + How to Avoid (Local Tips)",
          "channel": "[Honest Guide]",
          "length": "15 minutes",
          "why": "Critical for your safety priority—current scam warnings",
          "link": "youtube.com/watch?v=[VIDEO_ID]",
          "topics_covered": ["Common Budapest scams", "Taxi tips", "Nightlife safety", "Pickpocketing prevention"]
        }
      ],
      
      "practical_logistics": [
        {
          "title": "Vienna Public Transport Explained (How to Buy Tickets, Use Metro)",
          "channel": "[Local Guide]",
          "length": "10 minutes",
          "why": "Avoid confusing transport on arrival",
          "link": "youtube.com/watch?v=[VIDEO_ID]"
        },
        {
          "title": "Budapest Neighborhoods Explained (Where to Stay, Where to Visit)",
          "channel": "[Travel Blogger]",
          "length": "14 minutes",
          "why": "Picking right area impacts your whole experience",
          "link": "youtube.com/watch?v=[VIDEO_ID]"
        }
      ],
      
      "aesthetic_inspiration": [
        {
          "title": "Vienna Golden Hour (Photography & Cinematic Tour)",
          "channel": "[Visual Travel]",
          "length": "12 minutes",
          "why": "Inspiring for girlfriend's photography interests, beautiful locations",
          "link": "youtube.com/watch?v=[VIDEO_ID]"
        },
        {
          "title": "Budapest Hidden Gems (Local Secrets, Architecture, Street Art)",
          "channel": "[Urban Explorer]",
          "length": "18 minutes",
          "why": "Go beyond tourist trail, discover authentic Budapest",
          "link": "youtube.com/watch?v=[VIDEO_ID]"
        }
      ],
      
      "watch_order_recommendation": "1. 'Watch First' videos (get overview) → 2. Practical logistics (understand transport) → 3. Deep Dive (explore interests) → 4. Aesthetic inspiration (dream & plan photography)"
    },

    "potential_challenges": [
      "Budapest pickpocketing (low risk, manage with normal precautions)",
      "Vienna can feel 'perfect but cold' (address by mixing imperial sites with local cafes)"
    ],

    "mitigation_strategies": [
      "Follow 'Honest Guide' YouTube tips for avoiding Budapest scams (linked above)",
      "Skip tourist restaurants; seek local pubs and markets",
      "Spend time in Vienna coffee culture, not just palaces"
    ],

    "research_sources": [
      "Rick Steves Forums (15+ threads Vienna/Budapest pairing)",
      "Reddit r/travel (consensus: safest Central Europe combo)",
      "TripAdvisor comparisons (Vienna 4.5/5, Prague 4.2/5)",
      "Nomad List (Budapest cost ranking #3 in Europe)",
      "Skyscanner / Google Flights (real pricing data)",
      "Omio / Raileurope (train pricing)",
      "YouTube (40+ relevant travel videos analyzed)"
    ]
  },

  "alternative_recommendations": [
    {
      "cluster": "Barcelona + Lisbon",
      "rank": 2,
      "reason_to_choose": "If girlfriend's interests (fashion, beaches, modern culture) outweigh authentic history preference. Better for food/wine/contemporary experiences.",
      "trade_off": "Higher budget ($1.5K vs $800), more touristy, moderate scam risk",
      "transport_costs": "Flights $300-700 + 2hr flight Barcelona-Lisbon $40-100",
      "youtube_overview": [
        {"title": "Barcelona + Lisbon 6 Days (2024)", "link": "youtube.com/watch?v=[VIDEO_ID]"},
        {"title": "Barcelona Fashion & Street Style Guide", "link": "youtube.com/watch?v=[VIDEO_ID]"}
      ]
    },
    {
      "cluster": "Vienna + Prague",
      "rank": 3,
      "reason_to_choose": "If you specifically want to see Prague despite scams. Prague's beauty justifies risk for some travelers.",
      "trade_off": "Longer train (4+ hrs), Prague taxi/exchange scams documented, heavy crowds",
      "transport_costs": "Flights + 4.5hr train $50-100",
      "youtube_overview": [
        {"title": "Prague Scams & How to Avoid (2024)", "link": "youtube.com/watch?v=[VIDEO_ID]"},
        {"title": "Vienna to Prague Train Journey", "link": "youtube.com/watch?v=[VIDEO_ID]"}
      ]
    }
  ],

  "comparison_tool": {
    "type": "interactive_visual_with_transport",
    "top_n": 5,
    "metrics": [
      "Safety", "Scam Avoidance", "Authentic Culture", 
      "Girlfriend Interests", "Budget Fit", "Logistics", "Crowds", "Uniqueness",
      "Transport Cost", "Flight Availability"
    ],
    "action": "Display interactive comparison; user can click to explore transport prices & YouTube videos for each option"
  },

  "quick_booking_checklist": {
    "step_1": "Watch 'Vienna + Budapest 5 Days' YouTube video (get inspired)",
    "step_2": "Watch 'Transport Guide' YouTube video (understand logistics)",
    "step_3": "Book international flights (Google Flights link above)",
    "step_4": "Book Vienna → Budapest train (raileurope.com link above)",
    "step_5": "Book hotels (3 nights Vienna, 2-3 nights Budapest)",
    "step_6": "Watch local guides for your chosen neighborhoods",
    "step_7": "Save 'Scams to Avoid' video for pre-departure review"
  },

  "next_steps": {
    "if_satisfied": "Proceed to Phase 5 (detailed 5-6 day itinerary building with daily activities)",
    "if_want_different_transport": "Compare alternatives above (flight vs train, etc.)",
    "if_want_alternative_destination": "Click alternative recommendation above for its transport & videos",
    "if_want_different_approach": "Re-start questionnaire with new preferences"
  }
}
```

---

## Skill Usage Example (End-to-End)

### User Scenario: Varun & girlfriend, 5-6 days, early November, Europe

```
PHASE 1: Haiku asks basics
→ Trip Duration: 5-6 days
→ Countries: 2
→ Dates: Early November
→ First-timer: No (but girlfriend has limited Europe)

PHASE 2A: Haiku asks conditional
→ Transport: Open to any, prefer easy
→ Girlfriend interests: Fashion, art, photography, adventure, travel, beauty

PHASE 2B: Haiku asks preferences
→ Vibe: Historic cities & culture
→ Pace: Relaxed (2-3 activities/day)

HAIKU DETECTION: Sees conflict—
  User: "historic culture" (Central Europe vibe)
  Girlfriend: "fashion, beauty, adventure" (could be Southern Europe)
  
→ ESCALATES TO SONNET

SONNET CLARIFICATION:
  "I'm seeing you want historic + cultural for yourself,
   but your girlfriend loves fashion/beaches/adventure.
   How do we balance this? What matters MORE?"

USER ANSWER: "Both—but would pick something that has BOTH: 
history + modern culture + active experiences"

PHASE 3: Haiku resumes
→ Safety: Very important (scams are concern)
→ Authenticity: Very important (tired of tourist traps)
→ Budget: $1,500-3,000 combined
→ Must avoid: Prague (scams)
→ Must see: None specific

PHASE 4: Haiku complexity check
→ All answers clear, internally consistent
→ READY FOR RESEARCH

PHASE 3: SONNET RESEARCHES
Searches:
- "Vienna Budapest first time couple reddit"
- "Barcelona Lisbon vs Vienna Budapest"
- "Prague scams vs Vienna safety"
- "Girlfriend fashion art photography Europe"
- "5-6 days 2 countries Central Europe itinerary"

SONNET CLUSTERING:
Creates 6 clusters (as shown earlier in skill)

PHASE 4: OPUS DECIDES
Evaluates using weighted framework
Recommendation: Vienna + Budapest
Reasoning: Meets all criteria uniquely
Alternatives: Barcelona+Lisbon, Vienna+Prague

OUTPUT: Interactive comparison tool
User confirms choice or explores alternatives

PHASE 5: Ready for itinerary building
→ Haiku asks detailed logistics/activity preferences
→ Sonnet builds 5-6 day breakdown
→ Opus reviews for feasibility
```

---

## Key Differentiators of This Skill

✅ **Progressive & Adaptive**: Questions depend on answers (not linear checklist)
✅ **Complexity Detection**: Auto-escalates when ambiguity detected
✅ **Research-Backed**: Forum consensus + traveler experiences inform decisions
✅ **Clustering Approach**: Presents clusters not just individual cities
✅ **Weighted Scoring**: Transparent decision logic (not black-box)
✅ **Uniqueness Focus**: Balances "best" with "right for THIS person"
✅ **Multi-Agent**: Haiku (questions), Sonnet (research), Opus (decisions)
✅ **YouTube Integration**: Curated, quality-filtered videos for each destination
✅ **Real Transport Pricing**: Flight + train + bus options with actual prices
✅ **Booking Links**: Direct links to Google Flights, Skyscanner, Raileurope, etc.
✅ **Total Cost Breakdowns**: Shows per-person transport costs + budget remaining
✅ **Reusable**: Works for anyone, any layover scenario

---

## Success Criteria

This skill succeeds when:
1. **User feels understood** (questions feel personalized, not generic)
2. **Recommendation surprises positively** (good combo they hadn't considered)
3. **Trade-offs are clear** (why not just go to Vienna alone? Why this pair?)
4. **Research feels credible** (forum citations, traveler consensus)
5. **Logistics are sound** (actual travel times, real costs)
6. **Girlfriend/companion is considered** (not just user's preferences)
7. **Unique clustering** (not just top 5 cities combined randomly)

---

## Future Enhancements

- [ ] **Seasonal optimization**: "Best time to visit [destination] for [your interests]"
- [ ] **Visa/documentation automation**: "Do you need visas for these countries?"
- [x] **Real-time pricing**: Integration with Skyscanner/Kayak for actual flight costs (INCLUDED)
- [x] **YouTube video curation**: Hand-picked, quality-filtered travel videos (INCLUDED)
- [x] **Transport recommendations**: Flight, train, bus options with pricing (INCLUDED)
- [ ] **Traveler matching**: "89% of travelers like you chose Vienna+Budapest"
- [ ] **Day-by-day itinerary building**: Once destination chosen, auto-generate 5-6 day plan
- [ ] **Booking assistance**: Direct integration with booking platforms
- [ ] **Crowd calendar**: "Early November = ideal; avoid August"
- [ ] **Meal planning**: Restaurant recommendations by budget/interest
- [ ] **Activity booking**: Pre-book tours, museum entries, thermal bath slots
- [ ] **Travel insurance**: Recommendations & quick comparison

---

## End-to-End Usage: User Perspective

```
User: "Help me plan a 5-day layover before going to India"

Skill Execution:
1. Haiku: "How many days? (quick multiple choice)"
2. Haiku: "1 country or 2?"
3. Haiku: [adaptive follow-ups based on answers]
4. [Complexity escalation if needed → Sonnet clarifies]
5. Haiku: [continues with preferences]
6. Sonnet: [researches + clusters destinations]
7. Opus: [makes ranked recommendation]
8. Interactive comparison tool displayed
9. User clicks "Vienna + Budapest"
10. Skill ready to build detailed itinerary (Phase 5)

Total time: 5-10 minutes for comprehensive recommendation
```

---

## Technical Implementation Notes

### For Claude API Integration
- Use streaming for Haiku questions (real-time feel)
- Batch research queries in Sonnet (efficient)
- Use JSON for Opus output (structured recommendations)
- Store user profile in session (for iteration)

### For Prompt Engineering
- Haiku: Conversational, warm, curious tone
- Sonnet: Research-oriented, analytical, pattern-finding
- Opus: Authoritative, reasoned, transparent logic

### For UX
- Show progress ("Question 3 of 8")
- Display research citations real-time
- Interactive comparison tool (drag/drop priority weights)
- "Why this recommendation?" expandable explanations

---

**This skill is designed to be reused, remixed, and improved. Share feedback, iterations, and use cases!**
