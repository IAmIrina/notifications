import os
import os.path

import ecs_logging

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


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
            'formatter': 'ecs_logging',
        },
    },
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['default']
    }
}
