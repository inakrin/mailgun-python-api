from distutils.core import setup

setup(name='mailgunapi-client',
      version='1.24',
      description='Python Wrapper around MailGun HTTP API Upgraded',
      author='Zach Goldberg',
      author_email='zach@zachgoldberg.com',
      url='https://github.com/betao-dev/mailgun-python-api',
      packages=[
          'mailgun',
          ],
      package_dir={
        'mailgun': 'mailgun/',
        },
      install_requires=[
        'requests',
          ],
      )
