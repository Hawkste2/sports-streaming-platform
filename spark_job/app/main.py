from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    """creates a spark session

    Returns:
        SparkSession: A PySpark spark session
    """
    # naming the session after the repo. Only running locally since its not a large prod project
    return SparkSession.builder.appName("sports-streaming-pipeline").master("local[*]").getOrCreate()


def main() -> None:
    """main function to handle spark - mostly serves to call dataset / topic specific functions"""
    spark = create_spark_session()

    print(f"Spark started successfully. Spark version: {spark.version}")

    # stop spark when done processing data
    spark.stop()


if __name__ == "__main__":
    main()
