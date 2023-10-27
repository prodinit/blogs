# How to export env variables in circleci? (You wont find this in circleci documentation)

According to the circleci documentation i should echo commands into $BASH_ENV in order to interpolate variables

`echo 'export TF_VAR_ENVIRONMENT="${ENVIRONMENT}"' >> $BASH_ENV`

Unfortunately, does not seem to work.

Solution: we have to explicitly do source $BASH_ENV before each job that relies on it

```
jobs:
    job-name:
        executor:
            name: python/default
            tag: '3.9'
        steps:
        - checkout
        - run:
            name: source bash env
            command: |
                echo 'export TF_VAR_ENVIRONMENT="${ENVIRONMENT}"' >> $BASH_ENV
                source $BASH_ENV
```

Each step runs in its own shell, so if you have commands that depend on runtime definition of an environment variable, your only option is to combine those commands into a single step.

Note: BASH_ENV is purely bash-thing. So for example if you use alpine based docker image, which has dash by default, it will not work.

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="Devops" src="https://img.shields.io/badge/Devops-8A2BE2" />
<a>
<img alt="Cirle CI" src="https://img.shields.io/badge/Circle CI-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.