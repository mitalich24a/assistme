import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import Any

logger = logging.getLogger(__name__)


class RetryExecutor:
    """
    Executes an async function with retry support.
    """

    def __init__(
        self,
        max_attempts: int = 3,
        delay_seconds: float = 1.0,
    ) -> None:

        self._max_attempts = max_attempts
        self._delay_seconds = delay_seconds

    async def execute(
        self,
        func: Callable[..., Awaitable[Any]],
        *args,
        **kwargs,
    ) -> Any:

        last_exception = None

        for attempt in range(1, self._max_attempts + 1):

            try:

                return await func(
                    *args,
                    **kwargs,
                )

            except Exception as ex:

                last_exception = ex

                logger.warning(
                    "Retry %s/%s failed: %s",
                    attempt,
                    self._max_attempts,
                    str(ex),
                )

                if attempt < self._max_attempts:

                    await asyncio.sleep(
                        self._delay_seconds,
                    )

        logger.error(
            "Operation failed after %s attempts.",
            self._max_attempts,
        )

        raise last_exception