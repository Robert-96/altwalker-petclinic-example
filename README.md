# altwalker-petclinic-example
AltWalker PetClinic example

## Intro

This is a MBT (Model-Based Testing) example for AltWalker, based on the "famous" [PetClinic](https://github.com/spring-projects/spring-petclinic).
This tutorial is basically a port of a [Java example made for GraphWalker](https://github.com/GraphWalker/graphwalker-example/tree/master/java-petclinic) with some adaptions and cleanup.
The models are a bit described in [GraphWalker docs](https://github.com/GraphWalker/graphwalker-project/wiki/PetClinic).


## Pre-requisites

- python3
- Firefox (or other browser)
- PetClinic

Install the python dependencies:

```pip install -r requirements.txt```


## Running

Just run run.sh :) in (Lin)unix...

```./run.sh```

or

```
altwalker check -m models/petclinic_full.json "random(vertex_coverage(100))"
altwalker verify -m models/petclinic_full.json tests
altwalker online tests -m models/petclinic_full.json "random(vertex_coverage(100))"
```

## About the porting

I used the model provided in the upstream project with a small change, since AltWalker doesnt support unnamed edges (as of v0.2.7) yet.
I also made some common vertices available in a BaseModel, that other models will inherit from.

## Credits

Credits go to GraphWalker team and the team behind the PetClinic example, along with the [AltWalker](https://altom.gitlab.io/altwalker/altwalker/index.html) team that inspired myself and also parts of this code.

## Contact

You can find me on [Twitter](https://twitter.com/darktelecom).

## LICENSE

[MIT](LICENSE).
