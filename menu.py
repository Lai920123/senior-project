from django.utils.translation import gettext as _

from netbox.registry import registry
from . import *

#
# Nav menus
#

ORGANIZATION_MENU = Menu(
    label=_('組織機構'),
    icon_class='mdi mdi-domain',
    groups=(
        MenuGroup(
            label=_('機房'),
            items=(
                get_model_item('dcim', 'site', _('數據中心')),
                get_model_item('dcim', 'region', _('地區')),
                get_model_item('dcim', 'sitegroup', _('數據中心組')),
                get_model_item('dcim', 'location', _('具體地點')),
            ),
        ),
        MenuGroup(
            label=_('機架'),
            items=(
                get_model_item('dcim', 'rack', _('機櫃')),
                get_model_item('dcim', 'rackrole', _('機櫃角色')),
                get_model_item('dcim', 'rackreservation', _('預留')),
                MenuItem(
                    link='dcim:rack_elevation_list',
                    link_text=_('立面圖'),
                    permissions=['dcim.view_rack']
                ),
            ),
        ),
        MenuGroup(
            label=_('租賃'),
            items=(
                get_model_item('tenancy', 'tenant', _('租戶')),
                get_model_item('tenancy', 'tenantgroup', _('租户組')),
            ),
        ),
        MenuGroup(
            label=_('聯繫方式'),
            items=(
                get_model_item('tenancy', 'contact', _('聯繫人')),
                get_model_item('tenancy', 'contactgroup', _('聯繫人组')),
                get_model_item('tenancy', 'contactrole', _('聯繫人角色')),
                get_model_item('tenancy', 'contactassignment', _('聯繫方式分配'), actions=[]),
            ),
        ),
    ),
)

DEVICES_MENU = Menu(
    label=_('設備'),
    icon_class='mdi mdi-server',
    groups=(
        MenuGroup(
            label=_('Devices'),
            items=(
                get_model_item('dcim', 'device', _('設備')),
                get_model_item('dcim', 'module', _('模組')),
                get_model_item('dcim', 'devicerole', _('設備角色')),
                get_model_item('dcim', 'platform', _('平台')),
                get_model_item('dcim', 'virtualchassis', _('虛擬機櫃')),
                get_model_item('dcim', 'virtualdevicecontext', _('Virtual Device Contexts')),
            ),
        ),
        MenuGroup(
            label=_('類型'),
            items=(
                get_model_item('dcim', 'devicetype', _('設備型號')),
                get_model_item('dcim', 'moduletype', _('模組類型')),
                get_model_item('dcim', 'manufacturer', _('製造商')),
            ),
        ),
        MenuGroup(
            label=_('設備組件'),
            items=(
                get_model_item('dcim', 'interface', _('接口')),
                get_model_item('dcim', 'frontport', _('前端口')),
                get_model_item('dcim', 'rearport', _('后端口')),
                get_model_item('dcim', 'consoleport', _('Console 端口')),
                get_model_item('dcim', 'consoleserverport', _('Console 伺服器端口')),
                get_model_item('dcim', 'powerport', _('電源接口')),
                get_model_item('dcim', 'poweroutlet', _('電源插座PDU')),
                get_model_item('dcim', 'modulebay', _('模組架')),
                get_model_item('dcim', 'devicebay', _('設備架')),
                get_model_item('dcim', 'inventoryitem', _('庫存物品')),
                get_model_item('dcim', 'inventoryitemrole', _('庫存項目角色')),
            ),
        ),
    ),
)

CONNECTIONS_MENU = Menu(
    label=_('連接'),
    icon_class='mdi mdi-connection',
    groups=(
        MenuGroup(
            label=_('Connections'),
            items=(
                get_model_item('dcim', 'cable', _('線纜'), actions=['import']),
                get_model_item('wireless', 'wirelesslink', _('無線連接')),
                MenuItem(
                    link='dcim:interface_connections_list',
                    link_text=_('接口連接'),
                    permissions=['dcim.view_interface']
                ),
                MenuItem(
                    link='dcim:console_connections_list',
                    link_text=_('Console 連接'),
                    permissions=['dcim.view_consoleport']
                ),
                MenuItem(
                    link='dcim:power_connections_list',
                    link_text=_('電源連接'),
                    permissions=['dcim.view_powerport']
                ),
            ),
        ),
    ),
)

