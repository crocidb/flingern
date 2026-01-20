import markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class GalleryPreprocessor(Preprocessor):
    # Match !![my-gallery-name]
    RE = re.compile(r'!!\[(?P<name>[^\]]+)\]')

    def run(self, lines):
        new_lines = []
        for line in lines:
            def repl(m):
                name = m.group('name')
                return f'<div id="gallery" data-gallery="{name}"></div>'

            new_line = self.RE.sub(repl, line)
            new_lines.append(new_line)
        return new_lines


class GalleryExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(GalleryPreprocessor(md), 'gallery', 25)

