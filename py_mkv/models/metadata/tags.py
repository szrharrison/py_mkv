from typing import TypeVar

from lib.models.metadata.target_types import AudioTargetTypes, VideoTargetTypes, TargetTypesInt, TargetTypesStr

SimpleSubTags = TypeVar("SimpleSubTags", "TagName", "TagString", "TagDefault", "TagBinary")
TargetsSubTags = TypeVar("TargetsSubTags", "TargetType", "TargetTypeValue", "TagAttachmentUID", "TagChapterUID", "TagEditionUID", "TagTrackUID")
UIDTags = TypeVar("UIDTags", "TagChapterUID", "TagTrackUID", "TagEditionUID", "TagAttachmentUID")
Taggable = TypeVar("Taggable", "Tag", str)


class Tag:
    def __init__(self, *content: Taggable):
        content_strings = map(lambda tag: str(tag), content)
        self.value = "\n" + indent_content("\n".join(content_strings)) + "\n"

    def __str__(self):
        return "<" + self.__class__.__name__ + ">" + self.value + "</" + self.__class__.__name__ + ">"


class TagBinary(TagString):
    def __init__(self, content: bytearray):
        super().__init__(str(content))


class SimpleTag(Tag):
    def __init__(self, *content: SimpleSubTags):
        self.__class__.__name__ = "SimpleTag"
        super().__init__(*content)


class Targets(Tag):
    def __init__(self, *content: TargetsSubTags):
        super().__init__(*content)


class TargetType(TagString):
    def __init__(self, content: TargetTypesStr):
        super().__init__(content)
        if isinstance(content, (VideoTargetTypes, AudioTargetTypes)):
            self.value = content.name
        else:
            self.value = content


class TargetTypeValue(TagString):
    def __init__(self, content: TargetTypesInt):
        super().__init__(content)
        if isinstance(content, (VideoTargetTypes, AudioTargetTypes)):
            self.value = content.value
        else:
            self.value = content


class TagTrackUID(TagString):
    pass


class TagChapterUID(TagString):
    pass


class TagAttachmentUID(TagString):
    pass


class TagEditionUID(TagString):
    pass
