import streamlit as st
import openai

# Set your OpenAI API key
OPENAI_API_KEY = "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"

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def generate_response(user_input, chat_history):
    messages = [{"role": "system", "content": "You are an AI assistant helping with Q&A."}]

    # Append previous chats
    for chat in chat_history:
        messages.append({"role": "user", "content": chat["question"]})
        messages.append({"role": "assistant", "content": chat["answer"]})

    # Append new user input
    messages.append({"role": "user", "content": user_input})

    # Query the LLM model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use another model
        messages=messages,
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]

def main():
    st.title(" Conversational AI - Ask Anything")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous conversations
    st.subheader("Chat History:")
    for chat in st.session_state.chat_history:
        st.write(f"**You:** {chat['question']}")
        st.write(f"**AI:** {chat['answer']}")
        st.write("---")

    # User input
    user_input = st.text_input("Enter your message:", key="user_input")

    # Get response button
    if st.button("Send"):
        if user_input:
            # Generate AI response
            ai_response = generate_response(user_input, st.session_state.chat_history)

            # Store in chat history
            st.session_state.chat_history.append({"question": user_input, "answer": ai_response})

            # Display response
            st.success(f"**AI:** {ai_response}")
        else:
            st.warning("⚠️ Please enter a message.")

if __name__ == "__main__":
    main()
