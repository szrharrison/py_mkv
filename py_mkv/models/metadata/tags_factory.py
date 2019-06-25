from lib.models.metadata.tags import SimpleTag, TagName, TagString, Targets, TargetType, TargetTypeValue, UIDTags
from lib.models.metadata.target_types import TargetTypes
from lib.models.metadata.tag_types import TagTypes


def total_parts(number_of_parts: int) -> SimpleTag:
    return SimpleTag(
        TagName(TagTypes.TOTAL_PARTS),
        TagString(str(number_of_parts))
    )


def targets(target_type: TargetTypes, uid: UIDTags = None) -> Targets:
    if uid is None:
        return Targets(
            TargetType(target_type),
            TargetTypeValue(target_type)
        )
    else:
        return Targets(
            TargetType(target_type),
            TargetTypeValue(target_type),
            uid
        )


def title(name: str) -> SimpleTag:
    return SimpleTag(
        TagName(TagTypes.TITLE),
        TagString(name)
    )


def part_number(number: int) -> SimpleTag:
    return SimpleTag(
        TagName(TagTypes.PART_NUMBER),
        TagString(str(number))
    )
