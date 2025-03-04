Feature: Fake Store API Products Tests


  @get_products
  Scenario: Fetch all products successfully
    When I send a GET request to fetch all products
    Then the response status should be 200
    And the response should match the expected product schema

  @get_products
  Scenario: Fetch a single product successfully
    When I send a GET request to fetch product with ID 1
    Then the response status should be 200
    And the response should match the expected product schema

  @get_products
  Scenario Outline: Fetch a non-existing product
    When I send a GET request to fetch product with ID <product_id>
    Then the response status should be 200

    Examples:
      | product_id |
      | 9999       |
      | abc        |


  @create_product
  Scenario: Create a new product
    When I send a POST request with valid product data
    Then the response status should be 200
    And the response should match the expected create product schema

  @create_product
  Scenario: Create a product with missing fields
    When I send a POST request with invalid data
    Then the response status should be 200

  @delete_product
  Scenario: Delete a product successfully
    When I send a DELETE request to delete product with ID 1
    Then the response status should be 200
    And the response should match the expected product schema

  @delete_product
  Scenario Outline: Delete a non-existing product
    When I send a DELETE request to delete product with ID <product_id>
    Then the response status should be 200

    Examples:
      | product_id |
      | 9999       |
      | abc        |
