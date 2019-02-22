# -------------------------------------------------------------------------------------------------------------------- #
# Title: Unit Testig The Mailroom 4
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-02-21, Initial release
# -------------------------------------------------------------------------------------------------------------------- #
import pytest


from mailroom_4 import *


def test_get_last_donation():
    assert get_last_donation('Gustavo Cerati') == str(750)
    assert get_last_donation('Fito Paez') == str(550)
    assert get_last_donation('Adam Jones') == str(2000)


def test_send_thank_you():
    assert send_thank_you('Gustavo Cerati', '750') == 'Dear Gustavo Cerati,'\
                                                '\n\nThank you for your generous donation of $750.00!'\
                                                '\n\nSincerely,'\
                                                '\nThe Team at KEXP\n\n'

    assert send_thank_you('Draco Rosa', '1500') == 'Dear Draco Rosa,' \
                                                   '\n\nThank you for your generous donation of $1500.00!' \
                                                   '\n\nSincerely,' \
                                                   '\nThe Team at KEXP\n\n'



def test_generate_donations_report():
    lst_donations = ({'Name': 'Danny Carey', 'Date': '20192102', 'Donation': '1500'},
                     {'Name': 'Gustavo Cerati', 'Date': '20191802', 'Donation': '750'},
                     {'Name': 'Gustavo Cerati', 'Date': '20191802', 'Donation': '750'},
                     {'Name': 'Fito Paez', 'Date': '20191602', 'Donation': '550'},
                     {'Name': 'Fito Paez', 'Date': '20191002', 'Donation': '250'},
                     {'Name': 'Jeff Friedl', 'Date': '20191002', 'Donation': '71'},
                    )

    lst_unique_donors = ['Danny Carey', 'Fito Paez', 'Gustavo Cerati',
                         'Jeff Friedl']

    assert generate_donations_report(lst_donations, lst_unique_donors) == [{'Name': 'Danny Carey', 'Total': 1500.0, 'Count': 1, 'Average': 1500.0},
                                                                           {'Name': 'Fito Paez', 'Total': 800.0, 'Count': 2, 'Average': 400.0},
                                                                           {'Name': 'Gustavo Cerati', 'Total': 1500.0, 'Count': 2, 'Average': 750.0},
                                                                           {'Name': 'Jeff Friedl', 'Total': 71.0, 'Count': 1, 'Average': 71.0},
                                                                           ]



def test_unique_donors():
    lst_donations = ({'Name': 'Danny Carey', 'Date': '20192102', 'Donation': '1500'},
    {'Name': 'Gustavo Cerati', 'Date': '20191802', 'Donation': '750'},
    {'Name': 'Gustavo Cerati', 'Date': '20191802', 'Donation': '750'},
    {'Name': 'Fito Paez', 'Date': '20191602', 'Donation': '550'},
    {'Name': 'Fito Paez', 'Date': '20191002', 'Donation': '250'},
    {'Name': 'Jeff Friedl', 'Date': '20191002', 'Donation': '71'},
    {'Name': 'Miguel Bose', 'Date': '20191002', 'Donation': '1000'},
    {'Name': 'Willie Colon', 'Date': '20191002', 'Donation': '1500'})
    assert unique_donors(lst_donations) == ['Danny Carey', 'Fito Paez', 'Gustavo Cerati',
                                            'Jeff Friedl', 'Miguel Bose', 'Willie Colon']




# TODO: This function does not return anything, just prints.
@pytest.mark.skip(reason='This function does not return anything, just prints.')
def test_print_donors():
    pass


# TODO: This function does not return anything, just prints.
@pytest.mark.skip(reason='This function does not return anything, just prints.')
def test_print_all_donations():
    pass


# TODO: This function does not return anything, just prints.
@pytest.mark.skip(reason='This function does not return anything, just prints.')
def test_print_donations_report():
    pass


pytest.main(['-rp', 'mailroom_4.py'])
