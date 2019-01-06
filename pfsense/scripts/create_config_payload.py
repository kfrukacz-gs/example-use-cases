
import yaml
from cloudify import ctx

NEW_CONFIG_PATH = 'resources/config.json'

ctx.logger.info('Creating the runtime property pfsense_new_config')
pfsense_config = ctx.download_resource(NEW_CONFIG_PATH)

with open(pfsense_config) as pfsense_config_file:
    pfsense_config_data = yaml.safe_load(pfsense_config_file)

ctx.instance.runtime_properties['pfsense_new_config'] = pfsense_config_data
ctx.logger.info('The value of pfsense_config_data is: {0}'
                .format(pfsense_config_data))
