import ollama

exit_conditions = (":q", "quit", "exit")

print("Hybrid AI Chatbot (Local + Offline) is ready! Type ':q' to quit.\n")

while True:
    query = input("> ").strip().lower()

    if query in exit_conditions:
        print("Goodbye! 👋")
        break

    if not query:
        continue

    # 🔹 Simple rule-based responses FIRST (fast + reliable)
    if "hello" in query or "hi" in query:
        print("🪴 Hello! Nice to meet you.")
        continue
    elif "how are you" in query:
        print("🪴 I'm running locally and doing great 😄")
        continue
    elif "name" in query:
        print("🪴 I'm your hybrid chatbot!")
        continue
    elif "joke" in query:
        print("🪴 Why do programmers hate nature? Too many bugs 🐛")
        continue

    # 🔹 Otherwise, use Ollama AI
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": query}
            ]
        )

        print("🪴", response['message']['content'])

    except Exception as e:
        # 🔹 Fallback if Ollama fails
        print("⚠️ AI unavailable, using fallback mode.")
        print("🪴 I heard you say:", query)