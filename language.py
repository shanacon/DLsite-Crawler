from dataclasses import dataclass
from enum import Enum
from typing import Dict

class LocaleLanguage(Enum):
    jp = 'ja_JP'
    en = 'en_US'
    cn = 'zh_CN'
    tw = 'zh_TW'
    kr = 'ko_KR'
    es = 'es_ES'
    de = 'de_DE'
    fr = 'fr_FR'
    id = 'id_ID'
    it = 'it_IT'
    pt = 'pt_BR'
    sv = 'sv_SE'
    th = 'th_TH'
    vi = 'vi_VN'

class LanguageCode(Enum):
    JPN = '日本語'
    CHI  = '中文'
    CHI_HANT = '繁體中文'
    CHI_HANS = '简体中文'
    KO_KR = '한국어'
    ENG = 'English'
    SPA = 'Español'
    FRE = 'Français'
    ITA = 'Italiano'
    POR = 'Português'
    DUT = 'Deutsch'
    IND = 'Bahasa Indonesia'
    THA = 'ภาษาไทย'
    VIE = 'Tiếng Việt'
    SV = 'Svenska'
    def has_value(value):
        return value in LanguageCode._member_names_

@dataclass
class LanguageName():
    JPN : Dict[LocaleLanguage, str] = None
    CHI_HANT : Dict[LocaleLanguage, str] = None
    CHI_HANS : Dict[LocaleLanguage, str] = None
    KO_KR : Dict[LocaleLanguage, str] = None
    ENG : Dict[LocaleLanguage, str] = None
    SPA : Dict[LocaleLanguage, str] = None
    FRE : Dict[LocaleLanguage, str] = None
    ITA : Dict[LocaleLanguage, str] = None
    RUS : Dict[LocaleLanguage, str] = None
    POR : Dict[LocaleLanguage, str] = None
    GER : Dict[LocaleLanguage, str] = None
    ARA : Dict[LocaleLanguage, str] = None
    CZE : Dict[LocaleLanguage, str] = None
    DUT : Dict[LocaleLanguage, str] = None
    IND : Dict[LocaleLanguage, str] = None
    POL : Dict[LocaleLanguage, str] = None
    THA : Dict[LocaleLanguage, str] = None
    VIE : Dict[LocaleLanguage, str] = None