import sentry_sdk
from src.infrastructure.cli.main_menu import MainMenu


def enable_sentry():
    """Enable Sentry SDK."""

    sentry_sdk.init(
        dsn="https://d3d8241a2b7e3da8de6337ae8c4b3297@o4507153289248768.ingest.de.sentry.io/4507153294950480",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
        debug=False,
        enable_tracing=True,
        environment="development",
    )


def main():
    enable_sentry()
    MainMenu().run()


if __name__ == "__main__":
    main()
