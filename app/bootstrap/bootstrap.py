from app.bootstrap.dependency_checker import DependencyChecker


class Bootstrap:

    @staticmethod
    def initialize() -> None:

        DependencyChecker.check()