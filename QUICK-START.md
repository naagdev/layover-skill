# Quick Start Guide - Layover Destination Skill

Choose your preferred method to get started:

## 🚀 Fastest: Claude.ai (No Setup Required)

1. Go to [claude.ai](https://claude.ai)
2. Start a new conversation
3. Copy the entire content of [SKILL.md](SKILL.md)
4. Paste it with: "I have a skill for you. Here's the definition:"
5. Then say: "Help me plan my layover destination!"

**Done!** Claude will start asking you questions.

---

## 🐍 Python (Local CLI)

### Prerequisites
- Python 3.8+
- Anthropic API key

### Setup (1 minute)

```bash
# 1. Clone the repository
git clone https://github.com/naagdev/layover-skill.git
cd layover-skill

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 4. Run the CLI
python layover-planner.py
```

### Usage
```bash
python layover-planner.py
```

Follow the interactive prompts to plan your layover!

---

## 🟢 Node.js (Local CLI)

### Prerequisites
- Node.js 16+
- Anthropic API key

### Setup (1 minute)

```bash
# 1. Clone the repository
git clone https://github.com/naagdev/layover-skill.git
cd layover-skill

# 2. Install dependencies
npm install

# 3. Create .env file
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 4. Run the CLI
npm start
```

### Usage
```bash
npm start
```

Follow the interactive prompts to plan your layover!

---

## 📚 API Usage (Python)

If you want to integrate this into your own application:

```python
from anthropic import Anthropic

# Load the skill
with open('SKILL.md', 'r') as f:
    skill = f.read()

# Create client
client = Anthropic()

# Use in your code
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    system=f"You are a layover planner using this skill:\n\n{skill}",
    messages=[
        {"role": "user", "content": "Help me find a layover destination for 5 days in Europe with my partner"}
    ]
)

print(response.content[0].text)
```

---

## 🌐 API Usage (Node.js)

```javascript
const Anthropic = require("@anthropic-ai/sdk").default;
const fs = require("fs");

const skill = fs.readFileSync("SKILL.md", "utf-8");
const client = new Anthropic();

const response = await client.messages.create({
  model: "claude-3-5-sonnet-20241022",
  max_tokens: 2048,
  system: `You are a layover planner using this skill:\n\n${skill}`,
  messages: [
    {
      role: "user",
      content: "Help me find a layover destination for 5 days in Europe with my partner",
    },
  ],
});

console.log(response.content[0].text);
```

---

## ✅ Verify Installation

After setup, verify everything works:

### Python
```bash
python layover-planner.py
# Should see: "🌍 LAYOVER DESTINATION DESIGNER 🌍"
# Then Claude will ask you a question
```

### Node.js
```bash
npm start
# Should see: "🌍 LAYOVER DESTINATION DESIGNER 🌍"
# Then Claude will ask you a question
```

---

## 📋 File Structure

```
layover-skill/
├── SKILL.md                    # Main skill definition
├── PROMPTS.md                  # System prompts for agents
├── EXAMPLES.md                 # Real usage examples
├── IMPLEMENTATION.md           # Detailed implementation
├── README.md                   # Overview
├── SETUP.md                    # GitHub setup
├── CLAUDE-SKILL-GUIDE.md       # Claude skill installation
├── QUICK-START.md             # This file
├── layover-planner.py         # Python CLI tool
├── layover-planner.js         # Node.js CLI tool
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── .claude-skill             # Plugin metadata
```

---

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not found"
- Copy `.env.example` to `.env`
- Add your API key to `.env`
- Get one at: https://console.anthropic.com

### "SKILL.md not found"
- Make sure you're in the layover-skill directory
- Check that SKILL.md exists in the current folder

### Connection errors
- Verify your API key is valid
- Check your internet connection
- Ensure you have Anthropic API access

### "Module not found"
- Python: Run `pip install -r requirements.txt`
- Node.js: Run `npm install`

---

## 🎯 What to Expect

The skill will:
1. Ask you 3-4 initial questions about your trip
2. Ask follow-up questions based on your answers
3. Detect if your preferences are conflicting and ask for clarification
4. Ask deeper questions about vibe, safety, budget
5. Research destinations and suggest 3-5 options
6. Provide details, costs, transport, and booking links

**Total time: 15-30 minutes** for a complete recommendation

---

## 📖 More Information

- **How it works**: See [SKILL.md](SKILL.md)
- **System prompts**: See [PROMPTS.md](PROMPTS.md)
- **Real examples**: See [EXAMPLES.md](EXAMPLES.md)
- **Implementation details**: See [IMPLEMENTATION.md](IMPLEMENTATION.md)

---

## 🤝 Support

- Questions? Check [EXAMPLES.md](EXAMPLES.md)
- Issues? Open a GitHub issue
- Want to customize? Edit SKILL.md

**Happy planning! 🌍✈️**
