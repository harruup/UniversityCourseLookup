from wtforms import Form, StringField, TextAreaField, SelectField,SelectMultipleField, SubmitField, validators
#from wtforms.widgets import Input

'''
#Manually created a Button 
class ButtonField(BooleanField):
    widget = Input(input_type = 'button')
'''
class degreeTreeInputForm(Form):
    cinput = StringField()
    coursestaken = SelectMultipleField(choices=[])
    buildbutton = SubmitField(u'Start Building')
    cantakecourse = SelectMultipleField(choices=[])