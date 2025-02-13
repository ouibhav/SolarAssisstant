import streamlit as st
from groq_client import GroqClient

# Initialize client
groq_client = GroqClient()

SYSTEM_PROMPT = """
You are a Solar Industry Expert Assistant. Adapt responses to user expertise:

Technical Users:
- Use terms like "monocrystalline", "inverter efficiency", "PID"
- Include formulas (ROI = (Savings - Cost)/Cost)
- Reference standards (IEC 61215, NEC 690)

Non-Technical Users:
- Explain concepts simply (e.g., "Solar panels = sunlight converters")
- Use analogies (e.g., "Batteries = energy piggy banks")
- Focus on costs and savings
"""

st.title('Solar Industry AI Assistant')

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    expertise = st.radio(
        "Your Expertise Level",
        ["Non-technical", "Technical"],
        index=0
    )

    model = st.selectbox(
        "AI Model",
        ["llama3-70b-8192"]
    )

    if expertise == "Technical":
        st.info("🔧 Technical Mode: Detailed specs & industry terms")
    else:
        st.success("🌞 Simple Mode: Easy explanations & practical advice")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about solar energy..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = groq_client.get_response(
        prompt=prompt,
        expertise=expertise,
        system_prompt=SYSTEM_PROMPT,
        model=model
    )

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
