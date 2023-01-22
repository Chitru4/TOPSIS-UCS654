from distutils.core import setup
setup(
  name = 'TOPSIS',         # How you named your package folder (MyLib)
  packages = ['TOPSIS'],   # Choose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library is used to run TOPSIS on given data to rank items',   # Give a short description about your library
  author = 'Chitraksh Kumar',                   # Type in your name
  author_email = 'chitraksh24@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Chitru4/TOPSIS-UCS654', 
  download_url = 'https://github.com/Chitru4/TOPSIS-UCS654/archive/refs/tags/v_0.1.tar.gz',   
  keywords = ['TOPSIS', 'RANKING', 'PROJECT', 'UCS654'],   # Keywords that define your package best
  install_requires=[           
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)