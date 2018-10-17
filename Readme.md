# Autocomplete SSH hosts for AWS

## Setup autocompletion

To get it working you need to install `bash-completion` and `boto3` python library.

On MacOS X run:

    $ brew install bash-completion
    $ pip install boto3 awscli
    $ aws configure

Enter your credentials to get access to AWS API.

Create symlink to `.ssh_autocompletion` file in your home folder:

    $ ln -sf  $(pwd)/.ssh_autocompletion ~/

Import `.ssh_autocompletion` in your `~/.bashrc`:

    $ echo 'source ~/.ssh_autocompletion' >> ~/.bashrc
    $ . ~/.bash.rc

## Generating/updating ssh config

Create for ssh `config.d` folder:

    $ mkdir -p ~/.ssh/config.d

and create symlink to script in /usr/local/bin:

    $ ln -sf $(pwd)/update_aws_ssh_config /usr/local/bin/update_aws_ssh_config

To generate or update ssh config for AWS hosts run:

    update_aws_ssh_config > ~/.ssh/config.d/aws

## Usage

To test autocompletion enter in terminal:

    $ ssh host_[TAB]
