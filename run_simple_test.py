#!/usr/bin/env python3
"""
Simple test launcher to isolate build issues
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Launch a minimal Streamlit test"""
    
    print("🧪 SIMPLE STREAMLIT TEST")
    print("=" * 30)
    
    # Set environment variables for demo mode
    os.environ["VISA_AGENT_VERSION"] = "v1.2_human_loop"
    os.environ["VISA_AGENT_FORCE_LLM"] = "false"
    
    # Get the project root directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    print(f"📁 Working directory: {project_root}")
    print(f"🐍 Python executable: {sys.executable}")
    print(f"📦 Python path: {sys.path[0]}")
    
    # Check if streamlit is available
    try:
        import streamlit
        print(f"✅ Streamlit version: {streamlit.__version__}")
    except ImportError:
        print("❌ Streamlit not installed!")
        print("   Try: pip install streamlit")
        return False
    
    # Check if main app file exists
    app_file = "src/ui/streamlit_app.py"
    if not os.path.exists(app_file):
        print(f"❌ Main app file not found: {app_file}")
        return False
    
    print(f"✅ Main app file found: {app_file}")
    
    # Try to launch with minimal configuration
    print("\n🚀 Launching Streamlit...")
    print("   URL: http://localhost:8503")
    print("   Press Ctrl+C to stop")
    print("-" * 30)
    
    try:
        # Launch with minimal config to avoid hanging
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            app_file,
            "--server.port", "8503",
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false"
        ]
        
        print(f"Command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching Streamlit: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
