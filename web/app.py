'''Application Initialization'''
import logging

from flask import Flask
from flask_restful import (
    Resource,
    Api,
)
from resources import FontExtractionResource

app = Flask(__name__)

api = Api(app)
api.add_resource(FontExtractionResource, '/font_extraction', endpoint='font_extraction')


if __name__ == '__main__':
    '''Initialize app and run server'''
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug(app.config.get('DEBUG'))
    app.run(debug=True, host='0.0.0.0')