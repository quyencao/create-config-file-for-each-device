import os
import tarfile
import tempfile
from jinja2 import BaseLoader, Environment

def create_config_file(code, host='localhost', port=5672):
    # Templates
    config_template = '''
{
    "code": "{{ CODE }}",
    "host": "{{ HOST }}",
    "port": {{ PORT }}
}
    '''

    config = Environment(loader=BaseLoader()).from_string(config_template)
    config_string = config.render(CODE=code, HOST=host, PORT=port)

    with tempfile.TemporaryDirectory() as directory:
        # Create config.json file
        config_json_file = os.path.join(directory, 'config.json')

        with open(config_json_file, 'w') as c:
            c.write(config_string)

        # Create tar.gz file
        config_tarfile = '{}.tar.gz'.format(code)

        with tarfile.open(config_tarfile, mode='w') as tf:
            tf.add(config_json_file, os.path.join('config', 'config.json'))

if __name__ == "__main__":
    device_code = '12345654321'
    host = 'localhost'
    port = 5642

    create_config_file(device_code, host, port)