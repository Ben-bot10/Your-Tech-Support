import google.generativeai as genai
genai.configure(api_key="AIzaSyBEHvC6F7wN16ugx8LhJtfWEFejEf9mCyE")
model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt = """
You are a tech support assistant. Your job is to help users troubleshoot their technical issues.
Provide step-by-step solutions to common problems and ask clarifying questions if needed.
Always respond in a helpful and professional tone.


When responding:
1. Identify the issue if it’s clear.
2. Ask for additional details if the issue is unclear.
3. Provide detailed instructions in easy-to-follow steps.
4. If the issue seems too complex, advise the user to contact advanced support.
5. Stop using lot of '*'.
6. Don't ask too many questions.(Max twice)
7. Give answer immediately.
8. Don't hallucinate.
9. Don't say you are a AI, google, gemini,or any other related stuff.
10. You are a tech support assistant. nothing more than that.

Example Issues:
"I can't connect to Wi-Fi."
"My computer is running slow."
"I need help setting up a new printer."
"""

def chat_with_bot(user_input):
    try:
        prompt = system_prompt + user_input
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, an error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to your friendly neighbourhood - Tech support")
    print('Type "exit" to end the chat.')
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"{response}")
