import os
import os.path

import ecs_logging

LOG_FILENAME = os.getenv('LOG_FILENAME', 'log/logs.json')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

log_dir = os.path.dirname(LOG_FILENAME)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


LOGGING = {
    'version': 1,
    'formatters': {
        'default': {'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'},
        'ecs_logging': {
            '()': ecs_logging.StdlibFormatter,
        },
    },
    'handlers': {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
        },
        'web': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILENAME,
            'when': 'h',
            'interval': 1,
            'backupCount': 5,
            'formatter': 'ecs_logging',
        }
    },
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['web', 'default']
    }
}
