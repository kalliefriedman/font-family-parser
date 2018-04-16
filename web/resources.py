'''App Resources classes'''
from flask import request
from flask_restful import (
    abort,
    Resource,
    fields,
)
import re
import requests


def parse_families(data):
    indexes = [a.end() for a in list(re.finditer(r'{font-family:', data))]
    inline_font_fams = []
    for index in indexes:
        inline_font_fams.append(',')
        while (data[index] != '}') and (data[index] != ';'):
            inline_font_fams.append(data[index])
            index = index + 1
    inline_font_fams = ''.join(inline_font_fams)
    return [ x for x in inline_font_fams.split(',') if x ]

def get_stylesheet_families(url, data):
    stylesheet_font_fams = []
    substrings = re.findall(r'href="(.*?).css"', data)
    for string in substrings:
        try:
            data = requests.get(str(url + string + '.css')).text
            stylesheet_font_fams = parse_families(data) + stylesheet_font_fams
        except:
            pass
    return stylesheet_font_fams


class FontExtractionResource(Resource):
    '''Extraction Resource'''
    def get(self):
        url = request.args.get('url')
        data = requests.get(str(url)).text
        if not data:
            abort(404, message='URL content does not exist')
        font_families = parse_families(data)
        font_families = get_stylesheet_families(url, data) + font_families
        font_families = [ item.replace('/', '').replace('\"', '').lstrip().rstrip().strip('\'') for item in font_families ]
        font_families = list(set(font_families))
        return {'font_families': font_families}



