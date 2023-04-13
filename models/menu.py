# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Schedules'), False, URL('regcont', 'schedules'), []),
    (T('Add Scehdule'), False, URL('regcont', 'addSchedule'), []),
    (T('Courses'), False, URL('regcont', 'courses'), []),
    (T('Add Course'), False, URL('regcont', 'addCourse'), []),


]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        
    ]

