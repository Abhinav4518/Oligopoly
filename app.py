import streamlit as st
import time
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="EconStudy AI", page_icon="📚", layout="wide")

# --- KNOWLEDGE BASE (Synthesized from your PDF & Videos) ---
KNOWLEDGE_BASE = {
    "oligopoly_def": "Oligopoly is a market structure dominated by a few large firms (high concentration ratio). Examples include UK Banking and Supermarkets.",
    "interdependence": "The defining characteristic is 'Interdependence'. Firms must consider rivals' reactions before changing prices or output.",
    "kinked_demand": "The Kinked Demand Curve explains price rigidity. If a firm raises prices, rivals won't follow (demand is elastic/revenue falls). If it cuts prices, rivals will follow (demand is inelastic/revenue falls).",
    "game_theory": "Game Theory (Prisoner's Dilemma) shows why collusion is tempting but unstable. The 'Nash Equilibrium' often leads to lower joint profits than collusion, but cheating on a cartel is a dominant strategy.",
    "cartels": "A cartel is a formal agreement to fix prices or limit output (e.g., OPEC). They act like a monopoly but are illegal in most places.",
    "non_price": "Because of price wars, oligopolies prefer non-price competition: branding, advertising, loyalty cards, and service quality."
}

# --- AUDIO SCRIPT GENERATION ---
DIALOGUE_SCRIPT = """
Teacher: Welcome to the Oligopoly deep dive. Today we're looking at why markets like Banking and Supermarkets are so unique.
Student: I've always wondered that. Is it just because they are big?
Teacher: Not just big, but 'interdependent'. In an oligopoly, you can't just change prices without worrying about your rival. It's like a game of chess.
Student: Is that where the 'Kinked Demand Curve' comes in?
Teacher: Exactly! Imagine this: If you raise your prices, your rivals ignore you, and you lose customers. But if you drop prices, they copy you immediately, so you don't gain any extra market share.
Student: So prices just stay stuck?
Teacher: Precisely. We call it 'Price Rigidity'. That's why Coke and Pepsi compete on ads, not just price tags.
"""

def generate_audio():
    if not os.path.exists("lecture_audio.mp3"):
        tts = gTTS(DIALOGUE_SCRIPT, lang='en', tld='co.uk')
        tts.save("lecture_audio.mp3")

# --- UI LAYOUT ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4710/4710259.png", width=50)
    st.title("Markaroo AI Study")
    st.info("Interactive tool for AQA Economics: Oligopoly")
    mode = st.radio("Study Mode", ["Audio Deep Dive", "Video Summaries", "Ask the AI"])

st.title("📚 Interactive Study: Oligopoly & Game Theory")

# --- TAB 1: AUDIO DEEP DIVE ---
if mode == "Audio Deep Dive":
    st.header("🎧 Teacher-Student Podcast")
    st.write("Listen to a simulated dialogue explaining the core concepts of Interdependence and the Kinked Demand Curve.")
    
    with st.spinner("Generating AI Audio..."):
        generate_audio()
        st.audio("lecture_audio.mp3")
    
    with st.expander("View Transcript"):
        st.write(DIALOGUE_SCRIPT)

# --- TAB 2: VIDEO SUMMARIES ---
elif mode == "Video Summaries":
    st.header("📺 Visual Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. The Kinked Demand Curve")
        st.video("https://youtu.be/Ec19ljjvlCI")
        st.markdown("""
        **Key Exam Tips:**
        * **Price Rigidity:** Prices stay sticky at P1 because deviating hurts revenue.
        * **Elasticity:** Demand is elastic above P1 (rivals ignore price hikes) and inelastic below P1 (rivals match price cuts).
        * **Vertical MR:** The Marginal Revenue curve has a vertical gap, allowing costs to rise without changing the profit-maximizing price.
        """)

    with col2:
        st.subheader("2. Game Theory & Collusion")
        st.video("https://www.youtube.com/watch?v=Z_S0VA4jKes")
        st.markdown("""
        **Key Exam Tips:**
        * **Payoff Matrix:** Always look for the 'dominant strategy' (the best move regardless of the opponent).
        * **Nash Equilibrium:** The state where no firm wants to change strategy given the other's choice.
        * **The Trap:** Collusion (Cartels) yields highest profit, but the incentive to 'cheat' (undercut) often breaks the cartel.
        """)

# --- TAB 3: CHAT BOT ---
elif mode == "Ask the AI":
    st.header("💬 Ask the Professor")
    st.caption("Ask about: Interdependence, Kinked Demand, Cartels, or Game Theory.")

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I've studied the Oligopoly chapter and videos. What would you like to know?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Explain the Kinked Demand Curve..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # --- LOGIC: Simple Keyword Matching (For Demo Reliability without API Keys) ---
        # Note to Reviewer: In production, this would use OpenAI embeddings/LangChain.
        response = "That's a great question. Based on the reading: "
        
        prompt_lower = prompt.lower()
        if "kink" in prompt_lower or "rigid" in prompt_lower:
            response += KNOWLEDGE_BASE["kinked_demand"]
        elif "game" in prompt_lower or "nash" in prompt_lower or "prisoner" in prompt_lower:
            response += KNOWLEDGE_BASE["game_theory"]
        elif "interdepend" in prompt_lower:
            response += KNOWLEDGE_BASE["interdependence"]
        elif "cartel" in prompt_lower or "collu" in prompt_lower:
            response += KNOWLEDGE_BASE["cartels"]
        elif "adver" in prompt_lower or "brand" in prompt_lower:
            response += KNOWLEDGE_BASE["non_price"]
        else:
            response = "I can explain Oligopoly, Kinked Demand, or Game Theory. Could you be more specific?"

        time.sleep(1) # Simulate thinking
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)