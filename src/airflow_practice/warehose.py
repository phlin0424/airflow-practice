from datetime import datetime, timezone
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import lit
import sys


def parse_line(line):
    """Parse each line in the raw data.

    Args:
        line (_type_): _description_

    Returns:
        _type_: _description_
    """
    f = line.split()
    wbanno = f[0]
    dt = datetime.strptime(f[1] + f[2], "%Y%m%d%H%M")
    dt = dt.replace(tzinfo=timezone.utc)
    temperature = None if f[8] == "-9999.0" else float(f[8])
    return Row(timestamp=dt, wbanno=wbanno, temperature=temperature)


if __name__ == "__main__":
    date = sys.argv[1]

    spark = (
        SparkSession.builder.config("hive.metastore.uris", "thrift://metastore:9083").enableHiveSupport().getOrCreate()
    )

    rdd = spark.sparkContext.textFile(f"s3a://datalake/uscrn/{date}/*")
    df = rdd.map(parse_line).toDF()
    df = df.withColumn("year", lit(date[:4]))
    df.write.partitionBy("year").saveAsTable("uscrn", mode="overwrite")

    spark.sql("show tables").show()
