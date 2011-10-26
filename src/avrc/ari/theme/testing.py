from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig


class AriThemeSandBoxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import avrc.ari.theme
        xmlconfig.file('configure.zcml', avrc.ari.theme, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrc.ari.theme:default')


ARI_THEME_FIXTURE = AriThemeSandBoxLayer()

ARI_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ARI_THEME_FIXTURE,),
    name='AriTheme:Integration'
    )

ARI_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ARI_THEME_FIXTURE,),
    name='AriTheme:Functional'
    )
