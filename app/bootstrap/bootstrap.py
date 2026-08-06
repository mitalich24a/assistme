from app.bootstrap.dependency_checker import DependencyChecker
from app.bootstrap.mcp_server_starter import McpServerStarter
from app.bootstrap.package_manager import PackageManager


class Bootstrap:

    @staticmethod
    def initialize() -> None:

        PackageManager.ensure_requirements()

        DependencyChecker.check()

        McpServerStarter.start()