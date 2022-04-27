



#
# def search_emai(my_emial, email):
#     if my_emial in email:
#         return True
#
#     else:
#         return False
#
#
# def main():
#     users_email = ['aaaa@.pl','bbbb@.pl','ccc@c.pl']
#     wanted_email = ['bbbb@.pl']
#
#     result = search_emai(wanted_email,users_email)
#     print('email on list',result)
#
#
# if __name__ == '__main__':
#     main()


def search(my_email, email_list):
    for email in email_list:
        if email == my_email:
            return True

    return False


def main():
    users_emails = ['aaa@a.pl', 'bbb@b.pl', 'ccc@c.pl']
    wanted_email = 'ddd@b.pl'

    result = search(wanted_email, users_emails)
    print('Email on list: ', result)


if __name__ == '__main__':
    main()