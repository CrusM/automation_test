from .openapi import SwaggerLoader, ReferenceSchemaDataType, ObjectSchemaDataType, ArraySchemaDataType, \
    change_to_camel, get_internal_response_schema_name, get_internal_request_schema_name,format_url_to_snake
import copy
import core.utilities.codedom as codedom
import os
import time
import json
import logging


_SCHEMA_BASE = [".schemabase", "SchemaBase"]
_COMMON = [".common", ['ApiTestResult, ApiTestHelper']]
_CASE_BASE = [".casebase", "ApiTestBase"]
_TOOL_PACKAGE = "product.common.tools.casegen"
SETTING = None

repo_desc = """
    This file is auto generated by the case auto generator
    Swagger File: %(swagger_file)s
    Description: The Object Report for the API Definition
    API Doc Version: %(doc_version)s
    Date: %(gen_date)s,
"""


class ObjectCreator:
    def __init__(self, swagger: SwaggerLoader):
        self.swagger = swagger
        self.code_statements = list()

    def generate(self):
        info = {
            "swagger_file": self.swagger.main_file,
            "doc_version": self.swagger.description_data[self.swagger.main_file]['info']['version'],
            "gen_date": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # description
        script_doc = codedom.DocStatement(lines=[repo_desc % info])
        self.code_statements.append(script_doc)





