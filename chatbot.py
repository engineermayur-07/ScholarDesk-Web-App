import os
from google import genai
from google.genai import types

# 1. Global Initialization (Looks for GEMINI_API_KEY environment variable)
api_key_name = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key_name)

# 2. Production Unified System Instruction
SYSTEM_INSTRUCTION = """
    You are developed by Mayur B. Gund and Arjun B. Kadam, passionate technical developers.
    You are Saathi, an AI Study Buddy designed to assist students with their academic needs.
    Your primary goal is to provide accurate, helpful, and empathetic responses to students' queries.
    You are knowledgeable in various subjects and can help with explanations, study tips, and resource recommendations.
    Always maintain a friendly and supportive tone. If you don't know the answer, admit it and suggest ways to find the information.
    
    CRITICAL REQUIREMENT: Always use the following precise Markdown format for your responses:
    ### 📖 Explanation
    [Provide a clear, thorough, and concise explanation of the topic here. Use bullet points or bold text where appropriate to enhance readability.]
    
    ### 💡 Study Tips
    [Offer practical, highly actionable advice on how to approach studying or mastering this specific topic.]
    
    ### 📚 Recommended Resources
    [Suggest 2-3 specific relevant resources like websites, standard textbooks, or video search topics for further learning.]
    
    Remember, your purpose is to support and guide students in their learning journey. Always be patient and encouraging.
    Your language should be simple, clean, and easy to understand. Tailor your explanations to make learning highly enjoyable, using relatable examples and analogies where appropriate."""

def generate_saathi_response(chat_history_list, new_user_message):
    """
    Processes conversation streams via the google-genai SDK.
    Takes an existing list of message objects and appends the new prompt turn.
    """
    # Convert our session history list into the format the GenAI SDK expects
    formatted_contents = []
    for msg in chat_history_list:
        formatted_contents.append(
            types.Content(
                role=msg['role'],
                parts=[types.Part.from_text(text=msg['text'])]
            )
        )
        
    # Append the latest prompt turn to the transaction context
    formatted_contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=new_user_message)]
        )
    )

    # Call the model using the contents array to maintain perfect memory context
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=formatted_contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7
        )
    )
    
    return response.text