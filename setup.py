from setuptools import setup
with open("README.md", "r") as fh:
      long_description = fh.read()
setup(name='insight-api',
      version='0.2',
      description='InSight Mars Mission Raw Photo API Wrapper',
      url='http://github.com/konradit/insight-api',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Konrad Iturbe',
      author_email='mail@chernowii.com',
      packages=['insightmars'],
      zip_safe=False)

