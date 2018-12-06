@auth
Feature: Authentication
    In order to ensure users can be created and login
    As the Maintainer
    I want to test creating a user and logging in


    Scenario:
        Given there are no users
        When a user is created
        Then there is 1 user

    @web
    Scenario Outline: User logs in
        Given a user visits the site "/"
        When I log in as "<username>"
        Then I should see the "<auth class>"

        Examples: Users
            | username          | auth class |
            | registeredUser    | logged_in  |
            | unregisteredUser  | errornote  |