from snowflake import SnowflakeGenerator, Snowflake

gen = SnowflakeGenerator(42)
snowflakeId = next(gen)
print(snowflakeId)

sf = Snowflake.parse(snowflakeId)

print(f"{sf.timestamp = }")
print(f"{sf.instance = }")
print(f"{sf.epoch = }")
print(f"{sf.seq = }")
print(f"{sf.seconds = }")
print(f"{sf.milliseconds = }")
print(f"{sf.datetime = }")