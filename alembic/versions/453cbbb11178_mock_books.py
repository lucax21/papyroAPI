"""mock books

Revision ID: 453cbbb11178
Revises: b99ebfd3f1c8
Create Date: 2022-07-28 18:48:03.033431

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '453cbbb11178'
down_revision = 'b99ebfd3f1c8'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
       INSERT INTO book(identifier)
            VALUES ( '-PUrAAAAYAAJ'),
            ( 'YKwtAAAAYAAJ'),
            ( 'u7cuAAAAYAAJ'),
            ( 'nrheAAAAIAAJ'),
            ( '39YKs0NbOXwC'),
            ( 'cdPuAAAAMAAJ'),
            ( 'kOknAQAAIAAJ'),
            ( 'U0ocAQAAIAAJ'),
            ( 'QJ5FAAAAYAAJ'),
            ( 'O2JaAAAAMAAJ'),
            ( 'TxAgAAAAMAAJ'),
            ( 'tZJ_BAAAQBAJ'),
            ( 'xh1SDwAAQBAJ'),
            ( 'YUW3WSCW7kwC'),
            ( '6CzPCwAAQBAJ'),
            ( 'KuEuAAAAYAAJ'),
            ( 'uYZWAQAAQBAJ'),
            ( '8jd9AgAAQBAJ'),
            ( '6-5NDAAAQBAJ'),
            ( 'VdOWAAAAQBAJ'),
            ( '-ouaBAAAQBAJ'),
            ( 'Ldp2AwAAQBAJ'),
            ( 'kerCBwAAQBAJ'),
            ( 'RhVTAAAAMAAJ'),
            ( 't71YAAAAYAAJ'),
            ( 'DplIAgAAQBAJ'),
            ( 'ka5WAQAAQBAJ'),
            ( 'RtacAgAAQBAJ'),
            ( 'WypsCgAAQBAJ'),
            ( 'VKRwAAAAIAAJ'),
            ( 'EXIKAQAAIAAJ'),
            ( 'FZVgAAAAIAAJ'),
            ( 'fGFoDwAAQBAJ'),
            ( 'nSYOAQAAMAAJ'),
            ( 'bf2nCwAAQBAJ'),
            ( 'UpYrDQAAQBAJ'),
            ( 'AoZDAgAAQBAJ'),
            ( 'OqkvAAAAYAAJ'),
            ( 'CNL6p2RILvoC'),
            ( '_gR3AgAAQBAJ'),
            ( 'JdnYBAAAQBAJ'),
            ( '9aq1kPl-sdEC'),
            ( '5_ylBAAAQBAJ'),
            ( 'k1DwCAAAQBAJ'),
            ( '2MN1DwAAQBAJ'),
            ( 'QwL8BAAAQBAJ'),
            ( 'wL5XBAAAQBAJ'),
            ( 'Bis2DwAAQBAJ'),
            ( 'wX8bAgAAQBAJ'),
            ( 'wBc2AQAAIAAJ'),
            ( 'NjCgAAAAMAAJ'),
            ( 'AY5HDwAAQBAJ'),
            ( '8C-aBwAAQBAJ'),
            ( 'f0ksAAAAYAAJ'),
            ( 'aYyaBAAAQBAJ'),
            ( 'fZtxDwAAQBAJ'),
            ( 'mX5lAAAAMAAJ'),
            ( 'QPkfAAAAIAAJ'),
            ( 'g0EtAAAAYAAJ'),
            ( 'urmtDwAAQBAJ'),
            ( 'jU2jDwAAQBAJ'),
            ( 'zKdVAAAAMAAJ'),
            ( 'ilMmAQAAIAAJ'),
            ( '-64vAQAAMAAJ'),
            ( 'kAB5CgAAQBAJ'),
            ( 'fiUtAAAAIAAJ'),
            ( 'DVeoDwAAQBAJ'),
            ( 'roQVAQAAMAAJ'),
            ( '49l2AwAAQBAJ'),
            ( 'x-8QAQAAMAAJ'),
            ( 'rnK1AAAAIAAJ'),
            ( 'inktAAAAYAAJ'),
            ( 'ldc8AAAAYAAJ'),
            ( 'gnIEDgAAQBAJ'),
            ( 'xfEdAQAAIAAJ'),
            ( 'GjouAAAAYAAJ'),
            ( 'JQQvAAAAYAAJ'),
            ( 'RbFcAAAAMAAJ'),
            ( 'RxFHAAAAYAAJ'),
            ( 'C_i5AAAAIAAJ'),
            ( 'jkxHBAAAQBAJ'),
            ( 'qbBZBAAAQBAJ'),
            ( 'g8IUBQAAQBAJ'),
            ( 'ZPWEBAAAQBAJ'),
            ( 'hpBKBAAAQBAJ'),
            ( 'of2lBAAAQBAJ'),
            ( 'A3abAwAAQBAJ'),
            ( '4lJxBAAAQBAJ'),
            ( '9fSEBAAAQBAJ'),
            ( 'xvo8BQAAQBAJ'),
            ( 'P-S5AwAAQBAJ'),
            ( 'UhSqBAAAQBAJ'),
            ( 'Dps2BAAAQBAJ'),
            ( '3UsXAgAAQBAJ'),
            ( 'Yz6yBAAAQBAJ'),
            ( 'dUYDAwAAQBAJ'),
            ( 'IcQLBQAAQBAJ'),
            ( 'jVyDAwAAQBAJ'),
            ( 'apJQAgAAQBAJ'),
            ( 'GcgXNITpKy0C'),
            ( 'TIsMOoBcJIMC'),
            ( '6yK5AAAAIAAJ'),
            ( 'sGc8j8Jfsd4C'),
            ( 'eVtMAAAAYAAJ'),
            ( 'NJ_uAAAAMAAJ'),
            ( 'WqYVAQAAIAAJ'),
            ( 'oDlZTbTmmGwC'),
            ( 'mjoaAAAAIAAJ'),
            ( 'ndNAAQAAIAAJ'),
            ( 'PkQtAAAAYAAJ'),
            ( 'jmZ-AwAAQBAJ'),
            ( '0XIDAAAAQBAJ'),
            ( '8voWAQAAMAAJ'),
            ( '4zrqrsIUOc0C'),
            ( 's00KAQAAIAAJ'),
            ( 'Ka0tAAAAYAAJ'),
            ( 'evX0DAAAQBAJ'),
            ( 'P2otAAAAYAAJ'),
            ( 'a2nzAgAAQBAJ'),
            ( 'JOskBQAAQBAJ'),
            ( 'n2ETAQAAMAAJ'),
            ( 'OQw-AAAAYAAJ'),
            ( 'EjoTAQAAMAAJ'),
            ( 'Kk-wDwAAQBAJ'),
            ( '9F4tAAAAYAAJ'),
            ( '0vPSGLn_64QC'),
            ( 'HsHfBgAAQBAJ'),
            ( 'GXXuAAAAMAAJ'),
            ( 'nNMQAQAAMAAJ'),
            ( 'sy4zDQAAQBAJ'),
            ( 'I5BOAQAAIAAJ'),
            ( 'oLPMqbcynh4C'),
            ( 'uPorAAAAYAAJ'),
            ( 'tmwtAAAAYAAJ'),
            ( 'Q79TAAAAMAAJ'),
            ( '1i-YBAAAQBAJ'),
            ( 'M99TAgAAQBAJ'),
            ( '0PtSAwAAQBAJ'),
            ( 'bSOHBAAAQBAJ'),
            ( 'yfKwNBmNIrEC'),
            ( 'bXyeCgAAQBAJ'),
            ( 'SgNTBAAAQBAJ'),
            ( 'Ak9ZiZuHDUIC'),
            ( 'szJ7mowe0W4C'),
            ( 'QCKYBAAAQBAJ'),
            ( 'At0Y1jFNekcC'),
            ( '3l4YAwAAQBAJ'),
            ( 'P_WEBAAAQBAJ'),
            ( 'Vx86BAAAQBAJ'),
            ( '4tdsBAAAQBAJ'),
            ( 'xHcWdWaVbD8C'),
            ( 'yUotAAAAYAAJ'),
            ( 'TbzwAwAAQBAJ'),
            ( 'tRajDwAAQBAJ'),
            ( 'RsldvgAACAAJ'),
            ( 'JzFTAAAAMAAJ'),
            ( 'RHmADwAAQBAJ'),
            ( 'D_0xAQAAIAAJ'),
            ( 'tWgtAAAAYAAJ'),
            ( 'XIUVAQAAMAAJ'),
            ( 'FKCNDwAAQBAJ'),
            ( 'a1MnDwAAQBAJ'),
            ( 'xYS7TStMWeMC'),
            ( 'IRA8EAAAQBAJ'),
            ( 'mn8tAAAAYAAJ'),
            ( 'SMqFDwAAQBAJ'),
            ( 'Y8KbDwAAQBAJ'),
            ( 'kDRKBQAAQBAJ'),
            ( 'j_ClDuQZNMYC'),
            ( 'cVMnDwAAQBAJ'),
            ( 'pUt8DwAAQBAJ'),
            ( 'bVMnDwAAQBAJ'),
            ( 'iNtSEAAAQBAJ'),
            ( 'HOl7DwAAQBAJ'),
            ( 'zA08lDv_UzgC'),
            ( 'Ocg2EAAAQBAJ'),
            ( '4K5QEAAAQBAJ'),
            ( 'Cep7DwAAQBAJ'),
            ( 'PNOZzQEACAAJ'),
            ( 'kBFKEAAAQBAJ'),
            ( 'o110DwAAQBAJ'),
            ( 'TZNzEAAAQBAJ'),
            ( 'j_GnBAAAQBAJ'),
            ( 'UwlzDwAAQBAJ'),
            ( '1QtyDwAAQBAJ'),
            ( 'XnfGCwAAQBAJ'),
            ( 'LkYS4DJvensC'),
            ( '-WdlBAAAQBAJ'),
            ( 'tcLfBgAAQBAJ'),
            ( 'FMEZkNHgLzIC'),
            ( '6R5IjwEACAAJ'),
            ( 'N6d6HaKHPX8C'),
            ( 'yNf0DwAAQBAJ'),
            ( 'Cub0DwAAQBAJ'),
            ( 'BjI9BAAAQBAJ'),
            ( 'h_uYp0-SvgYC'),
            ( 'M4arDwAAQBAJ'),
            ( 'oZ39DwAAQBAJ'),
            ( 'X5uSDwAAQBAJ'),
            ( '_SlJzQEACAAJ'),
            ( 'ZWwiDgAAQBAJ'),
            ( 'o-ZhDwAAQBAJ'),
            ( 'smjECwAAQBAJ'),
            ( '5UjiCgAAQBAJ'),
            ( '2CgzDwAAQBAJ'),
            ( '5bgqAgAAQBAJ'),
            ( 'TgSsPgAACAAJ'),
            ( 'PwI2AAAAIAAJ'),
            ( 'duwuAAAAYAAJ'),
            ( 'UPmYBAAAQBAJ'),
            ( 'd7xnzgEACAAJ'),
            ( 'vvQ8AAAAYAAJ'),
            ( 'LB4wEAAAQBAJ'),
            ( 'S2o8AAAAYAAJ'),
            ( '9Y11AAAAMAAJ'),
            ( 'S3Y_EAAAQBAJ'),
            ( 'LOQgAQAAIAAJ'),
            ( 'MQ60XwAACAAJ'),
            ( 'ENIeAQAAIAAJ'),
            ( 'M5sgvgAACAAJ'),
            ( 'G-FBEAAAQBAJ'),
            ( 'aJlFAAAAYAAJ'),
            ( 'wSQsAAAAYAAJ'),
            ( 'bastAAAAYAAJ'),
            ( 'W_YTAQAAIAAJ'),
            ( 'hh53BwAAQBAJ'),
            ( 'MAoeAQAAIAAJ'),
            ( 'BqotAAAAYAAJ'),
            ( '5ZIwLgEACAAJ'),
            ( '4ktaAAAAMAAJ'),
            ( '1FOLvgAACAAJ'),
            ( 'N_M6vgAACAAJ'),
            ( 'OgOZDwAAQBAJ'),
            ( 'WmWRoAEACAAJ'),
            ( 'MplDAAAAYAAJ'),
            ( 'F2YOzgEACAAJ'),
            ( 'pk6JtQEACAAJ'),
            ( 'CsKfzQEACAAJ'),
            ( '5IfwswEACAAJ'),
            ( '6AosAAAAYAAJ'),
            ( 'Os59GwAACAAJ'),
            ( 'p4KyAAAAIAAJ'),
            ( 'EAzUZwEACAAJ'),
            ( 'Ia5BxAEACAAJ'),
            ( 'hoppzgEACAAJ'),
            ( 'vhHOtgAACAAJ'),
            ( 'jLMStwAACAAJ'),
            ( '5BCazgEACAAJ'),
            ( '6WyzZwEACAAJ'),
            ( '0uAwPAAACAAJ'),
            ( 'reWCzgEACAAJ'),
            ( 'yeakjwEACAAJ'),
            ( 'RhrxZwEACAAJ'),
            ( 'UMuCPgAACAAJ'),
            ( 'L7_-ZwEACAAJ'),
            ( 'TlNlAAAACAAJ'),
            ( 'V1q2kQEACAAJ'),
            ( '06d2tAEACAAJ'),
            ( 'xVTwZwEACAAJ'),
            ( 'UeguzgEACAAJ'),
            ( 'GS_ItgAACAAJ'),
            ( 'imSFGwAACAAJ'),
            ( '-GtqGwAACAAJ'),
            ( '8BQ_HQAACAAJ'),
            ( 'B44iMwEACAAJ'),
            ( 'mE34tgAACAAJ'),
            ( '58HglwEACAAJ'),
            ( 'u83stgAACAAJ'),
            ( 'XK5gvgAACAAJ'),
            ( 'R7e4zQEACAAJ'),
            ( 'DelfQwAACAAJ'),
            ( 'goyvXwAACAAJ'),
            ( '-8TImgEACAAJ'),
            ( 'ZIIWuAAACAAJ'),
            ( 'HaWLZwEACAAJ'),
            ( 'V9p9NQEACAAJ'),
            ( '_cLBkgEACAAJ'),
            ( '3l4DaAEACAAJ'),
            ( 'Em9PtwAACAAJ'),
            ( 'yv0qHAAACAAJ'),
            ( 'FiM2AAAACAAJ'),
            ( 'lp4QEAAAQBAJ'),
            ( 'F9KykgEACAAJ'),
            ( 'ZOR3zQEACAAJ'),
            ( 'Buq0PgAACAAJ'),
            ( 'aRUwYAAACAAJ'),
            ( 'XGDAkQEACAAJ'),
            ( 'X5NTwQEACAAJ'),
            ( 'A9K6xQEACAAJ'),
            ( 'JV4WuAEACAAJ'),
            ( 'DPwsHAAACAAJ'),
            ( 'lVAqGwAACAAJ'),
            ( 'K8NeHQAACAAJ'),
            ( '4vHtZwEACAAJ'),
            ( '53jQkQEACAAJ'),
            ( 'IpEpGwAACAAJ'),
            ( 'dfNQAQAACAAJ'),
            ( 'xPVFkgEACAAJ'),
            ( 'fEmBAAAACAAJ'),
            ( 'tlQzHQAACAAJ'),
            ( 'rVf2ZwEACAAJ'),
            ( '_SRhkgEACAAJ'),
            ( 'vwIkHAAACAAJ'),
            ( 'SgsSogEACAAJ'),
            ( '-2ubzgEACAAJ'),
            ( 'NAgCmwEACAAJ'),
            ( 'QU6WnQEACAAJ'),
            ( 'NeyPHAAACAAJ'),
            ( 'CWXKAAAACAAJ'),
            ( 'shEEQgAACAAJ'),
            ( 'vWu9swEACAAJ'),
            ( 'TBvhoAEACAAJ'),
            ( 'qD-LmwEACAAJ'),
            ( 'U1O_NAEACAAJ'),
            ( '2POscQAACAAJ'),
            ( 'z-vjzQEACAAJ'),
            ( 'uzKNmwEACAAJ'),
            ( 'HkC4HAAACAAJ'),
            ( 'i189mwEACAAJ'),
            ( 'pJ6mnQAACAAJ'),
            ( 'jsTpPgAACAAJ'),
            ( 'NxbIkQEACAAJ'),
            ( 'YHe1XwAACAAJ'),
            ( 'vOsSnQAACAAJ'),
            ( 'z1eUngEACAAJ'),
            ( 'pWGsPgAACAAJ'),
            ( 'iFXrugAACAAJ'),
            ( 'dzxZHQAACAAJ'),
            ( '-n0RzwEACAAJ'),
            ( 'w_qMtAEACAAJ'),
            ( 'Rb07DwAAQBAJ'),
            ( 'Ll1FAAAACAAJ'),
            ( 'eXL8ZwEACAAJ'),
            ( 'fnwvugEACAAJ'),
            ( 'ozYQzgEACAAJ'),
            ( 'iFXTZwEACAAJ'),
            ( 'pfTwHAAACAAJ'),
            ( '7GjtugAACAAJ'),
            ( 'c8UNyAEACAAJ'),
            ( 'VQWktAEACAAJ'),
            ( 'vpdcuAAACAAJ'),
            ( 'IVe2HAAACAAJ'),
            ( 'kqwwswEACAAJ'),
            ( 'GrlJQwAACAAJ'),
            ( 'TiyYPgAACAAJ'),
            ( 'zpzloQEACAAJ'),
            ( '1desAQAACAAJ'),
            ( 'WwJFjwEACAAJ'),
            ( 'idPTGwAACAAJ'),
            ( 'DFRokgEACAAJ'),
            ( 'M3-8NAEACAAJ'),
            ( 'nfTwjgEACAAJ'),
            ( 'k8zUZwEACAAJ'),
            ( 'E2LkHAAACAAJ'),
            ( 'jG06twAACAAJ'),
            ( 'uWXvAAAACAAJ'),
            ( 'r5MfAAAAMAAJ'),
            ( 'v68CAAAAMAAJ'),
            ( 'kX8tAAAAYAAJ'),
            ( 'rUAsAAAAIAAJ'),
            ( 'Puo_AQAAIAAJ'),
            ( 'MV8VAQAAMAAJ'),
            ( 'GHktAAAAYAAJ'),
            ( 'ss4tAAAAYAAJ'),
            ( 'VhMTAQAAIAAJ'),
            ( '7WItAAAAYAAJ'),
            ( 'cEiTBAAAQBAJ'),
            ( 'qiXPBAAAQBAJ'),
            ( 'OKlYAwAAQBAJ'),
            ( 'tFz3AgAAQBAJ'),
            ( 'i1YtAAAAYAAJ'),
            ( 'n6TYAAAAMAAJ'),
            ( 'mkIRAQAAMAAJ'),
            ( 'b7MzAQAAIAAJ'),
            ( 'zXMtAAAAYAAJ'),
            ( 'w4ctAAAAYAAJ'),
            ( 'lJ1VBAAAQBAJ'),
            ( 'VKstAAAAYAAJ'),
            ( 'r-AeCAAAQBAJ'),
            ( '8ucjAAAAMAAJ'),
            ( 'IVoOAQAAMAAJ'),
            ( 'k_2nCwAAQBAJ'),
            ( '4zJZAAAAMAAJ'),
            ( 'C1sTAQAAMAAJ'),
            ( 'BWw0AQAAMAAJ'),
            ( 'Xy6XGUCswIgC'),
            ( 'zXItAAAAYAAJ'),
            ( '25NZAAAAMAAJ'),
            ( 'rnAtAAAAYAAJ'),
            ( 'FFEtAAAAYAAJ'),
            ( '4XwtAAAAIAAJ'),
            ( '0qofAQAAIAAJ'),
            ( 'NzktAAAAYAAJ'),
            ( 'zvhmAAAAMAAJ'),
            ( '5uXQDgAAQBAJ'),
            ( 'wqxoAAAAMAAJ'),
            ( 'I133AgAAQBAJ'),
            ( 'xSheBAAAQBAJ'),
            ( 'tAVtBAAAQBAJ'),
            ( 'Pw38BAAAQBAJ'),
            ( '03Y6AQAAIAAJ'),
            ( 'o14TBgAAQBAJ'),
            ( 'um5FAQAAIAAJ'),
            ( '_lz3AgAAQBAJ'),
            ( 'QoMCAAAAMAAJ'),
            ( 'Y4qUAgAAQBAJ'),
            ( '8QofAQAAIAAJ'),
            ( 'FuKGDwAAQBAJ'),
            ( 'PwuoAAAAIAAJ'),
            ( 'SwlXAAAAYAAJ'),
            ( 'fsGJ7uL-Yq4C'),
            ( 'ltFVAAAAMAAJ'),
            ( 'iA0fAAAAMAAJ'),
            ( 'SaMtAAAAYAAJ'),
            ( 'cACjBQAAQBAJ'),
            ( '-NVVAAAAMAAJ'),
            ( 'EflCszJqy_4C'),
            ( 'j3BaAAAAMAAJ'),
            ( 'Hq5oAAAAMAAJ'),
            ( '2p9lAAAAMAAJ'),
            ( '623uAAAAMAAJ'),
            ( 'nORCDAAAQBAJ'),
            ( 'U0BQDQAAQBAJ'),
            ( 'uzkrAQAAIAAJ'),
            ( 'q5J2AgAAQBAJ'),
            ( 'IrItAAAAYAAJ'),
            ( 'kW8tAAAAIAAJ'),
            ( 'rqlOAQAAIAAJ'),
            ( 'MxMwAAAAYAAJ'),
            ( 'lRXvAAAAMAAJ'),
            ( 'IvM3AQAAIAAJ'),
            ( 'v6UtAQAAIAAJ'),
            ( 'WWocq3eYQjkC'),
            ( 'htZVAAAAMAAJ'),
            ( 'BGRNAAAAYAAJ'),
            ( 'sM0dAQAAIAAJ'),
            ( 'K1AKAQAAIAAJ'),
            ( 'TuYZAAAAMAAJ'),
            ( 'moLDCwAAQBAJ'),
            ( 'auulBAAAQBAJ'),
            ( 'QyRhAgAAQBAJ'),
            ( 'RoZQAgAAQBAJ'),
            ( 'lGQdBAAAQBAJ'),
            ( 'SF33AgAAQBAJ'),
            ( '8FFfAAAAcAAJ'),
            ( 'tlx3BgAAQBAJ'),
            ( 'L35VAAAAMAAJ'),
            ( 'K4v1AgAAQBAJ'),
            ( 'HMAtAAAAYAAJ'),
            ( 'UKtTAgAAQBAJ'),
            ( 'NTodAQAAIAAJ'),
            ( '50ktAAAAYAAJ'),
            ( 'RWstAAAAYAAJ'),
            ( 'MeJmAAAAMAAJ'),
            ( '-Gt3yA_cEmwC'),
            ( 'kl33AgAAQBAJ'),
            ( 'wzOLBAAAQBAJ'),
            ( 'zq8tAAAAYAAJ'),
            ( 'RVz3AgAAQBAJ'),
            ( '941aAAAAMAAJ'),
            ( '5TwuAAAAYAAJ'),
            ( 'xkIYAQAAIAAJ'),
            ( '9DVdbl5MDlYC'),
            ( 'P75lAAAAMAAJ'),
            ( 'otTtAAAAMAAJ'),
            ( 'mWloAAAAMAAJ'),
            ( 'm40eAQAAIAAJ'),
            ( 'uX0fAAAAMAAJ'),
            ( 'otFLAAAAMAAJ'),
            ( 'b3czAQAAIAAJ'),
            ( 'OW-wZ140X1cC'),
            ( 'bzstAAAAYAAJ'),
            ( '34GBAAAAMAAJ'),
            ( 'i3LuAAAAMAAJ'),
            ( '7DktAAAAIAAJ'),
            ( 'JWUQAgAAQBAJ'),
            ( 'jchGhiv9y7UC'),
            ( 'YSjaAQAAQBAJ'),
            ( 'fgWhDwAAQBAJ'),
            ( '8_krAAAAYAAJ'),
            ( 'eNcBCwAAQBAJ'),
            ( 'co9VAAAAMAAJ'),
            ( '0JJ2AgAAQBAJ'),
            ( '0qstAAAAYAAJ'),
            ( '_vsbAQAAMAAJ'),
            ( 'kQMrAQAAMAAJ'),
            ( 'oS3PCwAAQBAJ'),
            ( 'bxsRAQAAMAAJ'),
            ( '7WUQAgAAQBAJ'),
            ( 'qPCeDQAAQBAJ'),
            ( 'yMktAAAAYAAJ'),
            ( 'GumjDwAAQBAJ'),
            ( 'vlooAQAAIAAJ'),
            ( 'c6UtAAAAYAAJ'),
            ( '5_48DgAAQBAJ'),
            ( 'M5cfAQAAIAAJ'),
            ( 'i4gwAQAAIAAJ'),
            ( 'IoZNDAAAQBAJ'),
            ( 'tSogAQAAQBAJ'),
            ( '_Ub7AwAAQBAJ'),
            ( 'ObgtAAAAYAAJ'),
            ( 'nP0WAQAAIAAJ'),
            ( 'YUATAQAAMAAJ'),
            ( 'Sm_BBAAAQBAJ'),
            ( '9GrBBAAAQBAJ'),
            ( 'B7EBeDesoWcC'),
            ( '-GK5Yq5m7nIC'),
            ( 'NrD8AgAAQBAJ'),
            ( '1vyM4XmEaikC'),
            ( 'Kg6cBAAAQBAJ'),
            ( 'wPuEBAAAQBAJ'),
            ( 'CwaABAAAQBAJ'),
            ( 'mO-ZBAAAQBAJ'),
            ( 'FFyiAgAAQBAJ'),
            ( 'ziVFDwAAQBAJ'),
            ( '0NQuAAAAYAAJ'),
            ( 'y5VwEAAAQBAJ'),
            ( 'Q9s1DwAAQBAJ'),
            ( '6oEFAQAAIAAJ'),
            ( 'n-4x3NBYZAQC'),
            ( 'lWlODwAAQBAJ'),
            ( 'Q0pECgAAQBAJ'),
            ( 'oFnyDwAAQBAJ'),
            ( 'EpzeDwAAQBAJ'),
            ( 'tyF6DwAAQBAJ'),
            ( 'DketHVzvmkoC'),
            ( 'sLhxDwAAQBAJ'),
            ( 'Wpc6AQAAMAAJ'),
            ( 'pMDCCwAAQBAJ'),
            ( 'hG0VAQAAMAAJ'),
            ( 'HQa6m863d2QC'),
            ( 'j30LBgAAQBAJ'),
            ( 'QgkrDQAAQBAJ'),
            ( 'ELRFEAAAQBAJ'),
            ( 'b-Y8BAAAQBAJ'),
            ( 't_w6DwAAQBAJ'),
            ( 'NvZyDgAAQBAJ'),
            ( 'W2dnDwAAQBAJ'),
            ( 'Ih9WCgAAQBAJ'),
            ( 'TtaaDwAAQBAJ'),
            ( 'EU21DgAAQBAJ'),
            ( 'EE6NDwAAQBAJ'),
            ( '_IedCwAAQBAJ'),
            ( '7Ec8AwAAQBAJ'),
            ( 'yTjACQAAQBAJ'),
            ( 'bR2aCwAAQBAJ'),
            ( 'LC8QDgAAQBAJ'),
            ( 'MzVREAAAQBAJ'),
            ( 'rARBkvcn_e8C'),
            ( 'YmyhCwAAQBAJ'),
            ( 'qowEAwAAQBAJ'),
            ( '3qbMDwAAQBAJ'),
            ( 'CmcUDAAAQBAJ'),
            ( 'HASBDAAAQBAJ'),
            ( 'BggKBAAAQBAJ'),
            ( '8h1KEAAAQBAJ'),
            ( 'njezbPXbTBYC'),
            ( '38pqEAAAQBAJ'),
            ( '-jL6T_ZBgwcC'),
            ( 'YLfCBAAAQBAJ'),
            ( '64J4RAAACAAJ'),
            ( 'm1C0zgEACAAJ'),
            ( 'CBTPBAAAQBAJ'),
            ( '8rvxDwAAQBAJ'),
            ( 'Kx96DwAAQBAJ'),
            ( 'CLxxDwAAQBAJ'),
            ( 'FQCIDwAAQBAJ'),
            ( 'Ev08EAAAQBAJ'),
            ( 'JK5xDwAAQBAJ'),
            ( '4cpqEAAAQBAJ'),
            ( 'OHpXDAAAQBAJ'),
            ( '-_MMbijUmTEC'),
            ( 'axyJDwAAQBAJ'),
            ( 'C8R5DwAAQBAJ'),
            ( 'tsbYBgAAQBAJ'),
            ( 'uKmHipKkEMUC'),
            ( 'lfQqEAAAQBAJ'),
            ( 'YZ7tDwAAQBAJ'),
            ( 'YlbdDwAAQBAJ'),
            ( 'EUAgCwAAQBAJ'),
            ( 'n4YPEAAAQBAJ'),
            ( 'hRntAwAAQBAJ'),
            ( 'wDSkDwAAQBAJ'),
            ( 'tFqkzgEACAAJ'),
            ( 'I7BqDwAAQBAJ'),
            ( 'zg4gAwAAQBAJ'),
            ( 'eycGEAAAQBAJ'),
            ( '_o6eDAAAQBAJ'),
            ( '2rFVDwAAQBAJ'),
            ( 'JAxKEAAAQBAJ'),
            ( 'QQCIDwAAQBAJ'),
            ( 'Qn_xDwAAQBAJ'),
            ( 'JdE4BQAAQBAJ'),
            ( 'OP5oDwAAQBAJ'),
            ( 'ENJxDwAAQBAJ'),
            ( 'BP1xDwAAQBAJ'),
            ( 'TQRTBAAAQBAJ'),
            ( 'f8obEAAAQBAJ'),
            ( 'HizRDwAAQBAJ'),
            ( 'BXDczgEACAAJ'),
            ( 'DcN8EAAAQBAJ'),
            ( 'QuhxDwAAQBAJ'),
            ( 'Xbh5DwAAQBAJ'),
            ( 'arVxDwAAQBAJ'),
            ( 'qbwoEAAAQBAJ'),
            ( 'AJ4LAAAAYAAJ'),
            ( 'hVSSzQEACAAJ'),
            ( 'K-j0DwAAQBAJ'),
            ( 'NcV5DwAAQBAJ'),
            ( 'WBTaDAAAQBAJ'),
            ( 'wJl2AgAAQBAJ'),
            ( 'ayv6DwAAQBAJ'),
            ( 'ox_5DwAAQBAJ'),
            ( 'qQtyDwAAQBAJ'),
            ( 'NcNQAAAACAAJ'),
            ( 'ptdxDwAAQBAJ'),
            ( 'MN11EAAAQBAJ'),
            ( 'u7PtDwAAQBAJ'),
            ( 'IrpxDwAAQBAJ'),
            ( 'YpCCULGJ5noC'),
            ( 'cyxKEAAAQBAJ'),
            ( 'JeG_AwAAQBAJ'),
            ( 'cR85EAAAQBAJ'),
            ( 'JLt2DQAAQBAJ'),
            ( 'pDLDDwAAQBAJ'),
            ( 'c1U-EAAAQBAJ'),
            ( '4h9kEAAAQBAJ'),
            ( 'e5hODwAAQBAJ'),
            ( 'PWNRCgAAQBAJ'),
            ( 'qOnXp0r1DhcC'),
            ( 'mnjDCAAAQBAJ'),
            ( 'XQAKBAAAQBAJ'),
            ( 'WeBBCwAAQBAJ'),
            ( '0QxcAAAAMAAJ'),
            ( 'C4YPEAAAQBAJ'),
            ( 'CrplAAAAMAAJ'),
            ( 'pRl6DwAAQBAJ'),
            ( 'my9QEAAAQBAJ'),
            ( 'ckthEAAAQBAJ'),
            ( 'Wz0xEAAAQBAJ'),
            ( '2HJVAAAAMAAJ'),
            ( 'rQm2DwAAQBAJ'),
            ( 'hxFdtwEACAAJ'),
            ( 'bhJjp673R-EC'),
            ( 'fvM8AAAAYAAJ'),
            ( 'HYRNEAAAQBAJ'),
            ( 'sZRRDwAAQBAJ'),
            ( 'n-mnZwEACAAJ'),
            ( 'Ze9pEAAAQBAJ'),
            ( 'k8M1EAAAQBAJ'),
            ( 'VuH8DwAAQBAJ'),
            ( 'Li6yzgEACAAJ'),
            ( 'dFad7J4xdcEC'),
            ( '1UmmAwAAQBAJ'),
            ( '7_BnCwAAQBAJ'),
            ( 'Ed5sqAj0taAC'),
            ( 'ixdOAAAAMAAJ'),
            ( 't_4FEAAAQBAJ'),
            ( 'sQhZAAAAMAAJ'),
            ( '0WE8AAAAQBAJ'),
            ( 'DPDSBAAAQBAJ'),
            ( 'BvH4DAEACAAJ'),
            ( 'OF8QEAAAQBAJ'),
            ( 'mBC8wAEACAAJ'),
            ( '4T-9ygEACAAJ'),
            ( 'HYnboQEACAAJ'),
            ( 'KEgjzAEACAAJ'),
            ( 'Fz75ywEACAAJ'),
            ( 'Ext-EAAAQBAJ'),
            ( 'oPJFzwEACAAJ'),
            ( 'ZIfCugEACAAJ'),
            ( 'vLItAAAAYAAJ'),
            ( 'n-SVtAEACAAJ'),
            ( '_7buAAAAMAAJ'),
            ( 'U3ErkgEACAAJ'),
            ( 'yrXCzgEACAAJ'),
            ( '1Zq_AAAACAAJ'),
            ( 'LyotAAAAIAAJ'),
            ( '56x1AAAAMAAJ'),
            ( 'ePj2MAAACAAJ'),
            ( 'YkUpzgEACAAJ'),
            ( 'c587DwAAQBAJ'),
            ( 'uyG8rQEACAAJ'),
            ( 'Pm4tAAAAYAAJ'),
            ( 'kGztzgEACAAJ'),
            ( '4-lvEAAAQBAJ'),
            ( 'N1ByPgAACAAJ'),
            ( '3Ve8AAAACAAJ'),
            ( 'mE8vzwEACAAJ'),
            ( 'oWj6zQEACAAJ'),
            ( 'QFsLRQAACAAJ'),
            ( 'es1VEAAAQBAJ'),
            ( '9Y24swEACAAJ'),
            ( 'ElScAAAACAAJ'),
            ( 'bFt9EAAAQBAJ'),
            ( 'ULY6zwEACAAJ'),
            ( 'qR18tAEACAAJ'),
            ( 'fk4pwQEACAAJ'),
            ( 'bYQ2DwAAQBAJ'),
            ( 'xMYmygAACAAJ'),
            ( 'Bx6TDwAAQBAJ'),
            ( 'CR6TDwAAQBAJ'),
            ( 'DJhnnQEACAAJ'),
            ( 'x-1bAAAAMAAJ'),
            ( 'uE-LoAEACAAJ'),
            ( 'L9DkmQEACAAJ'),
            ( '6gr8Ix031KYC'),
            ( 'Vb7ZzQEACAAJ'),
            ( 'vDz7wAEACAAJ'),
            ( 'JlRfAAAAMAAJ'),
            ( 'x_J4PgAACAAJ'),
            ( 'mO8JfAEACAAJ'),
            ( 'o1g9PwAACAAJ'),
            ( '4HwQwQEACAAJ'),
            ( 'gfpZDwAAQBAJ'),
            ( 'sKx_zgEACAAJ'),
            ( 'iV4UBAAAQBAJ'),
            ( 'uSEgAQAAQBAJ'),
            ( 'ca5gnQEACAAJ'),
            ( 'g4PnSAAACAAJ'),
            ( 'EuE3SAAACAAJ'),
            ( 'W66qtAEACAAJ'),
            ( 'V-2FPwAACAAJ'),
            ( 'XNrVoAEACAAJ'),
            ( 'o8M4AwAAQBAJ'),
            ( 'HPalBAAAQBAJ'),
            ( 'rzgtAAAAIAAJ'),
            ( 'KT1dJOI2uZ8C'),
            ( 'BdouAAAAYAAJ'),
            ( '7voeAQAAIAAJ'),
            ( 'lgScBQAAQBAJ'),
            ( 'ZVYtAAAAYAAJ'),
            ( 's4M3AQAAMAAJ'),
            ( 'r0EtAAAAYAAJ'),
            ( 'TlItAAAAIAAJ'),
            ( 'd4UwAAAAYAAJ'),
            ( 'YWstAAAAIAAJ'),
            ( 't4JfAAAAMAAJ'),
            ( 'F5csAQAAMAAJ'),
            ( 'GwdXAAAAYAAJ'),
            ( '-90rAAAAYAAJ'),
            ( 'CcoOAQAAIAAJ'),
            ( 'k_A8AAAAYAAJ'),
            ( 'xNQrAAAAYAAJ'),
            ( 'M4wxAQAAIAAJ'),
            ( 'W98VAgAAQBAJ'),
            ( 'sx0OAQAAIAAJ'),
            ( '_5OgAAAAMAAJ'),
            ( 'Hf4qAQAAIAAJ'),
            ( 'yRVTAAAAMAAJ'),
            ( 'QJSVBAAAQBAJ'),
            ( 'q-IdAQAAIAAJ'),
            ( '0Jg6AQAAIAAJ'),
            ( 'mk0KAQAAIAAJ'),
            ( 'BpMtAAAAYAAJ'),
            ( 'rvMiAQAAIAAJ'),
            ( 'zeFTAgAAQBAJ'),
            ( 'MSPtAAAAMAAJ'),
            ( 'fiokAQAAIAAJ'),
            ( 'ERawGnQJcT4C'),
            ( 'MkIuAAAAYAAJ'),
            ( 'bLEtAAAAYAAJ'),
            ( '_6VOAgAAQBAJ'),
            ( 'thHWAAAAMAAJ'),
            ( 'ftBaAAAAMAAJ'),
            ( 'ITozAQAAIAAJ'),
            ( 'fUir-dmkfXUC'),
            ( 'No7QDQAAQBAJ'),
            ( 'M8DuAAAAMAAJ'),
            ( 'FfESBgAAQBAJ'),
            ( '_BA2AAAAIAAJ'),
            ( 'jXstAAAAYAAJ'),
            ( 'SXEOAQAAIAAJ'),
            ( 'pmAgAQAAIAAJ'),
            ( 'Wh5UAAAAYAAJ'),
            ( 'lkJqDwAAQBAJ'),
            ( 'XY0VAQAAMAAJ'),
            ( 'sCoC4BbQNoEC'),
            ( 'MtpVAAAAMAAJ'),
            ( '2WIdBAAAQBAJ'),
            ( 'NvmfBAAAQBAJ'),
            ( 'qzhbAwAAQBAJ'),
            ( 'qRlXAAAAYAAJ'),
            ( '4M4QAAAAYAAJ'),
            ( 'tYwtAAAAYAAJ'),
            ( 'S74uAAAAYAAJ'),
            ( '97TlDAAAQBAJ'),
            ( 'gBRXAAAAYAAJ'),
            ( 'LexcAAAAMAAJ'),
            ( 'QF1gAAAAMAAJ'),
            ( 'XJstAAAAYAAJ'),
            ( 'HIuaBAAAQBAJ'),
            ( 'Dj42AAAAIAAJ'),
            ( 'recwAQAAIAAJ'),
            ( 'DTfACQAAQBAJ'),
            ( 'gvpXBgAAQBAJ'),
            ( 'uiS5AAAAIAAJ'),
            ( 'lQduDwAAQBAJ'),
            ( 'lgDen5jIGdcC'),
            ( '-LEtAAAAYAAJ'),
            ( 'QUNTAAAAMAAJ'),
            ( 'euVCDAAAQBAJ'),
            ( '2IRfAAAAMAAJ'),
            ( '5ClPCwAAQBAJ'),
            ( 'vpUrDQAAQBAJ'),
            ( 'WWEUAAAAIAAJ'),
            ( 'G5QtAAAAYAAJ'),
            ( '0FBfAAAAMAAJ'),
            ( 'BcXfBgAAQBAJ'),
            ( '1J1dAAAAMAAJ'),
            ( 'kYktAAAAYAAJ'),
            ( 'kfhVAgAAQBAJ'),
            ( 'PQYrAQAAMAAJ'),
            ( 'K9JSCwAAQBAJ'),
            ( 'ADouDwAAQBAJ'),
            ( '-HctAAAAYAAJ'),
            ( 't5VnAAAAMAAJ'),
            ( 'OngtAAAAYAAJ'),
            ( '6u0PAQAAIAAJ'),
            ( 'h6czAQAAIAAJ'),
            ( 'WjYlCwAAQBAJ'),
            ( 'dURQAAAAMAAJ'),
            ( 'ilkOAQAAMAAJ'),
            ( '_CMTAQAAMAAJ'),
            ( 'LysTAQAAMAAJ'),
            ( '30cTAQAAMAAJ'),
            ( 'Zk60AwAAQBAJ'),
            ( 'pnhfAAAAMAAJ'),
            ( 'hvUeAQAAMAAJ'),
            ( 'bc8XAAAAIAAJ'),
            ( 'JH4YAQAAIAAJ'),
            ( 'iIy_DAAAQBAJ'),
            ( 'gAQsAQAAIAAJ'),
            ( 'WatnVhpk6U4C'),
            ( '7dXRAAAAMAAJ'),
            ( 'sp8tAAAAYAAJ'),
            ( 'uV08AAAAYAAJ'),
            ( 'b0UYAAAAYAAJ'),
            ( 'sUrHPj_jclwC'),
            ( '5vx8BAAAQBAJ'),
            ( '5GP26y_xAc0C'),
            ( 'Vb2nCQAAQBAJ'),
            ( 'g68tAAAAYAAJ'),
            ( 'SIqfAAAAMAAJ'),
            ( 'DVYVAQAAMAAJ'),
            ( 'A5QtAAAAIAAJ'),
            ( 'SBuMDwAAQBAJ'),
            ( '7DQuAAAAYAAJ'),
            ( 'VXYDAAAAQBAJ'),
            ( '1jNTAAAAMAAJ'),
            ( 'cb6NBAAAQBAJ'),
            ( 'dt4MAAAAYAAJ'),
            ( 'KBc5AQAAIAAJ'),
            ( 'bGMNAQAAIAAJ'),
            ( 'xKJtAAAAIAAJ'),
            ( 'osQtAAAAYAAJ'),
            ( 'PjtnAAAAMAAJ'),
            ( 'X-C2AAAAIAAJ'),
            ( 'OPkdAQAAIAAJ'),
            ( 'SRi9DwAAQBAJ'),
            ( 'aucaAQAAIAAJ'),
            ( 'vOUbAAAAMAAJ'),
            ( 'rhrPBAAAQBAJ'),
            ( 'mBQGBAAAQBAJ'),
            ( '1ettAwAAQBAJ'),
            ( 'B3lABAAAQBAJ'),
            ( 'AXQIAAAAQAAJ'),
            ( 'v0YDAwAAQBAJ'),
            ( 'jwFSzBjjwoUC'),
            ( 'H7u2BAAAQBAJ'),
            ( 'gATPAgAAQBAJ'),
            ( 'CDE_S20T1R4C'),
            ( 'N6qwDQAAQBAJ'),
            ( 'WwCIDwAAQBAJ'),
            ( 'lcA4SGIdxCUC'),
            ( 'DJMwAAAAYAAJ'),
            ( 'usdcAAAAMAAJ'),
            ( '3CWy4bklp4YC'),
            ( 'M2PKAgAAQBAJ'),
            ( 'jMm_BAAAQBAJ'),
            ( 'rBOHBAAAQBAJ'),
            ( 'q2rjDwAAQBAJ'),
            ( 'LAt0mAWKbBMC'),
            ( 'qBIeEAAAQBAJ'),
            ( '5z1OEAAAQBAJ'),
            ( 'XhjuAgAAQBAJ'),
            ( '32riDwAAQBAJ'),
            ( 'BiMTBAAAQBAJ'),
            ( 'TUuGAAAAQBAJ'),
            ( 'I3sYAAAAYAAJ'),
            ( 'ShMrAAAAIAAJ'),
            ( 'UGEzAQAAIAAJ'),
            ( 'v3gtAAAAYAAJ'),
            ( 'YGZYAAAAMAAJ'),
            ( 'QPQdAQAAIAAJ'),
            ( 'HgEbAQAAIAAJ'),
            ( 'm4onAQAAIAAJ'),
            ( 'pSsrAQAAIAAJ'),
            ( 'xoTvDwAAQBAJ'),
            ( 'uZBVAAAAMAAJ'),
            ( 'FvNJDwAAQBAJ'),
            ( 'HawkAAAAMAAJ'),
            ( 'dFAkAAAAMAAJ'),
            ( '24IqAQAAIAAJ'),
            ( 'UpCkPvlPffYC'),
            ( 'DFpBEAAAQBAJ'),
            ( 'H5pBDwAAQBAJ'),
            ( 'hXitBAAAQBAJ'),
            ( 'N49QzQEACAAJ'),
            ( 'a-gCxJPjXoIC'),
            ( 'j6W5zgEACAAJ'),
            ( 'w6kkCgAAQBAJ'),
            ( '8HBoQYXLYakC'),
            ( 'ErpZEAAAQBAJ'),
            ( 'HdMHEAAAQBAJ'),
            ( '1UAwDgAAQBAJ'),
            ( 'IdMHEAAAQBAJ'),
            ( '9sL4DwAAQBAJ'),
            ( '-X9GEAAAQBAJ'),
            ( '80RKDwAAQBAJ'),
            ( 'p3IOAQAAIAAJ'),
            ( 'UwCIDwAAQBAJ'),
            ( 'ciNFDwAAQBAJ'),
            ( 'uhVKEAAAQBAJ'),
            ( 'FJzeDwAAQBAJ'),
            ( 'mlmNN8OA2MgC'),
            ( '4SITBAAAQBAJ'),
            ( 'F-0EEAAAQBAJ'),
            ( 'aslxDwAAQBAJ'),
            ( 'CYHQDwAAQBAJ'),
            ( 'Qd4NEAAAQBAJ'),
            ( 'rhVKEAAAQBAJ'),
            ( '1xR6DwAAQBAJ'),
            ( 'KSBQAAAAMAAJ'),
            ( 'VuRxDwAAQBAJ'),
            ( '3diuDAAAQBAJ'),
            ( 'cm6ODwAAQBAJ'),
            ( '2Jf9DwAAQBAJ'),
            ( 'tBVKEAAAQBAJ'),
            ( 'RSWVDwAAQBAJ'),
            ( 'jpDULFH8K5cC'),
            ( 'CnOi307r6CUC'),
            ( 'dMZxEAAAQBAJ'),
            ( 'uwQpEAAAQBAJ'),
            ( '_LpxDwAAQBAJ'),
            ( '13CODwAAQBAJ'),
            ( '41MOAQAAMAAJ'),
            ( 'fKgPEAAAQBAJ'),
            ( 'OvOnAgAAQBAJ'),
            ( 'dtNsEAAAQBAJ'),
            ( 'ltMuEAAAQBAJ'),
            ( 'CRdoEAAAQBAJ'),
            ( 'DSBJEAAAQBAJ'),
            ( 'wc0ovgAACAAJ'),
            ( '57a2kT7b754C'),
            ( 'cG6ODwAAQBAJ'),
            ( 'sQMtDwAAQBAJ'),
            ( 'ydhAAQAAIAAJ'),
            ( 'M3V5CgAAQBAJ'),
            ( 'z3UjEAAAQBAJ'),
            ( 'StpxDwAAQBAJ'),
            ( 'UloeAQAAIAAJ'),
            ( 'IA96DwAAQBAJ'),
            ( 'ODCbCgAAQBAJ'),
            ( 'taqzzgEACAAJ'),
            ( 'cBsmDwAAQBAJ'),
            ( 'cS4rAQAAMAAJ'),
            ( 'S3XKSGxpvfoC'),
            ( '1P19DwAAQBAJ'),
            ( 'OxvbzgEACAAJ'),
            ( 'YZc5EAAAQBAJ'),
            ( '4fN7DwAAQBAJ'),
            ( 'UuiYDwAAQBAJ'),
            ( 'JH48EAAAQBAJ'),
            ( 'Q8F5DwAAQBAJ'),
            ( 'grkNBQAAQBAJ'),
            ( 'Y1anDwAAQBAJ'),
            ( 'McErEAAAQBAJ'),
            ( 'p968DgAAQBAJ'),
            ( 'ngxKEAAAQBAJ'),
            ( 'BAgREAAAQBAJ'),
            ( 'lsY5EAAAQBAJ'),
            ( 'ekEvEAAAQBAJ'),
            ( 'dZ4tAAAAYAAJ'),
            ( 'ciITBAAAQBAJ'),
            ( 'MAzkDAAAQBAJ'),
            ( 'nuDyIvCizIcC'),
            ( 'PqktAAAAYAAJ'),
            ( 'esZxEAAAQBAJ'),
            ( 'dswpEAAAQBAJ'),
            ( '0UQBQgAACAAJ'),
            ( 'fakWEAAAQBAJ'),
            ( 'eG6ODwAAQBAJ'),
            ( 'sNdxDwAAQBAJ'),
            ( 'K12HDwAAQBAJ'),
            ( '75VwEAAAQBAJ'),
            ( '1S8PAQAAQBAJ'),
            ( 'Y2ERBAAAQBAJ'),
            ( 'T1WbBAAAQBAJ'),
            ( 'lugJCcFzewYC'),
            ( 'BJkk7U39jq4C'),
            ( 'mkYDAwAAQBAJ'),
            ( 'tn5tAwAAQBAJ'),
            ( 'OU6rH5qebpgC'),
            ( 'VzS9REv1OUcC'),
            ( 'nIWMAgAAQBAJ'),
            ( 'Q3VdBAAAQBAJ'),
            ( 'DZhQAgAAQBAJ'),
            ( 'SvmlBAAAQBAJ'),
            ( 'rZbDBAAAQBAJ'),
            ( '7k1yDwAAQBAJ'),
            ( 'Uqz5zgEACAAJ'),
            ( 'dOmwzgEACAAJ'),
            ( 'YIMtAAAAYAAJ'),
            ( 'SYtyEAAAQBAJ'),
            ( 'TtpxDwAAQBAJ'),
            ( 'bEumAwAAQBAJ'),
            ( 'F-1wDwAAQBAJ'),
            ( '4OX0DwAAQBAJ'),
            ( 'dWQz5A7zr7oC'),
            ( 'g9LuAAAAMAAJ'),
            ( '1ZBXDgAAQBAJ'),
            ( 'nCAvEAAAQBAJ'),
            ( '_e3rDwAAQBAJ'),
            ( 'VWQOAQAAMAAJ')
    ''')


def downgrade():
    op.execute('DELETE FROM book WHERE 1=1')
