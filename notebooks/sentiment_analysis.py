hospital_df.printSchema()
hospital_df.show(5, truncate=False)

from pyspark.sql.functions import col, when

hospital_sent_df = (
    hospital_df
    .withColumn(
        "sentiment_label",
        when(col("Ratings").cast("int") <= 2, "negative")
        .when(col("Ratings").cast("int") == 3, "neutral")
        .otherwise("positive")
    )
)

display(hospital_sent_df.groupBy("sentiment_label").count())

from pyspark.sql.functions import lower, regexp_replace, col

hospital_clean_df = (
    hospital_sent_df
    # convert to lowercase
    .withColumn("clean_text", lower(col("Feedback")))
    # remove punctuation and symbols
    .withColumn("clean_text", regexp_replace(col("clean_text"), "[^a-zA-Z0-9 ]", " "))
    # remove extra spaces
    .withColumn("clean_text", regexp_replace(col("clean_text"), " +", " "))
)

display(hospital_clean_df.select("Feedback", "clean_text", "sentiment_label"))


