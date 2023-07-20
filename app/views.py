from .view.users import LoginView, UserListCreateView, UserDetailView, UserUpdateView, UserDeleteView
from .view.characters import CharacterListCreateView, CharacterDetailView, CharacterUpdateView
from .view.states import StateDeleteView, StateListCreateView, StateUpdateView

user_list_create_view = UserListCreateView.as_view()

user_detail_view = UserDetailView.as_view()

user_update_view = UserUpdateView.as_view()

user_delete_view = UserDeleteView.as_view()

login_view = LoginView.as_view()

character_list_create_view = CharacterListCreateView.as_view()

character_detail_view = CharacterDetailView.as_view()

character_update_view = CharacterUpdateView.as_view()

state_list_create_view = StateListCreateView.as_view()

state_update_view = StateUpdateView.as_view()

state_delete_vew = StateDeleteView.as_view()
