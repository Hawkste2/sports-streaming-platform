from datetime import datetime

from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC_NBA_GAME_SCORES, KAFKA_TOPIC_NBA_TEAMS
from kafka import KafkaProducer
from kafka_producer import create_kafka_producer, publish_records
from nba import balldontlie_client, nba_transforms


def nba_driver(kafka_producer: KafkaProducer, dataset: str) -> None:
    """orchestrates ingestion for a specified NBA dataset.

    this function receives data from an api, transforms the data to match required schema,
    and publishes the results to a kafka broker

    Args:
        kafka_producer (KafkaProducer): a python kafka producer
        dataset (str): name of the nba dataset to process

    Raises:
        ValueError: If an unsupported dataset name is provided
    """
    client = balldontlie_client.create_balldontlie_client()

    if dataset == "nba_teams":
        teams_data = balldontlie_client.fetch_teams(client)
        team_records = nba_transforms.build_team_records(teams_data)
        publish_records(kafka_producer, KAFKA_TOPIC_NBA_TEAMS, team_records)
        # for testing, print
        # print(team_records[0])

    elif dataset == "nba_game_scores":
        game_data = balldontlie_client.fetch_games(client, datetime.today())
        game_score_events = nba_transforms.build_game_score_events(game_data)
        publish_records(kafka_producer, KAFKA_TOPIC_NBA_GAME_SCORES, game_score_events)
        # for testing, print
        # print(game_score_events[0])

    else:
        raise ValueError(f"Undefined NBA dataset: {dataset}.")


def main(dataset: str):
    """main function to direct argument dataset to the right function

    Args:
        dataset (str): name of the dataset to process

    Raises:
        ValueError: If an unsupported dataset league prefix is provided
    """
    kafka_producer = create_kafka_producer(KAFKA_BOOTSTRAP_SERVERS)

    if dataset.startswith("nba_"):
        nba_driver(kafka_producer, dataset)

    else:
        raise ValueError(f"Undefined league: {dataset}.")


if __name__ == "__main__":
    # main(sys.argv[1])
    main("nba_game_scores")
