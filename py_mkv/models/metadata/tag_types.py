    # Entities
    ARTIST = "ARTIST"
    LEAD_PERFORMER = "LEAD_PERFORMER"
    ACCOMPANIMENT = "ACCOMPANIMENT"
    COMPOSER = "COMPOSER"
    ARRANGER = "ARRANGER"
    LYRICS = "LYRICS"
    LYRICIST = "LYRICIST"
    CONDUCTOR = "CONDUCTOR"
    DIRECTOR = "DIRECTOR"
    ASSISTANT_DIRECTOR = "ASSISTANT_DIRECTOR"
    DIRECTOR_OF_PHOTOGRAPHY = "DIRECTOR_OF_PHOTOGRAPHY"
    SOUND_ENGINEER = "SOUND_ENGINEER"
    ART_DIRECTOR = "ART_DIRECTOR"
    PRODUCTION_DESIGNER = "PRODUCTION_DESIGNER"
    CHOREGRAPHER = "CHOREGRAPHER"
    COSTUME_DESIGNER = "COSTUME_DESIGNER"
    ACTOR = "ACTOR"
    CHARACTER = "CHARACTER"
    WRITTEN_BY = "WRITTEN_BY"
    SCREENPLAY_BY = "SCREENPLAY_BY"
    EDITED_BY = "EDITED_BY"
    PRODUCER = "PRODUCER"
    COPRODUCER = "COPRODUCER"
    EXECUTIVE_PRODUCER = "EXECUTIVE_PRODUCER"
    DISTRIBUTED_BY = "DISTRIBUTED_BY"
    MASTERED_BY = "MASTERED_BY"
    ENCODED_BY = "ENCODED_BY"
    MIXED_BY = "MIXED_BY"
    REMIXED_BY = "REMIXED_BY"
    PRODUCTION_STUDIO = "PRODUCTION_STUDIO"
    THANKS_TO = "THANKS_TO"
    PUBLISHER = "PUBLISHER"
    LABEL = "LABEL"
    # Search / Classification
    GENRE = "GENRE"
    MOOD = "MOOD"
    ORIGINAL_MEDIA_TYPE = "ORIGINAL_MEDIA_TYPE"
    CONTENT_TYPE = "CONTENT_TYPE"
    SUBJECT = "SUBJECT"
    DESCRIPTION = "DESCRIPTION"
    KEYWORDS = "KEYWORDS"
    SUMMARY = "SUMMARY"
    SYNOPSIS = "SYNOPSIS"
    INITIAL_KEY = "INITIAL_KEY"
    PERIOD = "PERIOD"
    LAW_RATING = "LAW_RATING"
    ICRA = "ICRA"
    # Temporal Information
    DATE_RELEASED = "DATE_RELEASED"
    DATE_RECORDED = "DATE_RECORDED"
    DATE_ENCODED = "DATE_ENCODED"
    DATE_TAGGED = "DATE_TAGGED"
    DATE_DIGITIZED = "DATE_DIGITIZED"
    DATE_WRITTEN = "DATE_WRITTEN"
    DATE_PURCHASED = "DATE_PURCHASED"
    # Spacial Information
    RECORDING_LOCATION = "RECORDING_LOCATION"
    COMPOSITION_LOCATION = "COMPOSITION_LOCATION"
    COMPOSER_NATIONALITY = "COMPOSER_NATIONALITY"
    # Personal
    COMMENT = "COMMENT"
    PLAY_COUNTER = "PLAY_COUNTER"
    RATING = "RATING"
    # Technical Information
    ENCODER = "ENCODER"
    ENCODER_SETTINGS = "ENCODER_SETTINGS"
    BPS = "BPS"
    FPS = "FPS"
    BPM = "BPM"
    MEASURE = "MEASURE"
    TUNING = "TUNING"
    REPLAYGAIN_GAIN = "REPLAYGAIN_GAIN"
    REPLAYGAIN_PEAK = "REPLAYGAIN_PEAK"
    # Identifiers
    ISRC = "ISRC"
    MCDI = "MCDI"
    ISBN = "ISBN"
    BARCODE = "BARCODE"
    CATALOG_NUMBER = "CATALOG_NUMBER"
    LABEL_CODE = "LABEL_CODE"
    LCCN = "LCCN"
    # Commercial
    PURCHASE_ITEM = "PURCHASE_ITEM"
    PURCHASE_INFO = "PURCHASE_INFO"
    PURCHASE_OWNER = "PURCHASE_OWNER"
    PURCHASE_PRICE = "PURCHASE_PRICE"
    PURCHASE_CURRENCY = "PURCHASE_CURRENCY"
    # Legal
    COPYRIGHT = "COPYRIGHT"
    PRODUCTION_COPYRIGHT = "PRODUCTION_COPYRIGHT"
    LICENSE = "LICENSE"
    TERMS_OF_USE = "TERMS_OF_USE"

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return super().__repr__() + "\n" + tag_descriptions[self]


