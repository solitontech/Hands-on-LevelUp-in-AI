# ⚠️ WARNING: DO NOT MODIFY THIS FILE ⚠️
# This client module is part of the SPL-7 infrastructure and any changes
# may break the registration process or cause unexpected behavior.
# If you encounter issues, please contact the SPL team for assistance.

import os
import json
import requests

BASE_URL = "https://spl7backend.solitontech.ai/v1"


def _handle_request_exception(response: requests.Response) -> dict:
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        try:
            # Try to parse JSON, fallback to text
            return err.response.json()
        except ValueError:
            return {"error": err.response.text, "status_code": err.response.status_code}
    except requests.exceptions.RequestException as err:
        return {"error": f"Request failed: {err}"}

def _get_api_key_from_env(api_key:str|None)->str:
    if api_key:
        return api_key
    env_api_key = os.getenv("SPL_API_KEY")
    if env_api_key:
        return env_api_key
    msg = "Either SPL API key should be provided as argument or present in environment variables as SPL_API_KEY."
    raise ValueError(msg)

def register_team(team_name: str, participants: list, api_key:str|None=None):
    """Registers a new team with a list of participants."""
    url = f"{BASE_URL}/register-team"
    headers = {"X-API-Key": _get_api_key_from_env(api_key), "Content-Type": "application/json"}
    payload = {
        "team_name": team_name,
        "participants": participants,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return _handle_request_exception(response)

def update_team_info(team_id: int,team_name:str, participants: list, api_key:str|None=None):
    """Updates the participants for a specific team."""
    url = f"{BASE_URL}/update-team/{team_id}"
    headers = {"X-API-Key": _get_api_key_from_env(api_key), "Content-Type": "application/json"}
    payload = {
        "team_name": team_name,
        "participants": participants,
    }
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    return _handle_request_exception(response)

def track_progress(task_id: str, artifacts: dict|None=None, api_key:str|None=None):
    """Tracks a user's progress on a specific task."""
    url = f"{BASE_URL}/track-progress"
    headers = {"X-API-Key": _get_api_key_from_env(api_key), "Content-Type": "application/json"}
    payload = {
        "task_id": task_id,
        "artifacts": artifacts or {},
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return _handle_request_exception(response)

# TODO: Temporary function until SSO authentication is implemented
def get_api_key(email:str)->str:
    url = f"{BASE_URL}/apikey/{email}"
    response = requests.get(url)
    data = _handle_request_exception(response)
    return data["api_key"]