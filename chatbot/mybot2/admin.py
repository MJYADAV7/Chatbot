from django.contrib import admin
from .models import User
from .models import Questions
from .models import Sub_questions
from .models import Responses
from .models import Conversation
# Register your models here.
admin.site.register(User)

admin.site.register(Questions)
admin.site.register(Sub_questions)

admin.site.register(Responses)
admin.site.register(Conversation)
