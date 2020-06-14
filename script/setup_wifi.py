"""Sertup wifi configuration

This module provide function to help setup wifi configuration. 
List of avalible functions:

setup_wifi_configuration() -- Setup wifi configuration
"""
__all__ = ["setup_wifi_configuration"]

import modules.helpers as helpers

WIFI_FILE_CONFIG_NAME = "_config_wifi.h"
MAIN_FILE_CONFIG_NAME = "app_config.h"
CONSTVAR_NAME = "APP_CONFIG_SETUP_WIFI"
TEMPL_FILE = "config_templates/wifi.conf"
MAIN_TEMPL_FILE = "config_templates/main.conf"

def setup_wifi_configuration(reset = 0):
    """Main function for handle setup wifi configuration for board

    Keywords arguments:
    reset - reset flags
    """

    main_config_path = "../src/" + MAIN_FILE_CONFIG_NAME 
    reset = 0

    try:
        is_validate = helpers.validate_configuration(main_config_path, CONSTVAR_NAME)
    except FileNotFoundError:
        main_template_content = helpers.load_content_file(MAIN_TEMPL_FILE)
        helpers.save_file("../src/" + MAIN_FILE_CONFIG_NAME , main_template_content)
        is_validate = 0

    if is_validate != 1 or reset == 1:
        template_content = helpers.load_content_file(TEMPL_FILE)

        print ("\r\n \r\nYou need configure your wifi connection before comailing code! \r\n")
        ssid = helpers.read_template_variable_cmd("SSID: ", "")
        pwd = helpers.read_template_variable_cmd("Password: ", "")

        config_content = helpers.concate_template_with_variables(template_content, (("SSID", ssid), ("PWD", pwd)))

        helpers.save_file("../src/" + WIFI_FILE_CONFIG_NAME , config_content)
        helpers.modify_main_config_file(main_config_path, "INCLUDE_WIFI", WIFI_FILE_CONFIG_NAME, CONSTVAR_NAME)
    else:
        print ("\r\n \r\nYou allready configured WiFi connection for your baord \r\n")