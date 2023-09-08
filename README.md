# altwalker-petclinic-example

AltWalker model-based testing example, implemented in Python, using the demo PetClinic site as a target.

## Overview

This repository contains a Model-Based Testing (MBT) example for [AltWalker](https://altwalker.github.io/altwalker/), based on the "famous" [PetClinic](https://github.com/spring-projects/spring-petclinic) web application. This tutorial is essentially a Python port of a [Java example](https://github.com/GraphWalker/graphwalker-example/tree/master/java-petclinic) originally created for GraphWalker, with some adaptations and cleanup. You can find some information about the models in the [GraphWalker documentation](https://github.com/GraphWalker/graphwalker-project/wiki/PetClinic).

## Pre-requisites

- Python3
- Firefox (or other browser)

## Setup

To install the required Python dependencies, run:

```bash
pip install -r requirements.txt
```

To start the PetClinic demo app, follow these steps:

1. Clone the PetClinic repository:

    ```bash
    git clone https://github.com/SpringSource/spring-petclinic.git
    cd spring-petclinic
    ```

1. Reset the repository to a specific commit:

    ```bash
    git reset --hard 482eeb1c217789b5d772f5c15c3ab7aa89caf279
    ```

1. Start the PetClinic app with Maven:

    ```bash
    mvn tomcat7:run
    ```

## Validating the Models and Code

You can validate the models and code using the following commands.

To check model syntax:

```bash
altwalker check -m models/petclinic.json "random(vertex_coverage(100))"
```

To verify the models against test scripts:

```bash
altwalker verify -m models/petclinic.json tests
```

## Running

To run the tests, use the following command:

```bash
altwalker online tests -m models/petclinic.json "random(vertex_coverage(100))" --report-xml-file altwalker.xml
```

If you intend to run this in a CI/CD pipeline or integrate it with a test management (e.g. [Xray](https://getxray.app), [Jenkins](https://www.jenkins.io/)), AltWalker will generate a Junit XML report .

## Credits

* Credit goes to [Sergio Freire](https://twitter.com/darktelecom) for porting this example to Python.
* Credit also goes to the [GraphWalker](https://graphwalker.github.io/) team and the team behind the PetClinic example.

## LICENSE

This project is licensed under the [MIT License](LICENSE).
