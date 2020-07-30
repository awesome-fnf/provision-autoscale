# -*- coding: utf-8 -*-

import fc2
import json
import logging

logger = logging.getLogger()


def handler(event, context):
    # Read event params
    logger.info("Process event: %s", event)
    params = json.loads(event)
    service_name = params['serviceName']
    function_name = params['functionName']
    alias = params['alias']
    provision_count = int(params.get('provisionCount', 1))

    # Init fc client
    creds = context.credentials
    client = fc2.Client(
        endpoint='https://{}.{}-internal.fc.aliyuncs.com'.format(context.account_id, context.region),
        accessKeyID=creds.access_key_id,
        accessKeySecret=creds.access_key_secret,
        securityToken=creds.security_token
    )

    # Update provision config
    client.put_provision_config(service_name, alias, function_name, provision_count)

    # Confirm update
    config = client.get_provision_config(service_name, alias, function_name).data
    logger.info("Resource: %s, target: %d, current: %d", config['resource'], config['target'], config['current'])
    return config
