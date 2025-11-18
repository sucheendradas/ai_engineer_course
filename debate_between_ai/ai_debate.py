import os
import requests
import json
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OLLAMA_BASE = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
BELIEVER_MODEL = os.getenv("BELIEVER_MODEL", "llama3.2:3b")
ATHEIST_MODEL = os.getenv("ATHEIST_MODEL", "llama3.2:3b")

class Debater:
    def __init__(self, name, model, role_description):
        self.name = name
        self.model = model
        self.role_description = role_description
        self.conversation_history = []
    
    def generate_response(self, prompt, debate_topic):
        # Build the context for the debate
        system_prompt = f"""You are role-playing as {self.name}, {self.role_description}
        
You are currently debating the topic: "{debate_topic}"
        
Guidelines:
- Stay true to your character's worldview
- Respond naturally to the previous arguments
- Keep responses concise (2-3 paragraphs maximum)
- Use logical reasoning and evidence where appropriate
- Maintain a respectful but firm tone
- Engage directly with the points raised by your opponent"""

        full_prompt = f"{system_prompt}\n\nPrevious exchange:\n{prompt}\n\n{self.name}:"
        
        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": 0.8,
                "top_p": 0.9,
            }
        }
        
        try:
            response = requests.post(f"{OLLAMA_BASE}/api/generate", json=payload)
            response.raise_for_status()
            result = response.json()
            return result["response"].strip()
        except Exception as e:
            return f"Error: {str(e)}"

def format_debate_display(speaker, text, width=80):
    """Format the debate output with nice borders"""
    border = "=" * width
    header = f" {speaker} ".center(width, " ")
    print(f"\n{border}")
    print(header)
    print(border)
    print(text)
    print(border)

def main():
    # Define the debaters
    believer = Debater(
        name="The Believer",
        model=BELIEVER_MODEL,
        role_description="a thoughtful religious believer who believes in God and the importance of faith. You find meaning, purpose, and evidence of divine presence in the universe, human consciousness, and moral reasoning."
    )
    
    atheist = Debater(
        name="The Atheist", 
        model=ATHEIST_MODEL,
        role_description="a rational atheist who relies on scientific evidence and logical reasoning. You don't believe in God or supernatural claims due to lack of empirical evidence and prefer naturalistic explanations for existence and morality."
    )
    
    # Debate topic
    debate_topic = "Does God exist? What is the basis for meaning and morality in human life?"
    
    print("\n" + "🤔 THE GREAT DEBATE 🤔".center(80))
    print(f"\nTopic: {debate_topic}")
    print(f"\nBeliever Model: {BELIEVER_MODEL}")
    print(f"Atheist Model: {ATHEIST_MODEL}")
    print("\n" + "="*80)
    
    # Initial prompt
    current_prompt = f"Debate Topic: {debate_topic}\n\nThe Believer will speak first, presenting their opening argument for the existence of God and the basis of meaning and morality."
    
    # Number of debate rounds
    rounds = 4
    
    for round_num in range(rounds):
        print(f"\n\n🎯 ROUND {round_num + 1}")
        print("="*50)
        
        # Believer's turn
        believer_response = believer.generate_response(current_prompt, debate_topic)
        format_debate_display("🙏 THE BELIEVER", believer_response)
        current_prompt += f"\n\nThe Believer: {believer_response}"
        
        # Add some delay for natural flow
        time.sleep(2)
        
        # Atheist's turn (respond to believer)
        atheist_prompt = current_prompt + f"\n\nThe Atheist should now respond directly to the Believer's points and present counter-arguments."
        atheist_response = atheist.generate_response(atheist_prompt, debate_topic)
        format_debate_display("🔬 THE ATHEIST", atheist_response)
        current_prompt += f"\n\nThe Atheist: {atheist_response}"
        
        # Update prompt for next round
        current_prompt += f"\n\nRound {round_num + 1} completed. In the next exchange, each side should respond to the most recent arguments while advancing their own position."
        
        time.sleep(2)
    
    # Closing statements
    print(f"\n\n🏁 FINAL THOUGHTS")
    print("="*50)
    
    # Believer's final thought
    final_believer_prompt = current_prompt + "\n\nThis is your final statement. Summarize your strongest arguments and provide a compelling conclusion to your position."
    believer_final = believer.generate_response(final_believer_prompt, debate_topic)
    format_debate_display("🙏 BELIEVER'S CONCLUSION", believer_final)
    
    time.sleep(2)
    
    # Atheist's final thought
    final_atheist_prompt = current_prompt + "\n\nThis is your final statement. Summarize your strongest arguments and provide a compelling conclusion to your position."
    atheist_final = atheist.generate_response(final_atheist_prompt, debate_topic)
    format_debate_display("🔬 ATHEIST'S CONCLUSION", atheist_final)
    
    print("\n\n✅ Debate completed!")

if __name__ == "__main__":
    main()