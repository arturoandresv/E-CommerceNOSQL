#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ecommerce_stack import EcommerceStack


app = cdk.App()
EcommerceStack(app, "EcommerceStack")

app.synth()
