#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { TemplateStack } from "../lib/template-stack";

const app = new cdk.App();
new TemplateStack(app, "${{ values.name }}Stack");
