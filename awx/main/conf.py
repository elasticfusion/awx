# Python
import json
import logging
import os

# Django
from django.utils.translation import ugettext_lazy as _

# Tower
from awx.conf import fields, register

logger = logging.getLogger('awx.main.conf')

register(
    'ACTIVITY_STREAM_ENABLED',
    field_class=fields.BooleanField,
    label=_('Enable Activity Stream'),
    help_text=_('Enable capturing activity for the Tower activity stream.'),
    category=_('System'),
    category_slug='system',
)

register(
    'ACTIVITY_STREAM_ENABLED_FOR_INVENTORY_SYNC',
    field_class=fields.BooleanField,
    label=_('Enable Activity Stream for Inventory Sync'),
    help_text=_('Enable capturing activity for the Tower activity stream when running inventory sync.'),
    category=_('System'),
    category_slug='system',
)

register(
    'ORG_ADMINS_CAN_SEE_ALL_USERS',
    field_class=fields.BooleanField,
    label=_('All Users Visible to Organization Admins'),
    help_text=_('Controls whether any Organization Admin can view all users, even those not associated with their Organization.'),
    category=_('System'),
    category_slug='system',
)

register(
    'TOWER_ADMIN_ALERTS',
    field_class=fields.BooleanField,
    label=_('Enable Tower Administrator Alerts'),
    help_text=_('Allow Tower to email Admin users for system events that may require attention.'),
    category=_('System'),
    category_slug='system',
)

register(
    'TOWER_URL_BASE',
    field_class=fields.URLField,
    schemes=('http', 'https'),
    allow_plain_hostname=True,  # Allow hostname only without TLD.
    label=_('Base URL of the Tower host'),
    help_text=_('This setting is used by services like notifications to render '
                'a valid url to the Tower host.'),
    category=_('System'),
    category_slug='system',
)

register(
    'REMOTE_HOST_HEADERS',
    field_class=fields.StringListField,
    label=_('Remote Host Headers'),
    help_text=_('HTTP headers and meta keys to search to determine remote host '
                'name or IP. Add additional items to this list, such as '
                '"HTTP_X_FORWARDED_FOR", if behind a reverse proxy.\n\n'
                'Note: The headers will be searched in order and the first '
                'found remote host name or IP will be used.\n\n'
                'In the below example 8.8.8.7 would be the chosen IP address.\n'
                'X-Forwarded-For: 8.8.8.7, 192.168.2.1, 127.0.0.1\n'
                'Host: 127.0.0.1\n'
                'REMOTE_HOST_HEADERS = [\'HTTP_X_FORWARDED_FOR\', '
                '\'REMOTE_ADDR\', \'REMOTE_HOST\']'),
    category=_('System'),
    category_slug='system',
)

def _load_default_license_from_file():
    try:
        license_file = os.environ.get('AWX_LICENSE_FILE', '/etc/tower/license')
        if os.path.exists(license_file):
            license_data = json.load(open(license_file))
            logger.debug('Read license data from "%s".', license_file)
            return license_data
    except:
        logger.warning('Could not read license from "%s".', license_file, exc_info=True)
    return {}


register(
    'LICENSE',
    field_class=fields.DictField,
    default=_load_default_license_from_file,
    label=_('Tower License'),
    help_text=_('The license controls which features and functionality are '
                'enabled in Tower. Use /api/v1/config/ to update or change '
                'the license.'),
    category=_('System'),
    category_slug='system',
)

register(
    'AD_HOC_COMMANDS',
    field_class=fields.StringListField,
    label=_('Ansible Modules Allowed for Ad Hoc Jobs'),
    help_text=_('List of modules allowed to be used by ad-hoc jobs.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'AWX_PROOT_ENABLED',
    field_class=fields.BooleanField,
    label=_('Enable job isloation'),
    help_text=_('Isolates an Ansible job from protected parts of the Tower system to prevent exposing sensitive information.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'AWX_PROOT_BASE_PATH',
    field_class=fields.CharField,
    label=_('Job isolation execution path'),
    help_text=_('Create temporary working directories for isolated jobs in this location.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'AWX_PROOT_HIDE_PATHS',
    field_class=fields.StringListField,
    label=_('Paths to hide from isolated jobs'),
    help_text=_('Additional paths to hide from isolated processes.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'AWX_PROOT_SHOW_PATHS',
    field_class=fields.StringListField,
    label=_('Paths to expose to isolated jobs'),
    help_text=_('Whitelist of paths that would otherwise be hidden to expose to isolated jobs.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'STDOUT_MAX_BYTES_DISPLAY',
    field_class=fields.IntegerField,
    min_value=0,
    label=_('Standard Output Maximum Display Size'),
    help_text=_('Maximum Size of Standard Output in bytes to display before requiring the output be downloaded.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'SCHEDULE_MAX_JOBS',
    field_class=fields.IntegerField,
    min_value=1,
    label=_('Maximum Scheduled Jobs'),
    help_text=_('Maximum number of the same job template that can be waiting to run when launching from a schedule before no more are created.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'AWX_ANSIBLE_CALLBACK_PLUGINS',
    field_class=fields.StringListField,
    label=_('Ansible Callback Plugins'),
    help_text=_('List of paths to search for extra callback plugins to be used when running jobs.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'DEFAULT_JOB_TIMEOUT',
    field_class=fields.IntegerField,
    min_value=0,
    default=0,
    label=_('Default Job Timeout'),
    help_text=_('Maximum time to allow jobs to run. Use value of 0 to indicate that no '
                'timeout should be imposed. A timeout set on an individual job template will override this.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'DEFAULT_INVENTORY_UPDATE_TIMEOUT',
    field_class=fields.IntegerField,
    min_value=0,
    default=0,
    label=_('Default Inventory Update Timeout'),
    help_text=_('Maximum time to allow inventory updates to run. Use value of 0 to indicate that no '
                'timeout should be imposed. A timeout set on an individual inventory source will override this.'),
    category=_('Jobs'),
    category_slug='jobs',
)

register(
    'DEFAULT_PROJECT_UPDATE_TIMEOUT',
    field_class=fields.IntegerField,
    min_value=0,
    default=0,
    label=_('Default Project Update Timeout'),
    help_text=_('Maximum time to allow project updates to run. Use value of 0 to indicate that no '
                'timeout should be imposed. A timeout set on an individual project will override this.'),
    category=_('Jobs'),
    category_slug='jobs',
)
