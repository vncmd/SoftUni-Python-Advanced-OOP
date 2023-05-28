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

# Different solution:

# from re import findall
#
#
# class NameTooShortError(Exception):
#     """ Name less than or equal to 4 characters"""
#     pass
#
#
# class MustContainAtSymbolError(Exception):
#     """ Email does not have @ """
#     pass
#
#
# class InvalidDomainError(Exception):
#     """ The domain is different than .com, .org... """
#     pass
#
#
# class MoreThanOneAtSymbolError(Exception):
#     """ Email must contain only one @ """
#
#
# class InvalidNameError(Exception):
#     """ Name can contain only letters, digits and underscores! """
#     pass
#
#
# MIN_LENGTH = 4
# VALID_DOMAINS = (".com", ".bg", ".net", ".org")
#
# patten_name = r'\w+'
# pattern_domain = r'\.[a-z]+'
#
# emails_data = input()
#
# while emails_data != "End":
#
#     if emails_data.count("@") > 1:
#         raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")
#
#     if len(emails_data.split("@")[0]) < MIN_LENGTH:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     if "@" not in emails_data:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     if findall(patten_name, emails_data)[0] != emails_data.split("@")[0]:
#         raise InvalidNameError("Name must be a real name!")
#
#     if findall(pattern_domain, emails_data)[-1] not in VALID_DOMAINS:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     print("Email is valid")
#
#     emails_data = input()
