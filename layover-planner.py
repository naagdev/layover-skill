#!/usr/bin/env python3
"""
Layover Destination Designer - CLI Tool
Interactive multi-agent layover destination planner
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

class LayoverDestinationPlanner:
    def __init__(self):
        """Initialize the planner with Claude API."""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. "
                "Please set it in .env file or as environment variable."
            )
        
        self.client = Anthropic()
        self.conversation_history = []
        self.skill_definition = self._load_skill()
        self.system_prompt = self._create_system_prompt()
    
    def _load_skill(self) -> str:
        """Load the SKILL.md file."""
        skill_path = Path(__file__).parent / "SKILL.md"
        
        if not skill_path.exists():
            raise FileNotFoundError(
                f"SKILL.md not found at {skill_path}. "
                "Make sure you're in the layover-skill directory."
            )
        
        with open(skill_path, 'r') as f:
            return f.read()
    
    def _create_system_prompt(self) -> str:
        """Create the system prompt with skill definition."""
        return f"""You are a layover destination planning assistant using the following multi-agent framework.

{self.skill_definition}

IMPORTANT INSTRUCTIONS:
1. Follow the 5-phase framework exactly as specified
2. In Phase 1, use Haiku's persona to ask adaptive, conversational questions
3. Detect complexity and flag for escalation when needed
4. Be friendly, conversational, and encouraging
5. Build a detailed user profile as the conversation progresses
6. Make recommendations personalized and specific

Remember: You are orchestrating Haiku → Sonnet → Opus agents in sequence as needed."""
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            system=self.system_prompt,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def start(self):
        """Start the interactive conversation loop."""
        print("\n" + "="*60)
        print("🌍  LAYOVER DESTINATION DESIGNER  🌍")
        print("="*60)
        print("\nWelcome! I'm here to help you find your perfect layover destination.")
        print("Tell me about your travel plans, and I'll guide you through the process.\n")
        print("(Type 'quit' or 'exit' to end the conversation)\n")
        print("="*60 + "\n")
        
        # Start with initial greeting
        initial_response = self.chat(
            "Hi! I'm ready to plan my layover destination. Can you help me find the perfect one?"
        )
        print(f"✨ {initial_response}\n")
        
        # Main conversation loop
        while True:
            try:
                user_input = input("👤 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print("\n🎉 Thank you for planning with me! Have an amazing layover! ✈️\n")
                    break
                
                # Get response
                response = self.chat(user_input)
                print(f"\n✨ {response}\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Planning session ended. Safe travels!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                print("Please try again.\n")


def main():
    """Main entry point."""
    try:
        planner = LayoverDestinationPlanner()
        planner.start()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"❌ File Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
