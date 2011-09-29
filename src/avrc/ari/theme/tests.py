import unittest2 as unittest
import transaction

from plone.testing.z2 import Browser
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings

from avrc.ari.theme.testing import ARI_THEME_INTEGRATION_TESTING
from avrc.ari.theme.testing import ARI_THEME_FUNCTIONAL_TESTING


class TestSetup(unittest.TestCase):
    layer = ARI_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.theme_path = '++theme++avrc.ari.theme'

    def test_theme_configured(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IThemeSettings)
        self.assertEqual(settings.enabled, True)
        self.assertEqual(settings.rules,
                '/%s/rules.xml' % self.theme_path
            )
        self.assertEqual(settings.absolutePrefix,
                '/%s' % self.theme_path
            )

        self.assertTrue(settings.parameterExpressions.has_key('ajax_load'))

        self.assertEqual(settings.parameterExpressions['ajax_load'], 'python: \'ajax_load\' in request.form')

        self.assertTrue(settings.parameterExpressions.has_key('home_page'))

        self.assertEqual(settings.parameterExpressions['home_page'], 'python: context_state.is_portal_root()')

    def test_css_registry_configured(self):
        portal = self.layer['portal']
        cssRegistry = getToolByName(portal, 'portal_css')
        css_dir = 'theme-css'

        css_files = [
            'edit_screen.css',
            'style_features.css',
            'style_screen.css',
            ]
        for css_file in css_files:
            self.assertTrue('%s/%s/%s' % (self.theme_path, css_dir, css_file)
                        in cssRegistry.getResourceIds()
                    )


class TestRendering(unittest.TestCase):

    layer = ARI_THEME_FUNCTIONAL_TESTING

    def setUp(self):
        app = self.layer['app']
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Document', 'page', title=u'Page 1')
        setRoles(portal, TEST_USER_ID, ['Anonymous'])
        transaction.commit()

    def test_render_home_page(self):
        app = self.layer['app']
        portal = self.layer['portal']
        transaction.commit()
        browser = Browser(app)
        browser.open(portal.absolute_url())
        self.assertTrue('<!-- Theme home.html -->' in browser.contents)

    def test_render_sub_page(self):
        app = self.layer['app']
        portal = self.layer['portal']
        transaction.commit()

        browser = Browser(app)
        browser.open(portal.absolute_url() + '/page')
        self.assertTrue('<!-- Theme default.html -->' in browser.contents)

    def test_render_zmi_page(self):
        app = self.layer['app']
        portal = self.layer['portal']

        transaction.commit()

        browser = Browser(app)
        browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))

        browser.open(portal.absolute_url() + '/manage_main')

        self.assertFalse('<!-- Theme default.html -->' in browser.contents)
        self.assertFalse('<!-- Theme home.html -->' in browser.contents)
