# Implementation Guide - Layover Destination Skill

How to set up and deploy the Layover Destination Skill

## Table of Contents
1. [Quick Start (Claude.ai)](#quick-start-claudeai)
2. [Claude API Setup](#claude-api-setup)
3. [Multi-Agent Orchestration](#multi-agent-orchestration)
4. [Deployment Options](#deployment-options)
5. [Environment Variables](#environment-variables)
6. [Testing](#testing)

---

## Quick Start (Claude.ai)

### Easiest Method: Direct Chat Usage

1. **Copy the SKILL.md content**
2. **Open Claude.ai**
3. **Paste this prompt to Claude:**

```
I want you to act as a layover destination recommendation engine using a multi-agent framework.

Here's the skill specification:
[PASTE SKILL.md CONTENT HERE]

Now, help me plan my layover destination. I have [duration] days and I'm interested in [brief preferences].
```

4. **Follow the interactive flow** as Claude guides you through questions
5. **Receive recommendation** with YouTube videos, transport options, and pricing

✅ **Done!** No setup required.

---

## Claude API Setup

### Prerequisites
- Python 3.8+
- Anthropic API key (get from console.anthropic.com)
- pip packages: `anthropic`, `python-dotenv`

### Installation

```bash
# Clone the skill repository
git clone https://github.com/yourusername/layover-skill.git
cd layover-skill

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Anthropic API key
```

### Basic Implementation

```python
from anthropic import Anthropic
import json

client = Anthropic()

# System prompts (from PROMPTS.md)
HAIKU_PROMPT = """[Full Haiku system prompt from PROMPTS.md]"""
SONNET_RESEARCH_PROMPT = """[Full Sonnet system prompt from PROMPTS.md]"""
OPUS_DECISION_PROMPT = """[Full Opus system prompt from PROMPTS.md]"""

class LayoverSkill:
    def __init__(self):
        self.conversation_history = []
        self.user_profile = {}
    
    def phase_1_questioning(self, user_input):
        """Phase 1: Haiku asks progressive questions"""
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=500,
            system=HAIKU_PROMPT,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def phase_2_research(self, user_profile):
        """Phase 2: Sonnet researches destinations"""
        research_prompt = f"""
        Based on this user profile:
        {json.dumps(user_profile, indent=2)}
        
        Research and cluster 5-7 optimal 2-country layover destination pairs.
        For each cluster, provide:
        - Safety, scam, authenticity, budget, logistics scores
        - Recommended YouTube videos with links
        - Transport options with real pricing
        - Why it matches this user's profile
        """
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            system=SONNET_RESEARCH_PROMPT,
            messages=[{"role": "user", "content": research_prompt}]
        )
        
        return response.content[0].text
    
    def phase_3_decision(self, clusters_analysis):
        """Phase 3: Opus makes final recommendation"""
        decision_prompt = f"""
        Here are the researched destination clusters:
        {clusters_analysis}
        
        Make a final recommendation. Provide:
        1. Primary recommendation (Rank #1)
        2. Alternatives (Rank #2-3)
        3. Transport pricing and booking links
        4. YouTube videos for each destination
        5. Budget breakdown
        """
        
        response = client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=3000,
            system=OPUS_DECISION_PROMPT,
            messages=[{"role": "user", "content": decision_prompt}]
        )
        
        return response.content[0].text
    
    def run_full_workflow(self):
        """Execute complete skill workflow"""
        print("🌍 Layover Destination Skill")
        print("=" * 50)
        
        # Phase 1: Questioning
        print("\n📝 Phase 1: Understanding Your Preferences")
        print("-" * 50)
        
        initial_input = input("Tell me about your layover plans: ")
        response = self.phase_1_questioning(initial_input)
        print(f"Assistant: {response}\n")
        
        # Continue multi-turn conversation
        while True:
            user_response = input("You: ")
            if user_response.lower() in ["done", "ready", "next"]:
                break
            response = self.phase_1_questioning(user_response)
            print(f"Assistant: {response}\n")
        
        # Extract user profile
        self.user_profile = self._extract_profile()
        
        # Phase 2: Research
        print("\n🔍 Phase 2: Researching Destinations")
        print("-" * 50)
        print("Analyzing Reddit, forums, YouTube, transport pricing...")
        clusters = self.phase_2_research(self.user_profile)
        print(f"\n{clusters}")
        
        # Phase 3: Decision
        print("\n⭐ Phase 3: Making Final Recommendation")
        print("-" * 50)
        recommendation = self.phase_3_decision(clusters)
        print(f"\n{recommendation}")
        
        return recommendation
    
    def _extract_profile(self):
        """Extract structured profile from conversation"""
        extraction_prompt = """
        Based on the conversation history, extract a structured user profile with:
        - trip_duration
        - countries_count
        - travel_dates
        - first_timer
        - vibe_preferences
        - daily_pace
        - safety_priority
        - authenticity_priority
        - budget
        - companion_info
        - constraints
        
        Return as JSON.
        """
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[
                {"role": "user", "content": extraction_prompt},
                *self.conversation_history
            ]
        )
        
        # Parse JSON from response
        import re
        json_match = re.search(r'\{.*\}', response.content[0].text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {}

# Usage
if __name__ == "__main__":
    skill = LayoverSkill()
    recommendation = skill.run_full_workflow()
```

---

## Multi-Agent Orchestration

### Architecture Diagram

```
User Input
    ↓
┌─────────────────────────────────┐
│  PHASE 1: Haiku Questioner      │ (claude-3-5-haiku)
│  - Adaptive questions            │
│  - Detect complexity             │
│  - Build user profile            │
└─────────────────────┬───────────┘
                      ↓
        ┌─────────────────────────────┐
        │  Complexity Detected?       │
        └─────┬───────────────┬───────┘
              │               │
            YES              NO
              │               │
              ↓               ↓
      ┌──────────────┐  ┌──────────────────┐
      │ PHASE 2a:    │  │ PHASE 2b: Sonnet │
      │ Sonnet       │  │ Research         │
      │ Clarifies    │  │                  │
      └──────┬───────┘  └────────┬─────────┘
             │                   │
             └─────────┬─────────┘
                       ↓
      ┌──────────────────────────────┐
      │ PHASE 3: Sonnet Researches   │
      │ - Reddit/forums              │
      │ - YouTube videos             │
      │ - Transport pricing          │
      │ - Creates clusters           │
      └────────────┬─────────────────┘
                   ↓
      ┌──────────────────────────────┐
      │ PHASE 4: Opus Decides        │
      │ - Ranks clusters             │
      │ - Transparent reasoning      │
      │ - Provides alternatives      │
      └────────────┬─────────────────┘
                   ↓
           Final Recommendation
```

### Error Handling

```python
class LayoverSkillException(Exception):
    """Base exception for skill errors"""
    pass

class ComplexityDetected(LayoverSkillException):
    """When Haiku detects conflicting preferences"""
    pass

class ResearchFailed(LayoverSkillException):
    """When Sonnet cannot find sufficient data"""
    pass

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ComplexityDetected as e:
            print(f"⚠️  Complexity detected: {e}")
            print("Escalating to Sonnet for clarification...")
            # Handle escalation
        except ResearchFailed as e:
            print(f"❌ Research failed: {e}")
            print("Try different preferences or check data sources")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            raise
    return wrapper
```

---

## Deployment Options

### Option 1: Streamlit Web App

```python
# requirements.txt
streamlit==1.28.0
anthropic==0.7.0
python-dotenv==1.0.0

# app.py
import streamlit as st
from layover_skill import LayoverSkill

st.title("🌍 Layover Destination Planner")

skill = LayoverSkill()

with st.spinner("Gathering your preferences..."):
    # Phase 1
    col1, col2 = st.columns(2)
    with col1:
        trip_duration = st.selectbox("How many days?", ["2-3", "4-5", "5-6", "Flexible"])
    with col2:
        countries = st.radio("Countries?", ["1", "2"])
    
    travel_dates = st.text_input("When?")
    first_timer = st.checkbox("First time in Europe?")

if st.button("Find My Destination!"):
    with st.spinner("Researching..."):
        recommendation = skill.run_full_workflow()
    
    st.success("Recommendation Ready!")
    st.markdown(recommendation)

# Run: streamlit run app.py
```

### Option 2: FastAPI Backend

```python
# requirements.txt
fastapi==0.104.0
uvicorn==0.24.0
anthropic==0.7.0

# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from layover_skill import LayoverSkill

app = FastAPI()

class LayoverRequest(BaseModel):
    duration: str
    countries: int
    dates: str
    first_timer: bool
    preferences: dict

@app.post("/recommend")
async def get_recommendation(request: LayoverRequest):
    try:
        skill = LayoverSkill()
        recommendation = skill.phase_3_decision(
            skill.phase_2_research(request.dict())
        )
        return {"recommendation": recommendation}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run: uvicorn api:app --reload
```

### Option 3: Cloud Deployment (Google Cloud Run)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Deploy to Cloud Run
gcloud run deploy layover-skill \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY
```

---

## Environment Variables

### .env File

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-xxxxxxxx

# Optional
LOG_LEVEL=INFO
DEBUG=False
CACHE_ENABLED=True
CACHE_TTL=3600

# API Configuration
MODEL_HAIKU=claude-3-5-haiku-20241022
MODEL_SONNET=claude-3-5-sonnet-20241022
MODEL_OPUS=claude-opus-4-20250514

# Research Configuration
REDDIT_SEARCH_LIMIT=20
YOUTUBE_SEARCH_LIMIT=10
PRICING_DATA_SOURCES=google_flights,skyscanner
```

### Load Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_HAIKU = os.getenv("MODEL_HAIKU", "claude-3-5-haiku-20241022")
```

---

## Testing

### Unit Tests

```python
# tests/test_skill.py
import pytest
from layover_skill import LayoverSkill

class TestLayoverSkill:
    @pytest.fixture
    def skill(self):
        return LayoverSkill()
    
    def test_phase_1_questioning(self, skill):
        response = skill.phase_1_questioning("Help me plan a layover")
        assert response  # Should get a response
        assert len(response) > 0
    
    def test_user_profile_extraction(self, skill):
        # Add conversation history
        skill.conversation_history = [
            {"role": "user", "content": "5-6 days"},
            {"role": "assistant", "content": "Great! How many countries?"},
            {"role": "user", "content": "2 countries"}
        ]
        profile = skill._extract_profile()
        assert profile.get("trip_duration")
    
    def test_phase_2_research(self, skill):
        test_profile = {
            "trip_duration": "5-6 days",
            "countries": 2,
            "budget": "$1500-3000",
            "safety_priority": "high"
        }
        clusters = skill.phase_2_research(test_profile)
        assert "Vienna" in clusters or "Budapest" in clusters
    
    def test_phase_3_decision(self, skill):
        test_clusters = """
        Vienna + Budapest: Score 8.95
        Barcelona + Lisbon: Score 6.96
        """
        recommendation = skill.phase_3_decision(test_clusters)
        assert len(recommendation) > 500

# Run: pytest tests/
```

### Integration Tests

```python
# tests/test_integration.py
def test_full_workflow():
    skill = LayoverSkill()
    
    # Simulate user interaction
    skill.phase_1_questioning("I need a 5-6 day layover")
    skill.phase_1_questioning("2 countries")
    skill.phase_1_questioning("Early November")
    
    # Extract profile
    profile = skill._extract_profile()
    assert profile
    
    # Research
    clusters = skill.phase_2_research(profile)
    assert clusters
    
    # Decide
    recommendation = skill.phase_3_decision(clusters)
    assert recommendation
    assert "recommendation" in recommendation.lower() or "vienna" in recommendation.lower()
```

---

## Monitoring & Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class LayoverSkill:
    def phase_1_questioning(self, user_input):
        logger.info(f"Phase 1: User input received: {user_input[:50]}...")
        response = client.messages.create(...)
        logger.info(f"Phase 1: Response generated ({len(response.content[0].text)} chars)")
        return response.content[0].text
    
    def phase_2_research(self, user_profile):
        logger.info(f"Phase 2: Starting research for profile: {user_profile.get('vibe')}")
        clusters = ...
        logger.info(f"Phase 2: {len(clusters)} destination clusters identified")
        return clusters
    
    def phase_3_decision(self, clusters):
        logger.info("Phase 3: Making final recommendation")
        recommendation = ...
        logger.info("Phase 3: Recommendation complete")
        return recommendation
```

---

## Performance Optimization

### Caching

```python
from functools import lru_cache

class LayoverSkill:
    @lru_cache(maxsize=128)
    def get_destination_scores(self, destination: str, factor: str):
        """Cache scored destinations to avoid re-research"""
        return ...
    
    def cache_research_results(self, clusters):
        """Store research results for future queries"""
        import pickle
        with open('cache/clusters.pkl', 'wb') as f:
            pickle.dump(clusters, f)
```

### Batch Processing

```python
def batch_research(profiles: list):
    """Research multiple profiles efficiently"""
    results = []
    for profile in profiles:
        result = LayoverSkill().phase_2_research(profile)
        results.append(result)
    return results
```

---

## Next Steps

1. **Set up environment** (copy .env.example → .env with your API key)
2. **Install dependencies** (`pip install -r requirements.txt`)
3. **Run tests** (`pytest tests/`)
4. **Choose deployment option** (Claude.ai, Streamlit, FastAPI, or Cloud Run)
5. **Customize** (adjust PROMPTS.md for your audience)
6. **Deploy** to production

---

For questions or issues, see EXAMPLES.md for real-world usage patterns.
