import pprint
from chameleon import PageTemplateLoader
import datetime
from pathlib import Path
from typing import Any, Dict

import yaml

from flingern import defs
from flingern.images import ImageProcessor


class FlingernWebsiteData:
    def __init__(self, path: Path):
        self.path = path
        self.conf = self.path / "site.yaml"

        with self.conf.open("r") as f:
            self.site: Dict[str, Any] = yaml.safe_load(f)

        self.site["year"] = datetime.datetime.today().year

        # figuring paths
        self.pub_dir = (self.path / defs.DIR_PUBLIC).resolve()

        if not self.pub_dir.is_dir():
            self.pub_dir.mkdir()

        self.image_processor = ImageProcessor(
            content_root=self.path / defs.DIR_CONTENT, public_dir=self.pub_dir, config=self.site
        )

        # loading templates
        self.site_templates = PageTemplateLoader(str(Path(defs.flingern_directory) / defs.DIR_THEME))

        pprint.pprint(self.site)
