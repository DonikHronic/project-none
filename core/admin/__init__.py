from starlette_admin.contrib.sqla import Admin, ModelView

from apps.core.models import Status, StatusType
from apps.user.models import User, Profile, ProfileType
from core.database import engine

admin = Admin(engine=engine, title="Example: SQLAlchemy")

admin.add_view(ModelView(StatusType))
admin.add_view(ModelView(Status))
admin.add_view(ModelView(User))
admin.add_view(ModelView(ProfileType))
admin.add_view(ModelView(Profile))
