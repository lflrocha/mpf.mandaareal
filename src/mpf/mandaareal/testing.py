# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mpf.mandaareal


class MpfMandaarealLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=mpf.mandaareal)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mpf.mandaareal:default')


MPF_MANDAAREAL_FIXTURE = MpfMandaarealLayer()


MPF_MANDAAREAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MPF_MANDAAREAL_FIXTURE,),
    name='MpfMandaarealLayer:IntegrationTesting',
)


MPF_MANDAAREAL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MPF_MANDAAREAL_FIXTURE,),
    name='MpfMandaarealLayer:FunctionalTesting',
)


MPF_MANDAAREAL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MPF_MANDAAREAL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MpfMandaarealLayer:AcceptanceTesting',
)
