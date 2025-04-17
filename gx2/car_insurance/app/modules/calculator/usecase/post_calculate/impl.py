from app.common.usecase import BaseUseCase
from app.config.logger import Logger
from app.modules.calculator.presentation import PremiumRequest, PremiumResponse
from .service import PremiumService

class PostCalculateUseCase(BaseUseCase):
    def __init__(self, request: PremiumRequest, service: PremiumService = None, logger: Logger = None) -> None:
        self.request = request
        self.service = service or PremiumService(self.request)
        self.logger = logger or Logger(PremiumService.__name__)

    async def invoke(self) -> PremiumResponse:
        try:
            return self.service.calculate()
        except Exception as e:
            message = f"Error to process calculate, error={e}"
            self.logger.error(message)
            return 500, e, message