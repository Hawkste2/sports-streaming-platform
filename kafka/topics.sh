#!/bin/bash

# creating the Kafka topic for raw NBA game scores. Not creating nba teams yet.
/opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --if-not-exists \
  --topic nba.game_scores.raw \
  --partitions 1 \
  --replication-factor 1 \
  --config retention.ms=259200000
