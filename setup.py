from distutils.core import setup
setup(
  name = 'Topsis-Chitraksh-102017040',        
  packages = ['Topsis-Chitraksh-102017040'],   
  version = '0.1',      
  license='MIT',        
  description = 'This library is used to run TOPSIS on given data to rank items',   
  author = 'Chitraksh Kumar',                   
  author_email = 'chitraksh24@gmail.com',      
  url = 'https://github.com/Chitru4/TOPSIS-UCS654', 
  download_url = 'https://github.com/Chitru4/TOPSIS-UCS654/archive/refs/tags/v_0.1.tar.gz',   
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