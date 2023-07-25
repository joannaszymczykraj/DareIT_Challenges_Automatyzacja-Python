import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.log_in_to_the_system import TestLoginPage
from test_cases.tc1_sign_out import TestSignOut
from test_cases.tc2_lack_of_login_or_password import TestLoginPage2
from test_cases.tc3_dev_team_contact import TestDevTeamContact
from test_cases.tc4_add_new_player import TestAddPlayer2
from test_cases.tc5_remind_password import TestRemindPassword
from test_cases.tc_add_a_player import TestAddPlayer


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestSignOut))
    test_suite.addTest(makeSuite(TestLoginPage2))
    test_suite.addTest(makeSuite(TestDevTeamContact))
    test_suite.addTest(makeSuite(TestAddPlayer2))
    test_suite.addTest(makeSuite(TestRemindPassword))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
