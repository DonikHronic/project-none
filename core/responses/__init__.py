from core.responses.schema import ResponseModel

default_error_response = ResponseModel(
    **dict(
        success=False,
        result=None,
        error=dict(
            error_note="error details",
            error_code=0,
            error_data=dict(description="error data if exists"),
        ),
    )
)
