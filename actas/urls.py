from django.conf.urls import url

from .views import index, lista, acta_base, subir, subir_validar, subir_confirmar,bajar_propuestas, \
    bajar_datos,bajar_propuesta_docx, mostrar_acta, enviar_pre_propuesta_docx,bajar_propuestas_cires,\
    lista_propuestas, bajar_encuentros_cires, bajar_participantes_cires, bajar_resumen

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^lista/$', lista, name='lista'),
    url(r'^lista/propuestas$', lista_propuestas, name='propuestas'),
    url(r'^base/(?P<id>\d+)$', acta_base, name='base'),
    url(r'^subir/$', subir, name='subir'),
    url(r'^subir/validar$', subir_validar, name='validar'),
    url(r'^subir/confirmar$', subir_confirmar, name='confirmar'),
    url(r'^bajar/(?P<string>\w+)/$', bajar_datos, name='bajar_propuestas'),
    url(r'^bajarpropuestadocx/(?P<uuid>\w+)/$', bajar_propuesta_docx, name='bajar_propuesta_docx'),
    url(r'^mostrarActa$', mostrar_acta, name='mostrar_acta'),
    url(r'^enviarprepropuesta$', enviar_pre_propuesta_docx, name='enviar_pre_propuesta_docx'),
    url(r'^bajarpropuestascires$', bajar_propuestas_cires, name='bajar_propuestas_cires'),
    url(r'^bajarencuentroscires$', bajar_encuentros_cires, name='bajar_encuentros_cires'),
    url(r'^bajarparticipantescires$', bajar_participantes_cires, name='bajar_participantes_cires'),
    url(r'^bajarresumen$', bajar_resumen, name='bajar_resumen')

]
