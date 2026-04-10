# 🎯 Claude Skill Plugin Installation Guide

This is a **Claude Skill** — meaning you can use it directly in Claude.ai or via the Claude API.

---

## ✅ Quick Installation (Claude.ai)

### Method 1: Direct File Input (Fastest)
1. Go to **[claude.ai](https://claude.ai)**
2. Start a new conversation
3. Paste this prompt:

```
I have a Layover Destination Designer skill. Here's the skill definition:

[Copy and paste the entire contents of SKILL.md from this repository]

Now, help me plan my perfect layover destination!
```

4. Claude will immediately start asking you progressive questions

---

### Method 2: GitHub Raw URL (Cloud-Based)
1. Go to **[claude.ai](https://claude.ai)**
2. Paste this prompt:

```
I want to use the Layover Destination Designer skill from this GitHub repository:
Raw skill URL: https://raw.githubusercontent.com/naagdev/layover-skill/main/SKILL.md

Please load this skill and help me find my perfect layover destination.
```

3. Claude will load the skill from the URL

---

### Method 3: Import via File Upload
1. Download **`SKILL.md`** from this repository
2. Go to **[claude.ai](https://claude.ai)** 
3. Click the **+** button to upload a file
4. Upload `SKILL.md`
5. Say: _"Use this as my skill definition. Help me plan a layover destination."_

---

## 🔧 Installation (Claude API)

### Prerequisites
```bash
pip install anthropic python-dotenv
```

### Setup

**1. Clone or download this repository:**
```bash
git clone https://github.com/naagdev/layover-skill.git
cd layover-skill
```

**2. Create `.env` file:**
```
ANTHROPIC_API_KEY=your_api_key_here
```

**3. Use in Python:**

```python
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize client
client = Anthropic()

# Load the skill
with open('SKILL.md', 'r') as f:
    skill_definition = f.read()

# Create system prompt with skill included
system_prompt = f"""You are a layover destination planner using the following skill framework:

{skill_definition}

Follow this framework to help users find their perfect layover destination."""

# Start the conversation
conversation_history = []

def chat(user_message):
    """Send a message and get a response."""
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        system=system_prompt,
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

# Start planning
if __name__ == "__main__":
    print("🌍 Layover Destination Designer")
    print("=" * 50)
    print("Type 'quit' to exit\n")
    
    # Start with the initial question
    initial_prompt = "Help me find my perfect layover destination!"
    response = chat(initial_prompt)
    print(f"Assistant: {response}\n")
    
    # Continue conversation
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye! Safe travels! 🌍")
            break
        if not user_input:
            continue
        
        response = chat(user_input)
        print(f"\nAssistant: {response}\n")
```

**4. Run the conversation:**
```bash
python skill_app.py
```

---

## 📋 What's Included

| File | Purpose |
|------|---------|
| **SKILL.md** | Complete skill framework with all 5 phases |
| **PROMPTS.md** | System prompts for Haiku, Sonnet, and Opus agents |
| **EXAMPLES.md** | Real usage examples with different traveler profiles |
| **IMPLEMENTATION.md** | Detailed implementation guide |
| **claude-skill-plugin.json** | Plugin metadata for skill registries |
| **.claude-skill** | Skill configuration file |
| **README.md** | Overview and quick start |
| **SETUP.md** | GitHub and deployment guide |

---

## 🎨 How It Works

```
You (User)
    ↓
Claude (Haiku agent)
    ↳ Asks adaptive questions
    ↳ Detects complexity
    ↓ (if complex)
Claude (Sonnet agent)
    ↳ Clarifies conflicts
    ↳ Researches options
    ↓
Claude (Opus agent)
    ↳ Ranks destinations
    ↳ Final recommendation
    ↓
Perfect Layover Destination 🎯
```

---

## 🚀 Features

✅ **5-Phase Framework** — Progressive, structured approach  
✅ **Multi-Agent Orchestration** — Haiku → Sonnet → Opus escalation  
✅ **Adaptive Questioning** — Questions depend on previous answers  
✅ **Complexity Detection** — Auto-escalates when conflicts detected  
✅ **Research-Backed** — Uses community insights from Reddit, TripAdvisor  
✅ **Destination Clustering** — Groups 5-7 optimal pairs, not just single cities  
✅ **Budget Breakdown** — Shows per-person costs  
✅ **Transport Options** — Flight, train, bus with pricing  
✅ **Booking Links** — Direct to Google Flights, Skyscanner, etc.  
✅ **Video Recommendations** — Curated YouTube content for each destination  

---

## 💡 Example Usage

**You:** "Help me plan a 5-day layover in November with my partner. We want culture and authenticity."

**Claude (Haiku):** "Perfect! Is this your partner's first time in Europe?"

**You:** "Yes, their first time."

**Claude (Haiku):** "Great! What budget range are we looking at?"

**You:** "Around $2000 total."

**Claude (escalates to Sonnet):** "I'm detecting some interesting priorities here..."

**[Sonnet asks clarifying questions]**

**[Sonnet researches destinations]**

**Claude (Opus):** 
- **Top Pick #1:** Prague + Vienna (historic, metro accessible, authentic, $1,850)
- **Top Pick #2:** Budapest + Krakow ($1,750)
- **Top Pick #3:** Lisbon + Sintra ($1,920)

[Shows YouTube videos, transport options, booking links, budget breakdowns]

---

## ❓ FAQ

**Q: Do I need an API key?**  
A: Only if using Claude API. Claude.ai users need no setup.

**Q: How long does planning take?**  
A: Usually 15-20 minutes of conversation for a complete recommendation.

**Q: Can I customize the skill?**  
A: Yes! Edit SKILL.md to adjust phases, questions, or criteria.

**Q: What if I have conflicting preferences?**  
A: The skill detects conflicts and escalates to Sonnet for clarification.

**Q: Can I use this offline?**  
A: No, it requires Claude API calls. Use Claude.ai and you'll have an internet connection.

---

## 📖 Documentation

- **SKILL.md** — Full skill specification
- **IMPLEMENTATION.md** — Implementation details
- **EXAMPLES.md** — Real usage examples
- **PROMPTS.md** — System prompts for each agent
- **README.md** — Quick overview
- **SETUP.md** — GitHub deployment

---

## 🤝 Support

For questions or issues:
1. Check the [documentation files](.)
2. Review [EXAMPLES.md](EXAMPLES.md) for usage patterns
3. Open an issue on GitHub: [layover-skill/issues](https://github.com/naagdev/layover-skill/issues)

---

**Ready to find your perfect layover? Start chatting with Claude! 🌍✈️**
