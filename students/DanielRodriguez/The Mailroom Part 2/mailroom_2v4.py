# -------------------------------------------------------------------------------------------------------------------- #
# Title: The Mailroom Part 2
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-31, Rewriting using Dictionaries
# D. Rodriguez, 2019-02-09, Use dictionaries to switch between user selections
# D. Rodriguez, 2019-02-16, Fix switch menu logic and added docstrings to functions
# -------------------------------------------------------------------------------------------------------------------- #


def get_last_donation(donor_name):
    """
    Get last donation from donation csv file  for given input name
    :param donor_name: Donor Name
    :return: Last donation
    """
    lst_donations = read_donations_file()
    for donation in lst_donations:
        if donation['Name'] == donor_name:
            return donation['Donation']


def send_thank_you(str_name):
    """
    Generate thank you note
    :parameter  str_name: Thank you note recipient
    """
    str_last_donation = get_last_donation(str_name)
    str_note_text = 'Dear ' + str_name.title() + ',\n\nThank you for your generous donation of $' + \
                    '{:.2f}'.format(float(str_last_donation)) + '!\n\nSincerely,\nThe Team at KEXP\n\n'
    print('\n\n' + str_note_text)
    obj_thank = open(str_name + '.txt', 'w')
    obj_thank.write(str_note_text)
    obj_thank.close()
    main_menu()


def generate_donations_report():
    """
    Prints formatted Donations Report

    :return: None
    """
    lst_donations = read_donations_file()
    lst_unique_donors = unique_donors(lst_donations)

    donations_report = []

    for unique_name in lst_unique_donors:
        donation_total = 0
        donation_int_count = 0
        for donation in lst_donations:
            if donation.get('Name') == unique_name:
                donation_total += float(donation.get('Donation'))
                donation_int_count += 1
        donations_report.append({'Name': unique_name, 'Total': donation_total, 'Count': donation_int_count,
                                 'Average': donation_total / donation_int_count})

    print('=' * int_table_header_multiplier)
    print('{:20}'.format('Name'),
          '{:15}'.format('| Total Given'),
          '{:10}'.format('| Num. Gifts'),
          '{:15}'.format('| Average Gift'))
    print('=' * int_table_header_multiplier)

    for report_row in donations_report:
        print('{:20}'.format(report_row['Name']), '|',
              '${:>12,.2f}'.format(report_row['Total']), '|',
              '{:^10}'.format(report_row['Count']), '|',
              '${:>12,.2f}'.format(report_row['Average']))

    print('=' * int_table_header_multiplier)


def add_new_donation():
    """
    Adds new donation to donations list csv file
    :return: None
    """
    str_name = input('Enter donor full name: ')
    str_date = input('Enter donation date (mm/dd/yyy): ')
    str_date_formatted = str_date[-4:] + str_date[3:5] + str_date[:2]
    flt_donation = input('Enter donation amount ($): ')

    # Add new dictionary row to donations list
    lst_donations.append({'Name': str_name, 'Date': str_date_formatted, 'Donation': flt_donation})
    lst_donations.sort(key=lambda x: x['Date'], reverse=True)

    # Adding new donation to csv file
    obj_donations = open('Donations_List.csv', 'a')
    obj_donations.write(str_name + ',' + str_date_formatted + ',' + flt_donation + '\n')
    obj_donations.close()


def unique_donors(lst_donations):
    """
    Generate list of unique donor names
    :param lst_donations: All donations read from csv file
    :return: List of unique donor names
    """
    for donation in lst_donations:
        if donation.get('Name') not in lst_unique_donors:
            lst_unique_donors.append(donation.get('Name'))

    lst_unique_donors.sort()

    return lst_unique_donors


def read_donations_file():
    """
    Read csv data file with donations into a list of dictionaries and sort by donation date newest first
    :return: List of all donations read from csv file
    """
    obj_donations = open('Donations_List.csv', 'r')
    lst_donations = []

    for row in obj_donations:
        str_name, str_date, str_donation = row.replace('\n', '').split(',')
        lst_donations.append({'Name': str_name, 'Date': str_date, 'Donation': str_donation})

    obj_donations.close()
    lst_donations.sort(key=lambda x: x['Date'], reverse=True)

    return lst_donations


def list_donors():
    """
    Prints a list of unique donor names based on data read from donations file (CSV)
    :return: None
    """
    lst_donations = read_donations_file()
    lst_unique_donors = unique_donors(lst_donations)

    print('\nThese are all our current donors sorted alphabetically:\n')
    int_count = 0
    for name in lst_unique_donors:
        int_count += 1
        print(int_count, '. ', name, sep='')


def menu_selection(prompt, dict_dispatch):
    """
    Main Menu fucntion
    :param prompt: User prompt to be displayed
    :param dict_dispatch: Dictionary containing calls to navigation functions
    :return: None
    """
    while True:
        response = input(prompt)
        if dict_dispatch[response]() == 'exit menu':
            # print('Inside if...')
            # break
            exit()


def main_menu():
    """
    Main Menu function
    :return: None
    """
    print('\n' + '=' * int_table_header_multiplier)
    print('{:^60}'.format('MAIN MENU'))
    print('=' * int_table_header_multiplier)

    menu_selection(main_prompt, main_dispatch)


def donations_menu():
    """
    Donations Menu function
    :return: None
    """
    print('\n' + '=' * int_table_header_multiplier)
    print('{:^60}'.format('DONATIONS SUB-MENU'))
    print('=' * int_table_header_multiplier)
    menu_selection(donations_prompt, donations_dispatch)


def thank_you_menu():
    """
    Thank You menu functions
    :return: None
    """
    print('\n' + '=' * int_table_header_multiplier)
    print('{:^60}'.format('THANK YOU SUB-MENU'))
    print('=' * int_table_header_multiplier)

    str_name = 'list'
    while str_name == 'list':
        str_name = input('\nType donor\'s Full Name to SEND THANK YOU NOTE.'
                         '\nType "list" to display a list of all current donor.'
                         '\nType "q" to RETURN TO MAIN MENU.\n> ')

        if str_name == 'list':
            list_donors()
        elif str_name == 'q':
            main_menu()
        else:
            send_thank_you(str_name)


def exit_menu():
    """
    Exit function
    :return: Exit menu keyword
    """
    return 'exit menu'


main_prompt = ('\nWhat would you like to do?'
               '\nType "1" to go to DONATIONS SUB-MENU.'
               '\nType "2" to go to THANK YOU NOTE SUB-MENU.'
               '\nType "q" to QUIT.\n> ')

main_dispatch = {
                '1': donations_menu,
                '2': thank_you_menu,
                'q': exit_menu
                }

donations_prompt = ('\nWhat would you like to do?'
                    '\nType "1" to generate a DONATIONS REPORT.'
                    '\nType "2" to RECORD NEW DONATION.'
                    '\nType "q" to RETURN TO MAIN MENU.\n> ')

donations_dispatch = {
                    '1': generate_donations_report,
                    '2': add_new_donation,
                    'q': main_menu
                     }


# -- Data -- #
lst_donations = []
lst_unique_donors = []
int_table_header_multiplier = 66

# -- Presentation (Input/Output) -- #
if __name__ == '__main__':
    main_menu()
