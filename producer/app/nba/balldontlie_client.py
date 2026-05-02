import time
from datetime import datetime

import requests
from config import BALLDONTLIE_API_KEY

BASE_URL = "https://api.balldontlie.io"
HEADERS = {"Authorization": BALLDONTLIE_API_KEY}
PARAMS = {"next_cursor": None, "per_page": 25}


def create_balldontlie_client():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


def fetch_teams(client: requests.Session, team_id: int = None) -> list[dict]:
    """fetches data from the teams endpoint. defaults to getting all teams.

    Args:
        client (requests.Session): requests session client
        team_id (int, optional): id of the team to get. Defaults to None.

    Returns:
        list[dict]: data returned from the api
    """
    teams_url = f"{BASE_URL}/v1/teams"

    # update url if only getting 1 team
    if team_id is not None:
        teams_url += f"/{team_id}"

    response = client.get(teams_url)
    response.raise_for_status()

    data = response.json()
    data = data.get("data", [])

    # when passing team_id, the result is actually a single dict. for consistancy, wrap as a list
    if isinstance(data, dict):
        data = [data]

    return data


def fetch_players(client: requests.Session, player_id=None) -> list[dict]:
    """fetches a list of all players data from the api endpoint. defaults to all players.

    Args:
        client (requests.Session): requests session client
        player_id (_type_, optional): id of the player to get. Defaults to None.

    Returns:
        list[dict]: data returned from the api
    """
    players_url = f"{BASE_URL}/v1/players"
    params = {"cursor": None, "per_page": 100}

    if player_id is not None:
        players_url = f"{players_url}/{player_id}"

    next_cursor = None
    all_data = []
    while True:
        params["cursor"] = next_cursor
        response = client.get(players_url, params=params)
        response.raise_for_status()

        resp_data = response.json()
        if resp_data.get("meta").get("nex_cursor") is None:
            data = resp_data.get("data", [])
            all_data.append(data)
            next_cursor = resp_data.get("meta").get("next_cursor")

            # api limits 5 requests / min. this is extra safe prevention of hitting that cap.
            time.sleep(15)
        else:
            break

    return all_data


def fetch_games(client: requests.Session, date: datetime) -> list[dict]:
    """fetches games for a specific date

    Args:
        client (requests.Session): requests session client
        date (datetime): date of games data to get

    Returns:
        list[dict]: data returned from the api
    """
    games_url = f"{BASE_URL}/v1/games"
    start_date = end_date = date.strftime("%Y-%m-%d")
    params = {"start_date": start_date, "end_date": end_date, "per_page": 100}

    response = client.get(games_url, params=params)
    response.raise_for_status()

    data = response.json()
    data = data.get("data", [])

    if isinstance(data, dict):
        data = [data]

    return data
