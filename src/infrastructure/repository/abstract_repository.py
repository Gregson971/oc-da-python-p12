from typing import Any, List, Type
from kink import inject
from sqlalchemy.orm import Session


class AbstractRepository:
    @inject
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity: Any) -> None:
        self.session.add(entity)
        self.session.commit()

    def get(self, entity: Type[Any], id: int) -> Any:
        return self.session.query(entity).get(id)

    def get_all(self, entity: Type[Any]) -> List[Any]:
        return self.session.query(entity).all()

    def update(self) -> None:
        self.session.commit()

    def delete(self, entity: Any) -> None:
        self.session.delete(entity)
        self.session.commit()
