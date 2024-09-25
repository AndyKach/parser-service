from infrastructure.db.base import Base, sync_engine
from infrastructure.db.models.lego_sets_orm import LegoSetsOrm
from infrastructure.db.models.websites_orm import WebsitesOrm
from infrastructure.db.models.prices_orm import LegoSetsPricesOrm


if __name__ == '__main__':
    Base.metadata.create_all(sync_engine)