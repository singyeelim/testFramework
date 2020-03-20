# Specification Heading

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
    gauge run specs


## Shop online : One item

tags: shopOnline_oneItem

* Launch browser and specify url
* Click on "Agree" button
* Navigate to Collection & accesories "News" "Model cars"
* Select "EQC" product
/* Todo: Verify that the page displayed is the selected product
* Click on " Add to basket" to proceed
/* Todo: Verify correct model, amount and quantity is displayed
* Click on " Go to shopping basket" to proceed
/* Todo: Verify correct model, quantity and total amount is displayed
* Click on "Continue to address and delivery" to proceed
* Key in "Email address" with value "testemail@email.com"
* Click on "Mr" radio button
* Key in "First name" with value "test_firstName"
* Key in "Last name" with value "test_lastName"
* Key in "Street" with value "test_street"
* Key in "Number" with value "9000"
* Key in "Postcode" with value "SP2 0FL"
* Key in "Town/city" with value "test_town"
* Key in "Phone" with value "07911 123456"
* Click on "Continue to payment type" to proceed
* Click on "Paypal" radio button
* Click on "Continue to verification and order placement" to proceed
/* Todo: Verify information displayed in 'Verification and order placement' are correct

