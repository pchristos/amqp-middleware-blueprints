from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

import os
import shutil


ctx.download_resource(
    os.path.join('tasks', 'utils.py'),
    os.path.join(os.path.dirname(__file__), 'utils.py')
)


from utils import run_command
from utils import SystemController


systemctl = SystemController('amqp-middleware')

systemctl.execute('disable')
systemctl.execute('delete')
systemctl.execute('reload')

if inputs['remove_source']:
    ctx.logger.info('Removing AMQP Middleware directory')
    shutil.rmtree('/opt/amqp-middleware')