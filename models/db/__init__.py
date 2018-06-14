from . import database
from . import element
from . import page

connection = database.connection
connect = database.connect
disconnect = database.disconnect

select_element = element.select
select_element_by_page_id = element.select_by_page_id
element = element.Element
select_page = page.select
page = page.Page