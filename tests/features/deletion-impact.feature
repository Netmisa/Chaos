Feature: Delete impacts in a Disruption

    Scenario: Delete an impact in a disruption

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        When I get "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.id" should be "7ffab234-3d49-4eea-aa2c-22f8680230b6"
        And the field "impacts.1.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"

        When I delete "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6"
        Then the status code should be "204"

        When I get "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6"
        Then the status code should be "404"

        When I get "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 1
        And the field "impacts.0.id" should be "7ffab234-3d49-4eea-aa2c-22f8680230b6"