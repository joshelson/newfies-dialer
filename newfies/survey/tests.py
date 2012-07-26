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

from django.contrib.auth.models import User
from common.test_utils import BaseAuthenticatedClient
from survey.models import SurveyApp, SurveyQuestion,\
    SurveyResponse, SurveyCampaignResult
import nose.tools as nt


class SurveyAdminView(BaseAuthenticatedClient):
    """
    TODO: Add documentation
    """
    def test_surveyadmin_view(self):
        response = self.client.get('/admin/survey/surveyapp/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveyapp/add/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveyquestion/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveyquestion/add/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveyresponse/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveyresponse/add/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveycampaignresult/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/admin/survey/surveycampaignresult/add/')
        self.failUnlessEqual(response.status_code, 200)


class SurveyCustomerView(BaseAuthenticatedClient):
    """
    TODO: Add documentation
    """
    fixtures = ['survey', 'surve_question', 'survey_response']

    def test_survey_view(self):
        """Test Function survey view"""
        response = self.client.get('/survey/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'frontend/survey/survey_list.html')
        response = self.client.get('/survey/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'frontend/survey/survey_change.html')
        response = self.client.get('/survey/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'frontend/survey/survey_change.html')
        response = self.client.get('/survey_report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'frontend/survey/survey_report.html')


class SurveyModel(object):
    """
    TODO: Add documentation
    """
    def setup(self):
        self.user =\
            User.objects.get(username='admin')

        # SurveyApp model
        self.survey = SurveyApp(
            name='test_survey',
            user=self.user,
        )
        self.survey.save()

        # SurveyQuestion model
        self.survey_question = SurveyQuestion(
            question='test_question',
            user=self.user,
            surveyapp=self.survey,
        )
        self.survey_question.save()

        # SurveyResponse model
        self.survey_response = SurveyResponse(
            key='5',
            keyvalue='egg',
            surveyquestion=self.survey_question,
        )
        self.survey_response.save()

    def test_name(self):
        nt.assert_equal(self.survey.name, "test_survey")
        nt.assert_equal(self.survey_question.question, "test_question")
        nt.assert_equal(self.survey_response.key, "5")

    def teardown(self):
        self.survey.delete()
        self.survey_question.delete()
        self.survey_response.delete()
