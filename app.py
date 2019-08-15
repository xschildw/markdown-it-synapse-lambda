#!/usr/bin/env python3

from aws_cdk import core

from markdown_it_synapse_lambda.markdown_it_synapse_lambda_stack import MarkdownItSynapseLambdaStack


app = core.App()
MarkdownItSynapseLambdaStack(app, "markdown-it-synapse-lambda")

app.synth()
