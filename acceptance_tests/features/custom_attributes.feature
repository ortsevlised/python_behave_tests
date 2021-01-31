Feature: Custom attributes can be added, edited and deleted

  Background: Going to custom attributes menu
    Given the admin logs into Table.co
    When he goes to the settings section
    And selects the custom attributes menu

  Scenario: Adding a custom attribute from the settings section
    When he adds the following attributes
      | title  | identifier | data_type |
      | random | random     | Number    |
    Then the list of custom attributes is updated with the new field
#
#  Scenario: Deleting a custom attribute from the settings section
#    When he deletes an attribute
#    Then the field is removed from the list of custom attributes

#  Scenario Outline: Error messages are displayed when fields are missing or incorrect
#    When he adds the following attributes
#      | title   | identifier   | data_type   |
#      | <title> | <identifier> | <data_type> |
#    Then the following <error_message> is displayed
#    Examples:
#      | title  | identifier | data_type | error_message                                                                                              |
#      |        |            |           | Please correct the following errors:,Please enter a title.,Please enter a slug.,Please select a data type. |
#      | random |            |           | Please correct the following errors:,Please enter a slug.,Please select a data type.                       |
#      |        | random     |           | Please correct the following errors:,Please enter a title.,Please select a data type.                      |
#      |        |            | Number    | Please correct the following errors:,Please enter a title.,Please enter a slug.                            |
#      | random | random     |           | Please correct the following errors:,Please select a data type.                                            |
#      | random |            | Number    | Please correct the following errors:,Please enter a slug.                                                  |
#      |        | random     | Number    | Please correct the following errors:,Please enter a title.                                                 |
#

#  Scenario: Cannot add a duplicate attribute
#    When he adds the following attributes
#      | title  | identifier | data_type |
#      | random | random     | Number    |
#      | random | random     | Number    |
#    Then the attributes are displayed in the list of custom attributes
          #Scenario: adding from other place
