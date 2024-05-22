# Associations : States and Counties

In this exercise, you job is to create the models and functions defined below:

## Models

1. [ ] `State`: A state must have a name, abbreviation, state flower, and capital city.
2. [ ] `County`: A county must have a name, county seat, population, and state.

## Functions

- [ ] `create_state(name, abbreviation, state_flower, capital_city)`: Creates and returns a new `State` object.
  - [ ] `create_state` is thoroughly tested
- [ ] `create_county(name, county_seat, population, state)`: Creates and returns a new county object.
  - [ ] `create_county` is thoroughly tested
- [ ] `find_counties_for_state(abbreviation)`: Return the `County`s in the state with the provided abbreviation.
  - [ ] `find_counties_for_state` is thoroughly tested
- [ ] `state_population(state)`: Returns the total population of all the counties in the state.
  - [ ] `state_population` is thoroughly tested
- [ ] `counties_containing_state_capital()`: Returns the `County`s where the county seat is the same as that county's state's capital.
  - [ ] `counties_containing_state_capital` is thoroughly tested
