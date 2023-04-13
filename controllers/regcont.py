

def addSchedule():

	form = SQLFORM(db.courseSchedules)

	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'

	return dict(form=form)

def schedules():

	grid = SQLFORM.grid(db.courseSchedules, csv=False)

	return dict(grid=grid)


def addCourse():

	form = SQLFORM(db.courses)

	if form.process().accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'

	return dict(form=form)

def courses():

	grid = SQLFORM.grid(db.courses)

	return dict(grid=grid)
