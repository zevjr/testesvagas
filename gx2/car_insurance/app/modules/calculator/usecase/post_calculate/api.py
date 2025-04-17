from app.common.usecase import usecase_dependency
from starlette import status
from .impl import PostCalculateUseCase
from fastapi import Depends, APIRouter
from app.modules.calculator.presentation import PremiumRequest, PremiumResponse


router = APIRouter(prefix='/calculate')

@router.post(path='/', name="Calculate", status_code=status.HTTP_201_CREATED, response_model=PremiumResponse)
async def calculate_premium(uc: PostCalculateUseCase = Depends(usecase_dependency(PremiumRequest, PostCalculateUseCase))):
    
    return await uc.invoke()
    