import requests
from retell inport Retail

# 🔐 Replace with your actual API key and agent ID
RETELL_API_KEY = ""
AGENT_ID = ""

BASE_URL = ""

headers = {
    "Authorization": f"Bearer {RETELL_API_KEY}",
    "Content-Type": "application/json"
}





def send_message( user_input):
    response = requests.post(
        f"{BASE_URL}",
        headers=headers,
        json={"text": user_input}
    )
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")


def get_response(session_id):
    response = requests.get(
        f"{BASE_URL}/session/{session_id}/messages",
        headers=headers
    )
    if response.status_code == 200:
        messages = response.json().get("messages", [])
        # Get the latest bot message
        bot_messages = [msg["text"] for msg in messages if msg["sender"] == "bot"]
        return bot_messages[-1] if bot_messages else "(No response yet)"
    else:
        raise Exception(f"Failed to get messages: {response.text}")


def main():
    print("🎤 Starting Retell AI Chat Session...")

    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("❌ Ending session.")
            break

        send_message(user_input)
        print("🧠 Waiting for response...")

        import time
        time.sleep(2)  # Give Retell some time to respond

        try:
            response = get_response(session_id)
            print(f"Bot: {response}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
