from aiohttp import ClientSession as Session
from gcloud.aio.storage import Storage


class CloudStorage:
    storage: Storage = None

    def initialise(self, session: Session) -> None:
        self.storage = Storage(session=session)

    def __call__(self) -> Storage:
        assert self.storage is not None
        return self.storage
