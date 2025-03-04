# Automation Strategy

## Goals

1. **Reduce Manual Testing** - Automate 80% of repetitive testing tasks
2. **Speed Up Feedback** - Get test results in just a couple of minutes after code changes
3. **Ensure API Reliability** - Keep APIs working 99.9% of the time
4. **Support Fast Development** - Help with CI/CD pipelines and quick releases

## Test Coverage Approach


| Test Type             | Target | What It Tests                 | Simple Explanation                                                                                                                                                  |
|-----------------------|--------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unit Tests**        | 90%    | Individual API methods        | Testing single API endpoints in isolation to verify they work correctly on their own (e.g., testing that "GET /products/1" returns the correct product)             |
| **Integration Tests** | 85%    | Complete API workflows        | API interactions with other systems. Testing how your API works with databases, other services and external dependencies                                            |
| **Contract Tests**    | 100%   | Response structure validation | Verifying API responses always match their expected format and schema (e.g., ensuring product responses always include id, name, price, etc. in the correct format) |


## Technology Choices

We chose these technologies because they're proven to work well:

- **[Behave](https://github.com/behave/behave?tab=readme-ov-file#behave)**: Makes tests readable by everyone
- **[Requests & JSONSchema](https://python-jsonschema.readthedocs.io/en/latest/validate/)**: Simple API testing and validation 
- **[Docker](https://www.docker.com/)**: Ensures tests run the same everywhere
- **[GitHub Actions](https://github.com/features/actions)**: Automates test execution
- **[Faker](https://github.com/joke2k/faker)**: Creates realistic test data

## Scaling Our Approach

### Modular Design
- Reuse components when possible
- Easy to add new endpoints and features

### Running Tests in Parallel
- Independent tests that don't affect each other
- Docker containers to isolate resources
- CI/CD setup for parallel execution

## Integration with Development

### CI/CD Pipeline
```
Code Change → PR Creation → Automated Tests → Review → Merge
```

- **When Committing**: Run quick validation tests
- **On Pull Requests**: Run full test suite
- **Nightly**: Run all tests 

### Feedback Systems
- Show test results directly in GitHub Actions
- Create easy-to-read test reports (TBD: xray, testrail)
- Send alerts for test failures (TBD: Slack/Teams, Email, SMS)

## Measuring Success

- **Test Coverage**: Check after each test run
- **Test Speed**: Track to find slow tests
- **Defect Finding**: Measure how well tests find bugs

## Continuous Improvement

1. **Review Quarterly**
   - Update our testing tools as needed
   - Find gaps in testing
   - Make tests run faster

2. **Documentation**
   - Keep test docs updated
   - Link tests to requirements
   - Share knowledge with the team
