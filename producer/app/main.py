from datetime import datetime

from nba import balldontlie_client, nba_transforms


def main(dataset: str):
    client = balldontlie_client.create_balldontlie_client()

    if dataset == "teams":
        teams_data = balldontlie_client.fetch_teams(client)
        team_records = nba_transforms.build_team_records(teams_data)
        print(team_records[0])

    elif dataset == "game_scores":
        game_data = balldontlie_client.fetch_games(client, datetime.today())
        game_score_events = nba_transforms.build_game_score_events(game_data)
        print(game_score_events[0])

    else:
        raise ValueError(f"Undefined dataset: {dataset}.")


if __name__ == "__main__":
    # main(sys.argv[1])
    main("game_scores")
