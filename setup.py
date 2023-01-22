from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'Topsis-Chitraksh-102017040',        
  packages = ['Topsis-Chitraksh-102017040'],   
  version = '0.1',      
  license='MIT',        
  description = 'This library is used to run TOPSIS on given data to rank items',   
  author = 'Chitraksh Kumar',                   
  author_email = 'chitraksh24@gmail.com',      
  url = 'https://github.com/Chitru4/Topsis-Chitraksh-102017040', 
  download_url = 'https://github.com/Chitru4/Topsis-Chitraksh-102017040/archive/refs/tags/v_0.1.tar.gz',   
  keywords = ['TOPSIS', 'RANKING', 'PROJECT', 'UCS654'],   
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