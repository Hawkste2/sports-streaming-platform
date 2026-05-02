CREATE TABLE IF NOT EXISTS raw.nba_game_score_events (
    event_id BIGSERIAL PRIMARY KEY,
    game_id BIGINT NOT NULL,
    game_date TIMESTAMPTZ,
    season INTEGER,
    status TEXT,
    period INTEGER,
    game_time TEXT,
    postseason BOOLEAN,
    postponed BOOLEAN,
    home_team_score INTEGER,
    visitor_team_score INTEGER,
    home_team_id BIGINT,
    home_team_name TEXT,
    visitor_team_id BIGINT,
    visitor_team_name TEXT,
    data_timestamp TIMESTAMPTZ,
    fetched_at_utc TIMESTAMPTZ NOT NULL,
    source TEXT NOT NULL,
    league TEXT NOT NULL,
    raw_payload JSONB,
    inserted_at_utc TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- TODO: Add the raw.nba_teams table to store the raw team data


CREATE TABLE IF NOT EXISTS nba_mart.nba_games (
    game_id BIGINT PRIMARY KEY,
    game_date TIMESTAMPTZ,
    season INTEGER,
    status TEXT,
    period INTEGER,
    game_time TEXT,
    postseason BOOLEAN,
    postponed BOOLEAN,
    home_team_score INTEGER,
    visitor_team_score INTEGER,
    home_team_id BIGINT,
    home_team_name TEXT,
    visitor_team_id BIGINT,
    visitor_team_name TEXT,
    data_timestamp TIMESTAMPTZ,
    latest_fetched_at_utc TIMESTAMPTZ NOT NULL,
    is_final BOOLEAN,
    winning_team_id BIGINT,
    point_differential INTEGER,
    updated_at_utc TIMESTAMPTZ NOT NULL DEFAULT NOW()
);