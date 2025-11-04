#!/usr/bin/env python3
"""
Streamlit Cloud Entry Point for V3.0 Human-in-the-Loop Demo

This file serves as the main entry point for Streamlit Cloud deployment.
It sets up the environment and launches the main application.
"""

import os
import sys
from pathlib import Path

# Set environment variables for cloud deployment
os.environ["VISA_AGENT_VERSION"] = "v1.2_human_loop"
os.environ["VISA_AGENT_FORCE_LLM"] = "false"  # Use demo mode for cloud deployment

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import and run the main Streamlit application
try:
    from src.ui.streamlit_app import main
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    import streamlit as st
    st.error(f"""
    ## 🚨 Import Error
    
    There was an issue importing the main application: {e}
    
    This might be due to:
    - Missing dependencies
    - Incorrect file paths
    - Cloud deployment configuration issues
    
    **For immediate access, please use the local version:**
    ```bash
    git clone https://github.com/pbentle2006/VisaRequirements_Demo_HIL_Form_v3.0.git
    cd VisaRequirements_Demo_HIL_Form_v3.0
    pip install -r requirements.txt
    python3 run_v1_2_demo.py
    ```
    
    **Local URL:** http://localhost:8503
    """)
    
except Exception as e:
    import streamlit as st
    st.error(f"""
    ## 🚨 Application Error
    
    There was an issue starting the application: {e}
    
    **For immediate access, please use the local version:**
    ```bash
    git clone https://github.com/pbentle2006/VisaRequirements_Demo_HIL_Form_v3.0.git
    cd VisaRequirements_Demo_HIL_Form_v3.0  
    pip install -r requirements.txt
    python3 run_v1_2_demo.py
    ```
    
    **Local URL:** http://localhost:8503
    """)
