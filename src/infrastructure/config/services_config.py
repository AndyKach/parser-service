from application.services.lego_sets_service import LegoSetsService
from application.services.scheduler_service import SchedulerService
from infrastructure.config.interfaces_config import scheduler_interface
from infrastructure.config.providers_config import websites_interfaces_provider
from infrastructure.config.repositories_config import lego_sets_repository, lego_sets_prices_repository


def get_lego_sets_service():
    return LegoSetsService(
        lego_sets_repository=lego_sets_repository,
        lego_sets_prices_repository=lego_sets_prices_repository,
        websites_interfaces_provider=websites_interfaces_provider,
    )

def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=scheduler_interface,
        lego_sets_service=get_lego_sets_service()
    )
