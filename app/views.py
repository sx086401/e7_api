from .view.users import UserListCreateView, UserDetailView, UserUpdateView, UserDeleteView
from .view.characters import CharacterListCreateView, CharacterDetailView, CharacterUpdateView

user_list_create_view = UserListCreateView.as_view()

user_detail_view = UserDetailView.as_view()

user_update_view = UserUpdateView.as_view()

user_delete_view = UserDeleteView.as_view()

character_list_create_view = CharacterListCreateView.as_view()

character_detail_view = CharacterDetailView.as_view()

character_update_view = CharacterUpdateView.as_view()
