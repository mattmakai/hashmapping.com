run:
	pelican -t theme -s settings.py -o s3site content
	cp -R static-html/* s3site/
	cp s3site/pages/* s3site/
	rm -rf s3site/pages/

init:
	pip install -r requirements.txt
