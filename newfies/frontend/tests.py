#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from common.test_utils import BaseAuthenticatedClient
from django.test import TestCase


class FrontendView(BaseAuthenticatedClient):
    """Test cases for Admin Interface."""

    def test_admin(self):
        """Test Function to check Admin index page"""
        response = self.client.get('/admin/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/base_site.html')
        response = self.client.login(username=self.user.username,
            password='admin')
        self.assertEqual(response, True)


class FrontendCustomerView(BaseAuthenticatedClient):
    """Test cases for Newfies-Dialer Customer Interface."""

    def test_index(self):
        """Test Function to check customer index page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')
        response = self.client.post('/login/',
                {'username': 'userapi',
                 'password': 'passapi'})
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        """Test Function to check customer dashboard"""
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/dashboard.html')


class FrontendForgotPassword(TestCase):
    """Test cases for Newfies-Dialer Customer Interface. for forgot password"""

    def test_check_password_reset(self):
        """Test Function to check password reset"""
        response = self.client.get('/password_reset/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'frontend/registration/password_reset_form.html')

        response = self.client.get('/password_reset/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'frontend/registration/password_reset_done.html')

        response = self.client.get('/reset/1-2xc-5791af4cc6b67e88ce8e/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'frontend/registration/password_reset_confirm.html')

        response = self.client.get('/reset/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'frontend/registration/password_reset_complete.html')
