from wtforms.validators import ValidationError


def checkUobEmail(message='User must have a UOB email address', valid_emails=["my.bristol.ac.uk", "bristol.ac.uk"]):
    """Checks whether the email input at sign up is a UOB email.

    Keyword arguements:
    message -- Validation error message (default "User must have a UOB email address").
    valid_emails -- List of valid UOB email extensions (default ['my.bristol.ac.uk', 'bristol.ac.uk']).
    """

    def _checkUobEmail(form, field):
        entered_email = field.data.split("@")[-1]
        if entered_email.lower() not in valid_emails:
            raise ValidationError(message)

    return _checkUobEmail
