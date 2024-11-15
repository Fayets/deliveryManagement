from fastapi import HTTPException, APIRouter, status
from src import schemas
from src.services.pedido_services import PedidoServices
from src.schemas import RegisterMessage
from fastapi.responses import JSONResponse

# Pedido Controller
router = APIRouter()

service = PedidoServices()

@router.post("/register", response_model=RegisterMessage, status_code=201)
def register_pedido(pedido: schemas.PedidoCreate):
    try:
        # Llamamos al servicio para crear el pedido
        pedido_created = service.create_pedido(pedido)   
        # Aquí se puede incluir más información si es necesario
        return JSONResponse(
            content={
                "message": "Pedido creado correctamente",
                "success": True,
            },
            status_code=status.HTTP_201_CREATED
        )
    except HTTPException as e:
        # Maneja el error y devuelve un mensaje personalizado
        return JSONResponse(
            content={
                "message": e.detail,
                "success": False,
            },
            status_code=e.status_code
        )
    except Exception as e:
        # Captura cualquier error inesperado
        return JSONResponse(
            content={
                "message": "Error inesperado al crear el pedido.",
                "success": False,
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