WIRELESS_MENU = Menu(
    label=_('無線'),
    icon_class='mdi mdi-wifi',
    groups=(
        MenuGroup(
            label=_('Wireless'),
            items=(
                get_model_item('wireless', 'wirelesslan', _('無線區域網')),
                get_model_item('wireless', 'wirelesslangroup', _('無線區域網組')),
            ),
        ),
    ),
)

IPAM_MENU = Menu(
    label=_('IP地址管理'),
    icon_class='mdi mdi-counter',
    groups=(
        MenuGroup(
            label=_('IP Addresses'),
            items=(
                get_model_item('ipam', 'ipaddress', _('IP 地址')),
                get_model_item('ipam', 'iprange', _('IP 範圍')),
            ),
        ),
        MenuGroup(
            label=_('Prefixes'),
            items=(
                get_model_item('ipam', 'prefix', _('IP網段')),
                get_model_item('ipam', 'role', _('網段和VLAN角色')),
            ),
        ),
        MenuGroup(
            label=_('ASNs'),
            items=(
                get_model_item('ipam', 'asnrange', _('ASN Ranges')),
                get_model_item('ipam', 'asn', _('ASNs')),
            ),
        ),
        MenuGroup(
            label=_('Aggregates'),
            items=(
                get_model_item('ipam', 'aggregate', _('Aggregates')),
                get_model_item('ipam', 'rir', _('RIRs')),
            ),
        ),
        MenuGroup(
            label=_('VRFs'),
            items=(
                get_model_item('ipam', 'vrf', _('VRFs')),
                get_model_item('ipam', 'routetarget', _('Route Targets')),
            ),
        ),
        MenuGroup(
            label=_('VLANs'),
            items=(
                get_model_item('ipam', 'vlan', _('VLANs')),
                get_model_item('ipam', 'vlangroup', _('VLAN Groups')),
            ),
        ),
        MenuGroup(
            label=_('Other'),
            items=(
                get_model_item('ipam', 'fhrpgroup', _('FHRP Groups')),
                get_model_item('ipam', 'servicetemplate', _('Service Templates')),
                get_model_item('ipam', 'service', _('Services')),
            ),
        ),
    ),
)

OVERLAY_MENU = Menu(
    label=_('網路虛擬化Overlay'),
    icon_class='mdi mdi-graph-outline',
    groups=(
        MenuGroup(
            label='L2VPNs',
            items=(
                get_model_item('ipam', 'l2vpn', _('L2VPNs')),
                get_model_item('ipam', 'l2vpntermination', _('Terminations')),
            ),
        ),
    ),
)

VIRTUALIZATION_MENU = Menu(
    label=_('虛擬化'),
    icon_class='mdi mdi-monitor',
    groups=(
        MenuGroup(
            label=_('Virtual Machines'),
            items=(
                get_model_item('virtualization', 'virtualmachine', _('虛擬機')),
                get_model_item('virtualization', 'vminterface', _('虛擬機接口')),
            ),
        ),
        MenuGroup(
            label=_('Clusters'),
            items=(
                get_model_item('virtualization', 'cluster', _('虛擬化叢集')),
                get_model_item('virtualization', 'clustertype', _('虛擬化叢集類型')),
                get_model_item('virtualization', 'clustergroup', _('叢集組')),
            ),
        ),
    ),
)

CIRCUITS_MENU = Menu(
    label=_('線路'),
    icon_class='mdi mdi-transit-connection-variant',
    groups=(
        MenuGroup(
            label=_('Circuits'),
            items=(
                get_model_item('circuits', 'circuit', _('線路')),
                get_model_item('circuits', 'circuittype', _('線路類型')),
            ),
        ),
        MenuGroup(
            label=_('Providers'),
            items=(
                get_model_item('circuits', 'provider', _('供應商')),
                get_model_item('circuits', 'provideraccount', _('供應商帳號')),
                get_model_item('circuits', 'providernetwork', _('供應商網路')),
            ),
        ),
    ),
)

