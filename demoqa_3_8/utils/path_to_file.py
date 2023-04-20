from selene.support.shared import browser
import os
from tests import attachments


def create_path(selector, path):
    browser.element(selector).set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(attachments.__file__), path)
        )
    )

