from os import getcwd

class Constants:
    _PathSHP_ = getcwd() + '/api_distance_public_transportation/SHPs/'
    _CRS_ = 'EPSG:5072'
    _SHP_ = {'estacao_metro': _PathSHP_ + 'SAD69-96_SHP_estacaometro/SAD69-96_SHP_estacaometro_point.shp',
             'estacao_trem': _PathSHP_ + 'SAD69-96_SHP_estacaotrem/SAD69-96_SHP_estacaotrem.shp',
             'ponto_onibus': _PathSHP_ + 'SAD69-96_SHP_pontoonibus/SAD69-96_SHP_pontoonibus.shp',
             'terminal_onibus': _PathSHP_ + 'terminal_onibus/sad6996_terminal_onibus.shp',
             }