from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    """creates a spark session

    Returns:
        SparkSession: A PySpark spark session
    """
    # naming the session after the repo. Only running locally since its not a large prod project
    return (
        SparkSession.builder.appName("sports-streaming-pipeline")
        .master("local[*]")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.1",
        )
        .getOrCreate()
    )


def main() -> None:
    """main function to handle spark - mostly serves to call dataset / topic specific functions"""
    spark = create_spark_session()

    print(f"Spark started successfully. Spark version: {spark.version}")

    # testing spark to read from the kafka docker
    kafka_df = (
        spark.read.format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "nba.game_scores.raw")
        .option("startingOffsets", "earliest")
        .load()
    )

    # actually not sure the exact meaning of this. a tutorial used it to test output. new to me.
    kafka_df.selectExpr("CAST(value AS STRING) as message").show(truncate=False)

    # stop spark when done processing data
    spark.stop()


if __name__ == "__main__":
    main()
