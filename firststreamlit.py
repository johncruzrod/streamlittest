import streamlit as st
import anthropic

# Use Streamlit's secret management to safely store and access your API key
api_key = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=api_key)

def query_model(user_input):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.5,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    # Adjust the following line according to the actual structure of `response`
    return response.content  # Make sure this matches the structure of your API response

st.title("Query Claude Model")

# User input
user_input = st.text_input("Enter your text to query the Claude model:")

if st.button("Submit"):
    if user_input:
        result = query_model(user_input)
        st.write(result)
    else:
        st.write("Please enter some text to query the model.")
