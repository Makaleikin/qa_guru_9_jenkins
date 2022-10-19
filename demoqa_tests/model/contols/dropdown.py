from selene import have
from selene.support.shared import browser
from selene import have, command

def select(element, option):
    element.perform(command.js.click)
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.perform(command.js.click)
