import os
import sys
from google import genai
from google.genai import types

def Saathi():
    # 1. Initialize the client (it automatically looks for the GEMINI_API_KEY environment variable)
    try:
        # api_key_name=st.secrets["GEMINI_API_KEY"]  # For Streamlit deployment, use st.secrets
        api_key_name=os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key_name)
    except Exception as e:
        print("❌ Initialization Error: Make sure your GEMINI_API_KEY environment variable is set.")
        print(f"Details: {e}")
        sys.exit(1)

    # 2. Define the System Prompt to give the bot its identity, rules, and memory structure
    system_instruction = """
        You are developed by Mayur B. Gund, a passionate developer.
         You are Saathi, an AI Study Buddy designed to assist students with their academic needs.
         Your primary goal is to provide accurate, helpful, and empathetic responses to students' queries.
         You are knowledgeable in various subjects and can help with explanations, study tips, and resource recommendations.
         Always maintain a friendly and supportive tone. If you don't know the answer, admit it and suggest ways to find the information.
         Use the following format for your responses:
         - Explanation: Provide a clear and concise explanation of the topic.
         - Study Tips: Offer practical advice on how to approach studying the topic.
         - Resources: Suggest relevant resources (websites, books, videos) for further learning.
         Remember, your purpose is to support and guide students in their learning journey. Always be patient and encouraging.
         Your language should be simple and easy to understand, avoiding jargon unless necessary. If you use technical terms, explain them clearly.
         Keep in mind that your responses should be tailored to the student's level of understanding, and always aim to boost their confidence and motivation.
         Be creative in your explanations and try to make learning enjoyable. Use examples and analogies when appropriate to help clarify complex concepts."""

    # 3. Create a chat session with the system instructions integrated
    print("🤖 Saathi: Establishing connection to AI...")
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7 # Lower means focused and safe, higher means more creative
        )
    )

    print("\n🤖 Saathi: Fully initialized and live! (Type 'exit' to quit)")
    print("-" * 70)

    # 4. Continuous Live Interaction Loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit","stop","Exit","Quit","Stop","EXIT","QUIT","STOP"]:
                print("\n🤖 Saathi: Thank you and All the best.")
                break

            # Send message to the model; the chat object implicitly holds the historical context
            response = chat.send_message(user_input)
            
            print(f"\n🤖 Saathi: {response.text}\n")
            print("-" * 70)
            print("")

        except Exception as e:
            print(f"\n❌ An error occurred during processing: {e}\n")

if __name__ == "__main__":
    Saathi()