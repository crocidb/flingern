import copy
from pprint import pprint
import markdown
from typing import Any, Dict

import yaml

from flingern import defs
from flingern.markdown.gallery import GalleryExtension
from flingern.websitedata import FlingernWebsiteData


class Page:
    def __init__(self, page_file, website: FlingernWebsiteData):
        self.website = website

        self.page = self.__loadfile(page_file)
        page_path = self.website.path / defs.DIR_CONTENT / page_file

        if not "menu" in self.page:
            self.page["menu"] = self.page["title"]

        self.name = page_path.stem
        self.content_path_root = (self.website.path / defs.DIR_CONTENT).resolve()
        self.content_path = page_path.parent.resolve().relative_to(self.content_path_root)

        self.complete_url = str(self.content_path / (self.name + ".html"))
        self.url = self.content_path if self.name == "index" else self.complete_url

        self.content = markdown.markdown(self.page["markdown"], extensions=["tables", GalleryExtension()])

    def __loadfile(self, filepath) -> dict[str, Any]:
        page_path = self.website.path / defs.DIR_CONTENT / filepath

        page_content = page_path.read_text()
        content = page_content.split("---")
        page_content_md = "---".join(content[2:])

        page: Dict[str, Any] = yaml.safe_load(content[1])

        page["markdown"] = page_content_md

        return page

    def build(self):
        print(" -> page '%s'" % self.complete_url)

        page_path = self.website.pub_dir / self.content_path
        if not page_path.is_dir():
            page_path.mkdir(parents=True, exist_ok=True)

        page_data = self.get_data()

        # process gallery images
        self.website.image_processor.process_galleries(page_data)

        self.site_page_template = self.website.site_templates["page.html"]
        result = self.site_page_template(site=self.website.site, page=page_data)

        result_file_path = self.website.pub_dir / self.complete_url
        if result_file_path.is_file():
            result_file_path.unlink()

        result_file_path.write_text(result)

    def get_data(self) -> dict[str, Any]:
        data = copy.deepcopy(self.page)
        data["url"] = str(self.complete_url)
        data["content"] = self.content
        data["content_path"] = str(self.content_path)
        return data

