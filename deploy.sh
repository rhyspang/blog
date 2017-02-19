#!/bin/bash
cd ..
mv blog/ blog_h/
git clone https://github.com/rhyspang/blog.git
virtualenv blog/venv
. venv/bin/activate
pip install -r requirements.txt
python blog/manager.py collectstatic
cp -r blog_h/media blog/
cp blog_h/blog_uwsgi.ini blog/
uwsgi blog/blog_uwsgi.ini

