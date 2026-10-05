import argparse
from dotenv import load_dotenv
from settings import Settings
import os
import yaml


def export_envs(environment: str = "dev") -> None:
    env_file = f".env.{environment}"
    load_dotenv("config/" + env_file)

    secrets_file = "secrets.yaml"
    if os.path.exists(secrets_file):
        with open(secrets_file, "r") as secrets:
            secrets_data = yaml.safe_load(secrets)

            for key, value in secrets_data.items():
                os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("FAKE_API_KEY: ", settings.FAKE_API_KEY)
