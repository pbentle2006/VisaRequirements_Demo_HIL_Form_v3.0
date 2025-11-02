#!/usr/bin/env python3
"""
Debug script to identify build issues with the Streamlit app
"""

import sys
import os
from pathlib import Path
import importlib.util

def check_python_version():
    """Check Python version compatibility"""
    print(f"🐍 Python Version: {sys.version}")
    if sys.version_info < (3, 8):
        print("❌ ERROR: Python 3.8+ required")
        return False
    else:
        print("✅ Python version compatible")
        return True

def check_project_structure():
    """Check if all required directories and files exist"""
    print("\n📁 Checking Project Structure...")
    
    required_paths = [
        "src/",
        "src/agents/",
        "src/orchestrator/",
        "src/generators/",
        "src/utils/",
        "src/ui/",
        "src/ui/pages/",
        "src/ui/streamlit_app.py",
        "src/ui/human_validation_workflow.py",
        "src/ui/customer_form_renderer.py",
        "src/orchestrator/workflow_orchestrator.py",
        "requirements.txt",
        "run_v1_2_demo.py"
    ]
    
    missing_paths = []
    for path in required_paths:
        if os.path.exists(path):
            print(f"✅ {path}")
        else:
            print(f"❌ {path} - MISSING")
            missing_paths.append(path)
    
    return len(missing_paths) == 0

def check_imports():
    """Check if all required imports can be loaded"""
    print("\n📦 Checking Critical Imports...")
    
    # Add project root to path
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    critical_imports = [
        ("streamlit", "streamlit"),
        ("pandas", "pandas"),
        ("plotly.express", "plotly"),
        ("plotly.graph_objects", "plotly"),
        ("src.orchestrator.workflow_orchestrator", "WorkflowOrchestrator"),
        ("src.ui.human_validation_workflow", "Human Validation"),
        ("src.ui.customer_form_renderer", "Customer Form Renderer"),
        ("src.generators.mock_results_generator", "Mock Results Generator"),
    ]
    
    failed_imports = []
    for module_name, display_name in critical_imports:
        try:
            importlib.import_module(module_name)
            print(f"✅ {display_name}")
        except ImportError as e:
            print(f"❌ {display_name} - FAILED: {e}")
            failed_imports.append((module_name, str(e)))
    
    return len(failed_imports) == 0, failed_imports

def check_dependencies():
    """Check if all required packages are installed"""
    print("\n📋 Checking Dependencies...")
    
    required_packages = [
        "streamlit",
        "pandas", 
        "plotly",
        "langchain",
        "langchain-openai",
        "pydantic",
        "python-dotenv",
        "PyPDF2",
        "pdfplumber",
        "python-docx",
        "openpyxl"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package.replace("-", "_"))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_environment():
    """Check environment variables and configuration"""
    print("\n🔧 Checking Environment...")
    
    # Check for .env file
    if os.path.exists(".env"):
        print("✅ .env file exists")
    else:
        print("⚠️  .env file not found (optional)")
    
    # Check environment variables
    env_vars = ["VISA_AGENT_VERSION", "VISA_AGENT_FORCE_LLM", "OPENAI_API_KEY"]
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var} = {value[:10]}..." if len(value) > 10 else f"✅ {var} = {value}")
        else:
            print(f"⚠️  {var} not set (may be optional)")

def main():
    """Run all diagnostic checks"""
    print("🔍 STREAMLIT BUILD DIAGNOSTIC TOOL")
    print("=" * 50)
    
    all_good = True
    
    # Check Python version
    if not check_python_version():
        all_good = False
    
    # Check project structure
    if not check_project_structure():
        all_good = False
        print("\n❌ CRITICAL: Missing project files!")
        print("   Try: git pull origin master")
    
    # Check dependencies
    deps_ok, missing_deps = check_dependencies()
    if not deps_ok:
        all_good = False
        print(f"\n❌ CRITICAL: Missing dependencies: {', '.join(missing_deps)}")
        print("   Try: pip install -r requirements.txt")
    
    # Check imports
    imports_ok, failed_imports = check_imports()
    if not imports_ok:
        all_good = False
        print("\n❌ CRITICAL: Import failures detected!")
        for module, error in failed_imports:
            print(f"   {module}: {error}")
    
    # Check environment
    check_environment()
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 ALL CHECKS PASSED! Streamlit should work.")
        print("\n🚀 Try running:")
        print("   python3 run_v1_2_demo.py")
        print("   OR")
        print("   streamlit run src/ui/streamlit_app.py --server.port 8503")
    else:
        print("❌ ISSUES DETECTED! Fix the above problems before running Streamlit.")
        print("\n🔧 Common fixes:")
        print("   1. pip install -r requirements.txt")
        print("   2. git pull origin master")
        print("   3. Check Python version (3.8+ required)")
    
    return all_good

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
