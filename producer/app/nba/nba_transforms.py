from datetime import datetime, timezone


def build_game_score_events(game_data: list[dict]) -> list[dict]:
    """builds the balldontlie game scores data for the kafka payload

    Args:
        game_data (list[dict]): data from balldontlie game scores api

    Returns:
        list[dict]: formatted game score event data for the kafka payload
    """
    fetched_at_utc = datetime.now(timezone.utc).isoformat()
    events = []

    for row in game_data:
        events.append(
            {
                "source": "balldontlie",
                "league": "NBA",
                "game_id": row["id"],
                "game_date": row["date"],
                "season": row["season"],
                "status": row["status"],
                "period": row["period"],
                "time": row["time"],
                "postseason": row["postseason"],
                "postponed": row["postponed"],
                "home_team_score": row["home_team_score"],
                "visitor_team_score": row["visitor_team_score"],
                "home_team_id": row["home_team"]["id"],
                "home_team_name": row["home_team"]["full_name"],
                "visitor_team_id": row["visitor_team"]["id"],
                "visitor_team_name": row["visitor_team"]["full_name"],
                "data_timestamp": row["datetime"],
                "fetched_at_utc": fetched_at_utc,
            }
        )

    return events


def build_team_records(team_data: list[dict]) -> list[dict]:
    """builds the balldontlie team data for the kafka payload

    Args:
        team_data (list[dict]): team info from the balldontlie api

    Returns:
        list[dict]: formatted team records for the kafka payload
    """
    fetched_at_utc = datetime.now(timezone.utc).isoformat()
    records = []

    for row in team_data:
        records.append(
            {
                "team_id": row["id"],
                "name": row["name"],
                "full_name": row["full_name"],
                "abbreviation": row["abbreviation"],
                "city": row["city"],
                "conference": row["conference"],
                "division": row["division"],
                "fetched_at_utc": fetched_at_utc,
            }
        )

    return records
