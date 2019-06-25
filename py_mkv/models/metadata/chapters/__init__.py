from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from typing import List

from lib.models.metadata.chapters.chapter import Chapter


class Chapters:
    chapters: List[Chapter]

    def __init__(self, *chapters: Chapter):
        self.chapters = [*chapters]

    def to_element(self) -> Element:
        root_element = Element("Chapters")
        edition_entry: Element = SubElement(root_element, "EditionEntry")
        for chapter in self.chapters:
            edition_entry.append(chapter.to_element())
        return root_element

    @staticmethod
    def from_string(chapters_str: str) -> 'Chapters':
        chapters_element: Element = ElementTree.fromstring(chapters_str)
        chapter_elements = chapters_element.findall(".//ChapterAtom")
        chapters = [Chapter.from_element(chapter_element) for chapter_element in chapter_elements]
        return Chapters(*chapters)
