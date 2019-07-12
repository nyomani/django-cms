from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

class AdminMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        user = request.user
        if user.is_authenticated:
            nodes.append(NavigationNode(_(user.first_name), "#", 1))
            nodes.append(NavigationNode(_('PROFILE'), "/profile", 2, 1))
            nodes.append(NavigationNode(_('SIGN OUT'), "/logout", 3, 1))
            nodes.append(NavigationNode(_('CHANGE PASSWORD'), "/password-reset", 3, 1))
            if user.is_staff:
                nodes.append(NavigationNode(_('CREATE Page'), "/create?page=1&language=en&edit", 4))
        else:
            nodes.append(NavigationNode(_('SIGN IN'), "/login", 4))
            nodes.append(NavigationNode(_('REGISTER'), "/register", 5))
        return nodes

menu_pool.register_menu(AdminMenu)