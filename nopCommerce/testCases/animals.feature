Feature: Testing Animal functionality
  Tests pertaining to Animal functionality
  Scenario Outline: Animals are cute

          Given a <animal>
          When the <animal> is a baby
          Then the <animal> is cute

          Examples:
          | animal |
          | dog    |
          | cat    |

      Scenario: Some animals are cuter

          Given a puppy
          When the puppy is a baby
          Then the puppy is cuter than cats