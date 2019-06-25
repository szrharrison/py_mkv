from typing import Dict, List

from py_mkv.models.file_extension import AudioFileExtension, FileExtension, SubtitleFileExtension


class CodecId(str):
    _extension: FileExtension

    def __init__(self, codec_id: str):
        super().__init__()
        if codec_id not in codec_ids:
            raise ValueError(f"`{codec_id}` is not a valid codec id.")
        else:
            self._extension = file_extensions_by_codec_id[codec_id]

    @property
    def extension(self) -> FileExtension:
        return self._extension


file_extensions_by_codec_id: Dict[str, FileExtension] = {
    # All AAC files will be written into an AAC file with ADTS headers before each packet. The ADTS headers will not contain the deprecated emphasis field.
    "A_AAC/MPEG2/*": AudioFileExtension.AAC,
    "A_AAC/MPEG4/*": AudioFileExtension.AAC,
    "A_AAC": AudioFileExtension.AAC,
    # These will be extracted to raw AC-3 files.
    "A_AC3": AudioFileExtension.AC3,
    "A_EAC3": AudioFileExtension.AC3,
    # ALAC tracks are written to CAF files.
    "A_ALAC": AudioFileExtension.CAF,
    # These will be extracted to raw DTS files.
    "A_DTS": AudioFileExtension.DTS,
    # FLAC tracks are written to raw FLAC files.
    "A_FLAC": AudioFileExtension.FLAC,
    # MPEG-1 Audio Layer II streams will be extracted to raw MP2 files.
    "A_MPEG/L2": AudioFileExtension.MP2,
    # These will be extracted to raw MP3 files.
    "A_MPEG/L3": AudioFileExtension.MP3,
    # Opus(tm) tracks are written to OggOpus(tm) files.
    "A_OPUS": AudioFileExtension.OPUS,
    # Raw PCM data will be written to a WAV file. Big-endian integer data will be converted to little-endian data in the process.
    "A_PCM/INT/LIT": AudioFileExtension.WAV,
    "A_PCM/INT/BIG": AudioFileExtension.WAV,
    # RealAudio(tm) tracks are written to RealMedia(tm) files.
    "A_REAL/*": AudioFileExtension.REAL_MEDIA,
    # These will be extracted to raw TrueHD/MLP files.
    "A_TRUEHD": AudioFileExtension.TRUE_HD,
    "A_MLP": AudioFileExtension.MLP,
    # TrueAudio(tm) tracks are written to TTA files. Please note that due to Matroska(tm)'s limited timestamp precision the extracted file's header will be different regarding two fields: data_length (the total number of samples in the file) and the CRC.
    "A_TTA1": AudioFileExtension.TRUE_AUDIO,
    # Vorbis audio will be written into an OggVorbis(tm) file.
    "A_VORBIS": AudioFileExtension.VORBIS,
    # WavPack(tm) tracks are written to WV files.
    "A_WAVPACK4": AudioFileExtension.WAV_PACK,

    # PGS subtitles will be written as SUP files.
    "S_HDMV/PGS": SubtitleFileExtension.SUBTITLE_BITMAP,
    # TextST subtitles will be written as a special file format invented for mkvmerge(1) and mkvextract(1).
    "S_HDMV/TEXTST": SubtitleFileExtension,
    # Kate(tm) streams will be written within an Ogg(tm) container.
    "S_KATE": SubtitleFileExtension.KATE,
    # SSA and ASS text subtitles will be written as SSA/ASS files respectively.
    "S_TEXT/SSA": SubtitleFileExtension.SSA,
    "S_TEXT/ASS": SubtitleFileExtension.ASS,
    "S_SSA": SubtitleFileExtension.SSA,
    "S_ASS": SubtitleFileExtension.ASS,
    # Simple text subtitles will be written as SRT files.
    "S_TEXT/UTF8": SubtitleFileExtension.SRT,
    "S_TEXT/ASCII": SubtitleFileExtension.SRT,
    # VobSub(tm) subtitles will be written as SUB files along with the respective index files, as IDX files.
    "S_VOBSUB": SubtitleFileExtension.SUB,
    # USF text subtitles will be written as USF files.
    "S_TEXT/USF": SubtitleFileExtension.UNIVERSAL_SUBTITLE_FORMATTING,
    # WebVTT text subtitles will be written as WebVTT files.
    "S_TEXT/WEBVTT": SubtitleFileExtension.WEB_VTT,

    # # MPEG-1 and MPEG-2 video tracks will be written as MPEG elementary streams.
    # mpeg1 = "V_MPEG1"
    # vmpeg2 = "V_MPEG2"
    # # H.264 / AVC video tracks are written to H.264 elementary streams which can be processed further with e.g. MP4Box(tm) from the GPAC(tm) package.
    # avc = "V_MPEG4/ISO/AVC"
    # # H.265 / HEVC video tracks are written to H.265 elementary streams which can be processed further with e.g. MP4Box(tm) from the GPAC(tm) package.
    # hevc = "V_MPEG4/ISO/HEVC"
    # # Fixed FPS video tracks with this CodecID are written to AVI files.
    # fourcc = "V_MS/VFW/FOURCC"
    # # RealVideo(tm) tracks are written to RealMedia(tm) files.
    # realV = "V_REAL/*"
    # # Theora(tm) streams will be written within an Ogg(tm) container
    # theora = "V_THEORA"
    # # VP8 / VP9 tracks are written to IVF files.
    # vp8 = "V_VP8"
    # vp9 = "V_VP9"

    # # Tags are converted to a XML format. This format is the same that mkvmerge(1) supports for reading tags.
    # tags = "Tags"
    # # Attachments are written to they output file as they are. No conversion whatsoever is done.
    # attachments = "Attachments"
    # # Chapters are converted to a XML format. This format is the same that mkvmerge(1) supports for reading chapters. Alternatively a stripped-down version can be output in the simple OGM style format.
    # chapters = "Chapters"
    # # Timestamps are first sorted and then output as a timestamp v2 format compliant file ready to be fed to mkvmerge(1). The extraction to other formats (v1, v3 and v4) is not supported.
    # timestamps = "Timestamps"
}

codec_ids: List[str] = {key for key, val in file_extensions_by_codec_id.items()}
