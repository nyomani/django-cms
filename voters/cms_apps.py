from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class VoterApphook(CMSApp):
    name = "Voter App"
    app_name="Voter"
    urls = ["voter.urls"]
apphook_pool.register(VoterApphook)
