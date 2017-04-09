from django.urls import reverse_lazy
from django.utils.html import escape
from table import Table
from table.utils import A, Accessor
from table.columns import LinkColumn, Link, Column
from .models import Contact

class HrefColumn(Column):
    def render(self, obj):
        text = Accessor(self.field).resolve(obj)
        return '<a href="%s">%s</a>' % (reverse_lazy('edit_contact', kwargs={'pk': A('id').resolve(obj)}), escape(text))

class ContactTable(Table):
    id = Column(field='id', header=u"№", sortable=True)
    name = HrefColumn(field='name', header=u"Прокатчик", sortable=True, searchable=True)
    places = Column(field='places', header=u"Города", sortable=True, searchable=True)
    phones = Column(field='phones', header=u"Телефоны", searchable=True)
    email = Column(field='email', header=u"Email", searchable=True)
    lastevent = Column(field='lastevent', header=u"Последнее событие", searchable=True)
    class Meta:
        model = Contact
        id = 't_contacts'
        attrs = {'class': 'table'}
        search = True
        search_placeholder = u"Найти имя или город"
        info_format = u"Всего _TOTAL_"
        zero_records = u"Нет записей"
        pagination_prev = u"Назад"
        pagination_next = u"Вперед"
        pagination_last = u"Последняя"
        pagination_first = u"Первая"
        ajax = True
        