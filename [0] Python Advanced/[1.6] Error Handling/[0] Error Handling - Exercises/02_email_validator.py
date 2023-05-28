class NameTooShortError(Exception):
    """ Name less than or equal to 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """ Email does not have @ """
    pass


class InvalidDomainError(Exception):
    """ the domain is different than .com, .org... """
    pass


emails_data = input()
while emails_data != "End":
    valid_email = True

    if '@' in emails_data:
        if len(emails_data.split('@')[0]) <= 4:
            valid_email = False

            raise NameTooShortError("Name must be more than 4 characters")

    else:
        valid_email = False

        raise MustContainAtSymbolError("Email must contain @")

    if emails_data.split('.')[-1] not in ['com', 'bg', 'org', 'net']:
        valid_email = False

        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if valid_email:
        print("Email is valid")

    emails_data = input()
