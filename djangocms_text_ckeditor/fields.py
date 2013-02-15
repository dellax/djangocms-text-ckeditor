from django.db import models
from django.contrib.admin import widgets as admin_widgets
from djangocms_text_ckeditor.html import clean_html
from djangocms_text_ckeditor.widgets import TextEditorWidget


class HTMLField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': TextEditorWidget}
        defaults.update(kwargs)

        # override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = TextEditorWidget

        return super(HTMLField, self).formfield(**defaults)

    def clean(self, value, model_instance):
        value = super(HTMLField, self).clean(value, model_instance)
        return clean_html(value, full=False)