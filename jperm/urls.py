from django.conf.urls import patterns, include, url
from jperm.views import *

urlpatterns = patterns('jperm.views',
                       (r'^rule/$', perm_rule_list),
                       (r'^perm_rule_add/$', perm_rule_add),
                       (r'^perm_rule_detail/$', perm_rule_detail),
                       (r'^perm_rule_edit/$', perm_rule_edit),
                       (r'^perm_rule_delete/$', perm_rule_delete),
                       (r'^role/$', perm_role_list),
                       (r'^role/perm_role_add/$', perm_role_add),
                       (r'^role/perm_role_delete/$', perm_role_delete),
                       (r'^role/perm_role_detail/$', perm_role_detail),
                       (r'^role/perm_role_edit/$', perm_role_edit),
                       (r'^role/push/$', perm_role_push),
                       (r'^role/recycle/$', perm_role_recycle),
                       (r'^role/get/$', perm_role_get),
                       (r'^sudo/$', perm_sudo_list),
                       (r'^sudo/perm_sudo_add/$', perm_sudo_add),
                       (r'^sudo/perm_sudo_delete/$', perm_sudo_delete),
                       (r'^sudo/perm_sudo_edit/$', perm_sudo_edit),
                       )