POWER_MENU = Menu(
    label=_('電力'),
    icon_class='mdi mdi-flash',
    groups=(
        MenuGroup(
            label=_('Power'),
            items=(
                get_model_item('dcim', 'powerfeed', _('電源線')),
                get_model_item('dcim', 'powerpanel', _('電源插座')),
            ),
        ),
    ),
)

PROVISIONING_MENU = Menu(
    label=_('設備配置'),
    icon_class='mdi mdi-file-document-multiple-outline',
    groups=(
        MenuGroup(
            label=_('Configurations'),
            items=(
                get_model_item('extras', 'configcontext', _('Config Contexts'), actions=['add']),
                get_model_item('extras', 'configtemplate', _('Config Templates'), actions=['add']),
            ),
        ),
    ),
)

CUSTOMIZATION_MENU = Menu(
    label=_('自訂'),
    icon_class='mdi mdi-toolbox-outline',
    groups=(
        MenuGroup(
            label=_('Customization'),
            items=(
                get_model_item('extras', 'customfield', _('自訂字串')),
                get_model_item('extras', 'customlink', _('自訂連結')),
                get_model_item('extras', 'exporttemplate', _('自訂驗證')),
                get_model_item('extras', 'savedfilter', _('已保存的篩選條件')),
                get_model_item('extras', 'tag', 'Tags'),
                get_model_item('extras', 'imageattachment', _('圖片附件'), actions=()),
            ),
        ),
        MenuGroup(
            label=_('Reports & Scripts'),
            items=(
                MenuItem(
                    link='extras:report_list',
                    link_text=_('報告'),
                    permissions=['extras.view_report'],
                    buttons=get_model_buttons('extras', "reportmodule", actions=['add'])
                ),
                MenuItem(
                    link='extras:script_list',
                    link_text=_('腳本'),
                    permissions=['extras.view_script'],
                    buttons=get_model_buttons('extras', "scriptmodule", actions=['add'])
                ),
            ),
        ),
    ),
)

OPERATIONS_MENU = Menu(
    label=_('運營'),
    icon_class='mdi mdi-cogs',
    groups=(
        MenuGroup(
            label=_('Integrations'),
            items=(
                get_model_item('core', 'datasource', _('Data Sources')),
                get_model_item('extras', 'webhook', _('Webhooks')),
            ),
        ),
        MenuGroup(
            label=_('Jobs'),
            items=(
                MenuItem(
                    link='core:job_list',
                    link_text=_('Jobs'),
                    permissions=['core.view_job'],
                ),
            ),
        ),
        MenuGroup(
            label=_('Logging'),
            items=(
                get_model_item('extras', 'journalentry', _('日誌列表'), actions=['import']),
                get_model_item('extras', 'objectchange', _('操作日誌'), actions=[]),
            ),
        ),
    ),
)


MENUS = [
    ORGANIZATION_MENU,
    DEVICES_MENU,
    CONNECTIONS_MENU,
    WIRELESS_MENU,
    IPAM_MENU,
    OVERLAY_MENU,
    VIRTUALIZATION_MENU,
    CIRCUITS_MENU,
    POWER_MENU,
    PROVISIONING_MENU,
    CUSTOMIZATION_MENU,
    OPERATIONS_MENU,
]

#
# Add plugin menus
#

for menu in registry['plugins']['menus']:
    MENUS.append(menu)

if registry['plugins']['menu_items']:

    # Build the default plugins menu
    groups = [
        MenuGroup(label=label, items=items)
        for label, items in registry['plugins']['menu_items'].items()
    ]
    plugins_menu = Menu(
        label=_("Plugins"),
        icon_class="mdi mdi-puzzle",
        groups=groups
    )
    MENUS.append(plugins_menu)

