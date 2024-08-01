# Contributing

How to contribute to this project.

## Contents

- [Cloning](#cloning)
- [Branching](#branching)
- [Versioning](#versioning)
- [Committing](#committing)
- [Submitting Code](#submitting-code)

## [Cloning](#contents)

There's an [issue](https://dmenin.wordpress.com/2020/03/25/docker-windows-error-exited-with-code-127)
related to the interpretation of end of line characters, for files created on
Linux, which impacts when running these files (scripts) inside Docker containers
on Windows.

When using Windows, clone the repository running:

```console
git clone --config core.autocrlf=input https://arms-summercamp-ci-server.northeurope.cloudapp.azure.com/arms-summercamp-2024/financial-operation-processor.git
```

Then configure the name and e-mail:

```console
git config user.name "First Last"
git config user.email "first.last@criticalsoftware.com"
```

## [Branching](#contents)

This project works with permanent and temporary branches.

`main` is a permanent branch containing the latest **stable** and **released**
code, and can never be broken.

`development` is a permanent integration branch containing the code **under development**
and eventually can be broken, but you'll need to accept the [sombrero of shame](https://medium.com/@EricBourget_75042/the-sombrero-of-shame-or-the-power-of-emergent-solutions-ecf130cdab92)
for that.

`release` is a permanent branch containing the code from a **released version**.
For that, the following name convention applies: **release-X.Y.Z**, where
X, Y and Z are: major, minor and patch [version numbers](#versioning).

`feature` is a temporary branch containing a **feature under development** which
latter will be merged against the development branch.
For that, the following name convention applies: **feature-brief-description**.

`experimental` is a temporary branch containing an **experiment or ideia**.
For that, the following name convention applies: **experimental-brief-description**.

## [Versioning](#contents)

The project follows the [semantic versioning 2.0.0](https://semver.org) schema to
communicate the changes for each release. Given the version number 1.0.0, this
represents the **Major.Minor.Patch**, being incremented when:

- Major version, have API incompatible changes
- Minor version, have backward compatible changes
- Patch version, have backward compatible bug fixes changes

## [Committing](#contents)

Before commit any code, make sure the name and email are configured on Git by
running the commands:

```console
git config user.name "My Name"
git config user.email "my.email@criticalsoftware.com"
```

The project is based on the [conventional commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#summary)
to specify the commit messages. The commit message should be structured as follows:

```text
Type: Brief description of what is being delivered, usually starting with a Verb

[Optional body with more details]
```

Where:

- Type can be: Chore, Doc, Fix and Feature

Example:

```text
Doc: Update documentation

Provide new contributing documentation

Add links on the readme to the new documentation
```

## [Submitting Code](#contents)

The `main`, `develop` and `release` branches have protection rules against **push**.

In order to submit changes, first create a new branch following the [branching](#branching)
guideline starting from the branch you want to contribute, this will be the
baseline.

Once the work is done, open a **pull request** from the new branch to the baseline
branch.

The changes will be reviewed before the code be accepted, and then the pull request
will be merged against the baseline.
