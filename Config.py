import os

ENVIRONMENT = True

if ENVIRONMENT:
    try:
        API_ID = 8763712
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = "835d27216f117e22a5c192b89a4ce457"
    BOT_TOKEN = "5095390657:AAH3zgBuZDjuDBaF_0IvJcv8x9UJ3KVUpiQ"
    DATABASE_URL = os.environ.get('DATABASE_URL', None) # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    CLASSES_CHAT=-1001631582129
    BOT_USERNAME = "SahilNoliaBot"
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
