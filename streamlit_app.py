#!/usr/bin/env python3
"""
Streamlit Cloud Entry Point for V3.0 Human-in-the-Loop Demo

This file serves as the main entry point for Streamlit Cloud deployment.
It sets up the environment and launches the main application.
"""

import os
import sys
from pathlib import Path
import streamlit as st

# Set environment variables for cloud deployment
os.environ["VISA_AGENT_VERSION"] = "v1.2_human_loop"
os.environ["VISA_AGENT_FORCE_LLM"] = "false"  # Use demo mode for cloud deployment

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def check_dependencies():
    """Check if all required dependencies are available"""
    missing_deps = []
    
    # Check core dependencies
    try:
        import langchain
        from langchain.prompts import PromptTemplate
        from langchain_openai import ChatOpenAI
        from langchain_community.document_loaders import TextLoader
    except ImportError as e:
        missing_deps.append(f"langchain components: {e}")
    
    try:
        import pandas
    except ImportError as e:
        missing_deps.append(f"pandas: {e}")
        
    try:
        import plotly
    except ImportError as e:
        missing_deps.append(f"plotly: {e}")
        
    try:
        import pydantic
    except ImportError as e:
        missing_deps.append(f"pydantic: {e}")
    
    return missing_deps

def show_dependency_error(missing_deps):
    """Show dependency error with instructions"""
    st.error(f"""
    ## 🚨 Missing Dependencies
    
    The following dependencies are missing:
    {chr(10).join(f"- {dep}" for dep in missing_deps)}
    
    **This is likely due to Streamlit Cloud using `requirements_cloud.txt` instead of `requirements.txt`**
    
    ### 🔧 Quick Fix Options:
    
    **Option 1: Use the main requirements.txt**
    - In Streamlit Cloud settings, ensure it uses `requirements.txt` (not `requirements_cloud.txt`)
    
    **Option 2: For immediate access, use local version:**
    ```bash
    git clone https://github.com/pbentle2006/VisaRequirements_Demo_HIL_Form_v3.0.git
    cd VisaRequirements_Demo_HIL_Form_v3.0
    pip install -r requirements.txt
    python3 run_v1_2_demo.py
    ```
    
    **Local URL:** http://localhost:8503
    
    ### 📞 Contact Information
    This demo showcases the V3.0 Human-in-the-Loop + Customer Form capabilities.
    For a live demonstration, please contact the development team.
    """)

# Check dependencies first
missing_deps = check_dependencies()

if missing_deps:
    # If LangChain is missing, show a working demo instead of just an error
    st.title("🛂 Visa Requirements Agent V3.0 - Demo Preview")
    
    st.error(f"""
    ## 🚨 LangChain Installation Issue
    
    The cloud deployment is missing LangChain components: {', '.join(missing_deps)}
    
    **This is a known Streamlit Cloud issue. The full demo works perfectly locally.**
    """)
    
    # Show a preview of what the demo contains
    st.success("""
    ## 🎯 V3.0 Human-in-the-Loop Demo Features
    
    This demo showcases an advanced enterprise visa processing system with:
    
    ### 👥 **Human-in-the-Loop Validation Workflow**
    - 4-step validation process with enterprise approval workflows
    - Quality scoring system (0-100%) with detailed analytics
    - Interactive question editing and validation
    - Multi-level approval system (Analyst → Manager → Director)
    
    ### 📋 **Customer Form Renderer**
    - Dynamic question types with intelligent field detection
    - Real-time validation and progress tracking
    - Draft saving and secure submission
    
    ### 🤖 **5-Agent AI System**
    - PolicyEvaluator, RequirementsCapture, QuestionGenerator
    - ValidationAgent, ConsolidationAgent
    - Advanced multi-agent orchestration
    
    ### 📊 **6-Page Navigation System**
    1. Workflow Analysis - Core processing
    2. Agent Architecture - System documentation  
    3. Agent Performance - Real-time metrics
    4. Human Validation - Approval workflows ⭐
    5. Customer Form - Interactive forms ⭐
    6. Policy Comparison - Multi-document analysis
    """)
    
    st.info("""
    ## 🚀 **Get Full Access**
    
    **Option 1: Run Locally (Recommended)**
    ```bash
    git clone https://github.com/pbentle2006/VisaRequirements_Demo_HIL_Form_v3.0.git
    cd VisaRequirements_Demo_HIL_Form_v3.0
    pip install -r requirements.txt
    python3 run_v1_2_demo.py
    ```
    **Local URL:** http://localhost:8503
    
    **Option 2: Contact for Live Demo**
    For a complete demonstration of the V3.0 capabilities, please contact the development team.
    
    **Repository:** https://github.com/pbentle2006/VisaRequirements_Demo_HIL_Form_v3.0
    """)
    
    # Show some sample screenshots or mockups if available
    st.subheader("📸 Demo Screenshots")
    st.info("The full demo includes interactive dashboards, form builders, validation workflows, and comprehensive analytics - all working seamlessly in the local version.")
    
else:
    # Import and run the main Streamlit application
    try:
        # Import the main streamlit app content directly
        exec(open('src/ui/streamlit_app.py').read())
        
    except FileNotFoundError:
        st.error("""
        ## 🚨 File Not Found
        
        The main application file `src/ui/streamlit_app.py` was not found.
        
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
