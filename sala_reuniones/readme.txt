
Se trabajo con codigo escrito en ingles:

State = Estado de la sala reuniones
Meeting Room = Sala de reuniones
Book meeting room = Reserva de sala reuniones
Employee = empleado
company = Empresa
supply = Insumos 

Usuarios:

administrador:

name: admin
password: test1234


usuarios o empleados:

usuario: julio
clave: test1234

Using the URLconf defined in sala_reuniones.urls, Django tried these URL patterns, in this order:


urls disponibles: 


^schema/$
^admin/
^ ^api/v1/ ^state/$ [name='state-list']
^ ^api/v1/ ^state\.(?P<format>[a-z0-9]+)/?$ [name='state-list']
^ ^api/v1/ ^state/(?P<pk>[^/.]+)/$ [name='state-detail']
^ ^api/v1/ ^state/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='state-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^ ^api/v1/ ^supply/$ [name='supply-list']
^ ^api/v1/ ^supply\.(?P<format>[a-z0-9]+)/?$ [name='supply-list']
^ ^api/v1/ ^supply/(?P<pk>[^/.]+)/$ [name='supply-detail']
^ ^api/v1/ ^supply/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='supply-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^ ^api/v1/ ^meetingroom/$ [name='meetingroom-list']
^ ^api/v1/ ^meetingroom\.(?P<format>[a-z0-9]+)/?$ [name='meetingroom-list']
^ ^api/v1/ ^meetingroom/(?P<pk>[^/.]+)/$ [name='meetingroom-detail']
^ ^api/v1/ ^meetingroom/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='meetingroom-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^ ^api/v1/ ^bookmeetingroom/$ [name='bookmeetingroom-list']
^ ^api/v1/ ^bookmeetingroom\.(?P<format>[a-z0-9]+)/?$ [name='bookmeetingroom-list']
^ ^api/v1/ ^bookmeetingroom/(?P<pk>[^/.]+)/$ [name='bookmeetingroom-detail']
^ ^api/v1/ ^bookmeetingroom/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='bookmeetingroom-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^ ^api/v1/ ^company/$ [name='company-list']
^ ^api/v1/ ^company\.(?P<format>[a-z0-9]+)/?$ [name='company-list']
^ ^api/v1/ ^company/(?P<pk>[^/.]+)/$ [name='company-detail']
^ ^api/v1/ ^company/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='company-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^ ^api/v1/ ^register/$ [name='register-list']
^ ^api/v1/ ^register\.(?P<format>[a-z0-9]+)/?$ [name='register-list']
^ ^api/v1/ ^register/(?P<pk>[^/.]+)/$ [name='register-detail']
^ ^api/v1/ ^register/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='register-detail']
^ ^api/v1/ ^users/$ [name='users-list']
^ ^api/v1/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='users-list']
^ ^api/v1/ ^users/(?P<pk>[^/.]+)/$ [name='users-detail']
^ ^api/v1/ ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='users-detail']
^ ^api/v1/ ^$ [name='api-root']
^ ^api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
^api-auth/
