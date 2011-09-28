from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class LeadthewayTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import avrc.theme.leadtheway
        xmlconfig.file('configure.zcml', avrc.theme.leadtheway, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrc.theme.leadtheway:default')

LEADTHEWAY_THEME_FIXTURE = LeadthewayTheme()

LEADTHEWAY_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(LEADTHEWAY_THEME_FIXTURE,), name="LeadthewayTheme:Integration")

LEADTHEWAY_THEME_FUNCTIONAL_TESTING = FunctionalTesting(bases=(LEADTHEWAY_THEME_FIXTURE,), name="LeadthewayTheme:Functional")
