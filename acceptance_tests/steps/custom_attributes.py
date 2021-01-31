import time

from behave import *
from faker import Faker
from hamcrest import *

from acceptance_tests.page_model.settings.custom_attributes.add_attributes import AddAttribute
from acceptance_tests.page_model.settings.custom_attributes.custom_attributes import CustomAttributes
from acceptance_tests.page_model.settings.custom_attributes.delete_attribute import DeleteAttribute

use_step_matcher("re")
faker = Faker()


@step("(?:s)?he adds the following attributes")
def step_impl(context):
    add_attributes = AddAttribute(context.driver)
    attributes = []
    for row in context.table:
        data_type, identifier, title = generate_attribute_fields(row)
        add_attributes.add_attribute(title, identifier, data_type)
        # assert_that(custom_attributes.is_currently_visible(custom_attributes.ERROR_ALERTS), equal_to(False))TODO put it somewhere else
        time.sleep(0.5)  # Try to avoid sleeps. However there's nothing to validate for state change there
        attributes.append({'title': title, 'identifier': identifier, 'data_type': data_type})
    context.attributes = attributes


def generate_attribute_fields(row):
    title_ = row['title']
    identifier_ = row['identifier']
    data_type = row['data_type']
    title = faker.word() if title_ == 'random' else title_
    identifier = faker.word() if identifier_ == 'random' else identifier_
    return data_type, identifier, title


@step("the following (?P<error_messages>.+) is displayed")
def step_impl(context, error_messages):
    attributes_page = CustomAttributes(context.driver)

    errors_list = error_messages.split(',')
    error_alerts = attributes_page.error_alerts
    assert_that(len(error_alerts), equal_to(len(errors_list)))
    assert_that(error_alerts[0].text, is_in(errors_list))

    title_error_message = attributes_page.title_error_message
    identifier_error_message = attributes_page.identifier_error_message
    data_type_error_message = attributes_page.data_type_error_message

    if title_error_message != "":
        assert_that(title_error_message, is_in(errors_list))
    if identifier_error_message != "":
        assert_that(identifier_error_message, is_in(errors_list))
    if data_type_error_message != "":
        assert_that(data_type_error_message, is_in(errors_list))


@then("the list of custom attributes is updated with the new field")
def step_impl(context):
    custom_attributes = CustomAttributes(context.driver)

    for attributes in context.attributes:
        details = {'name': attributes['title'].lower(), 'identifier': attributes['identifier'].lower(),
                   'data_type': attributes['data_type'].lower()}
        assert_that(details, is_in(custom_attributes.table_rows))


@when("he deletes an attribute")
def step_impl(context):
    delete_page = DeleteAttribute(context.driver)
    attributes_page = CustomAttributes(context.driver)

    attributes_amount = len(attributes_page.table_rows)
    attribute_fields = delete_page.delete_attribute('random')
    context.deleted_response = {
        'amount': attributes_amount - 1,
        'attribute_details': attribute_fields,
    }


@then("the field is removed from the list of custom attributes")
def step_impl(context):
    attributes_page = CustomAttributes(context.driver)
    time.sleep(1)  # todo remove
    table_of_attributes = attributes_page.table_rows
    assert_that(len(table_of_attributes), equal_to(context.deleted_response['amount']))
    assert_that(context.deleted_response['attribute_details'], not_(is_in(table_of_attributes)))
