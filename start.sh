#!/bin/bash
# Railway startup script for V3.0 Human-in-the-Loop Demo

echo "🚀 Starting V3.0 Human-in-the-Loop Demo on Railway..."

# Set environment variables for demo mode
export VISA_AGENT_VERSION="v1.2_human_loop"
export VISA_AGENT_FORCE_LLM="false"

# Start Streamlit with Railway configuration
streamlit run streamlit_app.py \
    --server.port $PORT \
    --server.address 0.0.0.0 \
    --server.headless true \
    --server.enableCORS false \
    --server.enableXsrfProtection false
