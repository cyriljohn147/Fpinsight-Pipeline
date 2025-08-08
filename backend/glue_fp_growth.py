from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set
from pyspark.ml.fpm import FPGrowth
import sys
from awsglue.utils import getResolvedOptions # type: ignore

args = getResolvedOptions(sys.argv, ['INPUT_S3','OUTPUT_S3','MIN_SUPPORT','MIN_CONF'])
spark = SparkSession.builder.appName("GlueFPGrowth").getOrCreate()

df = spark.read.option("header", True).csv(args['INPUT_S3'])
tx = df.groupBy("InvoiceNo").agg(collect_set("Description").alias("items"))

fp = FPGrowth(itemsCol="items", minSupport=float(args['MIN_SUPPORT']), minConfidence=float(args['MIN_CONF']))
model = fp.fit(tx)

model.associationRules.write.mode("overwrite").json(f"{args['OUTPUT_S3']}/rules")
spark.stop()
