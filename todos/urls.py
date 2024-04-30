from django.urls import path
from todos.views import TodoListCreateAPIView, TodoDetailAPIView

urlpatterns =[
    # path('create', TodoCreateAPIView.as_view(), name="create-todo"),
    # path('list', TodoListAPIView.as_view(), name='list-todo'),
    path('', TodoListCreateAPIView.as_view(), name='TodoListCreate' ),
    path("<int:id>", TodoDetailAPIView.as_view(), name='EditToDo'),
]