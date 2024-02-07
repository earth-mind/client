# Contributing to EarthMind

Thank you for your interest in contributing to EarthMind! 

We value the contributions of each person and want to make sure that everyone who wants to help can do so in a way that feels welcoming and inclusive.

## How to Contribute

There are many ways to contribute to our project:

- **Submitting bugs and feature requests** by opening issues on GitHub.
- **Improving documentation** to help new users or contributors.
- **Submitting pull requests** with fixes and improvements.

Please read through our [submission guidelines](#submission-guidelines) before submitting your pull request or issue.

### Submission Guidelines

- **Fork the repository** and make your changes on a new branch.
- **Follow our coding standards** and ensure your code is clean and well-documented.
- **Write tests** for any new functionality and ensure all tests pass.
- **Submit a pull request** with a detailed description of the changes and reference any related issues.
- **Commit Message Guidelines**: We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) specification for our commit messages. This leads to more readable messages that are easy to follow when looking through the project history and helps automate the versioning and release process. Please format your commit messages in accordance with this standard. 

We will review your submission and get back to you as soon as possible.

## Commit Message Guidelines

We encourage the use of [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) for all contributions to ensure a clear and consistent commit history. Here's a quick guide on how to format your commit messages:

### Format of the Commit Message

Your commit messages should be structured as follows:

```md
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types** include:

- `feat`: Introduces a new feature.
- `fix`: Fixes a bug.
- `docs`: Adds or updates documentation.
- `style`: Makes changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- `refactor`: Refactors existing code without changing its functionality.
- `test`: Adds missing tests or corrects existing tests.
- `chore`: Other changes that don't modify `src` or `test` files.

**Example**:

```md
feat(login): add the remember me feature

allow users to remain logged in for up to 30 days
include a new checkbox on the login form
Closes #123
```

Adhering to the Conventional Commits standard makes your contributions easier to understand and manage. For more details, please visit the [Conventional Commits website](https://www.conventionalcommits.org/en/v1.0.0/#summary).
