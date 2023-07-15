import meraki
import datetime

# Defining your API key as a variable in source code is not recommended
API_KEY = ''
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

current_time = datetime.datetime.now(datetime.timezone.utc)

maintenance_start = "2023-07-15T08:00:00Z"
maintenance_end = "2023-07-15T12:00:00Z"
maintenance_start = datetime.datetime.fromisoformat(maintenance_start)
maintenance_end = datetime.datetime.fromisoformat(maintenance_end)

print(current_time)

def get_organization_id():
    """
    Retrieves the ID of the first organization that the API key has access to.

    API -> ORG ID

    """
    organizations = dashboard.organizations.getOrganizations()
    organization_id = organizations[0]['id']
    return organization_id


def get_networks(organization_id):
    """
    Retrieves a filtered list of networks within the specified organization.

    ORG ID -> networks[0..*], filtered by ID and NAME

    """
    networks = dashboard.organizations.getOrganizationNetworks(organization_id, total_pages='all')
    filtered_list = [{k: v for k, v in d.items() if k in ['id', 'name']} for d in networks]
    return filtered_list


def get_adminEmail(organization_id):
    """
    Retrieves the ID of the first organization that the API key has access to.

    ORG ID -> admins[0..*], filtered by admin email

    """
    admins = dashboard.organizations.getOrganizationAdmins(organization_id)
    email = [admin['email'] for admin in admins]
    return email


def get_alerts(network_id):
    """
    Retrieves the current alert setting of the specfied network.

    Network ID -> alert settings (CSV of some sort) (dict)

    """
    alerts = dashboard.networks.getNetworkAlertsSettings(network_id)
    return alerts


def turn_off_alerts(email, network_id):

    '''

    network_id -> API payload to be delivered to Meraki API

    email (email[]) -> 0..* alert mutes

    for email in emails[]:
        # change email settings - mute alerts

    '''

    destination = {'emails': email, 'snmp': False, 'allAdmins': False, 'httpServerIds': []}
    payload = [{'type': 'ipConflict',
                'enabled': False,
                'alertDestinations': {
                    'emails': email,
                    'allAdmins': False,
                    'snmp': False,
                    'httpServerIds': ['']},
                'filters': {}}]
    put_alerts = dashboard.networks.updateNetworkAlertsSettings(network_id, defaultDestinations=destination,
                                                                alerts=payload)
    return put_alerts


def alerts_on(email, network_id):

    '''

    INVERSE OF ABOVE

    network_id -> API Payload to be sent to meraki API

    email email[] -> 0..* alert unmutes

    for email in email[]:
        # change email settings - unmute alerts

    '''

    destination = {'emails': email, 'snmp': False, 'allAdmins': True, 'httpServerIds': []}
    alert = [{'type': 'ipConflict', 'enabled': True,
              'alertDestinations': {'emails': email, 'allAdmins': False, 'snmp': False, 'httpServerIds': ['']},
              'filters': {}}]
    put_alerts = dashboard.networks.updateNetworkAlertsSettings(network_id, defaultDestinations=destination,
                                                                alerts=alert)
    return put_alerts

# data members

# Get the ID of the first organization in the list
organization_id = get_organization_id()

# Get a filtered list of networks within the organization, WILL BE USED TO DISPLAY TO THE PAGE
networks = get_networks(organization_id)
network_id = networks[0]['id']  ########THIS IS JUST FOR TESTING WILL HAVE TO TAKE USER INPUT

# Gets a list of admin emails.
email = get_adminEmail(organization_id)

# Get the current alert settings of the first network in the list
# alert_settings = get_alerts(network_id)
# Put the alert settings of the first network in the list TURNS ALERTS OFF
# alert_off = turn_off_alerts(email, network_id)
# Put the alert settings of the first network in the list TURNS ALERTS ON
# alert_on = alerts_on(email, network_id)


if maintenance_start <= current_time <= maintenance_end:
    # If the current time is within the maintenance window, turn off alerts for all networks
    alert_off = turn_off_alerts(email, network_id)
    print(
        f"Alerts have been turned off for all networks during the maintenance window ({maintenance_start} - {maintenance_end}) for network{network_id}.")

if current_time > maintenance_end:
    alert_on = alerts_on(email, network_id)

# print(f"The ID of the organization is {organization_id}")