import xml.etree.ElementTree as ElementTree
from typing import Union
from xml.etree.ElementTree import Element, SubElement

from py_mkv.lib import get_bool_from_any
from py_mkv.models.language import Language
from py_mkv.models.timestamp import Timestamp

FlagType = Union[bool, str, int]


class Chapter(Element):
    _name: str
    _start_time: Timestamp
    _end_time: Timestamp
    _language: Language
    _enabled: bool
    _hidden: bool
    _uid: int

    def __init__(self, name: str = "", start_time: Union[str, Timestamp] = None, end_time: Union[str, Timestamp] = None,
                 language: Language = Language.English, enabled: FlagType = True, hidden: FlagType = False, uid: int = None):
        super().__init__("ChapterAtom")
        self.name = name
        if start_time is None:
            start_time = Timestamp()
        elif isinstance(start_time, str):
            start_time = Timestamp.from_string(start_time)
        self.start_time = start_time
        if end_time is None:
            end_time = Timestamp()
        elif isinstance(end_time, str):
            end_time = Timestamp.from_string(end_time)
        self.end_time = end_time
        self.language = language
        self.enabled = enabled
        self.hidden = hidden
        self.uid = uid

    def __str__(self) -> str:
        return ElementTree.tostring(self, encoding="utf-8")

    @property
    def start_time(self) -> Timestamp:
        return self._start_time

    @start_time.setter
    def start_time(self, value: Timestamp):
        start_time = self._get_or_create_sub_element("ChapterTimeStart")
        start_time.text = str(value)
        self._start_time = value

    @property
    def end_time(self) -> Timestamp:
        return self._end_time

    @end_time.setter
    def end_time(self, value: Timestamp):
        end_time = self._get_or_create_sub_element("ChapterTimeEnd")
        end_time.text = str(value)
        self._end_time = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        display = self._get_or_create_sub_element("ChapterDisplay")
        name = display.find("./ChapterString")
        if name is None:
            name = SubElement(display, "ChapterString")
        name.text = value
        self._name = value

    @property
    def language(self) -> Language:
        return self._language

    @language.setter
    def language(self, value: Language):
        display = self._get_or_create_sub_element("ChapterDisplay")
        language = display.find("./ChapterLanguage")
        if language is None:
            language = SubElement(display, "ChapterLanguage")
        language.text = str(value)
        self._language = language

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: FlagType):
        value = get_bool_from_any(value)
        enabled = self._get_or_create_sub_element("ChapterFlagEnabled")
        enabled.text = str(int(value))
        self._enabled = value

    @property
    def hidden(self) -> bool:
        return self._hidden

    @hidden.setter
    def hidden(self, value: FlagType):
        value = get_bool_from_any(value)
        hidden = self._get_or_create_sub_element("ChapterFlagHidden")
        hidden.text = str(int(value))
        self._hidden = value

    @property
    def uid(self) -> int:
        return self._uid

    @uid.setter
    def uid(self, value: int):
        uid = self._get_or_create_sub_element("ChapterUID")
        uid.text = str(value)
        self._uid = value

    def _get_or_create_sub_element(self, tag_name: str) -> Element:
        element = self.find(f"./{tag_name}")
        if element is None:
            element = SubElement(self, tag_name)
        return element

    @staticmethod
    def from_string(chapter_string: str) -> 'Chapter':
        chapter_element: Element = ElementTree.fromstring(chapter_string)
        return Chapter.from_element(chapter_element)

    @staticmethod
    def from_element(chapter_element: Element) -> 'Chapter':
        start_time = Timestamp.from_string(chapter_element.findtext("./ChapterTimeStart"))
        end_time = Timestamp.from_string(chapter_element.findtext("./ChapterTimeEnd"))
        name = chapter_element.findtext("./ChapterDisplay/ChapterString")
        language = Language.value_of(chapter_element.findtext("./ChapterDisplay/ChapterLanguage"))
        return Chapter(name, start_time, end_time, language)

    def parse_info_line(self, line: str):
        property_name = line.split(":")[0].strip()
        value = ":".join(line.split(":")[1:]).strip()
        if property_name == "Chapter UID":
            self.uid = int(value)
        elif property_name == "Chapter flag hidden":
            self.hidden = value
        elif property_name == "Chapter flag enabled":
            self.enabled = value
        elif property_name == "Chapter time start":
            self.start_time = Timestamp.from_string(value)
        elif property_name == "Chapter time end":
            self.end_time = Timestamp.from_string(value)
        elif property_name == "Chapter string":
            self.name = value
        elif property_name == "Chapter language":
            self.language = Language.value_of(value)
