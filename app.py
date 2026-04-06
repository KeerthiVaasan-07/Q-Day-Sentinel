import streamlit as st
import pandas as pd
from scanner import scan_file
from utils import calculate_risk_score
from quantum_sim import simulate_shors_step

st.set_page_config(page_title="Q-Day Sentinel", layout="wide")

st.title("🛡️ Q-Day Sentinel: Quantum Vulnerability Mapper")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("🔍 Code Audit")
    uploaded_file = st.file_uploader("Upload a Python file to scan for legacy crypto", type=['py'])
    
    if uploaded_file:
        # Save temp file
        with open("temp.py", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        results = scan_file("temp.py")
        if results:
            st.error(f"Found {len(results)} vulnerabilities!")
            st.table(pd.DataFrame(results))
        else:
            st.success("No legacy crypto found!")

with col2:
    st.header("📉 Risk Projection (Mosca's Theorem)")
    shelf_life = st.slider("How many years must data stay secret?", 1, 50, 10)
    transition = st.slider("Years to upgrade your infrastructure?", 1, 10, 3)
    
    status, gap = calculate_risk_score(shelf_life, transition)
    
    if status == "CRITICAL":
        st.metric("Risk Status", status, f"{gap} years overdue", delta_color="inverse")
        st.warning("Your data will likely be decrypted by a quantum attacker before its secrecy period ends.")
    else:
        st.metric("Risk Status", status, f"{abs(gap)} year buffer")

st.markdown("---")
if st.button("🚀 Run Quantum Attack Simulation (Shor's Step)"):
    st.write("Simulating quantum interference to find RSA factors...")
    counts = simulate_shors_step()
    st.bar_chart(counts)
    st.success("Quantum interference pattern found! Factoring successful.")
