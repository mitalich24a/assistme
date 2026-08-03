from app.bootstrap.package_manager import PackageManager
from app.bootstrap.dependency_checker import DependencyChecker


class Bootstrap:

    @staticmethod
    def initialize() -> None:

        PackageManager.ensure_requirements()

        DependencyChecker.check()