tag_descriptions = {
    TagTypes.ORIGINAL: "A special tag that is meant to have other tags inside (using nested tags) to describe the original work of art that this item is based on. "
                      "All tags in this list can be used \"under\" the ORIGINAL tag like LYRICIST, PERFORMER, etc.",
    TagTypes.SAMPLE: "A tag that contains other tags to describe a sample used in the targeted item taken from another work of art. "
                    "All tags in this list can be used \"under\" the SAMPLE tag like TITLE, ARTIST, DATE_RELEASED, etc.",
    TagTypes.COUNTRY: "The name of the country (biblio ISO-639-2) that is meant to have other tags inside (using nested tags) to country specific information about the item. "
                     "All tags in this list can be used \"under\" the COUNTRY_SPECIFIC tag like LABEL, PUBLISH_RATING, etc.",
    TagTypes.TOTAL_PARTS: "Total number of parts defined at the first lower level. (e.g. if TargetType is ALBUM, the total number of tracks of an audio CD)",
    TagTypes.PART_NUMBER: "Number of the current part of the current level. (e.g. if TargetType is TRACK, the track number of an audio CD)",
    TagTypes.PART_OFFSET: "A number to add to PART_NUMBER when the parts at that level don't start at 1. "
                         "(e.g. if TargetType is TRACK, the track number of the second audio CD)",
    TagTypes.TITLE: "The title of this item. "
                   "For example, for music you might label this \"Canon in D\", or for video's audio track you might use \"English 5.1\" This is akin to the TIT2 tag in ID3.",
    TagTypes.SUBTITLE: "Sub Title of the entity.",
    TagTypes.URL: "URL corresponding to the tag it's included in.",
    TagTypes.SORT_WITH: "A child element to indicate what alternative value the parent tag can have to be sorted, "
                       "for example \"Pet Shop Boys\" instead of \"The Pet Shop Boys\". "
                       "Or \"Marley Bob\" and \"Marley Ziggy\" (no comma needed).",
    TagTypes.INSTRUMENTS: "The instruments that are being used/played, separated by a comma. It should be a child of the following tags: ARTIST, LEAD_PERFORMER or ACCOMPANIMENT.",
    TagTypes.EMAIL: "Email corresponding to the tag it's included in.",
    TagTypes.ADDRESS: "The physical address of the entity. The address should include a country code. It can be useful for a recording label.",
    TagTypes.FAX: "The fax number corresponding to the tag it's included in. It can be useful for a recording label.",
    TagTypes.PHONE: "The phone number corresponding to the tag it's included in. It can be useful for a recording label.",
    TagTypes.ARTIST: "A person or band/collective generally considered responsible for the work. This is akin to the TPE1 tag in ID3.",
    TagTypes.LEAD_PERFORMER: "Lead Performer/Soloist(s). This can sometimes be the same as ARTIST.",
    TagTypes.ACCOMPANIMENT: "Band/orchestra/accompaniment/musician. This is akin to the TPE2 tag in ID3.",
    TagTypes.COMPOSER: "The name of the composer of this item. This is akin to the TCOM tag in ID3.",
    TagTypes.ARRANGER: "The person who arranged the piece, e.g., Ravel.",
    TagTypes.LYRICS: "The lyrics corresponding to a song (in case audio synchronization is not known or as a doublon to a subtitle track). "
                    "Editing this value when subtitles are found should also result in editing the subtitle track for more consistency.",
    TagTypes.LYRICIST: "The person who wrote the lyrics for a musical item. This is akin to the TEXT tag in ID3.",
    TagTypes.CONDUCTOR: "Conductor/performer refinement. This is akin to the TPE3 tag in ID3.",
    TagTypes.DIRECTOR: "This is akin to the IART tag in RIFF.",
    TagTypes.ASSISTANT_DIRECTOR: "The name of the assistant director.",
    TagTypes.DIRECTOR_OF_PHOTOGRAPHY: "The name of the director of photography, also known as cinematographer. This is akin to the ICNM tag in Extended RIFF.",
    TagTypes.SOUND_ENGINEER: "The name of the sound engineer or sound recordist.",
    TagTypes.ART_DIRECTOR: "The person who oversees the artists and craftspeople who build the sets.",
    TagTypes.PRODUCTION_DESIGNER: "Artist responsible for designing the overall visual appearance of a movie.",
    TagTypes.CHOREGRAPHER: "The name of the choreographer",
    TagTypes.COSTUME_DESIGNER: "The name of the costume designer",
    TagTypes.ACTOR: "An actor or actress playing a role in this movie. This is the person's real name, not the character's name the person is playing.",
    TagTypes.CHARACTER: "The name of the character an actor or actress plays in this movie. This should be a sub-tag of an ACTOR tag in order not to cause ambiguities.",
    TagTypes.WRITTEN_BY: "The author of the story or script (used for movies and TV shows).",
    TagTypes.SCREENPLAY_BY: "The author of the screenplay or scenario (used for movies and TV shows).",
    TagTypes.EDITED_BY: "This is akin to the IEDT tag in Extended RIFF.",
    TagTypes.PRODUCER: "Produced by. This is akin to the IPRO tag in Extended RIFF.",
    TagTypes.COPRODUCER: "The name of a co-producer.",
    TagTypes.EXECUTIVE_PRODUCER: "The name of an executive producer.",
    TagTypes.DISTRIBUTED_BY: "This is akin to the IDST tag in Extended RIFF.",
    TagTypes.MASTERED_BY: "The engineer who mastered the content for a physical medium or for digital distribution.",
    TagTypes.ENCODED_BY: "This is akin to the TENC tag in ID3.",
    TagTypes.MIXED_BY: "DJ mix by the artist specified",
    TagTypes.REMIXED_BY: "Interpreted, remixed, or otherwise modified by. This is akin to the TPE4 tag in ID3.",
    TagTypes.PRODUCTION_STUDIO: "This is akin to the ISTD tag in Extended RIFF.",
    TagTypes.THANKS_TO: "A very general tag for everyone else that wants to be listed.",
    TagTypes.PUBLISHER: "This is akin to the TPUB tag in ID3.",
    TagTypes.LABEL: "The record label or imprint on the disc.",
    TagTypes.GENRE: "The main genre (classical, ambient-house, synthpop, sci-fi, drama, etc). The format follows the infamous TCON tag in ID3.",
    TagTypes.MOOD: "Intended to reflect the mood of the item with a few keywords, e.g. \"Romantic\", \"Sad\" or \"Uplifting\". The format follows that of the TMOO tag in ID3.",
    TagTypes.ORIGINAL_MEDIA_TYPE: "Describes the original type of the media, "
                                 "such as, \"DVD\", \"CD\", \"computer image,\" \"drawing,\" \"lithograph,\" and so forth. "
                                 "This is akin to the TMED tag in ID3.",
    TagTypes.CONTENT_TYPE: "The type of the item. e.g. Documentary, Feature Film, Cartoon, Music Video, Music, Sound FX, ...",
    TagTypes.SUBJECT: "Describes the topic of the file, such as \"Aerial view of Seattle.\"",
    TagTypes.DESCRIPTION: "A short description of the content, such as \"Two birds flying.\"",
    TagTypes.KEYWORDS: "Keywords to the item separated by a comma, used for searching.",
    TagTypes.SUMMARY: "A plot outline or a summary of the story.",
    TagTypes.SYNOPSIS: "A description of the story line of the item.",
    TagTypes.INITIAL_KEY: "The initial key that a musical track starts in. The format is identical to ID3.",
    TagTypes.PERIOD: "Describes the period that the piece is from or about. For example, \"Renaissance\".",
    TagTypes.LAW_RATING: "Depending on the country it's the format of the rating of a movie (P, R, X in the USA, an age in other countries or a URI defining a logo).",
    TagTypes.DATE_RELEASED: "The time that the item was originaly released. This is akin to the TDRL tag in ID3.",
    TagTypes.DATE_RECORDED: "The time that the recording began. This is akin to the TDRC tag in ID3.",
    TagTypes.DATE_ENCODED: "The time that the encoding of this item was completed began. This is akin to the TDEN tag in ID3.",
    TagTypes.DATE_TAGGED: "The time that the tags were done for this item. This is akin to the TDTG tag in ID3.",
    TagTypes.DATE_DIGITIZED: "The time that the item was tranfered to a digital medium. This is akin to the IDIT tag in RIFF.",
    TagTypes.DATE_WRITTEN: "The time that the writing of the music/script began.",
    TagTypes.DATE_PURCHASED: "Information on when the file was purchased (see also purchase tags).",
    TagTypes.RECORDING_LOCATION: "The location where the item was recorded. "
                                "The countries corresponding to the string, same 2 octets as in Internet domains, or possibly ISO-3166. "
                                "This code is followed by a comma, then more detailed information such as state/province, another comma, and then city. "
                                "For example, \"US, Texas, Austin\". "
                                "This will allow for easy sorting. "
                                "It is okay to only store the country, or the country and the state/province. "
                                "More detailed information can be added after the city through the use of additional commas. "
                                "In cases where the province/state is unknown, but you want to store the city, simply leave a space between the two commas. "
                                "For example, \"US, , Austin\".",
    TagTypes.COMPOSITION_LOCATION: "Location that the item was originaly designed/written. "
                                  "The countries corresponding to the string, same 2 octets as in Internet domains, or possibly ISO-3166. "
                                  "This code is followed by a comma, then more detailed information such as state/province, another comma, and then city. "
                                  "For example, \"US, Texas, Austin\". "
                                  "This will allow for easy sorting. "
                                  "It is okay to only store the country, or the country and the state/province. "
                                  "More detailed information can be added after the city through the use of additional commas. "
                                  "In cases where the province/state is unknown, but you want to store the city, simply leave a space between the two commas. "
                                  "For example, \"US, , Austin\".",
    TagTypes.COMPOSER_NATIONALITY: "Nationality of the main composer of the item, mostly for classical music. "
                                  "The countries corresponding to the string, same 2 octets as in Internet domains, or possibly ISO-3166.",
    TagTypes.COMMENT: "Any comment related to the content.",
    TagTypes.PLAY_COUNTER: "The number of time the item has been played.",
    TagTypes.RATING: "A numeric value defining how much a person likes the song/movie. "
                    "The number is between 0 and 5 with decimal values possible (e.g. 2.7), 5(.0) being the highest possible rating. "
                    "Other rating systems with different ranges will have to be scaled.",
    TagTypes.ENCODER: "The software or hardware used to encode this item. (\"LAME\" or \"XviD\")",
    TagTypes.ENCODER_SETTINGS: "A list of the settings used for encoding this item. No specific format.",
    TagTypes.BPS: "The average bits per second of the specified item. This is only the data in the Blocks, and excludes headers and any container overhead.",
    TagTypes.FPS: "The average frames per second of the specified item. "
                 "This is typically the average number of Blocks per second. "
                 "In the event that lacing is used, each laced chunk is to be counted as a separate frame.",
    TagTypes.BPM: "Average number of beats per minute in the complete target (e.g. a chapter). Usually a decimal number.",
    TagTypes.MEASURE: "In music, a measure is a unit of time in Western music like \"4/4\". "
                     "It represents a regular grouping of beats, a meter, as indicated in musical notation by the time signature.. "
                     "The majority of the contemporary rock and pop music you hear on the radio these days is written in the 4/4 time signature.",
    TagTypes.TUNING: "It is saved as a frequency in hertz to allow near-perfect tuning of instruments to the same tone as the musical piece "
                    "(e.g. \"441.34\" in Hertz). The default value is 440.0 Hz.",
    TagTypes.ISRC: "The International Standard Recording Code, excluding the \"ISRC\" prefix and including hyphens.",
    TagTypes.ISBN: "International Standard Book Number",
    TagTypes.BARCODE: "EAN-13 (European Article Numbering) or UPC-A (Universal Product Code) bar code identifier",
    TagTypes.CATALOG_NUMBER: "A label-specific string used to identify the release (TIC 01 for example).",
    TagTypes.LABEL_CODE: "A 4-digit or 5-digit number to identify the record label, typically printed as (LC) xxxx or (LC) 0xxxx on "
                        "CDs medias or covers (only the number is stored).",
    TagTypes.LCCN: "Library of Congress Control Number",
    TagTypes.PURCHASE_ITEM: "URL to purchase this file. This is akin to the WPAY tag in ID3.",
    TagTypes.PURCHASE_INFO: "Information on where to purchase this album. This is akin to the WCOM tag in ID3.",
    TagTypes.PURCHASE_OWNER: "Information on the person who purchased the file. This is akin to the TOWN tag in ID3.",
    TagTypes.PURCHASE_PRICE: "The amount paid for entity. There should only be a numeric value in here. "
                            "Only numbers, no letters or symbols other than \".\". "
                            "For instance, you would store \"15.59\" instead of \"$15.59USD\".",
    TagTypes.PURCHASE_CURRENCY: "The currency type used to pay for the entity. Use ISO-4217 for the 3 letter currency code.",
    TagTypes.COPYRIGHT: "The copyright information as per the copyright holder. This is akin to the TCOP tag in ID3.",
    TagTypes.PRODUCTION_COPYRIGHT: "The copyright information as per the production copyright holder. This is akin to the TPRO tag in ID3.",
    TagTypes.LICENSE: "The license applied to the content (like Creative Commons variants).",
    TagTypes.TERMS_OF_USE: "The terms of use for this item. This is akin to the USER tag in ID3.",
    TagTypes.ICRA: "[binary]\tThe ICRA content rating for parental control. (Previously RSACi)",
    TagTypes.REPLAYGAIN_GAIN: "[binary]\tThe gain to apply to reach 89dB SPL on playback. This is based on the Replay Gain standard. "
                             "Note that ReplayGain information can be found at all TargetType levels (track, album, etc).",
    TagTypes.REPLAYGAIN_PEAK: "[binary]\tThe maximum absolute peak value of the item. This is based on the Replay Gain standard.",
    TagTypes.MCDI: "[binary]\tThis is a binary dump of the TOC of the CDROM that this item was taken from. This holds the same information as the MCDI in ID3."
}
