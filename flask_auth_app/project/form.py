# import statements
from wtforms import Form, SubmitField,StringField, DateField, IntegerField, SelectField, TextAreaField, HiddenField, validators
from wtforms.validators import DataRequired

class entryform(Form):
    #house id selector
    house_num = [('1', '1'),
                 ('2', '2'),
                 ('3', '3'),
                 ('4', '4'),
                 ('5', '5'),
                 ('6', '6'),
                 ('7', '7'),
                 ('8', '8'),
                 ('9', '9'),
                 ('10', '10'),
                 ('11', '11'),
                 ('12', '12'),
                 ('13', '13')]
    #species selector
    species_types = [('Eastern Blue Bird', 'Eastern Blue Bird'),
               ('Tree Swallow', 'Tree Swallow'),
               ('House Wren', 'House Wren'),
               ('Brown-Headed Cowbird', 'Brown-Headed Cowbird'),
               ('Unknown', 'Unknown'),
               ('Other', 'Other')]
    #cowbird selector
    cowbird_select = [('Yes', 'Yes'),
               ('No', 'No')]
    #damage selector
    damaged_select = [('Yes', 'Yes'),
               ('No', 'No')]
    #create form fields
    # houseId selector
    houseId = SelectField('houseId', choices=house_num)
    # date field
    date = DateField('date', format= '%Y-%m-%d', render_kw={"placeholder": "yyyy-mm-dd"})
    # id field
    id = IntegerField('userId', render_kw={"placeholder": "Id Number 0-5"})
    # number of eggs field
    eggs = IntegerField('egg', render_kw={"placeholder": "Num of eggs"})
    # number alive field
    alive = IntegerField('alive', render_kw={"placeholder": "Num alive"})
    # number dead field
    dead = IntegerField('dead', render_kw={"placeholder": "Num dead"})
    # species selector
    species = SelectField('species', choices=species_types)
    # cowbird selector
    cowbird = SelectField('cowbird', choices=cowbird_select)
    # damaged selector
    damaged = SelectField('damaged', choices=damaged_select)
    # comment textarea
    comment = TextAreaField('comment', render_kw={"placeholder": "Enter other species or add comments"})
    # entryId field
    entryId = HiddenField('entryId')
    # submit
    submit = SubmitField('Submit')

#form to edit an entry
class EditEntryForm(Form):
    #entryId field
    entryId = HiddenField('entryId')
    # houseId selector
    houseId = SelectField('houseId' )
    # date field
    date = DateField('date', format='%Y-%m-%d', render_kw={"placeholder": "mm-dd-yyyy"})
    # id field
    id = IntegerField('userId', render_kw={"placeholder": "Id Number 0-5"})
    # number of eggs field
    eggs = IntegerField('egg' ,render_kw={"placeholder": "Num of eggs"})
    # number alive field
    alive = IntegerField('alive', render_kw={"placeholder": "Num alive"})
    # number dead field
    dead = IntegerField('dead', render_kw={"placeholder": "Num dead"})
    # species selector
    species = SelectField('species')
    # cowbird selector
    cowbird = SelectField('cowbird')
    # damaged selector
    damaged = SelectField('damaged')
    # comment textarea
    comment = TextAreaField('comment', render_kw={"placeholder": "Enter other species or add comments"})
    # submit
    submit = SubmitField('Submit')