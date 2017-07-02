import os
from setuptools import setup

# ensure the .customize_rc_files.json file exists

HOME_DIR = os.environ['HOME']
CUSTOMIZE_RC_FILES = HOME_DIR + '.customize_rc_files.json'
if not os.path.exists(CUSTOMIZE_RC_FILES):
    with open(CUSTOMIZE_RC_FILES, 'w') as rcf:
        if os.environ.get('EDITOR'):
            rcf.write('{"_customize_default_editor": "%s"}' % os.environ['EDITOR'])
        else:
            rcf.write('{}')


setup(
    name='customize',
    version='0.0.1',
    description='Simple CLI to ease editing .rc files',
    author='Ed Minnix',
    author_email='egregius313@gmail.com',
    install_requires=['docopt==0.6.2']
)
