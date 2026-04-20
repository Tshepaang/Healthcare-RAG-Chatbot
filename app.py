import streamlit as st

st.set_page_config(page_title="Netcare Assistant", page_icon="🏥")
st.title("🏥 Netcare AI Assistant")
st.markdown("Ask me anything about Netcare services!")

# FAQ database (works without any API key)
faq_data = {
    "visiting hours": "Visiting hours are from 10:00 to 20:00 daily.",
    "visiting": "Visiting hours are from 10:00 to 20:00 daily.",
    "hours": "Visiting hours are from 10:00 to 20:00 daily.",
    "covid test": "Call 0800 123 456 or visit any Netcare Medicross.",
    "covid": "Call 0800 123 456 or visit any Netcare Medicross.",
    "testing": "Call 0800 123 456 or visit any Netcare Medicross.",
    "emergency": "Call 082 911 for ambulance services.",
    "ambulance": "Call 082 911 for ambulance services.",
    "medical aid": "We accept Discovery, Momentum, and Bonitas.",
    "medical": "We accept Discovery, Momentum, and Bonitas.",
    "insurance": "We accept Discovery, Momentum, and Bonitas.",
    "specialist": "Call 0860 123 456 to book a specialist.",
    "doctor": "Call 0860 123 456 to book a specialist.",
    "address": "Netcare hospitals are located nationwide. Main office: Johannesburg.",
    "phone": "Call Netcare at 0860 123 456.",
    "contact": "Call Netcare at 0860 123 456."
}

st.info("💡 Try asking: visiting hours, covid test, emergency number, medical aid, or specialist")

user_input = st.text_input("💬 Your question:", placeholder="e.g., What are visiting hours?")

if user_input:
    user_lower = user_input.lower()
    answer = None
    
    # Find matching answer
    for key, value in faq_data.items():
        if key in user_lower:
            answer = value
            break
    
    # If no match found
    if not answer:
        answer = "I'm not sure about that. Please contact Netcare directly at 0860 123 456 for assistance."
    
    st.success(f"**Answer:** {answer}")
    
    # Show what was matched (helpful for debugging)
    st.caption("💡 Need more answers? Add them to the FAQ database!")
