from flingern.page import Page
from flingern.websitedata import FlingernWebsiteData


class Section:
    def __init__(self, section_table, website: FlingernWebsiteData):
        self.data = section_table
        self.pages = []

        for page in self.data["pages"]:
            self.pages.append(Page(page, website))

    def build(self):
        for page in self.pages:
            page.build()


def create_sections(section_table, website: FlingernWebsiteData) -> list[Section]:
    sections = []

    for section in section_table:
        sections.append(Section(section, website))

    return sections
