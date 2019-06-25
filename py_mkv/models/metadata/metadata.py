from lib.models.metadata.tags import Tag, Tags
from lib.models.metadata.tags_factory import part_number, targets, title, total_parts
from lib.models.metadata.target_types import VideoTargetTypes


class Metadata:
    def __init__(self):
        self.content: str = ""
        self.__series = Tag()
        self.__season = Tag()
        self.__episode = Tag()
        self.__content_so_far = ""

    def series(self, series_name: str, season_count: int = None):
        if season_count is None:
            season_count = ""
        else:
            season_count = total_parts(season_count)
        self.__series = Tag(
            targets(VideoTargetTypes.COLLECTION),
            title(series_name),
            season_count
        )

    def season(self, season_number: int, episode_count: int = None):
        if episode_count is None:
            episode_count = "",
        else:
            episode_count = total_parts(episode_count)
        self.__season = Tag(
            targets(VideoTargetTypes.SEASON),
            part_number(season_number),
            episode_count
        )

    def episode(self, episode_number: int, episode_name: str = None, air_date: str = None):
        if episode_name is None:
            episode_name = ""
        else:
            episode_name = title(episode_name)

        self.__episode = Tag(
            targets(VideoTargetTypes.EPISODE),
            part_number(episode_number),
            episode_name
        )

    def build(self):
        self.content = Tags(
            self.__series,
            self.__season,
            self.__episode
        )
