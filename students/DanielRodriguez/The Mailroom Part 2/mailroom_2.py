# -------------------------------------------------------------------------------------------------------------------- #
# Title: THe Mailroom Part 2
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-31, Rewriting using Dictionaries
# D. Rodriguez, 2019-02-05, Use dictionaries to switch between user selections
# -------------------------------------------------------------------------------------------------------------------- #
# TODO: Rename variables to make them more descriptive


# -- Processing -- #
# Get las donation for given input name
def get_last_donation(donor_name):
    for donation in lst_donations:
        if donation['Name'] == donor_name:
            return donation['Donation']


# Send Thank You note
def send_thank_you(donor_name, str_last_donation):
    str_note_text = 'Dear ' + donor_name.title() + ',\n\nThank you for your generous donation of $' + \
                    '{:.2f}'.format(float(str_last_donation))+'!\n\nSincerely,\nThe Team at KEXP\n\n'
    print('\n\n' + str_note_text)
    obj_thank = open(donor_name + '.txt', 'w')
    obj_thank.write(str_note_text)
    obj_thank.close()
    
    
# Generate Donations Report
def generate_donations_report():
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
        # print(type(row))
        print('{:20}'.format(report_row['Name']), '|',
              '${:>12,.2f}'.format(report_row['Total']), '|',
              '{:^10}'.format(report_row['Count']), '|',
              '${:>12,.2f}'.format(report_row['Average']))

    print('=' * int_table_header_multiplier)


# Add new donation1
def add_new_donation(donor_name):
    print('\nAdd donation from', donor_name.title(), 'to Donations List.')
    str_new_name = donor_name.title()
    str_date = input('Enter donation date (mm/dd/yyy): ')
    str_date_formatted = str_date[-4:] + str_date[3:5] + str_date[:2]
    flt_donation = input('Enter donation amount ($): ')
    
    # Add new dictionary row to donations list
    lst_donations.append({'Name': str_new_name, 'Date': str_date_formatted, 'Donation': flt_donation})
    lst_donations.sort(key=lambda x: x['Date'], reverse=True)

    # Adding new donation to csv file
    obj_donations = open('Donations_List.csv', 'a')
    obj_donations.write(str_new_name + ',' + str_date_formatted + ',' + flt_donation + '\n')
    obj_donations.close()
    str_new_donation_response = input('\nThank ' + donor_name + ' for his donation of $'
                                      + flt_donation + '?'
                                      '\nType "1" for THANK YOU NOTE.'
                                      '\nType "2" to exit to the MAIN MENU.\n> ')
    if str_new_donation_response == '1':
        send_thank_you(donor_name, flt_donation)


# Generate list of unique donor names1
def unique_donors():
    for donation in lst_donations:
        if donation.get('Name') not in lst_unique_donors:
            lst_unique_donors.append(donation.get('Name'))
    lst_unique_donors.sort()


def open_donations_file():
    # Read csv data file with donations into a list of dictionaries and sort by donation date newest first
    obj_donations = open('Donations_List.csv', 'r')
    for row in obj_donations:
        str_name, str_date, str_donation = row.replace('\n', '').split(',')
        lst_donations.append({'Name': str_name, 'Date': str_date, 'Donation': str_donation})
    obj_donations.close()
    lst_donations.sort(key=lambda x: x['Date'], reverse=True)


# -- Data -- #
lst_donations = []
lst_unique_donors = []
int_table_header_multiplier = 66


# -- Presentation (Input/Output) -- #
if __name__ == '__main__':
    open_donations_file()
    unique_donors()
    
    # Main Menu
    str_main_menu_response = ''
    while str_main_menu_response != 'q':
        print('\n' + '=' * int_table_header_multiplier)
        print('{:^60}'.format('MAIN MENU'))
        print('=' * int_table_header_multiplier)
        str_main_menu_response = input('\nWhat would you like to do?'
                                       '\nType "1" to RECORD NEW DONATION.'
                                       '\nType "2" to generate a DONATIONS REPORT.'
                                       '\nType "q" to QUIT.\n> ')
        
        if str_main_menu_response == '1':
            # New Donation Menu
            str_new_donation_menu_response = 'list'
            while str_new_donation_menu_response == 'list':
                print('\n' + '=' * int_table_header_multiplier)
                print('{:^60}'.format('DONATIONS MENU'))
                print('=' * int_table_header_multiplier)
                str_new_donation_menu_response = input('Type donor\'s Full Name to RECORD NEW DONATION.'
                                                       '\nType "list" to display a list of all current donor.\n> ')
                
                if str_new_donation_menu_response == 'list':
                    print('\nThese are all our current donors sorted alphabetically:\n')
                    int_count = 0
                    for name in lst_unique_donors:
                        int_count += 1
                        print(int_count, '. ', name, sep='')
            
            # Send Thank You note
            else:
                # Check if donor exists in Donations List
                if str_new_donation_menu_response in lst_unique_donors:
                    str_last_donation = get_last_donation(str_new_donation_menu_response)
                    str_send_note_response = input('\n' + str_new_donation_menu_response + ' is already a donor.\nDo '
                                                   'you want to send a THANK YOU NOTE for his latest donation\nof '
                                                   '$' + str_last_donation + ' or RECORD NEW DONATION?'
                                                   '\nType "1" for THANK YOU NOTE.'
                                                   '\nType "2" to RECORD NEW DONATION:\n> ')
                    
                    # Send Thank You note to existing donor
                    if str_send_note_response == '1':
                        send_thank_you(str_new_donation_menu_response, str_last_donation)
                    
                    # Add new donation from existing donor
                    elif str_send_note_response == '2':
                        add_new_donation(str_new_donation_menu_response)
                        
                # Add new donation from new donor
                else:
                    add_new_donation(str_new_donation_menu_response)
                    unique_donors()

        elif str_main_menu_response == '2':
            generate_donations_report()
        
        # Secret Option to print all donations
        elif str_main_menu_response == 'all':
            print('All donations sorted from newest to oldest\n')
            for donation in lst_donations:
                print(donation)
        
        else:
            print('Please, enter a valid option.')
