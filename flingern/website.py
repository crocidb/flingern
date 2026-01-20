import pprint
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

        print(f"Processing website '{self.data.site['title']}'\n")

        self.sections = sections.create_sections(self.data.site["sections"], self.data)

    def build(self) -> None:
        # copy theme public assets
        theme_pub = self.data.pub_dir / "public"
        if theme_pub.is_dir():
            shutil.rmtree(theme_pub)
        shutil.copytree(Path(defs.flingern_directory) / defs.DIR_THEME_PUBLIC, theme_pub)

        for section in self.sections:
            section.build()

        print("")

