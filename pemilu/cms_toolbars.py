from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from ppln.models import IconExtension
from ppln.page   import MetaPage

@toolbar_pool.register
class MetaPageToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = MetaPage

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Set Page Description'), url=url,
                    disabled=not self.toolbar.edit_mode_active, position=0)