from distutils.core import setup

setup(name="wiki_scrapper",
      version="0.1",
      author="Krishap S",
      author_email="krishapsreenivasn.s2020@vitstudent.ac.in",
      url="https://github.com/Krishap-s/wiki_scraper",
      package=['package'],
      install_requires=[
          "beautifulsoup4==4.9.3",
          "bs4==0.0.1",
          "certifi==2020.12.5",
          "chardet==4.0.0",
          "idna==2.10",
          "requests==2.25.1",
          "soupsieve==2.1",
          "urllib==1.26.2"],
      short_description = "Wiki Web Scraper",
      long_description="Scraps from wiki page and stores in an object",
      long_description_content_type='text/markdown',
      )
