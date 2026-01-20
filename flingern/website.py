from flingern.websitedata import FlingernWebsiteData
import datetime
import shutil
from pathlib import Path
from typing import Any, Dict

import markdown
import yaml
from chameleon import PageTemplateLoader

from flingern import defs, sections
from flingern.images import ImageProcessor

from flingern.markdown.gallery import GalleryExtension


class FlingernWebsite:
    def __init__(self, path: Path, force: bool) -> None:
        self.data = FlingernWebsiteData(path)


        # if force:
        #     print("Force parameter passed, so deleting the whole site before\n")
        #     for item in self.pub_dir.iterdir():
        #         if item.is_file():
        #             item.unlink()
        #         elif item.is_dir():
        #             shutil.rmtree(item)


        self.sections = sections.create_sections(self.data.site["sections"], self.data)

        # # setup pages
        # for section in self.site["sections"]:
        #     for i, page in enumerate(section["pages"]):
        #         section["pages"][i] = self.setup_page(page)

    def build(self) -> None:
        for section in self.sections:
            section.build()

    # def build(self) -> None:
    #     print("Building site '%s'\n" % self.site["title"])
    #     # create theme structure
    #     theme_pub = self.pub_dir / "public"
    #     if theme_pub.is_dir():
    #         shutil.rmtree(theme_pub)
    #
    #     shutil.copytree(Path(defs.flingern_directory) / defs.DIR_THEME_PUBLIC, theme_pub)
    #
    #     # loading templates
    #     self.site_templates = PageTemplateLoader(str(Path(defs.flingern_directory) / defs.DIR_THEME))
    #     self.site_page_template = self.site_templates["page.html"]
    #
    #     # generate pages
    #     for section in self.site["sections"]:
    #         for page in section["pages"]:
    #             self.build_page(page)
    #
    #     print("")
    #
    # def setup_page(self, page_file: str) -> Dict[str, Any]:
    #     page_path = self.path / defs.DIR_CONTENT / page_file
    #     page_content = page_path.read_text()
    #
    #     content = page_content.split("---")
    #
    #     page: Dict[str, Any] = yaml.safe_load(content[1])
    #
    #     # if 'galleries' in page:
    #     #     page
    #     # print(page['galleries'])
    #
    #     page_name = page_path.stem
    #
    #     if not "menu" in page:
    #         page["menu"] = page["title"]
    #
    #     page_content_md = "---".join(content[2:])
    #
    #     content_path_root = (self.path / defs.DIR_CONTENT).resolve()
    #     content_path = page_path.parent.resolve().relative_to(content_path_root)
    #
    #     page["name"] = page_name
    #     page["content_path"] = str(content_path)
    #     page["url"] = str(content_path / (page["name"] + ".html"))
    #     page["content"] = markdown.markdown(page_content_md, extensions=["tables", GalleryExtension()])
    #
    #     return page
    #
    # def build_page(self, page: Dict[str, Any]) -> None:
    #     print(" -> page '%s'" % page["url"])
    #
    #     page_path = self.pub_dir / page["content_path"]
    #     if not page_path.is_dir():
    #         page_path.mkdir(parents=True, exist_ok=True)
    #
    #     # setup images
    #     self.image_processor.process_page_images(page)
    #
    #     result = self.site_page_template(site=self.site, page=page)
    #
    #     result_file_path = self.pub_dir / page["url"]
    #     if result_file_path.is_file():
    #         result_file_path.unlink()
    #
    #     # Write content
    #     result_file_path.write_text(result)
