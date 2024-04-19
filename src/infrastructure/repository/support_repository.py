from src.domain.interfaces.support_repository_interface import SupportRepositoryInterface
from src.domain.entities.collaborator import Support as SupportEntity


class SupportRepository(SupportRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def create_support(self, support: SupportEntity) -> None:
        support_entity = SupportEntity(
            first_name=support.first_name,
            last_name=support.last_name,
            email=support.email,
            password=support.password,
            role='support',
        )

        self.session.add(support_entity)
        self.session.commit()

    def get_support(self, support_id: int) -> SupportEntity:
        support = self.session.query(SupportEntity).get(support_id)

        if support is None:
            raise Exception("Support not found")

        return support

    def get_supports(self) -> list[SupportEntity]:
        supports = self.session.query(SupportEntity).all()

        if supports is None:
            raise Exception("Supports not found")

        return supports

    def update_support(self, support) -> None:
        support_entity = self.get_support(support.id)

        support_entity.first_name = support.first_name
        support_entity.last_name = support.last_name
        support_entity.email = support.email
        support_entity.password = support.password

        self.session.commit()

    def delete_support(self, support_id: int) -> None:
        support = self.get_support(support_id)

        self.session.delete(support)
        self.session.commit()
