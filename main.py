#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#import webapp2
from bottle import default_app, route, error, redirect, request, debug
from jinja2 import Environment, FileSystemLoader
from os.path import abspath
import sys
tempenv = abspath(__file__)
JINJA_ENV = Environment(
    loader=FileSystemLoader(tempenv[:tempenv.rfind('/')] + '/tmpls/'),
    extensions=['jinja2.ext.autoescape'])


@route('/')
def root():
  redirect('/characters')


@route('/characters')
def characters():
  try:
    query = request.query.get('character', '')
    page_title = 'Sod The Quest'
    tpl = JINJA_ENV.get_template('base-template.tpl')
  except:
    print ("EXCEPTION CAUGHT!")
    print ("{}".format(sys.exc_info()[0]))
    return
  return tpl.render(page_title=page_title, query=query)


@route('/create_character')
def create_character():
    try:
      page_title = 'STQ - Character Creation'
      tpl = JINJA_ENV.get_template('create-character.tpl')
    except:
      print ("EXCEPTION CAUGHT!")
      print ("{}".format(sys.exc_info()[0]))
      return
    return tpl.render(page_title=page_title)

app = default_app()
