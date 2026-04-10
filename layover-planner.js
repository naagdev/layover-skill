#!/usr/bin/env node

/**
 * Layover Destination Designer - Node.js CLI
 * Interactive multi-agent layover destination planner for Node.js/browser environments
 */

const Anthropic = require("@anthropic-ai/sdk").default;
const fs = require("fs");
const path = require("path");
const readline = require("readline");

class LayoverDestinationPlanner {
  constructor() {
    const apiKey = process.env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      throw new Error(
        "ANTHROPIC_API_KEY not found. Please set it as an environment variable."
      );
    }

    this.client = new Anthropic({ apiKey });
    this.conversationHistory = [];
    this.skillDefinition = this.loadSkill();
    this.systemPrompt = this.createSystemPrompt();
  }

  loadSkill() {
    const skillPath = path.join(__dirname, "SKILL.md");
    if (!fs.existsSync(skillPath)) {
      throw new Error(
        `SKILL.md not found at ${skillPath}. Make sure you're in the layover-skill directory.`
      );
    }
    return fs.readFileSync(skillPath, "utf-8");
  }

  createSystemPrompt() {
    return `You are a layover destination planning assistant using the following multi-agent framework.

${this.skillDefinition}

IMPORTANT INSTRUCTIONS:
1. Follow the 5-phase framework exactly as specified
2. In Phase 1, use Haiku's persona to ask adaptive, conversational questions
3. Detect complexity and flag for escalation when needed
4. Be friendly, conversational, and encouraging
5. Build a detailed user profile as the conversation progresses
6. Make recommendations personalized and specific

Remember: You are orchestrating Haiku → Sonnet → Opus agents in sequence as needed.`;
  }

  async chat(userMessage) {
    this.conversationHistory.push({
      role: "user",
      content: userMessage,
    });

    const response = await this.client.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 2048,
      system: this.systemPrompt,
      messages: this.conversationHistory,
    });

    const assistantMessage = response.content[0].text;
    this.conversationHistory.push({
      role: "assistant",
      content: assistantMessage,
    });

    return assistantMessage;
  }

  async start() {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    const question = (prompt) =>
      new Promise((resolve) => rl.question(prompt, resolve));

    console.log("\n" + "=".repeat(60));
    console.log("🌍  LAYOVER DESTINATION DESIGNER  🌍");
    console.log("=".repeat(60));
    console.log(
      "\nWelcome! I'm here to help you find your perfect layover destination."
    );
    console.log("Tell me about your travel plans, and I'll guide you through the process.\n");
    console.log("(Type 'quit' or 'exit' to end the conversation)\n");
    console.log("=".repeat(60) + "\n");

    try {
      // Initial greeting
      const initialResponse = await this.chat(
        "Hi! I'm ready to plan my layover destination. Can you help me find the perfect one?"
      );
      console.log(`✨ ${initialResponse}\n`);

      // Main loop
      while (true) {
        const userInput = await question("👤 You: ");

        if (!userInput.trim()) {
          continue;
        }

        if (userInput.toLowerCase() === "quit" || userInput.toLowerCase() === "exit") {
          console.log(
            "\n🎉 Thank you for planning with me! Have an amazing layover! ✈️\n"
          );
          break;
        }

        try {
          const response = await this.chat(userInput);
          console.log(`\n✨ ${response}\n`);
        } catch (error) {
          console.error(
            `\n❌ Error: ${error.message || error}. Please try again.\n`
          );
        }
      }
    } finally {
      rl.close();
    }
  }
}

async function main() {
  try {
    const planner = new LayoverDestinationPlanner();
    await planner.start();
  } catch (error) {
    console.error(`❌ Error: ${error.message || error}`);
    process.exit(1);
  }
}

main();
