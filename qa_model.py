import streamlit as st
from main_code1 import get_answer

def main():
    
    st.title("Question Answering System using BERT")

    # Example Context 1
    context = """
    The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
    It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
    Constructed from 1887 to 1889 as the entrance arch to the 1889 World's Fair, it was initially criticized
    by some of France's leading artists and intellectuals for its design.
    """

    st.subheader("Context:")
    st.write(context)

    # User Input: Question
    question = st.text_input("Enter your question:")

    # Get Answer Button
    if st.button("Get Answer"):
        if question:
            answer = get_answer(context, question)
            st.success(f"**Answer:** {answer}")
        else:
            st.warning("⚠️ Please enter a question.")

if __name__ == "__main__":
    main()
