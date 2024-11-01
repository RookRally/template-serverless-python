#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { ${{ values.name }}Stack } from "../lib/template-stack";

const app = new cdk.App();
new ${{ values.name }}Stack(app, "${{ values.name }}Stack");
