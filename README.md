# revit
Revit: The document AI

---

##### Start front
    npm run dev


##### Start back
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r .\back\docs\requirements.txt
    python .\back\src\main.py


#### .env file (must be on root directory)
    APP_CONTAINER_NAME=api_app          # [string] App conatiner name
    FASTAPI_APP=main:app                # [string] Main route
    FASTAPI_HOST=0.0.0.0                # [string] IP address
    FASTAPI_PORT=8080                   # [int] Port number
    FASTAPI_LOG_LEVEL=info              # [string] Log level fastapi parameter
    FASTAPI_RELOAD=true                 # [bool] Reloaded app fastapi parameter
    FASTAPI_WORKERS=1                   # [int] Workers fastapi parameter