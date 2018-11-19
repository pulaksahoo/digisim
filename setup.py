from setuptools import setup
setup(
  name = 'digg6',         # How you named your package folder (MyLib)
  packages = ['digg6'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Digital simulation library!',   # Give a short description about your library
  author = 'Kaif Khan',                   # Type in your name
  author_email = 'kaifkhan.khan0@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/khanstark',   # Provide either the link to your github or to your website
    # I explain this later on
  keywords = ['digital'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 2'
  ],
)
