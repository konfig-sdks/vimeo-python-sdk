# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vimeo_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    LIVEESSENTIALS = "Live\Essentials"
    LIVEEVENT_DESTINATIONS = "Live\Event destinations"
    SHOWCASESSHOWCASE_VIDEOS = "Showcases\Showcase videos"
    LIVEEVENT_THUMBNAILS = "Live\Event thumbnails"
    LIVEEVENT_VIDEOS = "Live\Event videos"
    USERSFOLLOWERS = "Users\Followers"
    VIDEOSCHAPTERS = "Videos\Chapters"
    VIDEOSESSENTIALS = "Videos\Essentials"
    FOLDERSESSENTIALS = "Folders\Essentials"
    LIKESESSENTIALS = "Likes\Essentials"
    SHOWCASESESSENTIALS = "Showcases\Essentials"
    FOLDERSVIDEOS = "Folders\Videos"
    USERSPICTURES = "Users\Pictures"
    VIDEOSVIDEO_COMMENTS = "Videos\Video comments"
    CATEGORIESUSERS = "Categories\Users"
    EMBED_PRESETSCUSTOM_LOGOS = "Embed Presets\Custom logos"
    EMBED_PRESETSESSENTIALS = "Embed Presets\Essentials"
    ON_DEMANDGENRES = "On Demand\Genres"
    ON_DEMANDREGIONS = "On Demand\Regions"
    PORTFOLIOSVIDEOS = "Portfolios\Videos"
    VIDEOSCREDITS = "Videos\Credits"
    WATCH_LATER_QUEUEESSENTIALS = "Watch Later Queue\Essentials"
    WEBINARREGISTRATIONS = "Webinar\Registrations"
    CHANNELSESSENTIALS = "Channels\Essentials"
    CHANNELSMODERATORS = "Channels\Moderators"
    CHANNELSSUBSCRIPTIONS_AND_SUBSCRIBERS = "Channels\Subscriptions and subscribers"
    CHANNELSVIDEOS = "Channels\Videos"
    ON_DEMANDESSENTIALS = "On Demand\Essentials"
    VIDEOSTEXT_TRACKS = "Videos\Text tracks"
    VIDEOSTHUMBNAILS = "Videos\Thumbnails"
    WEBINARESSENTIALS = "Webinar\Essentials"
    LIVEEMBED_PRIVACY = "Live\Embed privacy"
    VIDEOSTAGS = "Videos\Tags"
    VIDEOSUNLISTED_VIDEOS = "Videos\Unlisted videos"
    VIDEOSVERSIONS = "Videos\Versions"
    CHANNELSTAGS = "Channels\Tags"
    EMBED_PRESETSVIDEOS = "Embed Presets\Videos"
    GROUPSUSERS = "Groups\Users"
    ON_DEMANDBACKGROUNDS = "On Demand\Backgrounds"
    ON_DEMANDPROMOTIONS = "On Demand\Promotions"
    SHOWCASESCUSTOM_SHOWCASE_LOGOS = "Showcases\Custom showcase logos"
    SHOWCASESCUSTOM_SHOWCASE_THUMBNAILS = "Showcases\Custom showcase thumbnails"
    VIDEOSANIMATED_THUMBNAILS = "Videos\Animated thumbnails"
    CATEGORIESVIDEOS = "Categories\Videos"
    CHANNELSCATEGORIES = "Channels\Categories"
    CHANNELSPRIVATE_CHANNEL_MEMBERS = "Channels\Private channel members"
    GROUPSESSENTIALS = "Groups\Essentials"
    GROUPSSUBSCRIPTIONS = "Groups\Subscriptions"
    GROUPSVIDEOS = "Groups\Videos"
    ON_DEMANDPOSTERS = "On Demand\Posters"
    ON_DEMANDVIDEOS = "On Demand\Videos"
    PORTFOLIOSESSENTIALS = "Portfolios\Essentials"
    USERSESSENTIALS = "Users\Essentials"
    VIDEOSUPLOADS = "Videos\Uploads"
    WEBINAREMAILS = "Webinar\Emails"
    FOLDERSITEMS = "Folders\Items"
    LIVEEVENT_ACTIVATION = "Live\Event activation"
    LIVEEVENT_AUTOMATED_CLOSED_CAPTIONS = "Live\Event automated closed captions"
    LIVEEVENT_END = "Live\Event end"
    LIVEEVENT_LOW_LATENCY = "Live\Event low latency"
    ON_DEMANDPURCHASES_AND_RENTALS = "On Demand\Purchases and rentals"
    ON_DEMANDSEASONS = "On Demand\Seasons"
    TEAMSMEMBERS = "Teams\Members"
    USERSWATCH_HISTORY = "Users\Watch history"
    VIDEOSEMBED_PRIVACY = "Videos\Embed privacy"
    VIDEOSFRAGMENTS = "Videos\Fragments"
    AUTHENTICATION_EXTRASESSENTIALS = "Authentication Extras\Essentials"
    CATEGORIESESSENTIALS = "Categories\Essentials"
    EMBED_PRESETSTIMELINE_EVENTS = "Embed Presets\Timeline events"
    LIVEEVENT_M3U8_PLAYBACK = "Live\Event M3U8 playback"
    PAYMENTSESSENTIALS = "Payments\Essentials"
    USERSANALYTICS = "Users\Analytics"
    USERSFEEDS = "Users\Feeds"
    VIDEOSLIVE_M3U8_PLAYBACK = "Videos\Live M3U8 playback"
    VIDEOSNONDESTRUCTIVE_TRIMMING = "Videos\Nondestructive trimming"
    VIDEOSSHOWCASES = "Videos\Showcases"
    API_INFORMATIONESSENTIALS = "API Information\Essentials"
    AUTHENTICATION_EXTRASAUTHENTICATE = "Authentication Extras\Authenticate"
    AUTHENTICATION_EXTRASCONVERT = "Authentication Extras\Convert"
    AUTHENTICATION_EXTRASEXCHANGE = "Authentication Extras\Exchange"
    CATEGORIESCHANNELS = "Categories\Channels"
    CATEGORIESGROUPS = "Categories\Groups"
    LIVEEVENT_SESSIONS = "Live\Event sessions"
    SUBSCRIPTION_PLANSESSENTIALS = "Subscription Plans\Essentials"
    TAGSESSENTIALS = "Tags\Essentials"
    TUTORIALESSENTIALS = "Tutorial\Essentials"
    USERSSEARCH = "Users\Search"
    VIDEOSCONTENT_RATINGS = "Videos\Content ratings"
    VIDEOSCREATIVE_COMMONS = "Videos\Creative Commons"
    VIDEOSLANGUAGES = "Videos\Languages"
    VIDEOSRECOMMENDATIONS = "Videos\Recommendations"
    VIDEOSTRANSCRIPTS = "Videos\Transcripts"
