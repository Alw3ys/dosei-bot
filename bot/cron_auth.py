from fastapi import HTTPException, Request, status

DEPLOYPLEX_CRON_SECRET = "YOUR_SECRET_VALUE_HERE"


def authenticate_request(request: Request):
    auth_header = request.headers.get("authorization")
    if auth_header != f"Bearer {DEPLOYPLEX_CRON_SECRET}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)