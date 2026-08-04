class WorkflowMemory:
    """
    Shared in-memory storage for a workflow execution.

    All agents participating in the workflow can
    read/write values here.
    """

    def __init__(self):

        self._store: dict[str, object] = {}

    def set(
        self,
        key: str,
        value: object,
    ) -> None:

        self._store[key] = value

    def get(
        self,
        key: str,
        default=None,
    ):

        return self._store.get(
            key,
            default,
        )

    def has(
        self,
        key: str,
    ) -> bool:

        return key in self._store

    def delete(
        self,
        key: str,
    ) -> None:

        self._store.pop(
            key,
            None,
        )

    def clear(
        self,
    ) -> None:

        self._store.clear()

    def keys(
        self,
    ) -> list[str]:

        return list(
            self._store.keys()
        )

    def values(
        self,
    ) -> list[object]:

        return list(
            self._store.values()
        )

    def items(
        self,
    ):

        return self._store.items()

    def to_dict(
        self,
    ) -> dict:

        return dict(self._store)