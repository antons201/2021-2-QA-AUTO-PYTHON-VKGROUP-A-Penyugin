import os

from ui.pages.base_page import BasePage
from ui.locators.about_page_locators import AboutPageLocators


class AboutPage(BasePage):
    locators = AboutPageLocators()

    def get_version_from_file(self, file_path):
        dirname, filename = os.path.split(file_path)
        splitted_filename = filename.split('.')
        return splitted_filename[0][-1] + '.' + splitted_filename[1] + '.' + splitted_filename[2]

    def check_version(self, file_path, version_template):
        version = self.find(AboutPageLocators.VERSION_LOCATOR).text
        file_version = self.get_version_from_file(file_path)
        assert version == version_template.format(file_version)

    def check_copyright(self, expected_copyright):
        copyright_text = self.find(AboutPageLocators.COPYRIGHT_LOCATOR).text
        assert copyright_text == expected_copyright
