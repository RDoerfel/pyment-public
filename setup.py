from setuptools import setup

setup(name='pyment',
      version='1.0',
      description='Deep learning models for neuroimaging data',
      author='Esten H. Leonardsen',
      author_email='estenhl@psykologi.uio.no',
      url='https://github.com/estenhl/pyment-public',
      packages=['pyment'],
      python_requieres='3.9',
      install_requires=[
            'jupyterlab==3.2.1',
            'matplotlib==3.4.3',
            'mock==4.0.3',
            'nibabel==3.2.1',
            'pandas==1.3.4',
            'pytest==6.2.4',
            'requests==2.25.1',
            'scikit-learn==0.24.2',
            'tqdm==4.61.1',
            'xlrd==2.0.1',
            'tensorflow==2.9.1'
      ])
