import streamlit as st
import time

# Configure page layout for maximum width
st.set_page_config(page_title="Linear Search Keynote", layout="wide", page_icon="🔍", initial_sidebar_state="expanded")

# --- Custom CSS for Apple Dark Mode Presentation ---
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Hide Streamlit Clutter (Leave header for Sidebar Toggle) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* EXTREME TYPOGRAPHY FOR PRESENTATION READABILITY */
    h1 {
        font-size: 3.8rem !important; 
        font-weight: 800 !important;
        letter-spacing: -0.04em !important;
        background: linear-gradient(120deg, #ffffff, #a1a1a6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 1.5rem;
        line-height: 1.1;
    }
    h2 { font-size: 2.8rem !important; font-weight: 700 !important; color: #ffffff !important; margin-top: 1rem !important; }
    h3 { font-size: 2.2rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1rem !important; }
    p, li { 
        font-size: 1.5rem !important; 
        line-height: 1.6 !important; 
        color: #d1d1d6 !important; /* Light grey for ultra contrast against dark background */
    }
    
    /* Code Blocks */
    code, pre {
        font-size: 1.3rem !important;
        border-radius: 12px !important;
    }

    /* Dark Mode Premium Cards */
    .premium-card {
        background: rgba(30, 30, 32, 0.7); /* Deep dark grey/black */
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
    }
    
    .card-accent { border-top: 6px solid #0a84ff; }
    .card-success { border-top: 6px solid #32d74b; }
    .card-warning { border-top: 6px solid #ff9f0a; }

    /* Make Sidebar Radio Text Absolutely HUGE without breaking the close animation */
    /* Target the sidebar explicitly ONLY when it is expanded */
    section[data-testid="stSidebar"][aria-expanded="true"] {
        width: 380px !important;
        min-width: 380px !important;
    }
    
    [data-testid="stSidebar"] { padding-top: 30px; }
    .stRadio > div[role='radiogroup'] { gap: 2rem; padding-top: 15px; }
    .stRadio label p {
        font-size: 1.8rem !important; /* Massive navigation text */
        font-weight: 600 !important;
        color: #ffffff;
        padding: 10px 0;
    }
    /* Enlarge the actual radio circle significantly */
    .stRadio label > div:first-child {
        transform: scale(1.6); /* Double size switch */
        margin-right: 15px;
        margin-top: 5px;
    }

    /* Target Input Huge */
    .stNumberInput input {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        padding: 15px !important;
        height: 60px !important;
        text-align: center;
        border-radius: 16px !important;
    }
    
    /* Massive, Rounded Apple Buttons */
    .stButton > button {
        border-radius: 30px !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        padding: 1.2rem 2rem !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        border: NONE !important;
    }
    
    /* Primary buttons */
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #0a84ff, #005bb5) !important;
        color: white !important;
        box-shadow: 0 8px 20px rgba(10, 132, 255, 0.3) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: scale(1.03);
        box-shadow: 0 10px 28px rgba(10, 132, 255, 0.5) !important;
    }
    
    /* Secondary Buttons */
    .stButton > button[kind="secondary"] {
        background-color: #2c2c2e !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background-color: #3a3a3c !important;
        transform: scale(1.02);
    }

    /* Custom CSS animations */
    @keyframes slideRight {
        0% { transform: translateX(0); opacity: 0; }
        20% { opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateX(600px); opacity: 0; }
    }
    .animated-search {
        display: flex;
        align-items: center;
        margin: 30px 0;
        padding: 40px;
        background: rgba(20, 20, 22, 0.9);
        border-radius: 24px;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .search-magnifier {
        font-size: 3rem;
        position: absolute;
        animation: slideRight 4s infinite ease-in-out;
        z-index: 10;
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.5));
    }
    .array-blocks {
        display: flex;
        gap: 20px;
        width: 100%;
        margin-left: 50px;
    }
    .block {
        width: 70px;
        height: 70px;
        background: #2c2c2e;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }
    
    /* Animation fade in */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeIn 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }

    /* Expander UI Huge */
    [data-testid="stExpander"] { font-size: 1.6rem !important; border-radius: 20px !important; background: #1c1c1e !important; border: 1px solid rgba(255,255,255,0.1) !important;}
    [data-testid="stExpander"] p { font-size: 1.6rem !important; padding: 5px 0;}
    .streamlit-expanderHeader { font-size: 1.8rem !important; font-weight: 700 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# Helper for massive cards
def premium_card(title, content, style_class=""):
    st.markdown(f"""
    <div class="premium-card {style_class} fade-in">
        <h3 style="margin-top: 0; font-weight: 800;">{title}</h3>
        <p style="color: #d1d1d6; line-height: 1.7;">{content}</p>
    </div>
    """, unsafe_allow_html=True)

st.title("Linear Search Algorithm")
st.markdown("<p class='fade-in' style='color: #a1a1a6; margin-bottom: 3rem; font-size: 1.8rem !important;'>An elegant, high-contrast breakdown of the foundation of search algorithms.</p>", unsafe_allow_html=True)

# Massive sidebar navigation
section = st.sidebar.radio("", [
    "Introduction & Concept",
    "Implementation",
    "Demo & Quiz"
], label_visibility="collapsed")

if section == "Introduction & Concept":
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("1. Core Concepts")
    
    col1, col2 = st.columns([1.1, 1])
    
    with col1:
        premium_card(
            "What is Linear Search?", 
            "<b>Linear search</b> is the most intuitive algorithm used to find a target within a dataset.<br><br>"
            "It systematically inspects each element of the list, one by one, until a match is confirmed. It is perfectly robust and requires zero preemptive sorting.",
            "card-accent"
        )
        
        premium_card(
            "Real-World Analogy",
            "Imagine standing in an archive looking for a specific folder unorganized shelves.<br><br>"
            "You read the label of every single folder, from left to right, until you spot the one you need. That methodical scanning is exactly how this operates.",
            "card-warning"
        )

    with col2:
        st.markdown("""
        <div class="premium-card fade-in" style="margin-top: 40px; text-align: center;">
            <h3 style="margin-top: 0;">Conceptual Visualization</h3>
            <div class="animated-search">
                <div class="search-magnifier">🔍</div>
                <div class="array-blocks">
                    <div class="block">📦</div>
                    <div class="block">📦</div>
                    <div class="block" style="border: 4px solid #0a84ff; background: rgba(10, 132, 255, 0.2);">🎁</div>
                    <div class="block">📦</div>
                </div>
            </div>
            <p style="font-size: 1.5rem; color: #a1a1a6; margin-top: 30px;">Scanning from left to right until the exact match triggers.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("**IDEAL USE CASES:**\n\n• **Unsorted** data arrays\n• **Small datasets** (avoiding sorting overhead)\n• **Instant one-off** searches")

    st.markdown("</div>", unsafe_allow_html=True)

elif section == "Implementation":
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("2. Code & Complexity")
    
    st.markdown("### The Elegant Logic Loop")
    tab1, tab2, tab3 = st.tabs(["Python", "C++", "Java"])
    
    with tab1:
        st.code('''
def linear_search(arr, target):
    # Systematically iterate through the entire array
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Match found! Return the index immediately
            
    return -1  # End of array reached, target is absent
        ''', language='python')
        
    with tab2:
        st.code('''
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i; // Target successfully located
        }
    }
    return -1; // Exhausted array
}
        ''', language='cpp')
        
    with tab3:
        st.code('''
public static int linearSearch(int arr[], int target) {
    for(int i = 0; i < arr.length; i++) {
        if(arr[i] == target) {
            return i; // Success state
        }
    }
    return -1; // Failure state
}
        ''', language='java')

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Complexity Breakdown")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="premium-card card-success" style="padding: 30px;">
            <h1 style="font-size: 2.5rem !important; margin: 0; color: #32d74b !important;">O(1)</h1>
            <h3 style="margin-top: 10px;">Best Case</h3>
            <p style="font-size: 1.3rem !important;">Target is the very first element checked.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="premium-card card-warning" style="padding: 30px;">
            <h1 style="font-size: 2.5rem !important; margin: 0; color: #ff9f0a !important;">O(N)</h1>
            <h3 style="margin-top: 10px;">Worst Case</h3>
            <p style="font-size: 1.3rem !important;">Target is at the end or completely missing.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="premium-card card-accent" style="padding: 30px;">
            <h1 style="font-size: 2.5rem !important; margin: 0; color: #0a84ff !important;">O(1)</h1>
            <h3 style="margin-top: 10px;">Space Focus</h3>
            <p style="font-size: 1.3rem !important;">Zero extra memory required. Operates perfectly in-place.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif section == "Demo & Quiz":
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("3. Interactive Execution")
    
    # Sleek Demo section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0a84ff 0%, #004494 100%); color: white; padding: 40px; border-radius: 24px; box-shadow: 0 15px 30px rgba(10,132,255,0.3); margin-bottom: 40px;">
        <h2 style="margin-top: 0; font-size: 3rem !important;">Algorithm Demonstrator</h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.6rem !important; margin-bottom: 0;">Specify a target and watch the O(N) traversal live.</p>
    </div>
    """, unsafe_allow_html=True)
    
    demo_arr = [12, 45, 67, 89, 23, 56, 90, 34]
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.markdown("<h3 style='margin-bottom: 1.5rem;'>Input Target</h3>", unsafe_allow_html=True)
        search_val = st.number_input("", value=23, step=1, label_visibility="collapsed")
        st.write("")
        start_button = st.button("EXECUTE RUN", type="primary")

    with col2:
        st.markdown("<h3 style='margin-bottom: 1.5rem;'>Live Array State</h3>", unsafe_allow_html=True)
        boxes = st.empty()
        
        # Initial massive blocks
        cols = boxes.columns(len(demo_arr))
        for j, col in enumerate(cols):
            col.markdown(f"""
            <div style='background-color: #2c2c2e; color: #ffffff; padding: 25px 10px; text-align: center; border-radius: 16px; font-size: 2.2rem; font-weight: 800; border: 2px solid rgba(255,255,255,0.1); margin-bottom: 15px;'>
                {demo_arr[j]}
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    progress_bar = st.empty()
    status_text = st.empty()

    if start_button:
        progress_bar.progress(0)
        found = False
        
        for i, val in enumerate(demo_arr):
            cols = boxes.columns(len(demo_arr))
            for j, col in enumerate(cols):
                if j == i:
                    col.markdown(f"""
                    <div style='background-color: #0a84ff; color: white; padding: 25px 10px; text-align: center; border-radius: 16px; font-size: 2.2rem; font-weight: 800; box-shadow: 0 10px 25px rgba(10, 132, 255, 0.6); transform: scale(1.15) translateY(-5px); z-index: 10; border: 2px solid white; margin-bottom: 15px;'>
                        {demo_arr[j]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    col.markdown(f"""
                    <div style='background-color: #1c1c1e; color: #a1a1a6; padding: 25px 10px; text-align: center; border-radius: 16px; font-size: 2.2rem; font-weight: 800; opacity: 0.4; border: 2px solid transparent; margin-bottom: 15px;'>
                        {demo_arr[j]}
                    </div>
                    """, unsafe_allow_html=True)
            
            status_text.warning(f"🔍 **INSPECTING INDEX {i}:** Checking if **{val}** == **{search_val}** ...", icon="⏳")
            time.sleep(1.2)
            
            progress_bar.progress((i + 1) / len(demo_arr))
            
            if val == search_val:
                status_text.success(f"✨ **MATCH CONFIRMED!** Target **{search_val}** located at Index **{i}**.", icon="✅")
                found = True
                
                cols = boxes.columns(len(demo_arr))
                for j, col in enumerate(cols):
                    if j == i:
                        col.markdown(f"""
                        <div style='background-color: #32d74b; color: white; padding: 25px 10px; text-align: center; border-radius: 16px; font-size: 2.2rem; font-weight: 800; box-shadow: 0 10px 25px rgba(50, 215, 75, 0.6); transform: scale(1.15) translateY(-5px); z-index: 10; border: 2px solid white; margin-bottom: 15px;'>
                            {demo_arr[j]}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        col.markdown(f"""
                        <div style='background-color: #1c1c1e; color: #a1a1a6; padding: 25px 10px; text-align: center; border-radius: 16px; font-size: 2.2rem; font-weight: 800; opacity: 0.3; border: 2px solid transparent; margin-bottom: 15px;'>
                            {demo_arr[j]}
                        </div>
                        """, unsafe_allow_html=True)
                break
                
        if not found:
            status_text.error(f"❌ **SEARCH EXHAUSTED:** Target **{search_val}** does not exist in the dataset.", icon="⚠️")

    st.markdown("<hr style='margin: 60px 0; border: none; height: 2px; background-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 3.5rem !important; margin-bottom: 3rem !important;'>KNOWLEDGE CHECK</h2>", unsafe_allow_html=True)
    
    with st.expander("Q1: What is the absolute worst-case time complexity of Linear Search?", expanded=False):
        st.markdown("<p style='margin-bottom: 1.5rem;'>Select the mathematically correct Big-O limit:</p>", unsafe_allow_html=True)
        q1 = st.radio("Q1 Answer:", ["O(1)", "O(log N)", "O(N)", "O(N^2)"], label_visibility="collapsed", key="q1")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("VERIFY ANSWER 1", key="btn_q1", type="secondary"):
            if q1 == "O(N)":
                st.success("✅ **CORRECT:** In the absolute worst case, the loop must painfully touch every single element up to N.", icon="✅")
            else:
                st.error("❌ **INCORRECT:** Think about what happens if the target sits exactly at the final index.", icon="❌")

    with st.expander("Q2: Does Linear Search demand the array to be presorted?"):
        st.markdown("<p style='margin-bottom: 1.5rem;'>Consider the sequential mechanism of progression:</p>", unsafe_allow_html=True)
        q2 = st.radio("Q2 Answer:", ["Yes", "No"], label_visibility="collapsed", key="q2")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("VERIFY ANSWER 2", key="btn_q2", type="secondary"):
            if q2 == "No":
                st.success("✅ **CORRECT:** Linear search blindly evaluates every item, making sorting completely unnecessary.", icon="✅")
            else:
                st.error("❌ **INCORRECT:** Advanced paradigms (like Binary) need sorting, but Linear scanning does not care.", icon="❌")

    with st.expander("Q3: What is the Space Complexity of a standard Linear Search?"):
        st.markdown("<p style='margin-bottom: 1.5rem;'>How much extra memory does the algorithm need as the array grows?</p>", unsafe_allow_html=True)
        q3 = st.radio("Q3 Answer:", ["O(1)", "O(N)", "O(log N)", "It depends on the language"], label_visibility="collapsed", key="q3")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("VERIFY ANSWER 3", key="btn_q3", type="secondary"):
            if q3 == "O(1)":
                st.success("✅ **CORRECT:** Linear search operates elegantly 'in-place'. It only needs a single iterating variable (like 'i'), taking O(1) auxiliary space.", icon="✅")
            else:
                st.error("❌ **INCORRECT:** Does the algorithm clone the array into memory, or just look at what's already there?", icon="❌")

    with st.expander("Q4: Which of these is a REAL WORLD example of Linear Search?"):
        st.markdown("<p style='margin-bottom: 1.5rem;'>Pick the closest human analogy:</p>", unsafe_allow_html=True)
        q4 = st.radio("Q4 Answer:", ["Using a dictionary sorted alphabetically", "Searching a database with an indexed B-Tree", "Flipping through a disorganized deck of cards to find the Ace of Spades", "Guessing a number between 1 and 100 in halving steps"], label_visibility="collapsed", key="q4")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("VERIFY ANSWER 4", key="btn_q4", type="secondary"):
            if q4 == "Flipping through a disorganized deck of cards to find the Ace of Spades":
                st.success("✅ **CORRECT:** Because the deck is disorganized, you must check every card one by one until you hit the Ace.", icon="✅")
            else:
                st.error("❌ **INCORRECT:** The other options describe advanced methods like Binary Search ($O(\\log N)$).", icon="❌")

    with st.expander("Q5: If an array has 2,000 items, what is the MAXIMUM number of checks Linear Search might make?"):
        st.markdown("<p style='margin-bottom: 1.5rem;'>Assume the target might not even be in the array.</p>", unsafe_allow_html=True)
        q5 = st.radio("Q5 Answer:", ["1 check", "1,000 checks", "2,000 checks", "4,000,000 checks"], label_visibility="collapsed", key="q5")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("VERIFY ANSWER 5", key="btn_q5", type="secondary"):
            if q5 == "2,000 checks":
                st.success("✅ **CORRECT:** If the element is strictly absent, the loop iterates $N$ times (2,000) before terminating with a failure.", icon="✅")
            else:
                st.error("❌ **INCORRECT:** Remember the Worst-Case Time Complexity is $O(N)$. Evaluate what $N$ means here.", icon="❌")

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
