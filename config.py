from enum import Enum
from language import LanguageName
GENREDIC = {}
LANGNAME = {}

class AgeCode(Enum):
    general = 1
    r15 = 2
    r18 = 3
    name_map = {
        1: 'general',
        2: 'r15',
        3: 'r18',
    }


class CATCode(Enum):
    home = 'home'
    soft = 'soft'
    app = 'app'
    home_asmr = 'home/asmr'
    home_tool = 'home/tool'
    maniax = 'maniax'
    books = 'books'
    pro = 'pro'
    appx = 'appx'
    maniax_tool = 'maniax/tool'
    girls = 'girls'
    bl = 'bl'
    def has_value(value):
        return value in CATCode._value2member_map_ 
    
class SITECode(Enum):
    home = 'home'
    maniax = 'maniax'
    girls = 'girls'
    bl = 'bl'
    def has_value(value):
        return value in SITECode._value2member_map_ 
    
class TYPECode(Enum):
    RPG = 'RPG' # ロールプレイング
    ACN = 'ACN' # アクション
    SLN = 'SLN' # シミュレーション
    ADV = 'ADV' # アドベンチャー
    STG = 'STG' # シューティング
    PZL = 'PZL' # パズル
    TBL = 'TBL' # テーブル
    TYP = 'TYP' # タイピング
    DNV = 'DNV' # デジタルノベル
    QIZ = 'QIZ' # クイズ
    ETC = 'ETC' # その他ゲーム
    MNG = 'MNG' # マンガ
    ICG = 'ICG' # CG・イラスト
    NRE = 'NRE' # ノベル
    KSV = 'KSV' # 書籍
    MOV = 'MOV' # 動画
    SOU = 'SOU' # ASMR
    MUS = 'MUS' # 音楽
    TOL = 'TOL' # ツール/アクセサリ
    IMT = 'IMT' # 画像素材
    AMT = 'AMT' # 音素材
    ET3 = 'ET3' # その他
    VCM = 'VCM' # ボイスコミック
    def has_value(value):
        return value in TYPECode._value2member_map_ 
    
class OPTIONCode(Enum):
    WPD = 'WPD' # PDF同梱
    WAP = 'WAP' # APK同梱
    DLP = 'DLP' # ブラウザ対応
    REV = 'REV' # レビューあり
    SND = 'SND' # 音声あり
    MS2 = 'MS2' # 音楽あり
    MV2 = 'MV2' # 動画あり
    TRI = 'TRI' # 体験版あり
    GRO = 'GRO' # グロテスク表現あり
    DOT = 'DOT' # DLsite公式翻訳
    NM = 'NM'   # 言語不要
    OTL = 'OTL' # その他言語
    MEN = 'MEN' # ゲイ表現を含む作品
    SBK = 'SBK' # セーブのバックアップ機能あり
    ## コミックマーケット
    EVT = 'EVT' # コミックマーケット82
    C83 = 'C83' # コミックマーケット
    C84 = 'C84'
    C85 = 'C85'
    C86 = 'C86'
    C87 = 'C87'
    C88 = 'C88'
    C89 = 'C89'
    C90 = 'C90'
    C91 = 'C91'
    C92 = 'C92'
    C93 = 'C93'
    C94 = 'C94'
    C95 = 'C95'
    C96 = 'C96'
    C97 = 'C97'
    C98 = 'C98'
    C99 = 'C99'
    C100 = 'C100'
    C101 = 'C101'
    C102 = 'C102'
    C103 = 'C103'
    C104 = 'C104'
    # 即売会
    DE203 = 'DE203' # 2020年3月～5月即売会
    AC2 = 'AC2'     # エアコミケ2
    JGD = 'JGD'     # J.GARDEN
    CMT = 'CMT'     # コミティア
    def has_value(value):
        return value in OPTIONCode._value2member_map_ 